'''
PDF Data Loading Module
1. In this module we imported both PyMuPDFLoader and DirectoryLoader from langchain_community
-> PyMuPDFLoader only loads single PDF files where with DirectoryLoader we can load multiple PDF files from a folder
2. We created a class pdftodocument which has two methods foldertopdf and loadpdf
KEY POINTS:
1. any pdf laode doesnt use encoding as it is not a text file so we dont need to mention encoding in both methods
-> foldertopdf method uses DirectoryLoader to load all PDF files from a folder and returns a list of documents
-> loadpdf method uses PyMuPDFLoader to load a single PDF file and returns a document
'''
from langchain_community.document_loaders import( PyMuPDFLoader,DirectoryLoader)
print("PDF data loading module imported successfully.")
import os
print("path of execution:",os.getcwd())
class pdftodocument:
    def __init__(self,path):
        self.path = path
    def foldertopdf(self):
        loader = DirectoryLoader(
            self.path,
            glob = "**/*.pdf",
            loader_cls = PyMuPDFLoader,
        )
        pdffolder = loader.load()
        return pdffolder
    def loadpdf(self):
        loader = PyMuPDFLoader(self.path)
        pdfdocument = loader.load()
        return pdfdocument
    
pdffolder = pdftodocument("data/pdf_files/corefiles")
pdffolder.foldertopdf()
pdffolder2 = pdftodocument("data/pdf_files/platformfiles")
pdffolder2.foldertopdf()
print("PDF data loading module executed successfully.")