# 13 Sorting Algorithms in Python

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/sorts.png)


Implement, time & rank various sorting algorithms 

#### sample output

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/output.jpg)


### 1. Quick Sort 


[Quick Sort](https://github.com/paulnegz/sorts-py/blob/main/sort.py#L12) is based on the divide and conquer algorithm. Pick an element as a [pivot](https://github.com/paulnegz/sorts-py/blob/main/sort.py#L15) and partition the array around the selected pivot. Two [partitions](https://github.com/paulnegz/sorts-py/blob/main/sort.py#L17) (left & right) are made by placing array elements in the correct position relative to the pivot. The pivot is in-place and then partitions have to be sorted recusively

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/quick_sort.gif)


### 2. Merge Sort


[Merge Sort](https://github.com/paulnegz/sorts-py/blob/main/sort.py#L25) - works by dividing an array into smaller [subarrays](https://github.com/paulnegz/sorts-py/blob/main/sort.py#L29) (left & right). Repeat dividing the array till subarrays contains a single element. Sorting each subarray, while [merging](https://github.com/paulnegz/sorts-py/blob/main/util.py#L15) subarrays back together.

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/merge_sort.gif)


### 3. Tim Sort

[Tim Sort](https://github.com/paulnegz/sorts-py/blob/main/sort.py#L38)
 and [Tim Sort recursive](https://github.com/paulnegz/sorts-py/blob/main/sort.py#L49) are hybrid, stable sorting algorithm, derived from merge sort and insertion sort. Used in Java’s Arrays.sort(), Python’s sorted() and sort() functions. First sort a small run using Insertion Sort, then merges the pieces using a merge of merge sort. Divide the array into blocks known as RUN. Sort those runs using insertion sort and then merge runs.

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/tim_sort.png)
 


### 4. Heap Sort
[Heap Sort](https://github.com/paulnegz/sorts-py/blob/main/sort.py#L59) is a comparison-based sorting technique based on Binary Heap data structure. It is similar to the selection sort where we first find the minimum element and place the minimum element at the beginning. Repeat the same process for the remaining elements.

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/heap_sort.png)


### 5. Bubble Sort

[Bubble Sort](https://github.com/paulnegz/sorts-py/blob/main/sort.py#L68) is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/bubble_sort.gif)


### 6. Insertion Sort


[Insertion Sort](https://github.com/paulnegz/sorts-py/blob/main/sort.py#L82) is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/insertion_sort.gif)


### 7. Selection Sort


[Selection Sort](https://github.com/paulnegz/sorts-py/blob/main/sort.py#L92) is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/selection_sort.gif)


### 8. Tree Sort

[Tree Sort](https://github.com/paulnegz/sorts-py/blob/main/sort.py#L92) is a sorting algorithm that is based on [Binary Search Tree]() data structure. It first creates a binary search tree from the elements of the input list or array and then performs an in-order traversal on the created binary search tree to get the elements in sorted order. 


![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/tree_sort.png)

### 9. Shell Sort

[Shell Sort]() is mainly a variation of Insertion Sort. In insertion sort, we move elements only one position ahead. When an element has to be moved far ahead, many movements are involved. The idea of ShellSort is to allow the exchange of far items.

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/shell_sort.png)

### 10. Bucket Sort

[Bucket Sort]() works by distributing the elements into a fixed number of buckets based on their values and then sorting each bucket individually. It is efficient when the input data is uniformly distributed over a range. The algorithm's performance depends on the distribution of the data and the number of buckets used. 

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/bucket_sort.png)


### 11. Radix Sort

[Radix Sort](https://github.com/paulnegz/sorts-py/blob/main/sort.py#L91) is a stable sorting subroutine-based integer sorting algorithm. It is a sorting algorithm that does not use comparisons to sort a collection of integers. It classifies keys based on individual digits with the same significant position and value.

![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/radix_sort.png)


### 12. Counting Sort


![alt text](https://github.com/paulnegz/sorts-py/blob/main/img/counting_sort.png)

### 13. Cube Sort