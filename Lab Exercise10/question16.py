list1=["a","e","i","o","u"]
def make_ing_form(word):
    if word[-2:] == "ie":
        word = word.replace("ie","ying")
        print(word)
        
    elif word[-1] == "e":
        word = word.replace("e","ing")
        print(word)

    elif word[-2] in list1:
        var = word[-1]
        word=word.replace(var,var+var+"ing")
        print(word)
        
    
    else:
        word = word+"ing"
        print(word)

word =input("Enter the word: ")
make_ing_form(word)
