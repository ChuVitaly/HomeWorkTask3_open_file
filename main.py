

list_name_files = ['1.txt', '2.txt', '3.txt']
dict_text = {}

for fl in list_name_files:
    with open(f"{fl}", 'r') as f:
        text = f.readlines()
        size = len(text)
        new_dict = {size: text}
    dict_text.update(new_dict)
sorted_dict_text = sorted(dict_text.items(), key=lambda x: x[0])
dict_text = dict(sorted_dict_text)


i = 0
for value in dict_text.values():
    print(" Название файла: ".rjust(20, '='), list_name_files[i])
    k = sorted_dict_text[i][0]
    print(f"Количество строк: {k}")
    print("".join(map(str, value)))
    i += 1

