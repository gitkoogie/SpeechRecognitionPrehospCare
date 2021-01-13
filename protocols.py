import speech_recognition as sr


class ABCDE:


    def __init__(self):
        self.name = None
        self.age = None
        self.weight = None
        self.height = None
        self.airways = None
        self.breathing = None
        self.circulation = None
        self.disability = None
        self.exposure = None
        self.type = None
        self.mental = None

    def set_value(self, field, value):
        if field == "name":
            self.name = value
        elif field == "age":
            self.age = value
        elif field == "weight":
            self.weight = value
        elif field == "height":
            self.height = value
        elif field == "airways":
            self.airways = value
        elif field == "breathing":
            self.breathing = value
        elif field == "circulation":
            self.circulation = value
        elif field == "disability":
            self.disability = value
        elif field == "exposure":
            self.exposure = value
        elif field == "type":
            self.type = value
        elif field == "mental":
            self.mental = value
        else:
            print("Field not found in protocol")

    def print_protocol(self):
        print("----------------")
        print("FIRST ASSESSMENT")
        print("----------------")
        print("Patient Information")
        print("-------------------")
        print("Patient name: %s" % self.name)
        print("Patient age: %s years old" % self.age)
        print("Patient weight: %s kg" % self.weight)
        print("Patient height: %s cm" % self.height)
        print("-------------------")
        print("Type of situation: %s" % self.type)
        print("Mental status: %s" % self.mental)
        print("-------------------")
        print("Status Airways: %s" % self.airways)
        print("Status Breathing: %s" % self.breathing)
        print("Status Circulation: %s" % self.circulation)
        print("Status Disability: %s" % self.disability)
        print("Status Exposure: %s" % self.exposure)
        print("-------------------")
