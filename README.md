# 13 Sorting Algorithms in Python

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/sorts.png)


Using python standard libraries implememnt, time & rank various sorting algorithms 

#### sample output

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/output.jpg)


### 1. Quick Sort 


[Quick Sort](https://github.com/paulnegz/sorts-py/blob/main/sort.py#10) is based on the divide and conquer algorithm. Pick an element as a pivot and partition the array around the selected pivot. Two partitions are made by placing array elements in the correct position relative to the pivot. The pivot is in-place and then partitions have to be sorted recusively 

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/quick_sort.gif)


### 2. Merge Sort


[Merge Sort](https://github.com/paulnegz/sorts-py/blob/main/sort.py#L23) - works by dividing an array into smaller subarrays. Sorting each subarray, while merging subarrays back together.

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/merge_sort.gif)


### 3. Tim Sort

Timsort is a hybrid, stable sorting algorithm, derived from merge sort and insertion sort. Used in Java’s Arrays.sort(), Python’s sorted() and sort() functions. First sort a small run using Insertion Sort, then merges the pieces using a merge of merge sort. Divide the array into blocks known as RUN. Sort those runs using insertion sort and then merge runs.

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/tim_sort.png)
https://github.com/paulnegz/sorts-py/blob/main/sort.py#L37
 


### 4. Heap Sort
Heap sort is a comparison-based sorting technique based on Binary Heap data structure. It is similar to the selection sort where we first find the minimum element and place the minimum element at the beginning. Repeat the same process for the remaining elements.

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/heap_sort.png)


### 5. Bubble Sort

Bubble sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/bubble_sort.gif)


### 6. Insertion Sort

Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/insertion_sort.gif)


### 7. Selection Sort

Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/selection_sort.gif)


### 8. Tree Sort


### 9. Shell Sort


### 10. Bucket Sort


### 11. Radix Sort
Radix Sort algorithm is a stable sorting subroutine-based integer sorting algorithm. It is a sorting algorithm that does not use comparisons to sort a collection of integers. It classifies keys based on individual digits with the same significant position and value.

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/radix_sort.png)


### 12. Counting Sort


### 13. Cube Sort