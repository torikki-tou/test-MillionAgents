

class EmailShielded:
    def __init__(self, email: str):
        self._raw_email = email
        self.raw_email = self._raw_email

    @property
    def raw_email(self):
        return self._raw_email

    @raw_email.setter
    def raw_email(self, value):
        self._raw_email = value
        self.shielded_email = self.shield_email()

    def shield_email(self):
        name, domain = self.raw_email.split('@')
        return f'{"x" * len(name)}@{domain}'

    def __str__(self):
        return self.shielded_email


if __name__ == '__main__':
    print(EmailShielded('username@gmail.com'))
    print(EmailShielded('uname@gmail.com'))
