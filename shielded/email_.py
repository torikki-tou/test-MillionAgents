from shielded.base import BaseShielded


class EmailShielded(BaseShielded):
    def __init__(self, skype: str):
        super(EmailShielded, self).__init__(skype)

    def shield_value(self):
        name, domain = self.raw_value.split('@')
        return f'{"x" * len(name)}@{domain}'


if __name__ == '__main__':
    print(EmailShielded('username@gmail.com'))
    print(EmailShielded('uname@gmail.com'))
