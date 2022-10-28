
class BaseShielded:
    def __init__(self, value: str):
        self._raw_value = value
        self.raw_value = self._raw_value

    @property
    def raw_value(self):
        return self._raw_value

    @raw_value.setter
    def raw_value(self, value):
        self._raw_value = value
        self.shielded_value = self.shield_value()

    def shield_value(self):
        raise NotImplementedError

    def __str__(self):
        return self.shielded_value
