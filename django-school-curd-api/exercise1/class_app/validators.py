from django.core.exceptions import ValidationError
import re

def validate_subject_format(subject):
    error_message = "Subject must be in title case format."

    regex = r"^(?:\b[A-Z][a-z]+\b\s*)+$"

    if not re.match(regex, subject):
        raise ValidationError(error_message, params={'subject': subject})
    
def validate_professor_name(professor):
    error_message = 'Professor name must be in the format "Professor Adam".'

    regex = r"^(Professor)\s.*"

    if not re.match(regex, professor):
        raise ValidationError(error_message, params={'professor': professor})