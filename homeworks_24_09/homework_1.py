def copy_nonempty_lines(source_path: str, target_path: str) -> int:
    with open(source_path, 'r', encoding='utf-8') as file:
        data: list[str] = []

        for line in file.readlines():
            if line.strip():
                data.append(line.strip())

    with open(target_path, 'w', encoding='utf-8') as write_file:
        write_file.write('\n'.join(data))

    return len(data)
        

print(copy_nonempty_lines(input(), input()))
