from pdfreader import PDFDocument, SimplePDFViewer
import networkx as nx
import matplotlib.pyplot as plt
import streamlit as st
from pathlib import Path

def pdf_content_to_graph(file_name):
    # Open the PDF file
    fd = open(file_name, "rb")
    document = PDFDocument(fd)
    
    # Get the number of pages
    NUM_PAGES = document.root.Pages.Count
    
    # Create the PDF viewer
    viewer = SimplePDFViewer(fd)
    text = []
    
    # Iterate through all pages and extract text
    for i in range(1, NUM_PAGES + 1):
        viewer.navigate(i)
        viewer.render()
        result = viewer.canvas.strings
        text += result
    
    # Close the file after reading
    fd.close()
    
    # Create a graph from the text
    G = nx.Graph()
    edges = [(text[i], text[i + 1]) for i in range(len(text) - 1)]
    G.add_edges_from(edges)
    
    # Create the plot
    plt.figure(figsize=(20, 15))  # Ensure the figure is created
    options = {
        'node_color': 'green',
        'node_size': 100,
        'width': 1,
    }
    
    nx.draw(G, with_labels=True, **options)
    st.write(f"### Graph of Content for {Path(file_name).name}")
    # Display the plot using Streamlit
    st.pyplot(plt)  # Use st.pyplot() to show the plot in Streamlit
    
    return G

def compare_content(tab1, tab2):
    temp = []
    for text1, text2 in zip(tab1, tab2):
        if(text1 == text2):
            temp.append(True)
        else:
            temp.append(False)
    if False in temp:
        return False
    else:
        return True
def compare_pdf(file1, file2):
    G1 = pdf_content_to_graph (file1)
    G2 = pdf_content_to_graph (file2)
    if (nx.is_isomorphic(G1, G2) == False):
        return False
    else:
        fd1 = open(file1, "rb")
        document1 = PDFDocument(fd1)
        NUM_PAGES = document1.root.Pages.Count
        
        fd2 = open(file2, "rb")
        document2 = PDFDocument(fd2)
        NUM_PAGES = document2.root.Pages.Count
        
        viewer1 = SimplePDFViewer(fd1)
        i=1
        while i<= NUM_PAGES:
            
            viewer1.navigate(i)
            viewer1.render()
            result1 = viewer1.canvas.strings
            x1 = ''.join(result1)
            text1 = x1.split()
            i+=1
        
        #Second element
        viewer2 = SimplePDFViewer(fd2)
        i=1
        while i<= NUM_PAGES:
            
            viewer2.navigate(i)
            viewer2.render()
            result2 = viewer2.canvas.strings
            x2 = ''.join(result2)
            text2 = x2.split()
            i+=1
        
        # Comparing content function
        return compare_content(text1, text2)
