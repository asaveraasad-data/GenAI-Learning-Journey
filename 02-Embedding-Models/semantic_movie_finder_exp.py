from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np 

load_dotenv()

embeddings=OpenAIEmbeddings(model="text-embedding-3-small",  dimensions=300)

document=[
        "Interstellar is a science fiction movie.",

        "The Dark Knight is about Batman.",

         "Inception is based on dreams."
        
]

query="space movie"

doc_embedding=embeddings.embed_documents(document)
query_embedding=embeddings.embed_query(query)

score=cosine_similarity([query_embedding], doc_embedding)[0]
index, score=sorted(list(enumerate(score)),  key=lambda  x:x[1])[-1]

print(query)
print(document[index])
print("Simalrity Score is: ", score)