a = [1, 2, 2, 2, 3]
b = [2]
def array_diff(a, b):
    result = []
    for i in a:
        if i not in b:
            result.append(i)
    return result
print(array_diff(a, b))