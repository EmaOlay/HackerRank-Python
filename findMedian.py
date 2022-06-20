def findMedian(arr):
    # Write your code here
    arr.sort()
    median=int(len(arr)/2)
    return arr[median]