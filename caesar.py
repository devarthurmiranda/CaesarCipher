# Unicode link - https://en.wikipedia.org/wiki/List_of_Unicode_characters
# All letters start at 65

def encrypt(text, shift):
    result = ""
    for l in range(len(text)):
        char = text[l]
        if char.isupper():
            # remove 65 to normalize the letter (A = 0, B = 1 and so on...)
            # modulo ensures that after shifting, the result stays within the bounds of the alphabet
            # If the shift causes the character to go outside the range of A-Z, this operation wraps it around.
            # For example, if a letter is shifted back beyond 'A', it wraps around to 'Z'.
            # +65 converts the zero-indexed result back to the correct uppercase letter.
            result += chr((ord(char) + shift - 65) % 26 + 65) 
        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # For non-alphabetic characters, just add them as they are
            result += char

    return result

def decrypt(text, shift):
    result = ""
    # Traverse each character in the text
    for i in range(len(text)):
        char = text[i]

        # Decrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # For non-alphabetic characters, just add them as they are
            result += char

    return result

# Test
text = "Hello, World!"
encrypted_text = encrypt(text, 3)
print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text {decrypt(encrypted_text, 3)}")