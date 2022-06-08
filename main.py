from colors import color

cases = {
    "yes": "yes",
    "no": "no"
}

marks = [
    color.BOLD + color.GREEN + "Full mark" + color.END,
    color.BOLD + color.BLUE + "Minus 10 marks from overall but not below 40" + color.END,
    color.BOLD + color.RED + "Mark = 0" + color.END
]

freq_key_words = (
    color.BOLD + color.YELLOW + "Accepted ?" + color.END,
    color.BOLD + color.YELLOW + "Is there a valid reason ?" + color.END
)

def trim_and_lower(str):
    """
    Takes a string as argument
    returns white-space trimmed and lower cased string
    """
    return str.strip().lower()

def ask_input():
    """
    Calls input() awaits untill user enters input
    returns user input in a string format
    """
    user_input = input("yes/no: ")
    return user_input

def MC_Chart():
    run_engine = True
    while run_engine:
        print("CW Deadline CW Submission\nOn time ?")
        user_inpt = ask_input()

        if trim_and_lower(user_inpt) != cases["no"]:
            print(marks[0])
            run_engine = False
            
        elif trim_and_lower(user_inpt) != cases["yes"]:
            print("Within 24 hours ?")
            
            user_inpt = ask_input()
            if trim_and_lower(user_inpt) != cases["no"]:
                print("Late Submission")
                print("Is there a valid reason ?")

                user_inpt = ask_input()
                if trim_and_lower(user_inpt) != cases["no"]:
                    print("MC")
                    print(freq_key_words[0])
                    
                    user_inpt = ask_input()
                    if trim_and_lower(user_inpt) != cases["no"]:
                        print(marks[0])
                        run_engine = False

                    elif trim_and_lower(user_inpt) != cases["yes"]:
                        print(marks[1])
                        run_engine = False
                        
                elif trim_and_lower(user_inpt) != cases["yes"]:
                    print(marks[1])
                    run_engine = False
                    
            elif trim_and_lower(user_inpt) != cases["yes"]:
                print("Submitted within 5 days ?")
                
                user_inpt = ask_input()
                if trim_and_lower(user_inpt) != cases["no"]:
                    print(freq_key_words[1])
                    
                    user_inpt = ask_input()
                    if trim_and_lower(user_inpt) != cases["no"]:
                        print("MC late submission option")
                        print(freq_key_words[0])
                        
                        user_inpt = ask_input()
                        if trim_and_lower(user_inpt) != cases["no"]:
                            print(marks[0])
                            run_engine = False
                           
                        elif trim_and_lower(user_inpt) != cases["yes"]:
                            print(marks[2])
                            run_engine = False
                            
                    elif trim_and_lower(user_inpt) != cases["yes"]:
                        print(marks[2])
                        run_engine = False
                        
                elif trim_and_lower(user_inpt) != cases["yes"]:
                    print(freq_key_words[1])
                    
                    user_inpt = ask_input()
                    if trim_and_lower(user_inpt) != cases["no"]:
                        print("MC (non-submission/deferral before specified deadline)")
                        print("Accepted")
                        print("Deferral reassesment")
                        run_engine = False
                        
                    elif trim_and_lower(user_inpt) != cases["yes"]:
                        print(marks[2])
                        run_engine = False
                    else:
                        print(color.BOLD + color.RED + "** Invalid Input **" + color.END + "\n\n")
                        MC_Chart()    
                else:
                    print(color.BOLD + color.RED + "** Invalid Input **" + color.END + "\n\n")
                    MC_Chart()        
            else:
                print(color.BOLD + color.RED + "** Invalid Input **" + color.END + "\n\n")
                MC_Chart()            
        else:
            print(color.BOLD + color.RED + "** Invalid Input **" + color.END + "\n\n")
            MC_Chart()


if __name__ == "__main__":
    MC_Chart()