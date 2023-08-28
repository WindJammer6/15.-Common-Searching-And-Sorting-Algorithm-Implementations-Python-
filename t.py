import sys
import time
from time_it import time_it

#About Python's recursion limit:
#When you execute a recursive function in Python on a large input ( > 10^3 (1000)), you might encounter a 
#“maximum recursion depth exceeded error”. This is a common error when executing algorithms such as 
#DFS, factorial, etc. on large inputs. This is also common in competitive programming on multiple 
#platforms when you are trying to run a recursive algorithm on various test cases. 

#This case occurred for when we are trying to carry out Quick Sort Algorithm (recursive function) on  
#the large sorted List (see the main code below), where the number of recursive loops created
#exceeded 10^3 (1000), and you will get this error,
    #'RecursionError: maximum recursion depth exceeded'


#Solution to this:
#Handling recursion limit – The “sys” module in Python provides a function called 'setrecursionlimit()'
#to modify the recursion limit in Python. It takes one parameter, the value of the new recursion limit. 
#By default, this value is usually 10^3. If you are dealing with large inputs, you can set it to, 10^6 
#so that large inputs can be handled without any errors.

#Source(s): https://stackoverflow.com/questions/72309971/quicksort-recursionerror (stackoverflow)
#           https://www.geeksforgeeks.org/python-handling-recursion-limit/ (GeeksforGeeks)

#Hence the reason for this line of code
sys.setrecursionlimit(10**6)


#Bubble Sort Algorithm
@time_it
def bubble_sort(number_list):
    size = len(number_list)

    for i in range(size - 1):

        swapped = False
        for j in range(size - 1 - i):

            if number_list[j] > number_list[j+1]:
                temp = number_list[j]

                number_list[j] = number_list[j+1]
                number_list[j+1] = temp
                swapped = True

        if not swapped:
            break



#Quick Sort Algorithm
def swapping_two_elements_in_a_list(a, b, array):
    if array[a] != array[b] and a != b:
        temp = array[a]
        array[a] = array[b]
        array[b] = temp

def hoare_partition_scheme(number_list, start_index_of_list, end_index_of_list):

    pivot_index = start_index_of_list
    pivot = number_list[pivot_index]

    start_pointer = pivot_index + 1
    end_pointer = end_index_of_list

    while start_pointer <= end_pointer:

        while start_pointer < len(number_list) and number_list[start_pointer] <= pivot:
            start_pointer += 1

        while number_list[end_pointer] > pivot:
            end_pointer -= 1

        if start_pointer < end_pointer:
            swapping_two_elements_in_a_list(start_pointer, end_pointer, number_list)  
            
    swapping_two_elements_in_a_list(pivot_index, end_pointer, number_list)

    return end_pointer

def lomuto_partition_scheme(number_list, start_index_of_list, end_index_of_list):
  
    pivot = number_list[end_index_of_list]
    partition_index = start_index_of_list

    for i in range(start_index_of_list, end_index_of_list):
        if number_list[i] <= pivot:
            swapping_two_elements_in_a_list(i, partition_index, number_list)
            partition_index += 1

    swapping_two_elements_in_a_list(partition_index, end_index_of_list, number_list)

    return partition_index

# @time_it
def quick_sort(number_list, start_index_of_list, end_index_of_list):

    if start_index_of_list >= end_index_of_list:
        return

    else:
        #Just change the 'hoare_partition_scheme' function here to 'lomuto_partition_scheme' function to carry out the Quick Sort 
        #Algorithm via Lomuto Partition scheme instead of via Hoare Partition scheme
        partitioning_point = hoare_partition_scheme(number_list, start_index_of_list, end_index_of_list)
        quick_sort(number_list, start_index_of_list, partitioning_point - 1)
        quick_sort(number_list, partitioning_point + 1, end_index_of_list)



#Insertion Sort Algorithm
@time_it
def insertion_sort(number_list):

    for i in range(1, len(number_list)):

        anchor = number_list[i]

        j = i - 1
 
        while j >= 0 and anchor < number_list[j]:
            number_list[j + 1] = number_list[j]
            j = j - 1

        number_list[j + 1] = anchor



#Shell Sort Algorithm
@time_it
def shell_sort(number_list):

    gap = len(number_list)//2

    while gap > 0:

      
        #~~~(Start of 'gap-ed' Insertion Sort for a gap iteration in Shell Sort)~~~
        
        for i in range(gap, len(number_list)):

            anchor = number_list[i]

            j = i - gap

            while j >= 0 and anchor < number_list[j]:
                number_list[j + gap] = number_list[j]
                j -= gap

            number_list[j + gap] = anchor

        #~~~(End of 'gap-ed' Insertion Sort for a gap iteration in Shell Sort)~~~


        gap = gap // 2



#Merge Sort Algorithm
def merge_two_smaller_sorted_lists_to_a_merged_sorted_list(smaller_sorted_list_a, smaller_sorted_list_b, array):

    i = j = k = 0

    while i < len(smaller_sorted_list_a) and j < len(smaller_sorted_list_b):
        if smaller_sorted_list_a[i] <= smaller_sorted_list_b[j]:
            array[k] = smaller_sorted_list_a[i]
            i += 1

        else:
            array[k] = smaller_sorted_list_b[j]
            j += 1
        k += 1

    while i < len(smaller_sorted_list_a):
        array[k] = smaller_sorted_list_a[i]
        i += 1
        k += 1

    while j < len(smaller_sorted_list_b):
        array[k] = smaller_sorted_list_b[j]
        j += 1
        k += 1

# @time_it
def merge_sort(array):

    if len(array) <= 1:
        return array
    
    middle_element_index = len(array)//2
    
    left_smaller_subarray = array[:middle_element_index]
    right_smaller_subarray = array[middle_element_index:]

    merge_sort(left_smaller_subarray)
    merge_sort(right_smaller_subarray)

    merge_two_smaller_sorted_lists_to_a_merged_sorted_list(left_smaller_subarray, right_smaller_subarray, array)



#Selection Sort Algorithm
@time_it
def selection_sort(number_list):
    for i in range(len(number_list) - 1):
        minimum_element_index = i

        for j in range(i + 1, len(number_list)):
            if number_list[j] < number_list[minimum_element_index]:
                minimum_element_index = j

        if number_list[i] != number_list[minimum_element_index]:
            number_list[i], number_list[minimum_element_index] = number_list[minimum_element_index], number_list[i]



#Common Pythonic way to sort a list, created as a function
@time_it
def python_sort_function(number_list):
    number_list.sort()




if __name__ == '__main__':
    #Testing the sorting algorithms on a large sorted List
    print("Testing the sorting algorithms on a large sorted List:")

    large_unsorted_list = [6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769, 6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769]
    bubble_sort(large_unsorted_list)

    #Manually implementing the function time tracking code for Quick Sort (a recursive function) since the 'time_it' decorator
    #dosen't work for recursive functions
    large_unsorted_list2 = [6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769, 6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769]
    start_time = time.time()
    quick_sort(large_unsorted_list2, 0, len(large_unsorted_list2) - 1)
    end_time = time.time()
    print(quick_sort.__name__ + " took " + str((end_time - start_time) * 1000) + " milliseconds")

    large_unsorted_list3 = [6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769, 6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769]
    insertion_sort(large_unsorted_list3)

    large_unsorted_list4 = [6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769, 6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769]
    shell_sort(large_unsorted_list4)

    #Manually implementing the function time tracking code for Merge Sort (a recursive function) since the 'time_it' decorator
    #dosen't work for recursive functions
    large_unsorted_list5 = [6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769, 6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769]
    start_time = time.time()
    merge_sort(large_unsorted_list5)
    end_time = time.time()
    print(merge_sort.__name__ + " took " + str((end_time - start_time) * 1000) + " milliseconds")

    large_unsorted_list6 = [6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769, 6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769]
    selection_sort(large_unsorted_list6)

    large_unsorted_list7 = [6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769, 6307, 9949, 4984, 6460, 4200, 4747, 3835, 8996, 2264, 5701, 9712, 2279, 1242, 7974, 6937, 747, 2259, 2725, 2505, 7770, 705, 5700, 5453, 7675, 5854, 2145, 2846, 2811, 907, 9039, 7543, 2793, 5440, 547, 2352, 132, 2714, 3002, 3999, 8984, 8933, 7000, 5932, 8327, 6939, 6282, 2481, 3720, 3731, 3647, 926, 9132, 8585, 3384, 368, 8942, 6935, 8365, 9536, 7472, 3372, 3493, 6612, 888, 8031, 2159, 8832, 5974, 4286, 9078, 1599, 9174, 429, 7366, 9680, 187, 1732, 4302, 3501, 3119, 6925, 7193, 6487, 4857, 8033, 4224, 2712, 6982, 7357, 3749, 4239, 4573, 6694, 6826, 2155, 1422, 2563, 6757, 867, 5340, 3085, 1059, 5997, 4645, 8903, 8683, 6961, 7889, 9635, 2131, 4480, 4793, 1305, 8509, 8552, 8151, 7551, 508, 8986, 2510, 4056, 6153, 2717, 9124, 3192, 4566, 6662, 8158, 3733, 455, 5503, 2175, 3305, 1991, 5859, 334, 7685, 322, 8230, 3131, 9422, 4886, 6739, 6259, 1714, 9480, 3155, 1517, 8956, 9325, 8767, 8532, 7366, 751, 3702, 9396, 515, 5424, 6985, 717, 7244, 9484, 3322, 3797, 4573, 2883, 8039, 7641, 573, 1121, 3170, 951, 2134, 9372, 9597, 3755, 151, 932, 339, 2592, 2925, 1323, 5351, 2554, 167, 2494, 9492, 2952, 1082, 631, 5952, 6865, 5436, 8564, 8327, 4827, 6197, 3367, 8047, 2977, 2183, 5989, 4843, 2224, 3827, 2501, 6996, 9813, 4951, 9899, 4247, 3335, 983, 4682, 2469, 3082, 3609, 9356, 9567, 4471, 6899, 5851, 1254, 2995, 1364, 6403, 745, 9240, 9469, 1094, 854, 8240, 6985, 5074, 4886, 4393, 9864, 692, 5729, 4919, 9985, 2077, 1904, 2520, 9637, 4472, 9672, 1356, 2716, 3456, 5301, 938, 6950, 9224, 6467, 348, 2823, 1740, 1557, 3122, 3372, 6433, 744, 5301, 6692, 1603, 2106, 7510, 7694, 7889, 4587, 309, 5905, 2609, 4393, 3667, 9901, 2749, 9804, 3179, 1283, 2415, 907, 4639, 2705, 9722, 5560, 6800, 9499, 8334, 9510, 2284, 134, 7231, 4375, 1689, 7192, 6983, 8587, 9842, 5996, 8845, 9255, 7723, 6981, 9130, 9021, 2207, 635, 1846, 1884, 1925, 7392, 6254, 4483, 5183, 769]
    python_sort_function(large_unsorted_list7) 

    print("\n")


    #//////////////////////////////////////////////////////////////////


    #Testing the sorting algorithms on a large unsorted List
    print("Testing the sorting algorithms on a large unsorted List:")

    large_sorted_list = [i for i in range(10001)]
    bubble_sort(large_sorted_list)

    #Manually implementing the function time tracking code for Quick Sort (a recursive function) since the 'time_it' decorator
    #dosen't work for recursive functions
    large_sorted_list2 = [i for i in range(10001)]
    start_time = time.time()
    quick_sort(large_sorted_list2, 0, len(large_sorted_list2) - 1)
    end_time = time.time()
    print(quick_sort.__name__ + " took " + str((end_time - start_time) * 1000) + " milliseconds")

    large_sorted_list3 = [i for i in range(10001)]
    insertion_sort(large_sorted_list3)

    large_sorted_list4 = [i for i in range(10001)]
    shell_sort(large_sorted_list4)

    #Manually implementing the function time tracking code for Merge Sort (a recursive function) since the 'time_it' decorator
    #dosen't work for recursive functions
    large_sorted_list5 = [i for i in range(10001)]
    start_time = time.time()
    merge_sort(large_sorted_list5)
    end_time = time.time()
    print(merge_sort.__name__ + " took " + str((end_time - start_time) * 1000) + " milliseconds")

    large_sorted_list6 = [i for i in range(10001)]
    selection_sort(large_sorted_list6)

    large_sorted_list7 = [i for i in range(10001)]
    python_sort_function(large_sorted_list7)     
