def check_unique(alphabet):
    check_unique = ""
    for i in alphabet:
        if i not in check_unique:
            check_unique += i
    return len(check_unique)

word, secret_str, secret_word, alphabet, unique = input("Введите слово: "), "", input("Введите секретное слово: "), input("Введите алфавит: "), ""
maximum, lenght_word, lenght_s_word = max(len(word), len(secret_word)), len(word), len(secret_word)

for i in range(maximum):
    if i < lenght_word and word[i] not in unique:
        unique += word[i]
    if i < lenght_s_word and secret_word[i] not in unique:
        unique += secret_word[i]
while len(alphabet) < maximum or len(unique) > check_unique(alphabet):
    alphabet = input("Длина алфавита меньше чем слова или секретного слова или количество уникальных элементов алфавита меньше чем количество элементов в обычном и секретном словах вместе. Введите корректный алфавит: ")

for i in range(len(word)):
    secret_str += alphabet[(alphabet.find(secret_word[i % (len(secret_word))]) + alphabet.find(word[i]) + 1) % len(alphabet)]

print(secret_str)