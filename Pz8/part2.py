original_dict = {}
for i in range(7):  # range(7)
    original_dict[i] = i ** 3
print("Исходный словарь:")
print(original_dict)
modified_dict = original_dict.copy()
del modified_dict[0]
del modified_dict[6]
print("\nСловарь после удаления первого и последнего элементов:")
print(modified_dict)
