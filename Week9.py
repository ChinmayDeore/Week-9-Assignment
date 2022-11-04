## Chinmay D. 10/27/2022 Hg5590
def WorkTicket():
# Naming and starting the function
    dictionary = {"Field": "Fields", "UniqueID": "Name", "Randomly generated Decimal":"Employees"}
    print(type(dictionary))
    print(dictionary)
# Creates a dictionary to store all the employee information
    print("Enter Employee Information");
    dictionary["Field"] = input("Name: ");
    dictionary["UniqueID"] = input("Address: ");
    dictionary["Randomly generated Decimal"] = input("String Value: ");
    print(dictionary)
# Creates and prints an entry for Employee address  
    dictionary["Field"] = input("Name: ");
    dictionary["UniqueID"] = input("Phone: ");
    dictionary["Randomly generated Decimal"] = input("String Value: ");
    print(dictionary) 
# Creates and prints an entry for Employee phone number
    dictionary["Field"] = input("Name: ");
    dictionary["UniqueID"] = input("Social Security Number: ");
    dictionary["Randomly generated Decimal"] = input("String Value: ");    
    print(dictionary) 
# Creates and prints an entry for Employee SSN
    dictionary["Field"] = input("Name: ");
    dictionary["Yes or No String: "] = input("Manager? ");
    dictionary["Randomly generated Decimal"] = input('String Value: ');  
    print(dictionary) 
# Creates and prints an entry based on whether or not the Employee has a manager.
    dictionary["Field"] = input("Name: ");
    dictionary["UniqueID"] = input("Job Title: ");
    dictionary["Randomly generated Decimal"] = input("String Value: ");       
    print(dictionary) 
# Creates and prints an entry for Employee's job title
    dictionary["Field"] = input("Name: ");
    dictionary["UniqueID"] = input("Skills: ");
    dictionary["Randomly generated Decimal"] = input("String Value: ");   
    print(dictionary) 
# Creates and prints an entry for Employee's skills
WorkTicket()
# Calls the function and ends the program