from sentence_transformers import SentenceTransformer
import chromadb
from pathlib import Path
print("imported sucessfuly")
class dataQuery:
    def get_query(self):
        data =  str(input("Enter your query: "))
        query = [data]
        return query

obj = dataQuery()
dataquery = obj.get_query()

model = SentenceTransformer('all-MiniLM-L6-v2')
class embeddings:
    def get_embeddings(self, dataquery):
        embeddings = model.encode(dataquery)
        return embeddings

obj1 = embeddings()
data_embeddings = obj1.get_embeddings(dataquery)
DB_path = Path(__file__).parent.parent
client = chromadb.PersistentClient(path=DB_path/"embedding_storage"/"chromadb")
print(client.list_collections())
class retrieval:
    def char_retrieval(self,data_embeddings):
        collection = client.get_collection(name= "char_collection")
        results = collection.query(
            query_embeddings= data_embeddings.tolist(),
            n_results=5
        )
        return results
    def space_retrieval(self,data_embeddings):
        collection = client.get_collection(name= "space_collection")
        results = collection.query(
            query_embeddings= data_embeddings.tolist(),
            n_results=5
        )
        return results
    def nltk_retrieval(self,data_embeddings):
        collection = client.get_collection(name= "nltk_collection")
        results = collection.query(
            query_embeddings= data_embeddings.tolist(),
            n_results=5
        )
        return results
    
obj2 = retrieval()
char_results = obj2.char_retrieval(data_embeddings)
space_results = obj2.space_retrieval(data_embeddings)
nltk_results = obj2.nltk_retrieval(data_embeddings)
print("Char Retrieval Results: ", char_results)
print("Space Retrieval Results: ", space_results)
print("NLTK Retrieval Results: ", nltk_results) 