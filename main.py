#import spy_detail
from spy_detail import spy,Spy,ChatMessage
from steganography.steganography import Steganography #library.class import module
from datetime import datetime
import csv

date = datetime.now()
print date
print "Hello Detective"
print 'Let\'s get started'

def login_page():
    username = raw_input("Enter your username: ")
    password = raw_input("Enter your password: ")
    checkpassword(username, password)
def checkpassword(use, pwd):
    if use == "admin" and pwd == "admin":
        login(use)
    else:
        print "Your username and/or password was incorrect"
        login_page()
def login(use):
    print "Welcome " + use
    print "You have successfully logged in!"
login_page()


STATUS_MESSAGE = ['Galti bdi glti engineering','Attachment are good for email only ','Sleeping','Wake up']
frnd1 = Spy("priya","Ms.",24,3.5)
frnd2 = Spy("Raj","Mr.",26,4.5)
friends = [frnd1,frnd2]
message=[]

def load_friends():
    with open('friends.csv', 'rb') as friends_data:
        reader = csv.reader(friends_data)
        #next(reader)

        for row in reader:
            frnd = Spy(name=row[0],salutation=row[1],age=row[2],rating=row[3])
            friends.append(frnd)

load_friends()

def load_chat():
    with open('message.csv', 'rb') as message_data:
        reader = csv.reader(message_data)
       # next(reader)

        for row in reader:
            msg = ChatMessage(message=row[0],sent_by_me=row[1])
            message.append(msg)
        
load_chat()

def read_chat_history():
    read_msg=select_frnd()

    for chat in friends[read_msg].chats:
        if chat.sent_by_me:
            print('[%s]' % chat.time.strftime("%d %B %Y"))
            print('%s' % 'you said : ')
            print '%s' % chat.message
        else:
            print('[%s]' % chat.time.strftime("%d %B %Y"))
            print('%s said : ' % friends[read_msg].name)
            print '%s' % chat.message

            
def add_status(c_status):
    if c_status != None:
        print "Your current status is" + c_status
    else:
        print "You don't have any status currently" 
    
    exiting_status = raw_input(" You want to select from old status? Y/N ")
    if exiting_status.upper() == "N":
        new_status = raw_input("Enter your status : ")
        if len(new_status)>0:
            STATUS_MESSAGE.append(new_status)

    elif exiting_status.upper() == "Y":
        serial_no = 1
        for old_status in STATUS_MESSAGE:
            print str(serial_no) + ". " + old_status
            serial_no = serial_no + 1
        user_choice = input("Enter your choice : ")
        new_status = STATUS_MESSAGE[user_choice - 1]
    update_status = new_status
    return update_status

def add_friend():
    frnd =  Spy("","",0,0.0)

    frnd.name = raw_input("What is your name? ")
    frnd.sal = raw_input("What should we call you? ")
    frnd.age = input("What is your age? ")
    frnd.rating = input("What is your rating? ")    
    frnd.is_online = True
    if len( frnd.name)>2 and 12<frnd.age<50 and frnd.rating>spy.rating:
        with open('friends.csv','a') as friends_data: # a is Opens a file for appending. The file pointer is at
                                                    # the end of the file if the file exists. That is, the file
                                                    #  is in the append mode. If the file does not exist, it
                                                    #  creates a new file for writing.
            writer = csv.writer(friends_data)
            writer.writerow([frnd.name,frnd.sal,frnd.rating,frnd.age,frnd.is_online])    
    else:
        print " Friend can not be added "
    return len(friends) 


def select_frnd():
    serial_no = 1
    for frnd in friends:
        print str(serial_no) +" "+ frnd.name
        serial_no = serial_no + 1
    user_selected_frnd = input("Enter your choice: ")
    user_selected_frnd_index = user_selected_frnd -1
    return user_selected_frnd_index

def send_message():
    selected_frnd = select_frnd()
    orginal_image = raw_input("What is the name of orginal image? ")
    secret_text  = raw_input("What is your secret text? ")
    output_path = "output.png"
    Steganography.encode(orginal_image,output_path,secret_text)
    new_chat = ChatMessage(secret_text,True)

    friends[selected_frnd].chats.append(new_chat)
    print "Your secret message is ready! "
         
def read_message():
    selected_frnd = select_frnd()
    output_path =  raw_input("Which image you want to decode? ")
    secret_text = Steganography.decode(output_path)
    print "Secret message is " + secret_text
    new_chat = ChatMessage(secret_text,False)

    friends[selected_frnd].chats.append(new_chat)
    print "Your secret message has been saved! "


def start_chat(spy_name,spy_age,spy_rating):
    print "Here are you options " +spy_name
    current_status = None
    show_menu = True
    while show_menu:
        choice = input("What do you want to do? \n 1. Add a status \n 2. Add a friend \n 3. Send a message \n 4. Read a message \n 5. Read chat History \n 0. Exit ")
        if choice==1:
            update_status_message = add_status(current_status)
            print "update status is : " + update_status_message 
            #current_status = add_status(current_status)
            #print "update status is : " + current_status 
        elif choice==2:
            no_of_frnd = add_friend()
            print "You have " + str(no_of_frnd) + "friends"
        elif choice==3:
            send_message()
        elif choice==4:
            read_message()
        elif choice==5:
            read_chat_history()
        else:
            print "invalid input "
 

spy_exist = raw_input("Are you a new user? Y/N: ")
if spy_exist.upper()=="N":
    print "Welcome Back " + spy.name + " age " +str(spy.age)+ " having rating of " +str(spy.rating)
    start_chat(spy.name,spy.age,spy.rating)    #function calling and make dictionary with key or value

elif spy_exist.upper()== "Y":
    spy = Spy(" "," ",0,0.0)

    spy.name = raw_input("What is your spy name? ")
    if len(spy.name)>2:
        print "Welcome " + spy.name + " Glad to have you back with us."
        spy_salutation = raw_input("What should we call you (Mr. or Ms.)? ")
        if spy_salutation=="Mr." or spy_salutation=="Ms.":
            spy.name = spy_salutation +" "+ spy.name
            print "Alright " + spy.name + ". I would like to know a little bit more about you. How are you? "   
            spy_mood = raw_input(" ")
            #spy_age = 0
            #spy_rating = 0.0
            spy_is_online = True
            spy.age = input("What is your age? ")
            if spy.age>12 and spy.age<40:
                print "your  age is corret."
                spy.rating = input("What is your rating? ")
                if spy.rating>=5.0:
                    print "Great spy"
                elif 3.5<spy.rating<=5.0:
                    print "Average spy"
                else:
                    print "Who hired you"
                spy_is_online =True
                print "Authentication Complete. Welcome " + spy.name +" age " + str(spy.age) + "and rating of " + str(spy.rating) + " Proud to have you onboard."
                print "Authentication Complete. Welcome %s age  %s and rating of %d Proud to have you onboard." % (spy.name,spy.age,spy.rating)
                start_chat(spy.name,spy.age,spy.rating) #function calling
            else:
                print "you are not eligible to be a spy."
        else:
            print "invalid salutation.."
    else:
        print "oops.. Write your full name"
else:
    print "Invalid entry"