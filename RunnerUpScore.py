if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split(" "))
    arr.sort()
    c=arr[len(arr)-1]
    for i in range(0,n):
        if arr[-1]==c:
            arr.pop()
    print arr[-1]
