import re
URI=input("What's the URI? ").strip()

# username=URI.replace("https://twitter.com","")
# username=URI.removeprefix("https://twitter.com")
# print(username)

# username=re.sub(r"(https?://)?(www\.)?twitter\.com","",URI)
# print(username)


# matches=re.search(r"^(https://)?(www\.)?twitter\.com/(.+)$",URI,re.IGNORECASE)
# if matches:
#     print(f"Username: {matches.group(1)}")


#warlus operator
if matches:=re.search(r"^(?:https://)?(?:www\.)?twitter\.com/([a-z0-9_]+)$",URI,re.IGNORECASE):
    print(f"Username: {matches.group(1)}")


# re.split(pattern, string, maxsplit=0, flags=0)




