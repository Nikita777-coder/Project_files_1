word = input("Введите слово: ")
secret_str, alphabet = "", "abcdefghijklmnopqrstuvwxyz"

for i in word: 
    if i in alphabet:
        secret_str += alphabet[(alphabet.find(i) + 3) % len(alphabet)]
    else:
        secret_str += alphabet[(alphabet.find(i.lower()) + 3) % len(alphabet)].upper()

print(secret_str)