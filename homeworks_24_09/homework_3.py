import json

with open(input(), 'r', encoding='utf-8') as read_file, open(input(), 'w', encoding='utf-8') as write_file:
    data: dict[str, list[str]] = json.load(read_file)

    for line in data.values():
        word_counts = {}
        
        for word in line:
            word_counts[word] = word_counts.get(word, 0) + 1

        word = max(word_counts, key=word_counts.get)

        write_file.write(f'{word}: {word_counts[word]}\n')
