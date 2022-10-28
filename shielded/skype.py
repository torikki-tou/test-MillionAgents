from shielded.base import BaseShielded


class SkypeShielded(BaseShielded):
    def __init__(self, skype: str):
        super(SkypeShielded, self).__init__(skype)

    def shield_value(self):
        _, left_part = self.raw_value.split('skype:')
        strings_list = left_part.split('?')
        return self.raw_value.replace(strings_list[0], 'xxx')


if __name__ == '__main__':
    print(SkypeShielded('skype:alex.max'))
    print(SkypeShielded('<a href=\"skype:alex.max?call\">skype</a>'))
