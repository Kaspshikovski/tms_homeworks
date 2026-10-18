from collections.abc import Iterator


def generate_numbers() -> Iterator[int]:
    number = 1

    while True:
        yield number
        number += 1
    
        if number == 4:
            number = 1


steps = int(input())
numbers = generate_numbers()

for _ in range(steps):
    print(next(numbers))
