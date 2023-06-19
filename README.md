## Sorting Algorithms in Python

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/sorts.png)


### Quick Sort 

QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.
 https://github.com/paulnegz/sorts-py/blob/main/sort.py#L7


### Merge Sort

Merge sort is defined as a sorting algorithm that works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.
 https://github.com/paulnegz/sorts-py/blob/main/sort.py#L21


### Tim Sort

Timsort is a hybrid, stable sorting algorithm, derived from merge sort and insertion sort.
Used in Java’s Arrays.sort() as well as Python’s sorted() and sort().
First sort small pieces using Insertion Sort, then merges the pieces using a merge of merge sort. Divide the Array into blocks known as Run. We sort those runs using insertion sort and then merge those 
 https://github.com/paulnegz/sorts-py/blob/main/sort.py#L37
 


### Heap Sort



### Bubble Sort

Bubble sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.


### Selection Sort

Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 


### Insertion Sort

Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.
