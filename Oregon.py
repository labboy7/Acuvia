print("Hello Player...")
print("You have been selected to take part in......")
print("!ACUVIA!")
print("...........")
def fu_join():
    want = str(input("do you want to join?  Y/N"))
    if want == "Y":
        print("very well....")
    elif want == "N":
        print("please.........uwu")
        fu_join()
    else:
        print("please choose Y or N")
        fu_join()
fu_join()
def main():
    pass