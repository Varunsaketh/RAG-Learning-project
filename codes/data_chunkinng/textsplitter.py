from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import SpacyTextSplitter
from langchain_text_splitters import NLTKTextSplitter
'''import nltk
nltk.download('punkt_tab')   only run it once to download the required resources for nltk splitter
its like basic requirement of nltk splitter this is atoolkit '''
from codes.data_loading.textdata import textdocuments
from codes.data_loading.exceldata import exceldocuments
from codes.data_loading.pdfdata import pdfdocuments
char_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 500,
    chunk_overlap = 50,
    length_function = len
)
space_splitter = SpacyTextSplitter(
    chunk_size = 500,
    chunk_overlap = 50,
    length_function = len
)
nltk_splitter = NLTKTextSplitter(
    chunk_size = 500,
    chunk_overlap = 50,
    length_function = len
)

print("All text splitters are created ")
alldocumnets = textdocuments + exceldocuments + pdfdocuments
print("All documents are combined successfully.")
char_chunks = char_splitter.split_documents(alldocumnets)
print("Documents are split into chunks using RecursiveCharacterTextSplitter successfully.")
space_chunks = space_splitter.split_documents(alldocumnets)
print("Documents are split into chunks using SpacyTextSplitter successfully.")
nltk_chunks = nltk_splitter.split_documents(alldocumnets)
print("Documents are split into chunks using NLTKTextSplitter successfully.")