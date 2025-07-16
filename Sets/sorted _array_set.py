from Sequences.array_seq import Array_Seq


class Sorted_Array_Set:
    def __init__(self): self.A = Array_Seq() # O(1)
    def __len__(self): return len(self.A) # O(1)
    def __iter__(self): yield from self.A # O(n)
    def iter_order(self): yield from self # O(n)


    def build(self, X): # O(?)
        self.A.build(X)
        self._sort()

    def _merge_sort(self, A, a = 0, b = None): # Sort sub-array A[a:b]
        if b is None: # O(1) initialize
            b = len(A) # O(1)
        if 1 < b - a: # O(1) size k = b - a
            c = (a + b + 1) // 2 # O(1) compute center
            self._merge_sort(A, a, c) # T(k/2) recursively sort left
            self._merge_sort(A, c, b) # T(k/2) recursively sort right
            L, R = A[a:c], A[c:b] # O(k) copy
            i, j = 0, 0 # O(1) initialize pointers
            while a < b: # O(n)
                if (j >= len(R)) or (i < len(L) and L[i] < R[j]): # O(1) check side
                    A[a] = L[i] # O(1) merge from left
                    i = i + 1 # O(1) decrement left pointer
                else:
                    A[a] = R[j] # O(1) merge from right
                    j = j + 1 # O(1) decrement right pointer
                a = a + 1   
    def _sort(self): # O(logn)
        self._merge_sort(self.A)

    def _binary_search(self, k, i, j): # O(log n)
        if i >= j: return i
        m = (i + j) // 2
        x = self.A.get_at(m)
        if x.key > k: return self._binary_search(k, i, m - 1)
        if x.key < k: return self._binary_search(k, m + 1, j)
    def find_min(self): # O(1)
        if len(self) > 0: return self.A.get_at(0)
        else: return None
    def find_max(self): # O(1)
        if len(self) > 0: return self.A.get_at(len(self) - 1)
        else: return None
    def find(self, k): # O(log n)
        if len(self) == 0: return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key == k: return x
        else: return None
    def find_next(self, k): # O(log n)
        if len(self) == 0: return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key > k: return x
        if i + 1 < len(self): return self.A.get_at(i + 1)
        else: return None
    def find_prev(self, k): # O(log n)
        if len(self) == 0: return None
        i = self._binary_search(k, 0, len(self) - 1)
        x = self.A.get_at(i)
        if x.key < k: return x
        if i > 0: return self.A.get_at(i - 1)
        else: return None
    def insert(self, x): # O(n)
        if len(self.A) == 0:
            self.A.insert_first(x)
        else:
            i = self._binary_search(x.key, 0, len(self.A) - 1)
            k = self.A.get_at(i).key
            if k == x.key:
                self.A.set_at(i, x)
                return False
        if k > x.key: self.A.insert_at(i, x)
        else: self.A.insert_at(i + 1, x)
        return True
    def delete(self, k): # O(n)
        i = self._binary_search(k, 0, len(self.A) - 1)
        assert self.A.get_at(i).key == k
        return self.A.delete_at(i)