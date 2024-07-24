'''mutiple'''
class father:
    def father_speak():
        return "father class"
class mother:
    def mother_speak():
        return "mother class"
class kid(father,mother):
    def kid_speak():
        return "kid class"
obj=kid
print(obj.father_speak())
print(obj.mother_speak())
print(obj.kid_speak())