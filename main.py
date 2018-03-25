print "Hello buddy"
print 'Let\'s get started'
spy_name = raw_input("What is your spy name? ")
if len(spy_name)>2:
    print "Welcome " + spy_name + " Glad to have you back with us."
    spy_salutation = raw_input("What should we call you (Mr. or Ms.)? ")
    if spy_salutation=="Mr." or spy_salutation=="Ms.":
        spy_name = spy_salutation +" "+ spy_name
        print "Alright " + spy_name + ". I would like to know a little bit more about you."
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
            print "Authentication Complete. Welcome " + spy_name +"age " + str(spy_age) + "and rating of " + str(spy_rating) + " Proud to have you onboard."
        else:
            print "you are not eligible to be a spy."
    else:
        print "invalid salutation.."
else:
    print "oops.. Write your full name"