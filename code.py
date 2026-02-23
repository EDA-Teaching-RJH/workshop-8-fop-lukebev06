email = input("what's your email? ").strip()

if "@" in email and "." in email:
    print("valid")
else:
    print("invalid")

username, domain = email.split("@")

if username and domain.endswith(".ac.uk"):
    print("Valid")