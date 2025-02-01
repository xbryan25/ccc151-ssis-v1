import re


class IsValidVerifiers:
    @staticmethod
    def id_number(id_number):
        valid_id_number = re.match(r'^[0-9]{4}-[0-9]{4}$', id_number)

        return True if valid_id_number else False

    @staticmethod
    def first_name(first_name):
        valid_first_name = re.match(r'^[a-zA-Z ]+$', first_name)

        return True if valid_first_name else False

    @staticmethod
    def last_name(last_name):
        valid_last_name = re.match(r'^[a-zA-Z ]+$', last_name)

        return True if valid_last_name else False

    @staticmethod
    def program_code(program_code):
        valid_program_code = re.match(r'^[a-zA-Z]{3,}$', program_code)

        return True if valid_program_code else False

    @staticmethod
    def program_name(program_name):
        valid_program_name = re.match(r'^[a-zA-Z, ]+$', program_name)

        return True if valid_program_name else False
