class NumberInscriptionBuilder:
    SINGLE_DIGITS = ['', 'jeden', 'dwa', 'trzy', 'cztery', 'pięć', 'sześć', 'siedem', 'osiem', 'dziewięć']

    TEN_NUMBERS = ['dziesięć', 'jedenaście', 'dwanaście', 'trzynaście', 'czternaście',
                    'piętnaście', 'szesnaście', 'siedemnaście', 'osiemnaście', 'dziewiętnaście']

    TEN_MULTIPLES = ['', '', 'dwadzieścia', 'trzydzieści', 'czterdzieści', 'pięćdziesiąt', 'sześćdziesiąt',
                     'siedemdziesiąt', 'osiemdziesiąt', 'dziewięćdziesiąt']

    HUNDRED_MULTIPLES = ['', 'sto', 'dwieście', 'trzysta', 'czterysta', 'pięćset',
                         'sześćset', 'siedemset', 'osiemset', 'dziewięćset']

    BIG_NUMBERS = [
        {'l_poj': '', 'mianownik': '', 'dopelniacz': ''},
        {'l_poj': 'tysiąc', 'mianownik': 'tysiące', 'dopelniacz': 'tysięcy'},
        {'l_poj': 'milion', 'mianownik': 'miliony', 'dopelniacz': 'milionów'},
        {'l_poj': 'miliard', 'mianownik': 'miliardy', 'dopelniacz': 'miliardów'},
        {'l_poj': 'bilion', 'mianownik': 'biliony', 'dopelniacz': 'bilionów'}
    ]

    def __init__(self, number: str) -> None:
        self.inscription = None
        self.number = number
        self._process_number()

    @classmethod
    def max_numbers(cls):
        return len(cls.BIG_NUMBERS) * 3

    def _fill_with_zeros(self) -> None:
        """
        changes self.number with zeros at begin until number of digits is divisible by 3,
        i.e. '1234' is changed to '001234'
        """
        while len(self.number) % 3 != 0:
            self.number = f'0{self.number}'

    def _split_into_groups_by_three(self) -> None:
        """
        changes self.number so it's list with groups of 3 digits,
        i.e. '001234' is changed to ['001', '234']
        """
        self.number = [(self.number[i:i+3]) for i in range(0, len(self.number), 3)]

    def _reverse_groups_list(self) -> None:
        """
        flips groups list,
        so self.numbers starts with smallest numbers (units) and ends with biggest numbers (i.e. millions)
        """
        self.number = list(reversed(self.number))

    def _process_number(self) -> None:
        """
        processes string so WordNumberBuilder can easily read its groups of numbers
        """
        self._fill_with_zeros()
        self._split_into_groups_by_three()
        self._reverse_groups_list()

    @staticmethod
    def _get_big_number_form(digit: str, is_ten_number: bool) -> str:
        """
        :param digit: last digit from group
        :param is_ten_number: tells if group has ten_number
        :return: key from self.BIG_NUMBERS dictionaries, so program can now how to name group in polish properly
        """
        if digit in ('0', '5', '6', '7', '8', '9') or is_ten_number:
            return 'dopelniacz'
        if digit in ('2', '3', '4'):
            return 'mianownik'
        return 'l_poj'

    @staticmethod
    def _has_ten_number(three_digits: str) -> bool:
        """
        :param three_digits: group of three digits, i.e. '123'
        :return: True if group ends with ten number (between 10 and 19)
        """
        return three_digits[1] == '1'

    @staticmethod
    def _is_group_empty(group) -> bool:
        return group == '000'

    @staticmethod
    def _has_hundred_multiples_number(group) -> bool:
        return group[0] != '0'

    @staticmethod
    def _has_ten_multiples_number(group) -> bool:
        return group[1] != '0'

    @staticmethod
    def _has_units_number(group) -> bool:
        return group[2] != '0'

    def _is_zero(self):
        for group in self.number:
            if any(map(lambda x: x != '0', group)):
                return False
        return True

    def _read_three_digits(self, group: str) -> str:
        """
        :param group: group of three digits, i.e. '123'
        :return: inscription of group of three digits, i.e. 'sto dwadzieścia trzy'
        """
        if group == '000':
            return ''
        if self._has_ten_number(group):
            small_output = f'{self.TEN_NUMBERS[int(group[2])]}'
        else:
            has_units_number = self._has_units_number(group)
            has_ten_multiples_number = self._has_ten_multiples_number(group)
            small_output = ''
            if has_units_number and has_ten_multiples_number:
                small_output = f'{self.TEN_MULTIPLES[int(group[1])]} {self.SINGLE_DIGITS[int(group[2])]}'
            elif not has_units_number:
                small_output = f'{self.TEN_MULTIPLES[int(group[1])]}'
            elif not has_ten_multiples_number:
                small_output = f'{self.SINGLE_DIGITS[int(group[2])]}'
        if self._has_hundred_multiples_number(group):
            small_output = f' {small_output}' if small_output else small_output
            small_output = f'{self.HUNDRED_MULTIPLES[int(group[0])]}{small_output}'
        return f'{small_output}'

    def build_inscription(self) -> None:
        if self._is_zero():
            self.inscription = 'zero'
            return
        self.inscription = ''
        for num, digits in enumerate(self.number, start=0):
            digits_word = self._read_three_digits(digits)
            if not self._is_group_empty(digits):     # we don't have to mention group if it's empty
                digits_big_number_form = self.BIG_NUMBERS[num][self._get_big_number_form(digits[2],
                                                                                         self._has_ten_number(digits))]
                self.inscription = f'{digits_word} {digits_big_number_form} {self.inscription}'.rstrip()

    def set_number(self, number: str) -> None:
        self.number = number
        self.inscription = None

    def get_inscription(self) -> str:
        """
        :return: built inscription. If needed, builds it when called.
        """
        if self.inscription is None:
            self.build_inscription()
        return self.inscription
