'''
this may take some time to load because it should travel to loading teh start of pipe line and go step by step file by file and load to vectorDB
1. we imported chromadb and uuid for creating collection and unique ids for the documents
2.embeddings for the chromadb only accepts in the code in list[list[str]] it can be and ndlist but the sentence_tansformers embeddings model creates it as a numpy arrays 
3. we used PersistentClinet tahn the normal one because the vectors can be stored in RAM and at the given path it reduces each time load and stress caused on CPU 
'''
import chromadb
import uuid
from codes.data_chunkinng.textsplitter import char_chunks, space_chunks, nltk_chunks
print("Chromadb imported successfully.")
from codes.data_embeddings.embeddings import char_embeddings, space_embeddings, nltk_embeddings
print("Embeddings imported successfully.")

class storage:
    def __init__(self,collection_name,embeddings,chunks):
        self.client = chromadb.PersistentClient(path = "codes/embedding_storage/chromadb")
        self.collection_name = collection_name
        self.embeddings = embeddings
        self.chunks = chunks
    def create_collection(self):
        self.collection = self.client.get_or_create_collection(name=self.collection_name) 
        self.collection.add(
            ids = [str(uuid.uuid4()) for _ in range(len(self.embeddings))],
            embeddings = self.embeddings.tolist(),
            documents = [chunk.page_content for chunk in self.chunks],
            metadatas = [chunk.metadata for chunk in self.chunks]
        )
        print(f"Collection '{self.collection_name}' created successfully with {len(self.embeddings)} embeddings.")
        return self.collection

char_collection = storage("char_collection", char_embeddings, char_chunks).create_collection()
space_collection = storage("space_collection", space_embeddings, space_chunks).create_collection()
nltk_collection = storage("nltk_collection", nltk_embeddings, nltk_chunks).create_collection()
print("All collections created successfully.")

