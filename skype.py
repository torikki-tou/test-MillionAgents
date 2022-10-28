

class SkypeShielded:
    def __init__(self, skype: str):
        self._raw_skype = skype
        self.raw_skype = self._raw_skype

    @property
    def raw_skype(self):
        return self._raw_skype

    @raw_skype.setter
    def raw_skype(self, value):
        self._raw_skype = value
        self.shielded_skype = self.shield_skype()

    def shield_skype(self):
        _, left_part = self.raw_skype.split('skype:')
        strings_list = left_part.split('?')
        return self.raw_skype.replace(strings_list[0], 'xxx')

    def __str__(self):
        return self.shielded_skype


if __name__ == '__main__':
    print(SkypeShielded('skype:alex.max'))
    print(SkypeShielded('<a href=\"skype:alex.max?call\">skype</a>'))
