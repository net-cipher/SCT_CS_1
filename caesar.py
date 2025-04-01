def caesar_cipher(text, shift):
	result = ""
	for char in text:
		if char.isalpha():
			shifted = chr(ord(char) + shift) if char.islower() else chr(ord(char) + shift)
			result += shifted
		else:
			result += char
	return result
text = input("Enter Text:")
shift = int(input("Enter shift value:"))
print("Encrypted text:", caesar_cipher(text, shift))
