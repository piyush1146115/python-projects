import json

def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    person = {"name": name, "age": age, "email": email}
    return person

def delete_contact(people):
    display_people(people)

    while True:
        number = input("Enter a number to delete: ")

        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range")
            else:
                break
        except:
            print("Invalid number")
    people.pop(number - 1)
    print("Person deleted!")


def display_people(people):
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])


def search(people):
    search_name = input("Search for a name: ").lower()
    results = []

    for person in people:
        name = person["name"]
        if search_name in name.lower():
            results.append(person)
   
    display_people(results)




print("Hi, welcome to the Contact Management System.")
print()

with open("contacts.json", "r") as f:
    people = json.load(f)["contacts"]

# people = [
#     {"name": "PK", "age":14, "email": "pk@gmail.com"},
#     {"name":"Piyush", "age":15, "email": "piyush@gmail.com"},
#     {"name": "Trump", "age": 80, "email": "trump@gmail.com"}
# ]

while True:
    print()
    print("Contact list size:", len(people))
    command = input("You can 'Add', 'Delete' or 'Search' and 'Q' for quit : ").lower()    

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person Added")
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search(people)
    elif command == "q":
        break
    else:
        print("Invalid command.")

    # print(people)

with open("contacts.json", "w") as f:
    json.dump({"contacts": people}, f)