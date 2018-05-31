print("This is your journal app! We should start by making you account")
def account_details(name, age, gender):
    details = {
        'Name':name,
        'Age':age,
        'Gender':gender
    }
    return details

name = str(input("What is your first name?: "))
print("Ok " + (name) + " lets start your account")
age = int(input("what's your age?: "))
gender = str(input("What is your sex?: "))

details = account_details((name), (age), (gender))
print(details)

while True:
    first_entry = input("please enter your activities: ")
    if first_entry == True:
        print ("ok next entry!")
    elif first_entry == "Delete entry":
        entry_delete = input("which entry would you like to delete?: ")
        print("ok entry " + (entry_delete)+ " has been deleted")
    elif first_entry == "Exit entry":
        print("Goodbye!")
