from numpy import isclose

class Vector:
    def __init__(self, entries, num_entries):
        if type(entries) is not list:
            raise Exception("Vector must be constructed from a 1D list")
        if len(entries) != num_entries:
            raise Exception("Incorrect number of entries")
        for entry in entries:
            if type(entry) is not float:
                raise Exception("Vector can only contain floats")
        self.__entries = entries
        self.num_entries = num_entries

    def get_entry(self, i):
        if i < 0 or i >= self.num_entries:
            raise Exception("Index out of bounds")
        return self.__entries[i]

    def set_entry(self, i, val):
        if i < 0 or i >= self.num_entries:
            raise Exception("Index out of bounds")
        if type(val) is not float:
            raise Exception("Vector can only contain floats")
        self.__entries[i] = val

    def equals(self, v):
        if self.num_entries != v.num_entries:
            raise Exception("Cannot compare vectors of difference sizes for equality")
        out = True
        for i in range(self.num_entries):
            out &= isclose(self.get_entry(i), v.get_entry(i))
        return out

class Matrix:
    def __init__(self, entries, rows, cols):
        if type(entries) is not list:
            raise Exception("Matrix must be constructed from a 2D list")
        if len(entries) != rows:
            raise Exception("Incorrect number of rows")
        for row in entries:
            if type(row) is not list:
                raise Exception("Matrix must be constructed from a 2D list")
            if len(row) != cols:
                raise Exception("Incorrect number of entries in row")
            for entry in row:
                if type(entry) is not float:
                    raise Exception("Matrix can only contain floats")
        self.__entries = entries
        self.rows = rows
        self.cols = cols

    def get_entry(self, i, j):
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols:
            raise Exception("Index out of bounds")
        return self.__entries[i][j]

    def set_entry(self, i, j, val):
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols:
            raise Exception("Index out of bounds")
        if type(val) is not float:
            raise Exception("Matrix can only contain floats")
        self.__entries[i][j] = val

    def get_row(self, i):
        row = []
        for j in range(self.cols):
            row.append(self.get_entry(i, j))
        return Vector(row, self.cols)

    def get_col(self, j):
        col = []
        for i in range(self.rows):
            col.append(self.get_entry(i, j))
        return Vector(col, self.rows)
