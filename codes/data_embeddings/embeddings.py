''' we used sentence transformers model to split the embeddings
this i a python liberary where we can use for splitting it has all of its models available in hugging face 

1. we cant directly embed the documents the chunks are in document format so we changed them to text and used for embedding 
2. model loading takes some time so we loaded the model once and used it for all three spiltters to create embeddings'''

from sentence_transformers import SentenceTransformer
from codes.data_chunkinng.textsplitter import char_chunks, space_chunks, nltk_chunks
print("SentenceTransformer imported successfully.")
print("Text chunks imported successfully.")
class Embeddings:
    def __init__(self,chunks,model):
        self.chunks = chunks
        self.model = model
    def create_embeddings(self):
        texts = [chunk.page_content for chunk in self.chunks]
        embeddings = self.model.encode(texts)
        return embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')
char_embeddings = Embeddings(char_chunks, model).create_embeddings()
print("Embeddings created successfully using RecursiveCharacterTextSplitter.")
space_embeddings = Embeddings(space_chunks, model).create_embeddings()
print("Embeddings created successfully using SpacyTextSplitter.")
nltk_embeddings = Embeddings(nltk_chunks, model).create_embeddings()
print("Embeddings created successfully using NLTKTextSplitter.")

print("All embeddings created successfully.")
print("Length of embeddings:", len(char_embeddings), len(space_embeddings), len(nltk_embeddings))
print("Shape of embeddings:", char_embeddings.shape, space_embeddings.shape, nltk_embeddings.shape)