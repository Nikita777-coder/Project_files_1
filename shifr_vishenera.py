word, secret_str, k_s, alphabet = input("Введите слово: "), "", input("Введите секретное слово: "), "abcdefghijklmnopqrstuvwxyz"

for i in range(len(word)):
    if word[i] in alphabet:
        secret_str += alphabet[(alphabet.find(k_s[i % (len(k_s))].lower()) + alphabet.find(word[i]) + 1) % len(alphabet)]
    else:
        secret_str += alphabet[(alphabet.find(k_s[i % (len(k_s))].lower()) + alphabet.find(word[i].lower()) + 1) % len(alphabet)].upper()

print(secret_str)