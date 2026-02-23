import re

email = input("enter an email: ").strip()

if re.search(r"^.+@.+\.ac.uk$", email):
    print("format")

if re.search(r"^[^@]+@[^@]+\.ac.uk$", email):
    print("single @")

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.ac.uk$", email):
    print("letters no symbols")
