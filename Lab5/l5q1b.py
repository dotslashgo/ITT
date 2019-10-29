def transpose(_mat):
        _trans=[[_mat[i][j] for i in range(len(_mat))] for j in range(len(_mat[0]))]
        return _trans
dim=list(map(int, input('Enter the dimensions: ').split()))
_mat=[[ int(input()) for i in range(dim[0])] for j in range(dim[1])]
print(transpose(_mat))