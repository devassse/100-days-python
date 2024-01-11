#Encription and Decription

logo = '''
                       _                              _           
                      | |                            | |          
  ___ _ __ _   _ _ __ | |_ ___   __ _ _ __ __ _ _ __ | |__  _   _ 
 / __| '__| | | | '_ \| __/ _ \ / _` | '__/ _` | '_ \| '_ \| | | |
| (__| |  | |_| | |_) | || (_) | (_| | | | (_| | |_) | | | | |_| |
 \___|_|   \__, | .__/ \__\___/ \__, |_|  \__,_| .__/|_| |_|\__, |
            __/ | |              __/ |         | |           __/ |
           |___/|_|             |___/          |_|          |___/ 
'''

print(logo)
print("type 'Encode' to Encrypt secret and 'Decode' to Decrypt\n")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_length = len(alphabet)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(txt, shft):
    cipher_text = ""
    for letter in txt:
        position = alphabet.index(letter)
        new_position = position + shft

        if new_position > alphabet_length:
            print("Hey, whatch out the Limit")
        else:
            new_letter = alphabet[new_position]
            cipher_text += new_letter

    print(f"Shifted Word {cipher_text}")

def decrypt(txt, shft):
    cipher_text = ""
    for letter in txt:
        position = alphabet.index(letter)
        new_position = position - shft
        new_letter = alphabet[new_position]
        cipher_text += new_letter

    print(f"UnShifted Word {cipher_text}")

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
    