list = [3,4,5,4,5,6,4,55,4,556,6,4,56]

for i in range(1,len(list)):
    current_value = list[i]
    position = i
    while position > 0 and list[position - 1] > current_value:
        list[position] = list[position - 1]
        position = position - 1
    list[position] = current_value

print(list)