

class PhoneNumberShielded:
    def __init__(self, phone_number: str, simbols: int = 3):
        self.simbols = simbols
        self._raw_phone_number = phone_number
        self.raw_phone_number = self._raw_phone_number

    @property
    def raw_phone_number(self):
        return self._raw_phone_number

    @raw_phone_number.setter
    def raw_phone_number(self, value):
        self._raw_phone_number = value
        self.shielded_phone_number = self.shield_phone_number()

    def shield_phone_number(self):
        new_str = ''
        count = 0
        for char in self.raw_phone_number[::-1]:
            if char.isdigit() and count < self.simbols:
                new_str += 'x'
                count += 1
            else:
                new_str += char
        return new_str[::-1]

    def __str__(self):
        return self.shielded_phone_number


if __name__ == '__main__':
    print(PhoneNumberShielded('+7-937-663-40-90'))
