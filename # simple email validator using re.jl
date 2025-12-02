# simple email validator using re
import re

EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")

def is_valid_email(email: str) -> bool:
    return bool(EMAIL_RE.fullmatch(email))

if __name__ == "__main__":
    samples = [
        "alice@example.com",           # valid
        "bob.smith+tag@gmail.com",     # valid
        "user_name-100@sub.domain.co", # valid
        "user@localhost",              # invalid (no TLD)
        "invalid@@example.com",        # invalid (two @)
        ".startdot@domain.com",        # invalid (starts with dot)
        "name@domain..com",            # invalid (double dot)
        "한글@domain.com",             # invalid (non-ascii local part)
        "user@domain.c",               # invalid (TLD too short)
        "user@-domain.com",            # invalid (domain starts with hyphen)
    ]

    for s in samples:
        print(f"{s:30} -> {'OK' if is_valid_email(s) else 'INVALID'}")