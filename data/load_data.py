import ipywidgets as widgets
from IPython.display import display

def uploadpdf():
    # Create an upload widget
    upload_widget = widgets.FileUpload(accept='.pdf', multiple=False)
    # Display the widget to upload file
    display(upload_widget) 
    return upload_widget

def writeuploaded(upload_widget):
    # Save the uploaded file and use it in your code
    if upload_widget.value:
        uploaded_file = list(upload_widget.value.values())[0]
        file_name = uploaded_file['metadata']['name']
        # Save the uploaded file to disk
        #print(file_name)
        with open(file_name, 'wb') as f:
            f.write(uploaded_file['content'])
        print(f"File '{file_name}' uploaded and saved.")
        return file_name