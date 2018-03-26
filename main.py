#import spy_detail
from spy_detail import spy_name , spy_age, spy_rating

print "Hello buddy"
print 'Let\'s get started'

def start_chat(spy_name,spy_age,spy_rating):
    print "Here are you options " +spy_name
    show_menu = True
    while show_menu:
        choice = input("What do you want to do? \n 1. Add a status \n 2. Add a friend \n 0. Exit ")
        if choice==1:
            print "Will add a status"
        elif choice==2:
            print "Will add a friend "
        elif choice==0:
            show_menu = False
        else:
            print "invalid input "


spy_exist = raw_input("Are you a new user? Y/N: ")
if spy_exist.upper()=="N":
    print "Welcome Back " + spy_name+ " age " +str(spy_age)+ " having rating of " +str(spy_rating)
    start_chat(spy_name,spy_age,spy_rating)    #function calling

elif spy_exist.upper()== "Y":
    spy_name = raw_input("What is your spy name? ")
    if len(spy_name)>2:
        print "Welcome " + spy_name + " Glad to have you back with us."
        spy_salutation = raw_input("What should we call you (Mr. or Ms.)? ")
        if spy_salutation=="Mr." or spy_salutation=="Ms.":
            spy_name = spy_salutation +" "+ spy_name
            print "Alright " + spy_name + ". I would like to know a little bit more about you. How are you? "   
            spy_mood = raw_input(" ")
            #spy_age = 0
            #spy_rating = 0.0
            spy_is_online = True
            spy_age = input("What is your age? ")
            if spy_age>12 and spy_age<40:
                print "your  age is corret."
                spy_rating = input("What is your rating? ")
                if spy_rating>=5.0:
                    print "Great spy"
                elif 3.5<spy_rating<=5.0:
                    print "Average spy"
                else:
                    print "Who hired you"
                spy_is_online =True
                print "Authentication Complete. Welcome " + spy_name +" age " + str(spy_age) + "and rating of " + str(spy_rating) + " Proud to have you onboard."
                print "Authentication Complete. Welcome %s age  %s and rating of %d Proud to have you onboard." % (spy_name,spy_age,spy_rating)
                start_chat(spy_name,spy_age,spy_rating) #function calling
            else:
                print "you are not eligible to be a spy."
        else:
            print "invalid salutation.."
    else:
        print "oops.. Write your full name"
else:
    print "Invalid entry"