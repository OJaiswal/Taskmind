def is_valid_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    has_space = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in "!@#$":
            has_special = True
        elif char.isspace():
            has_space = True

    return (
        7 <= len(password) <= 20 and
        has_upper and
        has_lower and
        has_digit and
        has_special and
        not has_space
    )