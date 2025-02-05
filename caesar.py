# Unicode link - https://en.wikipedia.org/wiki/List_of_Unicode_characters
# All letters start at 65

import time

def encrypt_modular(text, shift):
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

def decrypt_modular(text, shift):
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

def encrypt(text, shift):
    result = ""

    # Traverse each character in the text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase letters
        if char.isupper():
            # Shift character
            shifted = ord(char) + shift
            # Check if the shifted character goes beyond 'Z'
            if shifted > ord('Z'):
                # Wrap around to the beginning of the alphabet
                shifted -= 26
            result += chr(shifted)

        # Encrypt lowercase letters
        elif char.islower():
            # Shift character
            shifted = ord(char) + shift
            # Check if the shifted character goes beyond 'z'
            if shifted > ord('z'):
                # Wrap around to the beginning of the alphabet
                shifted -= 26
            result += chr(shifted)

        else:
            # Non-alphabet characters remain unchanged
            result += char

    return result


def decrypt(text, shift):
    result = ""

    # Traverse each character in the text
    for i in range(len(text)):
        char = text[i]

        # Decrypt uppercase letters
        if char.isupper():
            # Shift character
            shifted = ord(char) - shift
            # Check if the shifted character is before 'A'
            if shifted < ord('A'):
                # Wrap around to the end of the alphabet
                shifted += 26
            result += chr(shifted)

        # Decrypt lowercase letters
        elif char.islower():
            # Shift character
            shifted = ord(char) - shift
            # Check if the shifted character is before 'a'
            if shifted < ord('a'):
                # Wrap around to the end of the alphabet
                shifted += 26
            result += chr(shifted)

        else:
            # Non-alphabet characters remain unchanged
            result += char

    return result

# Test
st1 = time.time()
text = "This is some confidential Roman empire information writen by Julius Caesar! Fighting! Nulla quis leo blandit, maximus libero sed, imperdiet felis. Maecenas non euismod elit, et mattis lorem. Sed consequat, nibh id dapibus porta, dolor velit scelerisque eros, eu tincidunt felis sem sed erat. Fusce eget ante libero. Suspendisse viverra erat sit amet metus pharetra, vitae cursus tellus porttitor. Curabitur vitae hendrerit est, ac fringilla odio. Duis mollis fringilla enim. Fusce consectetur scelerisque ex, et eleifend libero fringilla id. In magna tortor, sagittis vel commodo gravida, tempor id libero. Cras id condimentum dui."
encrypted_text = encrypt_modular(text, 3)
print(f"\n\nEncrypted text: {encrypted_text}")
print(f"\nDecrypted text {decrypt_modular(encrypted_text, 3)}")
et1 = time.time()
print(f"Elapsed time (modular): {et1 - st1}")

st2 = time.time()
text = "This is some confidential Roman empire information writen by Julius Caesar! Fighting! Nulla quis leo blandit, maximus libero sed, imperdiet felis. Maecenas non euismod elit, et mattis lorem. Sed consequat, nibh id dapibus porta, dolor velit scelerisque eros, eu tincidunt felis sem sed erat. Fusce eget ante libero. Suspendisse viverra erat sit amet metus pharetra, vitae cursus tellus porttitor. Curabitur vitae hendrerit est, ac fringilla odio. Duis mollis fringilla enim. Fusce consectetur scelerisque ex, et eleifend libero fringilla id. In magna tortor, sagittis vel commodo gravida, tempor id libero. Cras id condimentum dui."
encrypted_text = encrypt(text, 3)
print(f"\n\nEncrypted text: {encrypted_text}")
print(f"\nDecrypted text {decrypt(encrypted_text, 3)}")
et2 = time.time()
print(f"Elapsed time (not modular): {et2 - st2}")
