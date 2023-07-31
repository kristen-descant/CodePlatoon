from django.core.exceptions import ValidationError
import re

def validate_school_email(student_email):
    error_message = 'Email must be from school domain'
    
    regex = r"^(Professor)\s.*"

    good_email = re.match(regex, student_email)

    if good_email:
        return good_email
    else:
        raise ValidationError(error_message, params={'student_email': student_email})
    

print(validate_school_email('ProfessorAdam'))
# print(validate_school_email('kristen@notschool.com'))