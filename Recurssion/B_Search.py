def B_Search(arr, start, end, key):
    if start > end:
        return -1
    
    mid = start + (end - start) // 2
    if arr[mid] == key:
        return mid
    
    elif arr[mid] < key:
        start = mid + 1
        return B_Search(arr,start, end, key)
    
    else:
        end = mid - 1
        return B_Search(arr, start, end, key)
    
def main():
    arr = [10,20,30,40,50,60]
    start = 0
    end = len(arr) - 1
    key = 30
    ans = B_Search(arr, start, end, key)
    print("The key will be : \n", ans)

if __name__ == "__main__":
    main()