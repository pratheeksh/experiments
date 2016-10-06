def solution2(A):
    # write your code in Python 2.7
    sum_left = 0
    sum_of_array = sum(A)
    for i in xrange(len(A)):
        sum_right = sum_of_array - A[i] - sum_left
        print sum_left, sum_right, A[i]

        if sum_right == sum_left:
            return i
        sum_left += A[i]
    return -1


def Solution3(X):
    max_num = 0
    num_str = str(X)
    for i in (xrange(len(num_str) - 1)):
        cur_num = int(num_str[i])
        next_num = int(num_str[i + 1])

        if cur_num + next_num % 2 == 0:
            avg = (cur_num + next_num) / 2
        else:
            avg = (cur_num + next_num + 1) / 2
        print num_str[0:i], num_str[i + 2:], num_str[i], num_str[i + 1]
        new_num = int(num_str[0:i] + str(avg) + num_str[i + 2:])
        print new_num
        if new_num > max_num:
            max_num = new_num
    return max_num


def reverse_list(input_list, start, end):
    while (start < end):
        input_list[start], input_list[end] = input_list[end], input_list[start]
        start += 1
        end -= 1
    return input_list


def reverse_word_list(input_list):
    reverse_list(input_list, 0, len(input_list) - 1)
    print input_list
    end = 0
    start = 0
    i = 0
    while start < (len(input_list)):
        while input_list[start] != " " and end <= len(input_list) - 1:
            end += 1
            i += 1
            print end
        if start < end:
            reverse_list(input_list, start, end - 1)
            start = end + 1

    return  input_list
list_w = ["a", " ", "b", "c"]
print reverse_word_list(list_w)
print reverse_list(["a", "b", "c"], 0, 2)
