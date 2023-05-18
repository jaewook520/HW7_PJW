import numpy as np

def main():
    arr = np.array([[1,2],[3,4]])
    w,v = np.linalg.eig(arr)
    det = np.linalg.det(arr)
    print("Eigenvalues: ", end="")
    print(w)
    print()
    print("Eigenvectors: ", end="")
    print(v)
    print()
    print("Determinant: ", end="")
    print(det)
    print()
    
    vec1=[1,2,3]
    vec2=[4,5,6]
    vec3=np.cross(vec1, vec2)
    print("Cross product",end="")
    print(vec3)
    print()
    
    A=[[1,2,-2,],[2,1,-5],[1,-4,1]]
    b=[[-15],[-21],[18]]
    x = np.linalg.solve(A,b)
    print("Solution: ",end="")
    print(x)
    
if __name__ == "__main__":
    main()
