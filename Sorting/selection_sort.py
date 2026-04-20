class Solution: 
    def selectionSort(self, arr):
        n = len(arr)
        
        for i in range(n):
            m = i
            
            for j in range(i+1, n):
                if arr[j] < arr[m]:
                    m = j
            
            arr[i], arr[m] = arr[m], arr[i]
            
        return arr