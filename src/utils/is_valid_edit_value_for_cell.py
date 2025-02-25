from utils.is_valid_verifiers import IsValidVerifiers

# The methods in this class checks if the new value that will overwrite the old value in the table is valid


class IsValidEditValueForCell:

    @staticmethod
    def for_students_cell(index, value, id_numbers, full_names, data_from_csv):
        issue = ""
        valid = True

        if index.column() == 0 and value.strip() == "":
            issue = "ID number is blank"
            valid = False
        elif index.column() == 0 and not IsValidVerifiers.id_number(value.strip()):
            issue = "ID number not in correct format"
            valid = False
        elif index.column() == 0 and value.strip() in id_numbers:
            issue = "ID already exists"
            valid = False

        if index.column() == 1 and value.strip() == "":
            issue = "First name is blank"
            valid = False
        elif index.column() == 1 and not IsValidVerifiers.first_name(value.strip()):
            issue = "First name not in correct format"
            valid = False
        # Converts the old and new full names into all caps
        elif index.column() == 1 and f"{value.strip().upper()} {data_from_csv[index.row()][index.column() + 1].upper()}" in \
                [full_name.upper() for full_name in full_names]:
            issue = "Name combination exists"
            valid = False

        if index.column() == 2 and value.strip() == "":
            issue = "last name is blank"
            valid = False
        elif index.column() == 2 and not IsValidVerifiers.last_name(value.strip()):
            issue = "Last name not in correct format"
            valid = False
        elif index.column() == 2 and f"{data_from_csv[index.row()][index.column() - 1].upper()} {value.strip().upper()}" in \
                [full_name.upper() for full_name in full_names]:
            issue = "Name combination exists"
            valid = False

        if index.column() == 3 and value.strip() == "":
            issue = "Year level is blank"
            valid = False
        elif index.column() == 3 and value.strip() not in ["1st", "2nd", "3rd", "4th", "5th"]:
            issue = "Not valid year level"
            valid = False

        if index.column() == 4 and value.strip() == "":
            issue = "Gender is blank"
            valid = False
        if index.column() == 4 and value.strip() not in ["Male", "Female", "Others", "Prefer not to say"]:
            issue = "Not valid gender"
            valid = False

        return valid, issue

    @staticmethod
    def for_programs_cell(index, value, program_codes, program_names):
        issue = ""
        valid = True

        if index.column() == 0 and value.strip() == "":
            issue = "Program code is blank"
            valid = False
        elif index.column() == 0 and not IsValidVerifiers.program_code(value.strip()):
            issue = "Program code not in correct format"
            valid = False
        elif index.column() == 0 and value.strip().upper() in program_codes:
            issue = "Program code already exists"
            valid = False

        if index.column() == 1 and value.strip() == "":
            issue = "Program name is blank"
            valid = False
        elif index.column() == 1 and not IsValidVerifiers.program_name(value.strip()):
            issue = "Program name not in correct format"
            valid = False
        elif index.column() == 1 and value.strip().upper() in \
                [program_name.upper() for program_name in program_names]:
            issue = "Program name already exists"
            valid = False

        return valid, issue

    @staticmethod
    def for_colleges_cell(index, value, college_codes, college_names):
        issue = ""
        valid = True

        if index.column() == 0 and value.strip() == "":
            issue = "College code is blank"
            valid = False
        elif index.column() == 0 and not IsValidVerifiers.college_code(value.strip()):
            issue = "College code not in correct format"
            valid = False
        elif index.column() == 0 and value.strip().upper() in college_codes:
            issue = "College code already exists"
            valid = False

        if index.column() == 1 and value.strip() == "":
            issue = "College name is blank"
            valid = False
        elif index.column() == 1 and not IsValidVerifiers.college_name(value.strip()):
            issue = "College name not in correct format"
            valid = False
        elif index.column() == 1 and value.strip().upper() in \
                [college_name.upper() for college_name in college_names]:
            issue = "College name already exists"
            valid = False

        return valid, issue
