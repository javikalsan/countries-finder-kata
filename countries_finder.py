class CountriesFinder(object):
    def normalize(self, text):
        return self.leave_only_letters(self.remove_white_spaces(self.transform_to_lowercase(self.remove_spanish_accentuation(text))))

    def leave_only_letters(self, text):
        allowed = list('abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ ')
        for index, item in enumerate(text):
            if item not in allowed:
                text = text.replace(item, '')
        return text.replace('  ', ' ')

    def remove_white_spaces(self, text):
        return text.replace(' ', '')

    def transform_to_lowercase(self, text):
        return text.lower()

    def remove_spanish_accentuation(self, text):
        _text = list(text)
        for index, letter in enumerate(_text):
            if letter == 'á':
                _text[index] = 'a'
            if letter == 'é':
                _text[index] = 'e'
            if letter == 'í':
                _text[index] = 'i'
            if letter == 'ó':
                _text[index] = 'o'
            if letter == 'ú':
                _text[index] = 'u'
            if letter == 'Á':
                _text[index] = 'A'
            if letter == 'É':
                _text[index] = 'E'
            if letter == 'Í':
                _text[index] = 'I'
            if letter == 'Ó':
                _text[index] = 'O'
            if letter == 'Ú':
                _text[index] = 'U'
        return ''.join(_text)

    def find(self, countries, text):
        matches = []
        text_normalized = self.normalize(text)
        for country in countries:
            if self.normalize(country) in text_normalized:
                matches.append(country)
        return matches
