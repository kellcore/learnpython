i = 0
numbers = []

while i < 6:
    print(f"At the top, i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print("At the bottom, i is {i}")

print("The numbers: ")

for num in numbers:
    print(num)


def test_loop(total, iterator):
    i = 0
    numbers = []

    while i < total:
        print(f"At the top, i is {i}")
        numbers.append(i)
        i = i + iterator
        print("Numbers now: ", numbers)
        print(f"At the bottom, i is {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)


test_loop(10, 2)


def for_test_loop():
    test_list = []
    for i in range(0, 7, 2):
        print(f"Here comes number {i}")
        test_list.append(i)


for_test_loop()
