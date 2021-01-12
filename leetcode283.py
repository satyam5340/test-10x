import heapq
def balanceHeaps():
    '''
    use globals min_heap and max_heap, as per declared in driver code
    use heapify modules , already imported by driver code
    Balance the two heaps size , such that difference is not more than one.
    '''
    # code here

    global min_heap
    global max_heap

    if len(min_heap) > len(max_heap) + 1:
        curr = heapq.heappop(min_heap)
        heapq.heappush(max_heap, -curr)
    elif len(max_heap) > len(min_heap) + 1:
        curr = heapq.heappop(max_heap)
        heapq.heappush(min_heap, -curr)


def getMedian():
    '''
    use globals min_heap and max_heap, as per declared in driver code
    use heapify modules , already imported by driver code
    :return: return the median of the data received till now.
    '''
    # code here
    global min_heap
    global max_heap
    if len(min_heap) == len(max_heap):
        return (min_heap[0] + (-max_heap[0])) // 2
    else:
        if len(min_heap) > len(max_heap):
            return min_heap[0]
        else:
            return -max_heap[0]


def insertHeaps(x):
    '''
    use globals min_heap and max_heap, as per declared in driver code
    use heapify modules , already imported by driver code
    :param x: value to be inserted
    :return: None
    '''
    global min_heap
    global max_heap

    if len(max_heap) == 0 or -max_heap[0] > x:
        heapq.heappush(max_heap, -x)
    else:
        heapq.heappush(min_heap, x)

min_heap = []
max_heap = []
n = int(input())
for _ in range(n):
    m = int(input())
    insertHeaps(m)

    balanceHeaps()
    print(getMedian())


