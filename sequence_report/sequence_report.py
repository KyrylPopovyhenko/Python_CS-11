pos = 0
neg = 0
count = 0
total_sum = 0
max_num = None
min_num = None
num13 = 0

while True:
    num = int(input("Enter a number (or '0' to quit): "))
    if num == 0: #If there is 0 - stop
        print("Stopping")
        break

    if num == 13: #If there is 13 - skip it
        num13 += 1
        continue #pass does nothing but continue the code, while continue skips that number

    if num > 0: #If positive - add to pos
        pos += 1

    elif num < 0: #If negative - add to neg
        neg += 1

    total_sum += num #Total sum
    count += 1 #Count of numbers

    if min_num is None:
        min_num = num
        max_num = num

    if num < min_num:
        min_num = num

    if num > max_num:
        max_num = num


if count == 0:
    print("No data")
else:
    summary = [
    f"Positive: {pos} | Negative: {neg}",
    f"Count: {count} | Total: {total_sum} | 13s: {num13}",
    f"Minimum: {min_num} | Maximum: {max_num}"
]
    for i in range(3):
        print(i+1, summary[i])
