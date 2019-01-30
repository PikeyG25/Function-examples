class Human(object):

    def __init__(self, name, hair_color, eye_color, height, weight, iq, gender, race):
        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.height = height
        self.weight = weight
        self.iq = iq
        self.gender = gender
        self.race = race

    def intro_self(self):
        print("Hello my name is " + self.name)

    def describe_self(self):
        print("I have " + self.hair_color + " hair")
        print("I have " + self.eye_color + " eyes")
        print("I am ", self.height, " tall")
        print("I weigh ", self.weight, " lbs")
        print("I am a " + self.race + " " + self.gender + " with an iq of ", self.iq)

    def learn(self):
        iq = self.iq

    def bmi(self):
        kg_weight = self.weight*0.453592
        meter_height = self.height*0.0254
        bmi = kg_weight//(meter_height*meter_height)
        if bmi <= 18.5:
            print('Your BMI is', bmi, 'which means you are underweight.')

        elif bmi > 18.5 and bmi < 25:
            print('Your BMI is', bmi, 'which means you are normal.')

        elif bmi > 25 and bmi < 30:
            print('Your BMI is', bmi, 'which means you are overweight')

        elif bmi > 30:
            print('Your BMI is', bmi, 'which means you are obese.')

        else:
            print("There was an error with your input")


        bmi(self)


parker = Human("Parker", "blond", "blue", 6, 200, 24, "male", "white")
parker.intro_self()
parker.describe_self()
