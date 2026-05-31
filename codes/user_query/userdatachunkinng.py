from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_text_splitters import SpacyTextSplitter
from langchain_text_splitters import NLTKTextSplitter
from codes.user_query.dataentry import dataquery    
print("Text splitters imported successfully.")

class userdatachunkinng:
    def __init__ (self,query):
        self.query = query
    def char_splitter(self):
        char_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50 , length_function=len)
        return char_splitter
    def space_splitter(self):
        space_splitter = SpacyTextSplitter(chunk_size=500, chunk_overlap=50 , length_function=len)
        return space_splitter
    def nltk_splitter(self):
        nltk_splitter = NLTKTextSplitter(chunk_size=500, chunk_overlap=50 , length_function=len)
        return nltk_splitter

obj = userdatachunkinng(dataquery)
char_splitter = obj.char_splitter()
space_splitter = obj.space_splitter()
nltk_splitter = obj.nltk_splitter()
print("Text splitters created successfully.")