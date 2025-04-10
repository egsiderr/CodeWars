"""В этом небольшом задании вам дается строка чисел, разделенных пробелами,
вы должны вернуть наибольшее и наименьшее число.
Примеры:
high_and_low("1 2 3 4 5") # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"""

def high_and_low(numbers):
    # num_list = [int(num) for num in numbers.split()]
    # return f"{max(num_list)} {min(num_list)}"
    nums = numbers.split()
    return f"{max(nums)} {min(nums)}"

print(high_and_low("1 2 3 4 5"))