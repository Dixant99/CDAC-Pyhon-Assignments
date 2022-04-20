class String:
    def get_String(self):
        given=input("Please user enter the string :")
        return given

    def print_string(self,given):
        print(str.upper(given))

s=String()
b=s.get_String()
s.print_string(b)
