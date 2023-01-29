
#An Email Simulation
class Email():
    has_been_read = False
    is_spam = False

    def __init__(self, email_contents, from_address):
        self.email_contents = email_contents
        self.from_address = from_address

    def mark_as_read(self):
        self.has_been_read = True

    def mark_as_spam(self):
        self.is_spam = True

#defining functions to manipulate the emails
def add_email(a, b):
    new_email = Email(a, b)
    inbox.append(new_email)

def get_count():
    return len(inbox)

def get_email(i):
    return(f"""
    Email: {inbox[i].email_contents}
    Sender: {inbox[i].from_address}
    """)

def get_unread_emails():
    unread_list = [] 
    #for each email, add to a new list if unread   
    for a in inbox:                 
        if a.has_been_read == False:
            unread_list.append(a)
    #if no emails were unread, none would be added to the list so len = 0
    if len(unread_list) == 0:       
        return("You have no unread emails.")
    #if at least one item was added to the list, they will be returned neatly
    else:                      
        emails = ""
        for item in unread_list:
            emails += (f"""
            Email: {item.email_contents}
            Sender: {item.from_address}\n""")
        return(emails)
            
def get_spam_emails():
    #new empty list, no spam currently
    spam_list = []      
    #append all items in Email class labelled with spam as True
    for a in inbox:
        if a.is_spam == True:       
            spam_list.append(a)
    #if nothing added to the list, must be no spam
    if len(spam_list) == 0:     
        return("You have no spam.")
    else:
        emails = ""
        #return spam list
        for item in spam_list:      
            emails += (f"""
            Email: {item.email_contents}
            Sender: {item.from_address}\n""")
        return(emails)

def delete(a):
    del inbox[a]



inbox = []


    

user_choice = ""

while user_choice != "quit":
    user_choice = input("\nWhat would you like to do - read/mark spam/send/delete/quit? ")
    if user_choice == "read":
        #return number of emails in inbox
        print(f"\nYou have {get_count()} emails.")      
        type = int(input("""Please choose an option:
        1 - all unread emails
        2 - a specific email
        """))

        if type == 1:
            print(get_unread_emails())

        elif type == 2:
            email_num = int(input("What is the index of the email would you like? "))
            #change has_been_read to True
            inbox[email_num].mark_as_read()     
            print(f"{get_email(email_num)}")
        else:
            print("That's not a valid option.")

    elif user_choice == "mark spam":
        #can't do mark_as_spam function with empty inbox list, avoid errors
        if len(inbox) == 0:         
                print("You have no emails.")    
        else:
            email_num = int(input("\nWhat's the index of the email you'd like to mark as spam? "))
            #change is_spam to True
            inbox[email_num].mark_as_spam()     
            view = input("\nWould you like to view all the spam, y/n? ")

            if view == "y":
                print(get_spam_emails())
                    
            elif view == "n":
                continue
            
    #sending to inbox
    elif user_choice == "send":     
        contents = input("Write email message: ") 
        address = input("What's your email address? ")
        #the function adds this as Email class to the inbox list
        add_email(contents, address)    

    elif user_choice == "delete":
        delete_email = int(input("\nWhat's the index of the email you'd like to delete? "))
        delete(delete_email)

    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
