import secrets
import string


def check_password(password):
    if len(password) < 4:
        return False
    if any(c.isspace() for c in password):
        return False
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_special = any(c in string.punctuation for c in password)
    has_number = any(c.isdigit() for c in password)
    return has_lower and has_upper and has_special and has_number

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    punctuation = string.punctuation
    all_characters = lowercase + uppercase + numbers + punctuation

    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(numbers),
        secrets.choice(punctuation),
    ]
    password.extend(
        secrets.choice(all_characters) for _ in range(length - len(password))
    )
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def main():
    print(f"Your password is: {generate_password()}")


if __name__ == "__main__":
    main()