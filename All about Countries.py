class Nigeria():
    def capital(self):
       print("Abuja is the capital of Nigeria.")
    def language(self):
        print("Nigeria has over 500 languages.")
    def type(self):
        print("Nigeria is a Democratic Republic.")
class USA():
    def capital(self):
       print("Washington, D.C. is the capital of USA.")
    def language(self):
        print("English is America's primary language")
    def type(self):
        print("USA is a Republic.")
obj_ng = Nigeria()
obj_usa = USA()
for country in (obj_ng, obj_usa):
    country.capital()
    country.language()
    country.type()