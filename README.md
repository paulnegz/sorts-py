# 12 Sorting Algorithms in Python

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/sorts.png)


### 1. Quick Sort 

QuickSort is based on the divide and conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot. Partitions are made by placing array elements in the correct position relative to the pivot. The pivot is in-place and then partitions have to be sorted
![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/quick_sort.gif)
https://github.com/paulnegz/sorts-py/blob/main/sort.py#L7


### 2. Merge Sort

Merge sort works by dividing an array into smaller subarrays. Sorting each subarray, while merging the subarrays back together.
![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/merge_sort.gif)
https://github.com/paulnegz/sorts-py/blob/main/sort.py#L21


### 3. Tim Sort

Timsort is a hybrid, stable sorting algorithm, derived from merge sort and insertion sort. Used in Java’s Arrays.sort(), Python’s sorted() and sort() functions. First sort small a run using Insertion Sort, then merges the pieces using a merge of merge sort. Divide the array into blocks known as RUN. Sort those runs using insertion sort and then merge.

https://github.com/paulnegz/sorts-py/blob/main/sort.py#L37
 


### 4. Heap Sort



### 5. Bubble Sort

Bubble sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.
![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/bubble_sort.gif)

### 6. Insertion Sort

Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/insertion_sort.gif)

### 7. Selection Sort

Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 
![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/selection_sort.gif)
