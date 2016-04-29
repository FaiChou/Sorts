# -*- coding: utf-8 -*-

# ------------------------------------------------
# 程序: 排序
#
# 版本：1.0
#
# 作者：FaiChou
#
# 日期：2016-04-29
#
# 语言：Python 2.7
#
# 说明：总结了排序的实现方法，及代码实现
# ------------------------------------------------
"""
冒泡排序 BubbleSort
1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2.对第0个到第n-1个数据做同样的工作。这时，最大的数就“浮”到了数组最后的位置上。
3.针对所有的元素重复以上的步骤，除了最后一个。
4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

优化：
1.某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。用一个标记记录这个状态。
2.记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序，不用再排序了。因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。
"""
def buble_sort(ary):
    n = len(ary)
    k = n
    for i in range(n):
        flag = 1
        for j in range(k-1):
            if ary[j] > ary[j+1]:
                ary[j], ary[j+1] = ary[j+1], ary[j]
                k = j+1 # ?
                # print 'j = ',j
                flag = 0
        if flag:
            break
    return ary

def bubble(List): # wiki
    for j in range(len(List)-1,0,-1):
        for i in range(0,j):
            if List[i]>List[i+1]:List[i],List[i+1]=List[i+1],List[i]
    return List

"""
选择排序 SelectionSort
1.在未排序序列中找到最小元素，存放到排序序列的起始位置。
2.再从剩余未排序元素中继续寻找最小元素，然后放到已排序序列的末尾。
3.以此类推，知道所有元素均排序完毕。
"""
def select_sort(ary):
    n = len(ary)
    for i in range(0, n):
        min = i
        for j in range(i+1, n):
            if ary[j] < ary[min]:
                min = j
        ary[min], ary[i] = ary[i], ary[min]
    return ary

def selection_sort(L): # wiki
    N = len(L)
    exchanges_count = 0
    for i in range(N-1):
        min_index = i
        for j in range(i+1, N):
            if L[min_index] > L[j]:
                min_index = j
        if min_index != i:
            L[min_index], L[i] = L[i], L[min_index]
            exchanges_count += 1
        # print('iteration #{}: {}'.format(i, L))
    # print('Total {} swappings'.format(exchanges_count))
    return L

# testlist = [17, 23, 20, 14, 12, 25, 1, 20, 81, 14, 11, 12]
# print('Before selection sort: {}'.format(testlist))
# print('After selection sort:  {}'.format(selection_sort(testlist)))

"""
插入排序 InsertionSort
1.从第一个元素开始，该元素可以认为已经被排序。
2.取出下一个元素，在已经排序的元素序列中从后向前扫描。
3.如果被扫描的元素（已排序）大于新元素，将该元素后移一位。
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置。
5.将新元素插入到该位置的后面。
6.重复步骤2-5.
"""
def insert_sort(ary):
    n = len(ary)
    for i in range(1, n):
        if ary[i] < ary[i-1]:
            temp = ary[i]
            index = i # 待插入的下标 ?? 有必要吗？
            for j in range(i-1, -1, -1): # 从i-1循环到0（包括0）
                if ary[j] > temp:
                    ary[j+1] = ary[j]
                    index = j # 记录待插入下标
                else:
                    break
            ary[index] = temp
    return ary

def insertion_sort(n): # wiki
    if len(n) == 1:
        return n
    b = insertion_sort(n[1:])
    m = len(b)
    for i in range(m):
        if n[0] <= b[i]:
            return b[:i]+[n[0]]+b[i:]
    return b + [n[0]]

def insertion_sort2(lst): # wiki 
    if len(lst) == 1:
        return lst

    for i in xrange(1, len(lst)):
        temp = lst[i]
        j = i - 1
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp
    return lst

"""
希尔排序 ShellSort
基本思想：
将数组列在一个表中并对列分别进行插入排序，重复这过程，不过每次用更长的列（步长更长了，列数更少了）来进行。
最后整个表就只有一列了。将数组转换至表是为了更好地理解这算法，算法本身还是使用数组进行排序。
"""
def fc_range(start, stop, step=1.0): # halo faichou mis the point
    while start < stop:
        yield start
        start +=step

def shell_sort(ary):
    n = len(ary)
    gap = int(round(n/2))
    while gap > 0:
        for i in range(gap, n): # float ?
            temp = ary[i]
            j = i
            while j >= gap and ary[j-gap] > temp:
                ary[j] = ary[j-gap]
                j = j - gap
            ary[j] = temp
        gap = int(round(gap/2))
    return ary

"""
归并排序 MergeSort
归并排序的思想就是先递归分解数组，再合并数组。
先考虑合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，取了后相应的指
针就往后移一位。然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。
再考虑递归分解，基本思路是将数组分解成left和right，如果这两个数组内部数据是有序的，
那么就可以用上面合并数组的方法将这两个数组合并排序。如何让这两个数组内部是有序的?
可以再二分，直至分解出的小组只含有一个元素为止，此时认为该小组内部已有序。
然后合并排序相邻两个小组即可。
"""
def merge_sort(ary):
    if len(ary) <= 1 : return ary
    num = int(len(ary)/2) # 二分分解
    left = merge_sort(ary[:num])
    right = merge_sort(ary[num:])
    return merge(left, right) # 合并数组

def merge(left, right):
    '''
    合并操作
    将两个有序数组left[]和right[]合并成一个大的有序数组
    '''
    l, r = 0, 0
    result = []
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:] # 这里发生了一个好有趣的故事。l，1 分不清的故事，检查了3遍的故事。
    result += right[r:]
    return result


from collections import deque #

def merge_sort2(lst): # wiki 
    if len(lst) <= 1:
        return lst

    def merge2(left, right):
        merged,left,right = deque(),deque(left),deque(right)
        while left and right:
            merged.append(left.popleft() if left[0] <= right[0] else right.popleft())  # deque popleft is also O(1)
        merged.extend(right if right else left)
        return list(merged)

    middle = int(len(lst) // 2)
    left = merge_sort2(lst[:middle])
    right = merge_sort2(lst[middle:])
    return merge2(left, right)

"""
快速排序 QuickSort
1.从数列中挑出一个元素作为基数。
2.分区过程，将比此基数大的放到右边，小于或等于它的放到左边。
3.再对左右区间递归执行第二步，直至各区间只有一个数。
"""
def quick_sort(ary):
    return qsort(ary, 0, len(ary)-1)
def qsort(ary, left, right):
    if left >= right: return ary
    key = ary[left]
    lp = left
    rp = right
    while lp < rp:
        while ary[rp] >= key and lp < rp:
            rp -= 1
        while ary[lp] <= key and lp < rp:
            lp += 1
        ary[lp], ary[rp] = ary[rp], ary[lp]
    ary[left], ary[lp] = ary[lp], ary[left]
    qsort(ary, left, lp-1)
    qsort(ary, rp+1, right)
    return ary

def qsort2(arr): # wiki
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        return qsort2([x for x in arr[1:] if x < pivot]) + \
               [pivot] + \
               qsort2([x for x in arr[1:] if x >= pivot])

"""
堆排序 HeapSort
二叉堆性质：
1.父节点的键值总是大于或等于（小于或等于）任何一个子节点的键值。
2.每个节点的左右子树都是一个二叉堆（都是最大堆或最小堆）。

步骤：
1.构造最大堆（Build_Max_Heap）：若数组下标范围为0~n, 考虑到单独一个元素是大根堆，则
从下表n/2开始的元素均为大根堆。于是要从n/2-1开始，从前一次构造大根堆，这样就
能保证，构造到某个节点时，它的左右子树都已经是大根堆。
2.堆排序（HeapSort）：由于堆是用数组模拟的。得到一个大根堆后，数组内部并不是有序的。
因此需要将堆化数组有序化。思想是移除根节点，并做最大堆调整的递归运算。第一次将
heap[0]与heap[n-1]交换，再对heap[0...n-2]做最大堆调整。第二次将heap[0]
与heap[n-2]交换，再对heap[0...n-3]做最大堆调整。重复该操作直至heap[0]
和heap[1]交换。由于每次都是将最大的数并入到后面的有序区间，故操作完后整个数组就是有序的了。
3.最大堆调整（Max_Heapify）：该方法是提供给上述两个过程调用的。目的是将堆的末端子节点
做调整，使得子节点永远小于父节点。

"""
def heap_sort(ary):
    n = len(ary)
    first = int(n/2-1)
    for start in range(first, -1, -1):
        max_heapify(ary, start, n-1)
    for end in range(n-1, 0, -1):
        ary[end], ary[0] = ary[0], ary[end]
        max_heapify(ary, 0, end-1)
    return ary
def max_heapify(ary, start, end):
    root = start
    while True:
        child = root*2 + 1
        if child > end: break
        if child+1 <= end and ary[child] < ary[child+1]:
            child = child + 1
        if ary[root] < ary[child]:
            ary[root], ary[child] = ary[child], ary[root]
            root = child
        else:
            break

def heap_sort2(lst): # wiki 
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    # 创建最大堆
    for start in xrange((len(lst) - 2) // 2, -1, -1):
        sift_down(start, len(lst) - 1)

    # 堆排序
    for end in xrange(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return lst



ary = [1, 3, 4, 5, 9, 8, 6, 7, 2]

print 'ary =', ary

print 'bubble sort 1:', buble_sort(ary)
print 'bubble sort 2:', bubble(ary)

print 'select sort 1:', select_sort(ary)
print 'select sort 2:', selection_sort(ary)

print 'insert sort 1:', insert_sort(ary)
print 'insert sort 2:', insertion_sort(ary)
print 'insert sort 3:', insertion_sort2(ary)

print 'shell sort :', shell_sort(ary) 

print 'merge sort 1:', merge_sort(ary) 
print 'merge sort 2:', merge_sort2(ary)

print 'quick sort 1:', quick_sort(ary)
print 'quick sort 2:', qsort2(ary)

print 'heap sort 1:', heap_sort(ary)
print 'heap sort 2:', heap_sort2(ary)


