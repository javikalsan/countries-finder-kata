#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mamba import description, context, it, before
from expects import expect, equal

from countries_finder import CountriesFinder


with description('Find countries in a text') as self:
    with before.each:
        self.cf = CountriesFinder()

    with context('Given a Spanish input text'):
        with context('when normalizes text'):
            with it('-removes white spaces'):
                TEXT_WITH_WHITE_SPACES = 'This is my text'

                text_normalized = self.cf.remove_white_spaces(TEXT_WITH_WHITE_SPACES)

                expect(text_normalized).to(equal('Thisismytext'))

            with it('-leaves only words'):
                TEXT_WITH_WORDS_SYMBOLS_AND_NUMBERS = 'This is my 1 text. I am happy @ home'

                text_normalized = self.cf.leave_only_letters(TEXT_WITH_WORDS_SYMBOLS_AND_NUMBERS)

                expect(text_normalized).to(equal('This is my text I am happy home'))

            with it('-transforms to lowercase'):
                TEXT_WITH_UPPERCASE_LETTERS = 'This is mY InCredibLE caT'

                text_normalized = self.cf.transform_to_lowercase(TEXT_WITH_UPPERCASE_LETTERS)

                expect(text_normalized).to(equal('this is my incredible cat'))

            with it('-removes Spanish accentuation'):
                TEXT_WITH_SPANISH_ACCENTUATION = 'El pÍ del balcÓn está pérdido'

                text_normalized = self.cf.remove_spanish_accentuation(TEXT_WITH_SPANISH_ACCENTUATION)

                expect(text_normalized).to(equal('El pI del balcOn esta perdido'))

        with context('when searches for countries'):
            with it('-returns found countries'):
                COUNTRIES = ['Antártida', 'Italia', 'España']
                TEXT = 'En un antar ti dala, vivía 1 pit al iamado pepe'

                text_normalized = self.cf.find(COUNTRIES, TEXT)

                expect(text_normalized).to(equal(['Antártida', 'Italia']))
