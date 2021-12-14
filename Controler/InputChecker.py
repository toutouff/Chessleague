class Checkinput:
    def __init__(self):
        pass

    @staticmethod
    def int(question):
        is_valid = False
        while is_valid is False:
            entry = input(question)
            is_valid = Checkinput.int_tester(entry)
        return entry

    @staticmethod
    def str(question):
        is_valid = False
        while is_valid is False:
            entry = input(question)
            is_valid = Checkinput.str_tester(entry)
        return entry

    @staticmethod
    def pair(question):
        is_valid = False
        while is_valid is False:
            entry = input(question)
            is_valid = Checkinput.int_pair_tester(entry)
        return entry

    @staticmethod
    def int_tester(value):
        try:
            int(value)
            return True
        except ValueError:
            return False

    @staticmethod
    def str_tester(value):
        try:
            int(value)
            return False
        except ValueError:
            return True

    @staticmethod
    def int_pair_tester(value):
        is_int = Checkinput.int_tester(value)
        if is_int is True:
            test = int(value) % 2
            if test == 0:
                return True
            else:
                return False
        else:
            return False
