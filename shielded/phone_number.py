from shielded.base import BaseShielded


class PhoneNumberShielded(BaseShielded):
    def __init__(self, phone_number: str, simbols: int = 3):
        self.simbols = simbols
        super(PhoneNumberShielded, self).__init__(phone_number)

    def shield_value(self):
        new_str = ''
        count = 0
        for char in self.raw_value[::-1]:
            if char.isdigit() and count < self.simbols:
                new_str += 'x'
                count += 1
            else:
                new_str += char
        return new_str[::-1]


if __name__ == '__main__':
    print(PhoneNumberShielded('+7-800-555-35-35'))
    print(PhoneNumberShielded('+7 800 555 35 35'))
    print(PhoneNumberShielded('+798005553535'))
    print(PhoneNumberShielded('+7-800-555-35-35', 4))
    print(PhoneNumberShielded('+7 800 555 35 35', 1))
    print(PhoneNumberShielded('+798005553535', 20))
