import re

email = input("enter an email: ").strip()

if re.search(r"^\w+@\w.+\.ac.uk$", email):
    print("s")

if re.search(r"^\w+@\w.+\.(ac.uk | gov.uk | nhs.net)$", email):
    print("or ending check")

