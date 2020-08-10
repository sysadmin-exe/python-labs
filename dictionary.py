#declaring key-value for dictionary
user1 = {
    "fname": "victor",
    "lname": "efedi",
    "profession": "engineer",
    "country": "Nigeria"
}
#uing get to get the value of a key in a dictionary 
user1_country = user1.get("country")
user1_fname = user1.get("fname")
print(user1_fname + " is from " + user1_country)

#using keys to check if a dictionary key is available
if "country" in user1.keys():
    print("user country available")
else:
    print("user country not available")