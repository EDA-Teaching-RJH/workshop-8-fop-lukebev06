import re
email = input("enter your email: ").strip()

if re.search(".+@.+", email):
    print("valid")

if re.search(r".+@.+\.ac.uk", email):
    print("valid ukc")
else:
    print("not ukc")



