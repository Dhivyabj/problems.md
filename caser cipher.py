

message = input("Enter your message: ")
key = int(input("Enter shift key (number): "))
encrypted = ""

for char in message:
    if char.isalpha():
        shift = key % 26
        if char.isupper():
            encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted += chr((ord(char) - 97 + shift) % 26 + 97)
    else:
        encrypted += char  

print("Encrypted message:", encrypted)

#problems 1

number = 123456.7891

num_str = f"{number:.10f}".rstrip('0').rstrip('.') if '.' in str(number) else str(number)


if '.' in num_str:
    integer, decimal = num_str.split('.')
else:
    integer, decimal = num_str, ''


if len(integer) <= 3:
    formatted = integer
else:
    head = integer[-3:]
    tail = integer[:-3]
    tail_groups = [tail[max(i-2, 0):i] for i in range(len(tail), 0, -2)][::-1]
    formatted = ','.join(tail_groups) + ',' + head


if decimal:
    formatted_output = f"{formatted}.{decimal}"
else:
    formatted_output = formatted

print("Formatted currency:", formatted_output)


# Problem 2

from copy import deepcopy


list1 = [{"positions": [0, 5], "values": [1, 2]}]
list2 = [{"positions": [3, 6], "values": [3]}]


combined = deepcopy(list1)


for elem2 in list2:
    l2, r2 = elem2['positions']
    overlap_found = False

    for elem1 in combined:
        l1, r1 = elem1['positions']
        overlap = max(0, min(r1, r2) - max(l1, l2))

        
        if overlap > (r2 - l2) / 2:
            elem1['values'] += elem2['values']
            overlap_found = True
            break
        if not overlap_found:
            combined.append(elem2)



combined.sort(key=lambda x: x['positions'][0])

print(combined)


#Problem 3

prices = [20, 15, 7, 2, 13]

min_loss = float('inf')
buy_year = -1
sell_year = -1

for i in range(len(prices)):
    for j in range(i + 1, len(prices)):
        loss = prices[i] - prices[j]
        if 0 < loss < min_loss:
            min_loss = loss
            buy_year = i + 1 
            sell_year = j + 1

print("Buy Year:", buy_year)
print("Sell Year:", sell_year)
print("Minimized Loss:", min_loss)
