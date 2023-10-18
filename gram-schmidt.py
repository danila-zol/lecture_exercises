import operator
from random import randint, seed
from math import sqrt
import numpy as np

class Matrix:
    
    def __init__(self, d_arr):

        multi_array = [*d_arr]
        self.multi_array = multi_array
        self.matrix = self.multi_array


    def _apply_op(self, other, is_n, f):
        my_matrix = self.multi_array
        result = [[] for x in my_matrix]

        inter_result = 0

        my_row_len = len(my_matrix[0])
        my_row_n = len(my_matrix)

        n = 0
        e = 0
        while True:
            
            if e == my_row_len:
                e = 0
                n += 1

            if n == my_row_n:
                break

            e1 = my_matrix[n][e]
            e2 = other.multi_array[n][e] if is_n is False else other

            inter_result = f(e1, e2)
            result[n].append(inter_result)

            e += 1

        return result
   
    
    def _is_scalar(self, e):
        return True if type(e) == int or type(e) == float else False
    

    def __add__(self, other):
        return self._apply_op(other, self._is_scalar(other), operator.add)


    def __sub__(self, other):
        return self._apply_op(other, self._is_scalar(other), operator.sub)


    def __mul__(self, other):        
        return self._apply_op(other, self._is_scalar(other), operator.mul)


    def __truediv__(self, other):
        return self._apply_op(other, self._is_scalar(other), operator.truediv)


    def __matmul__(self, other):
        other_matrix = other.multi_array if isinstance(other, Matrix) else other
        my_matrix = self.multi_array
        result = [[] for x in my_matrix]

        inter_result = 0

        my_row_len = len(my_matrix[0])
        my_row_n = len(my_matrix)

        i = 0
        n = 0
        e = 0
        while True:
            
            if e == my_row_len:
                result[n].append(inter_result)
                inter_result = 0
                e = 0
                if i == my_row_n - 1:
                    n += 1
                    i = 0
                else:
                    i += 1

            if n == my_row_n:
                break

            e1 = my_matrix[n][e]
            e2 = other_matrix[e][i]

            inter_result += e1 * e2
            e += 1

        return result
    
    
    def _transpose(self, result):
        l = len(self.multi_array[0])
        r = result
        e = 0

        def transpose_el(e1, discard_this):
            nonlocal e
            nonlocal r
            nonlocal l
            if e == l:
                e = 0

            r[e].append(e1)
            e += 1

            return 0

        return transpose_el


    def T(self):
        # A bit inefficient since we store both the real result and the result of _apply_op that is
        # discarded in memory but eh ¯\_(ツ)_/¯ at least it's DRY.

        result = [[] for x in self.multi_array[0]]
        transpose_el = self._transpose(result)
        self._apply_op(0, True, transpose_el)
        return Matrix(result)

    
    def _decompose(self):
        return DecomposedMatrix(self.multi_array)

    def _is_zero_v(self, v):
        result = False
        for e in v:
            result = True if e == 0 else False

            e += 1

        return result

    def gram_schmidt(self):
        def proj(u, v):
            return u * (np.dot(v, u) / np.dot(u, u))


        def u_const_proj(u, v):
            def p(v):
                nonlocal u
                return proj(u, v)

            return p


        def get_calc_step(f, u, v):
            p = u_const_proj(u, v)
            def step(v):
                return f(v) - p(v)

            return step


        rv = []

        vectors = self._decompose()
        calc_step = lambda x: x

        for v in vectors:
            u = calc_step(v)
            calc_step = get_calc_step(calc_step, u, v)

            if (not self._is_zero_v(u)):
                rv.append(u)
        
        rv = np.array(rv)

        # Normalize
        rv_normalized = []
        for v in rv:
            mag = 0
            temp = 0

            for x in v:
                temp += pow(x, 2)

            mag = sqrt(temp)
            rv_normalized.append(list(v / mag))

        return Matrix(rv_normalized)

    
    def _gram_schmidt_hardcoded(self):
        ''' 
        Used for testing
        '''
        def proj(u, v):
            return u * (np.dot(v, u) / np.dot(u, u))

        def get_magnitude(v):
            mag = 0
            temp = 0

            for x in v:
                temp += pow(x, 2)

            mag = sqrt(temp)

            return mag

        d = self._decompose()
        v1 = next(d)
        v2 = next(d)
        v3 = next(d)
        v4 = next(d)

        u1 = v1
        e1 = u1 / get_magnitude(u1)

        u2 = v2 - proj(u1, v2)
        e2 = u2 / get_magnitude(u2)

        u3 = v3 - proj(u1, v3) - proj(u2, v3)
        e3 = u3 / get_magnitude(u3)

        u4 = v4 - proj(u1, v4) - proj(u2, v4) - proj(u3, v4)
        e4 = u4 / get_magnitude(u4)

        rv = [list(e1), list(e2), list(e3), list(e4)]

        return Matrix(rv)


    def __repr__(self):
        s = "%r" % (self.multi_array[0])
        for a in self.multi_array[1:]:
            s = "%s\n %r" % (s, a)
        return "[%s]" % (s)
        

class DecomposedMatrix:

    def __init__(self, m):
        self._original_m = m
        self._d = self._decompose(self._original_m)


    def __iter__(self):
        return self


    def __next__(self):
        return self._d()
 

    def _decompose(self, m):
        # Ideally would return an iterable instead of a closure, but I don't have the time.
        v = []
        column = 0
        stop_column = len(m[0])
        def step() -> list:
            nonlocal column
            nonlocal v
            nonlocal m

            if column == stop_column:
                raise StopIteration

            for row in m:
                v.append(row[column])

            column += 1
            r = list(v)
            v = []
            return np.array(r)

        return step


seed()
test_matrix = Matrix([[randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)],
                      [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)],
                      [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)],
                      [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]])

test_matrix = Matrix([[1, 1, 0], [2, 2, 0], [1, 2, 1]])
print(test_matrix, '\n')
print(test_matrix.gram_schmidt(), '\n')
