import re

#\d and {m}

phone = input("enter a british phone number: ").strip()

pnp = r"^07\d{9}$"
# pnp = phone number pattern
if re.search(pnp,phone):
    print("that is a valid uk number")

#     -- error validation --
else:
    if len(phone) != 11:
        print("number must be 11 digits long.")
    elif not phone.startswith("07"):
        print("number must start with 07")
    elif not phone.isdigit():
        print("must only contain numbers")
    else:
        print("invalid")