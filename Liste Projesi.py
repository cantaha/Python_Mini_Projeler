list_methods = []
for method in dir(list):
    if method.startswith("__"):
        continue
    else:
        list_methods.append(method)


set_methods = []
for method in dir(set):
    if method.startswith("__"):
        continue
    else:
        set_methods.append(method)

tuple_methods = []
for method in dir(tuple):
    if method.startswith("__"):
        continue
    else:
        tuple_methods.append(method)

dict_methods = []
for method in dir(dict):
    if method.startswith("__"):
        continue
    else:
        dict_methods.append(method)

str_methods = []
for method in dir(str):
    if method.startswith("__"):
        continue
    else:
        str_methods.append(method)


basliklar = ["List Method", "Set Method", "Tuple Method", "Dict Method", "String Method"]
classes = [list_methods, set_methods, tuple_methods, dict_methods, str_methods]

max_len = 0
for class_ in classes:
    if len(class_) > max_len:
        max_len = len(class_)

with open("Methods.xls", "w") as mt:
    for baslik in basliklar:
        print(baslik, end="")
        print(" " * (30 - len(baslik)), end="")
        mt.write(baslik)
        mt.write(" " * (30 - len(baslik)))

    for i in range(max_len):
        print()
        mt.write("\n")
        for class_ in classes:
            if i >= len(class_):
                print("-----", end="")
                print(" " * 25, end="")
                mt.write("-----")
                mt.write(" " * 25)
            else:
                print(class_[i], end="")
                print(" " * (30 - len(class_[i])), end="")
                mt.write(class_[i])
                mt.write(" " * (30 - len(class_[i])))

