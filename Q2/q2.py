import numpy as np
from numpy import dot
from numpy.linalg import norm

def cos_sim(A, B):
  return dot(A, B)/(norm(A)*norm(B))

def main():
    doc = np.array([[1,1,0,1,0,1],[1,1,1,0,1,0],[1,1,0,1,0,0]])
    query = [1,1,0,0,1,0]
    doc1=doc[0,:]
    doc2=doc[1,:]
    doc3=doc[2,:]
    print('doc1 = {0:.2f}'.format(cos_sim(doc1, query)))
    print('doc2 = {0:.2f}'.format(cos_sim(doc2, query)))
    print('doc3 = {0:.2f}'.format(cos_sim(doc3, query)))
    
if __name__ == "__main__":
    main()
