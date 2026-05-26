from langchain_community.document_loaders import TextLoader
import os
print(os.getcwd())
from langchain_community.document_loaders import DirectoryLoader
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
tf.loadfile()
tf2.loadfile()
