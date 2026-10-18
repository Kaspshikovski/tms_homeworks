class SuperStr(str):

    def is_repeatance(self, elem):
        if not self or not elem:
            return False

        return self == elem * (len(self) // len(elem))

    def is_palindrom(self):
        return self.lower() == self[::-1].lower()
