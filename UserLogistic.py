#defining demographic variables 

userhsvalue = 0
userbsvalue = 0
userfemale = 0
userinc = 0

#user interaction
print("Hello there! Welcome to MoneyChecker. ")
userexperience = input("Were you directed here from MoneyMaker Project? ")
while userexperience != "yes" and userexperience != "Yes" and userexperience !="no" and userexperience !="No":
    userexperience = input("I'm sorry, I didn't get that. Please answer with a yes or no. Were you directed here from MoneyMaker Project? ")
if userexperience == "yes" or userexperience == "Yes":
    print("Ok! Great! MoneyMaker has already told you whether or not your income will increase or decrease. MoneyChecker is here to confirm that increase or decrease. ")
else:
    print("That's alright, I do reccommend that you run the MoneyMaker program first beforehand. If you want to jump straight into MoneyChecker, that's ok too. ")
userready = input("Would you like to proceed with MoneyChecker? ")
while userready != "yes" and userready != "Yes" and userready != "no" and userready !="No":
    userready = input("I'm sorry, I didn't get that. Please answer with a yes or no. Would you like to proceed with MoneyChecker? ")
if userready == "yes" or userready == "Yes":
    print("Great! Let's get started by asking for your demographics! ")
    username = input("I am robot Angela. What is your name? ")
    print(" ")
    print("Cool! Hi there " + username + "! I have a few questions for you. ")
    userhighschool = input("Have you received a high school diploma? ")
    while userhighschool != "yes" and userhighschool !="no" and userhighschool !="Yes" and userhighschool !="No":
        userhighschool = input("Sorry, I didn't get that. Please answer with a yes or no. Have you received a high school diploma? ")
    if userhighschool == "yes" or userhighschool == "Yes":
        userhsvalue = 100
        print("")
        print("Great! Nice to know that. Let's keep going.")
        userbachelor = input("Do you also have a bachelor degree? ")
        while userbachelor != "yes" and userbachelor !="no" and userbachelor !="Yes" and userbachelor !="No":
            userbachelor = input("Sorry, I didn't get that. Please answer with a yes or no. Do you also have a bachelor degree? ")
        if userbachelor == "yes" or userbachelor == "Yes":
            userbsvalue = 100
            print("Wow! You are really accomplished! Let's keep going.")
        else:
            print("Ok, let's keep going. ")
    else:
        print("That's alright, let's continue.")

    print("")
    usergender = input("Are you a female or male? ")
    while usergender != "female" and usergender !="Female" and usergender !="male" and usergender !="Male":
            usergender = input("Sorry, I didn't get that. Please answer with female or male. What was your sex at birth? ")

    if usergender == "female" or usergender == "Female":
        userfemale = 100
        print("")
        print("Ok, Ms. " + username + ". ")

    else:
        print("")
        print("Ok, Mr. " + username + ". ")

    print("We're almost there! One more question. ")
    userinc = input("What was you annual income last year? Please do not include any symbols in your answer. ")
    useraccuracy = input("Just to make sure, all the information is correct so far? ")
    while useraccuracy != "yes" and useraccuracy !="no" and useraccuracy !="Yes" and useraccuracy !="No":
        useraccuracy = input("Sorry, I didn't get that. Please answer with a yes or no. Just to make sure, all the information is correct so far")

    if useraccuracy == "yes" or useraccuracy == "Yes":
        print("")
        print("Great! Thank you for that. We will now process your information for you. ")
        funuser = input("Would you like to hear a joke in the meantime? ")
        print("")
        if funuser == "yes" or funuser == "Yes":
            joketime = input("What did the fish say when he swan into a wall? ")
            print("")
            print("Dam. HAHAHAHA!!")
            userthoughts = input("Was that a funny joke? ")
            if userthoughts == "yes" or userthoughts == "Yes":
                print("Great to know! Happy to please you anytime. ")
            else:
                print("Welp. Sorry to hear that. ")
        else:
            print("What a pity. You won't be able to hear my joke. Let's give you your stats then. ")
        userhsvalue = int(userhsvalue)
        userbsvalue = int(userbsvalue)
        userfemale = int(userfemale)
        userinc = int(userinc)
        userlinear = 28.55*userhsvalue +14.60*userbsvalue + 319.61*userfemale + 1.076*userinc -5513.61
        if userlinear > userinc:
            userfinal1 = "increase"
        if userlinear < userinc:
            userfinal1 = "decrease"
        userlogistic = -24.5+ 0.000092*userinc - 0.0267*userhsvalue -0.0566*userbsvalue +0.516*userfemale 
else:
    print("That's ok, rerun me when you are ready!" )
    exit()



