
# email=input("What's your email ? ").strip()

# if '@' in email:
#     print("Valid")
# else:
#     print("In valid")



# username,domain=email.split('@')
# if username and domain.endswith('.edu'):
#     print("Valid")
# else:
#     print("In valid")



# import re
# email=input("What's your email ? ").strip()

# if re.search(r'^[^@]+@[^@]+\.edu$', email):
#     print("valid")
# else:
#     print("In valid")


# import re
# email=input("What's your email ? ").strip()

# if re.search(r'^[a-zA-Z0-9_]+@[a-zA-z0-9_]+\.edu$', email):
#     print("valid")
# else:
#     print("In valid")


# import re
# email=input("What's your email ? ").strip()

# if re.search(r'^\w+@(\w\.)?\w+\.edu$', email, re.IGNORECASE):
#     print("valid")
# else:
#     print("In valid")

# # re.fullmatch() no need of $ at end
# #re.match() no need of ^ and start