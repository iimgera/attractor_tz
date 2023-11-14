class CesarCipher(object):
    _alphabet = None
    _shift = None

    def set_alphabet(self, value):
        self._alphabet = value

    def set_shift(self, value):
        self._shift = value

    def encode(self, plain_text):
        if self._alphabet is None or self._shift is None:
            raise ValueError("First set the alphabet and shift.")

        encoded_text = ""
        for char in plain_text:
            if char.lower() in self._alphabet:
                is_upper = char.isupper()
                char = char.lower()
                encoded_char = self._shift_char(char, is_upper)
                encoded_text += encoded_char
            else:
                encoded_text += char

        return encoded_text

    def _shift_char(self, char, is_upper):
        char_index = (self._alphabet.index(char) + self._shift) % len(self._alphabet)
        return self._alphabet[char_index].upper() if is_upper else self._alphabet[char_index]


cipher = CesarCipher()
cipher.set_alphabet("abcdefghijklmnopqrstuvwxyz")
cipher.set_shift(3)

source_text = "The quick brown fox jumps over the lazy dog"
encrypted_text = cipher.encode(source_text)
print("Source text:", source_text)
print("Encrypted text:", encrypted_text)
