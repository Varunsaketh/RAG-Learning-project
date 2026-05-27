'''
TEXT DATA LOADING MODULE
1.in this module we imported both TextLoader and DirectoryLoader from langchain_community
-> TextLoader only lades single text files where with DirectoryLoader we can load multiple text files from a folder
2. We created a class texttodocument which has two methods loadfolder and loadfile
-> loadfolder method uses DirectoryLoader to load all text files from a folder and returns a list of documents
-> loadfile method uses TextLoader to load a single text file and returns a document
3. We created an instance of texttodocument class and called both loadfolder and loadfile methods to test the functionality of the module
4. handled many errors related to filepath issues so check the path before execution if it starts from head of your project give path normally 
else we need to mentionn "../../data/textfiles/languages/programming_languages.txt" .. for number of folders that shoudl be opended to find files
'''

from langchain_community.document_loaders import TextLoader
print("Text data loading module imported successfully.")
import os
print("path of execution:",os.getcwd())
from langchain_community.document_loaders import DirectoryLoader
print("Directory loader imported successfully.")
class texttodocument:
    def __init__(self,path):
        self.path  = path
    def loadfolder(self):
        loader = DirectoryLoader(
            self.path,
            glob = "**/*.txt",
            loader_cls = TextLoader,
            loader_kwargs = {"encoding" : "utf-8"}
        )
        textdocuments = loader.load()
        return textdocuments
    def loadfile(self):
        loader = TextLoader(self.path, encoding = "utf-8")
        textdocument = loader.load()
        return textdocument

td = texttodocument("data/textfiles/concepts")
td.loadfolder()
tf = texttodocument("data/textfiles/languages/programming_languages.txt")
tf2 = texttodocument("data/textfiles/languages/pythonintro.txt")
concetpstext = tf.loadfile()
textfilest= tf2.loadfile()
textdocuments = concetpstext + textfilest
print ("Text data loading module executed successfully.")
