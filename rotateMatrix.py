#48. Rotate Image

from typing import List


class Solution:
    def rotateMatrix(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left  = 0
        right = len(matrix) - 1
