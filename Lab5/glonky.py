class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        self._mat = [[int(i) for i in input().split()[:cols]] for x in range(rows)]

    def __str__(self):
        for i in range(self.rows):
            for j in range(self.cols):
                print(self._mat[i][j], end=' ')
            print()

    def __add__(self, other):
        ret = [[x + y for x, y in zip(row1, row2)] for row1, row2 in zip(self._mat, other)]
        return ret

    def __getitem__(self, index):
        return self._mat[index]
    def transpose(self):
        trans_a=[[]]
        trans_a=[[self[j][i] for j in range(len(a))] for i in range(len(a[0]))]
        return trans_a
