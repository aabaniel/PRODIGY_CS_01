
def caesar_cipher(sentence, shift_val):
    output = ""
    for char in sentence:
        if char.isalpha():
            if char.isupper():
                output += chr((ord(char) - 65 + shift_val) % 26 + 65)
            else:
                output += chr((ord(char) - 97 + shift_val) % 26 + 97)
        else:
            output += char
    return output

print("Mode of Caesar cipher")
choice = int(input("Cipher [1] or Decipher [2]: "))

sentence = input("Enter a sentence: ")

shift_val = int(input("Enter the shift value: "))

if choice == 1:
    output = caesar_cipher(sentence, shift_val)
    print("Ciphered sentence:", output)

elif choice == 2:
    deciphered_sentence = caesar_cipher(sentence, -shift_val)
    print("Deciphered sentence:", deciphered_sentence)

else:
    print("Inputted mode is incorrect!")

input("")
