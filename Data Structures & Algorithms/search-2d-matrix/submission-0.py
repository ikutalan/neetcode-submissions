class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # use the last element in each row to do binary search to locate row
        # r_mid = n //2
        # if target > matrix[r_mid], look in rows blow n//2 (greater half)
        # else look in smaller half
        # if r_l < target < r_r
        # row is the r_r
        # do binary search in the row just found

        # do BS in the for each last element in each row
        if not matrix or not matrix[0]:
            return False

        start, end = 0, len(matrix)
        if target > matrix[end - 1][-1]:
            return False
        while start < end:
            mid = (start + end) // 2
            if matrix[mid][-1] == target:
                return True
            if target > matrix[mid][-1]:
                # search in the greater half
                start = mid + 1
            else:
                end = mid
        # found the row 
        row = start
        if row == len(matrix):
            return False
        
        n = len(matrix[row])
        start, end = 0, len(matrix[row])
        while start < end:
            mid = (start + end) // 2
            if target <= matrix[row][mid]:
                end = mid
            else:
                start = mid + 1
        if start == n or matrix[row][start] != target:
            return False
        else:
            return True
