#declaring key-value for dictionary
user1 = {
    "fname": "victor",
    "lname": "efedi",
    "profession": "engineer",
    "country": "Nigeria"
}

user1_country = user1.get("country")
user1_fname = user1.get("fname")
print(user1_fname + " is from " + user1_country)

if "country" in user1.keys():
    print("user country available")
else:
    print("user country not available")