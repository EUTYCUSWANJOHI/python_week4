class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hey, my name is {self.name} and i am {self.age} years and i am a {self.gender}")
person1 = person("john", 27, "male")
person1.introduce()

