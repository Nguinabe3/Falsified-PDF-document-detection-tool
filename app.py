import streamlit as st
import os
from content.content import compare_pdf

# Directory where uploaded files will be saved
data_directory = os.getcwd() + "/data"

# Function to save uploaded file
def save_uploaded(uploaded_file):
    paths = os.path.join(data_directory, uploaded_file.name)
    if os.path.exists(paths):
        os.remove(paths)
    with open(paths, "wb") as f:
        f.write(uploaded_file.getbuffer())
    return paths  # Return the file path to use it later

def main():
    st.title("Multi-Level Detection of Falsified PDF Documents System")

    # Create file uploaders in the sidebar
    with st.sidebar:
        st.info("### Please upload two PDF files to check for document falsification.")
        file1 = st.file_uploader("Click Browse Files to Upload the First PDF file", type=["pdf"])
        if file1:
            file1_path = save_uploaded(file1)
            st.success(f"First PDF uploaded: {file1.name}")
        else:
            st.warning("Please upload the first PDF file.")

        file2 = st.file_uploader("Click Browse Files to Upload the Second PDF file", type=["pdf"])
        if file2:
            file2_path = save_uploaded(file2)
            st.success(f"Second PDF uploaded: {file2.name}")
        else:
            st.warning("Please upload the second PDF file.")

    # Ensure both files are uploaded before showing the button
    if file1 and file2:
        # Add a button to trigger the comparison
        if st.button("Check Falsification"):
            # Call the compare function when the button is clicked
            result = compare_pdf(file1_path, file2_path)
            #print(type(result))
            if result == True:
                st.success("No falsification detected")
                os.remove(file1_path)
                os.remove(file2_path)
            else:
                st.error("Warning, falsification detected")
                os.remove(file1_path)
                os.remove(file2_path)
    else:
        st.info("Upload both PDF files to compare.")

# Ensure that the main function is executed when running the app
if __name__ == "__main__":
    # Create the data directory if it doesn't exist
    if not os.path.exists(data_directory):
        os.makedirs(data_directory)
    
    main()