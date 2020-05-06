import random
import matplotlib.pyplot as plt
import time

'''
Creating various sorting algorithms from StackSkills course "Python Programming, CS, Algorithms and Data Structures"
'''

# ------- sorting algorithm definitions
'''
Bubble Sort Algorithm
'''
def bubble_sort(arr):
    while arr != sorted(arr):
        for n in range(len(arr)-1):
            if arr[n] > arr[n+1]:
                arr[n], arr[n+1] = arr[n+1], arr[n]

'''
Selection Sort Algorithm
'''
def selection_sort(arr):
    n=0
    while n < len(arr):
        for spot in range(n+1, len(arr)):
            if arr[spot] < arr[n]:
                arr[spot], arr[n] = arr[n], arr[spot]
        n+=1

'''
Insertion Sort Algorithm
'''
def insertion_sort(arr):
    for key in range(1, len(arr)):
        work_key = key
        while arr[work_key] <= arr[work_key-1]:
            arr[work_key-1], arr[work_key] = arr[work_key], arr[work_key-1]
            work_key -= 1
            if work_key < 1:
               break

'''
Merge Sort Algorithm
'''

def merge_sorted(arrL, arrR):
    sorted_arr = []
    i, j = 0, 0

    while i < len(arrL) and j < len(arrR):
        if arrL[i] < arrR[j]:
            sorted_arr.append(arrL[i])
            i+=1
        else:
            sorted_arr.append(arrR[j])
            j+=1

    while i < len(arrL):
        sorted_arr.append(arrL[i])
        i += 1
    while j < len(arrR):
        sorted_arr.append(arrR[j])
        j += 1
    return sorted_arr

def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        mid = len(arr)//2
        l1 = merge_sort(arr[:mid])
        l2 = merge_sort(arr[mid:])
        return merge_sorted(l1, l2)

''' 
Quick Sort Algorithm 
'''
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[-1]
        smaller, equal, larger = [],[],[]
        for num in arr:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
    return quick_sort(smaller) + equal + quick_sort(larger)

'''
Built in Python Sorting function
'''
def bi_sort(arr):
    sorted(arr)

'''
Random list generator
'''
def create_rand_list(run):
    rand_list = [random.randint(0,100) for num in range(run)]
    return rand_list

def create_sorted_list(run):
    rand_list = [random.randint(0,100) for num in range(run)]
    return sorted(rand_list)
'''
Script to determine runtime
'''
def run_time(func, arr):
    tic = time.time()
    func(arr)
    toc = time.time()
    return toc-tic

# -----------------------------------------------------------

# --- algorithm performance metric based on number of interation step
runs = list(range(1,2000,50))

# initialize arrays to count number of iterations for plotting
bubble=[]
selection=[]
insertion=[]
quick=[]
merge=[]
BI=[]

# --- run sorting algorithms and extract data from runtime for each run scenario
for run in runs:
    bubble.append(run_time(bubble_sort,create_rand_list(run)))
    selection.append(run_time(selection_sort,create_rand_list(run)))
    insertion.append(run_time(insertion_sort,create_rand_list(run)))
    quick.append(run_time(quick_sort,create_rand_list(run)))
    merge.append(run_time(merge_sort,create_rand_list(run)))
    BI.append(run_time(bi_sort,create_rand_list(run)))

# --- plot runtime ----------------------------------------
f, ax = plt.subplots(1,1,figsize=(10,8))

plt.plot(runs, bubble,label='bubble')
plt.plot(runs, selection,label='selection')
plt.plot(runs, insertion,label='insertion')
plt.plot(runs, merge,label='merge')
plt.plot(runs, quick,label='quick')
plt.plot(runs,BI,label='Built-In .Sorted()')

ax.legend()
plt.xlabel('Length of Random Array')
plt.ylabel('Time to Sort (sec)')
plt.title("Sorting Algorithm Performance",fontsize=14)
plt.grid(color='gray',alpha=0.25)
plt.tight_layout()
plt.savefig('rand_perf.png',dpi=300)
print("-"*20+"Complete"+"-"*20)


