

class EmailShielded:
    def __init__(self, email: str):
        self.raw_email = email

    @property
    def shielded_email(self):
        name, domain = self.raw_email.split('@')
        return f'{"x" * len(name)}@{domain}'

    def __str__(self):
        return self.shielded_email


if __name__ == '__main__':
    print(EmailShielded('username@gmail.com'))
    print(EmailShielded('uname@gmail.com'))
