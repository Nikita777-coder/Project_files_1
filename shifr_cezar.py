word = input("Введите слово: ")
secret_str = "" 

for i in word: 
    secret_str += chr(ord(i) + 3)

print(secret_str)