#Sorting Algorithms in Python

![alt text](https://github.com/paulnegz/sorts-py/blob/main/sorts.png)

##Quick Sort 

QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.


Bubble sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list and moving it to the sorted portion of the list. 

Insertion sort is a simple sorting algorithm that works similar to the way you sort playing cards in your hands. The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked and placed at the correct position in the sorted part.

Merge sort is defined as a sorting algorithm that works by dividing an array into smaller subarrays, sorting each subarray, and then merging the sorted subarrays back together to form the final sorted array.


TimSort is a sorting algorithm based on Insertion Sort and Merge Sort.

Used in Java’s Arrays.sort() as well as Python’s sorted() and sort().
First sort small pieces using Insertion Sort, then merges the pieces using a merge of merge sort.
We divide the Array into blocks known as Run. We sort those runs using insertion sort one by one and then merge those runs using the combine function used in merge sort. If the size of the Array is less than run, then Array gets sorted just by using Insertion Sort. The size of the run may vary from 32 to 64 depending upon the size of the array. Note that the merge function performs well when size subarrays are powers of 2. The idea is based on the fact that insertion sort performs well for small arrays.
