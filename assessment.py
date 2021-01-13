import speech_recognition as sr
import difflib
from helpers import helperfunctions
from protocols import ABCDE

#create protocol
p = ABCDE()

# create recognizer instance
r = sr.Recognizer()

# list all available input devices
#print(sr.Microphone.list_microphone_names())

# create microphone instance
mic = sr.Microphone() # device_index = 1

# procedure = step in loop
# field tracks field in protocol under modification
field = "start"
type = None

# ------------------------
# initial patient data
# ------------------------
print("Please say: name, age, weight, height?")
# get input
with mic as source:
    r.adjust_for_ambient_noise(source, duration=2)
    print("Start talking: ")
    audio = r.listen(source, phrase_time_limit=5)
    print("Stop talking.")

# recognize speech
try:
    #str = r.recognize_sphinx(audio)
    str = r.recognize_google(audio)
except sr.UnknownValueError:
    print("Google / Sphinx could not understand audio")
except sr.RequestError as e:
    print("Google / Sphinx error; {0}".format(e))


list = helperfunctions.get_data_from_string(str)

# print values in protocol for name, age, weight, height
p.set_value("name", list[0])
p.set_value("age", list[1])
p.set_value("weight", list[2])
p.set_value("height", list[3])

# ------------------------
# assessment
# ------------------------
# program start
while(1):
    print("------------------------")
    print("Current field %s" % field)
    print("Current type %s" % type)
    print("------------------------")
    str = None
    audio = None

    if field == "start":
        print("What do you wanna do?")
        print("------------------------")
        # get input
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=2)
            print("Start talking: ")
            audio = r.listen(source, phrase_time_limit=5)
            print("Stop talking.")

        # recognize speech
        try:
            #str = r.recognize_sphinx(audio)
            str = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google / Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Google / Sphinx error; {0}".format(e))

        print("You said: %s" % str)
        ret, res = helperfunctions.occur_in_bag(field, str)
        #print("ret val: %s" % ret)
        #print("res val: %s" % res)
        if ret == 1:
            field = "assessment"
            type = None
        elif ret == -1:
            break
        else:
            print("You said '%s' which was not recognized" % res)


    elif field == "assessment":
        print("What assessment?")
        print("airways, breathing, circulation, disability, exposure")
        print("mental, type")
        print("------------------------")
        # get input
        with mic as source:
            r.adjust_for_ambient_noise(source, duration=2)
            print("Start talking: ")
            audio = r.listen(source, phrase_time_limit=5)
            print("Stop talking.")

        # recognize speech
        try:
            #str = r.recognize_sphinx(audio)
            str = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Google / Sphinx could not understand audio")
        except sr.RequestError as e:
            print("Google / Sphinx error; {0}".format(e))



        print("You said: %s" % str)
        ret, res = helperfunctions.occur_in_bag(field, str)
        #print("ret val: %s" % ret)
        #print("res val: %s" % res)
        if ret == 1:
            field = "status"
            type = res
        elif ret == -1:
            break

        else:
            print("You said '%s' which was not recognized" % res)


    elif field == "status":
        ret = helperfunctions.what_type(type)

        if ret == 1:
            # get input
            with mic as source:
                r.adjust_for_ambient_noise(source, duration=2)
                print("Start talking: ")
                audio = r.listen(source, phrase_time_limit=5)
                print("Stop talking.")

            # recognize speech
            try:
                #str = r.recognize_sphinx(audio)
                str = r.recognize_google(audio)
            except sr.UnknownValueError:
                print("Google / Sphinx could not understand audio")
            except sr.RequestError as e:
                print("Google / Sphinx error; {0}".format(e))
            #str = r.recognize_google(audio)

            print("You said: %s" % str)
            print("------------------------")
            ret, res = helperfunctions.occur_in_bag(field, str, type)
            #print("ret val: %s" % ret)
            #print("res val: %s" % res)
            if ret == 1:
                p.set_value(type, res)
                field = "assessment"
                type = None
            elif ret == -1:
                break

            else:
                print("You said '%s' which was not recognized" % res)
        else:
            print("Type not found. Please retry")

        #elif type == "mental":


        #elif type == "type":
    else:
        print("field not found")


print("Program executing")
p.print_protocol()
