def multiply(_mat1, _mat2):
    _res=[[0 for i in range(len(_mat1))] for j in range(len(_mat2[0]))]
    for i in range(len(_mat1)):
        for j in range(len(_mat2[0])):
            for k in range(len(_mat2)):
                _res[i][j]+=_mat1[i][k] * _mat2[k][j]
    return _res
dim=list(map(int, input('Enter the dimensions of matrices: ').split()))
print('Enter matrix 1')
_mat1=[[ int(input()) for i in range(dim[0])] for j in range(dim[1]) ]
print('Enter matrix 2')
_mat2=[[ int(input()) for i in range(dim[2])] for j in range(dim[3]) ]
print(multiply(_mat1, _mat2))
