#defining demographic variables 

userhsvalue = 0
userbsvalue = 0
userfemale = 0
userinc = 0

#user interaction
print("Hello there! Welcome to MoneyMaker! We are here to predict your income in 5 years! We will get started by asking for your demographics. Please do not include any symbols in your answers. ")
print(" ")
userready = input("Are you ready? ")
print("")
while userready != "yes" and userready !="no" and userready != "Yes" and userready !="No":
    userready = input("Sorry, I didn't get that. Please answer with a yes or no. Are you ready? ")
    
if userready == "yes" or userready == "Yes":
    print("Ok! Let's get started")
    usercalifornian = input("Ok, we need to first confirm that you live in California, and plan on doing so for the next 5 years. Is that correct? ")
    while usercalifornian != "yes" and usercalifornian != "Yes" and usercalifornian != "no" and usercalifornian != "No":
        usercalifornian = input("I'm sorry, I didn't get that. Please answer with a yes or no. Are you currently residing in California? ")
    if usercalifornian == "yes" or usercalifornian == "Yes":
        print("Great! Let's start. ")
    if usercalifornian == "no" or usercalifornian == "No":
        print("Sorry, this program is specified for individuals residing in California. Bye bye! ")
        exit()
    print("")
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
            joketime = input("Life is a constant battle between the heart and the brain. But guess who wins? ")
            print("")
            print("The skeleton. HAHAHAHA!!")
            userthoughts = input("Was that a funny joke? ")
            if userthoughts == "yes" or userthoughts == "Yes":
                print("Great to know! Happy to please you anytime. ")
            else:
                print("Well, you have horrible humor. ")
        else:
            print("What a pity. You won't be able to hear my joke. Let's give you your stats then. ")
            
        userhsvalue = int(userhsvalue)
        userbsvalue = int(userbsvalue)
        userfemale = int(userfemale)
        userinc = int(userinc)
        userfinal = 28.55*userhsvalue +14.60*userbsvalue + 70.61*userfemale + 1.076*userinc - 5513.61
        userincrease = int(userfinal - userinc)
        if userincrease > 0:
            userfinal = str(userfinal)
            userincrease = str(userincrease)
            print("In 5 years, your annual income will become around $" + userfinal + ", an $" + userincrease + " amount increase from right now. Keep up your work!")
        userincrease = int(userincrease)
        if userincrease < 0:
            userfinal = str(userfinal)
            userdecrease = -userincrease
            userdecrease = str(userdecrease) 
            print("In 5 years, your annual income will become around $" + userfinal + ", an $" + userdecrease + " amount decrease from right now. Make sure to work harder to catch up! ")
        if userincrease == 0:
            print("Welp. Your income did not change at all. That's disappointing. ")
        if userhsvalue == 0:
            print("It seems that you did not receive a high school diploma. If you had gotten your high school diploma, you could have an addition of $2826.45 to your annual income in 5 years. This means that you are making $2827.45 more each year. ")
        if userbsvalue == 0:
            print("Just so you know, if you had gotten your bachelor's degree, there would have been additional increase of $1445.40 in 5 years. That means you are making $1445.40 more each year. ")
        userretire = input("Are you interested in knowing how much money you will be making when you retire? ")
        while userretire != "yes" and userretire != "Yes" and userretire != "no" and userretire != "No":
            userretire = input("Sorry, I didn't get that. Please answer with a yes or no. Are you interested in knowing how much money you will be making when you retire? ")
        if userretire == "yes" or userretire == "Yes":
            print("Great! Now we will need to ask your age and your estimated retirement age. ")
            userage = input("How old are you right now? ")
            userretirementage = input("At what age do you plan on retiring? ")
            useryears = int(userretirementage) - int(userage)
            inflation = 1.021705
            multiplefive = useryears / 5
            remainingfive = useryears % 5
            numberfive = remainingfive / 5
            userfinalretirement = (inflation**useryears)*(userincrease*multiplefive + userincrease*numberfive) + userinc
            userretirementage = str(userretirementage)
            userfinalretirement = str(userfinalretirement)
            print("Your income value at " + userretirementage + " age will be $" + userfinalretirement + ". ")
        if userretire == "no" or userretire == "No":
            print("Thats ok. There are more choices to make. ")
        
        print("Thank you for using MoneyMaker! I reccommend that you use our other MoneyChecker program as well! ")

    if useraccuracy == "no" or useraccuracy == "No":
        print("Ok, rerun me then, we can start again! ")
        exit()

if userready != "yes" and userready !="Yes":
    print("Ok, rerun me when you are ready!")




