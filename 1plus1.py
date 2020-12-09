i = 1
while i == 1:
    print("Hello!")
    cont = input("Do you wish to proceed? (Y/n) ")

    if cont == "Y":
        userAnswer = input("What is 1plus1? ")
        if userAnswer == "2":
            print("Congratulations I am proud of you!")
        else:
            print("You should know better :(")
    elif cont == "n":
        print("Okay bai bai!")
    else:
        print("You doorknob, you're supposed to answer with Y or N !")
    if cont == "n":
        break
