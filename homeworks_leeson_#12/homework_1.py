from collections.abc import Iterator


def generate_fibonacci(number: int) -> Iterator[int]:
    if number < 0:
        raise ValueError("Количество чисел не может быть отрицательным")

    a, b = 0, 1

    if number >= 1:
        yield a

    if number >= 2:
        yield b

    for _ in range(number - 2):
        a, b = b, a + b
        yield b
    
    
number = int(input())
numbers = generate_fibonacci(number)

while True:
    try:
        print(next(numbers))
    except StopIteration:
        break
