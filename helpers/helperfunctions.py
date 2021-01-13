import difflib
import sys
import os

# converst sentence into fields
def get_data_from_string(str):
    return_data = ["name", "age", "weight", "height"]
    print(str)
    list = str.split()
    i = 0
    for val in list:
        if val == "name":
            return_data[0] = list[i+1]
        elif val == "age":
            return_data[1] = list[i+1]
        elif val == "weight":
            return_data[2] = list[i+1]
        elif val == "height":
            return_data[3] = list[i+1]

        i = i + 1
    return return_data

# check what type of assessment that is being conducted and print
# corresponding alternatives
def what_type(type):
    list = ["airways", "breathing", "circulation", "disability", "exposure"]
    if type in list:
        print("What status?")
        print("Stable / Unstable / Critical")
        print("------------------------")
        return 1
    elif type == "mental":
        print("What status?")
        print("alert / verbal response / painful stimuli / unresponsive")
        print("------------------------")
        return 1
    elif type == "type":
        print("What status?")
        print("medicine / trauma / maternity / cardiac arrest / deceased / transport")
        print("------------------------")
        return 1
    else:
        return 0

# main bag function that directs to correct bag depending on what field in
# protocol and what type of assessment
def occur_in_bag(field, str, type = None):

    # check is user want to quit
    if str == "quit":
        return -1, str

    if field == "start":
        ret, identifier = occur_in_bag_start(str)
        if ret == 1:
            return ret, identifier

        return ret, str


    elif field == "assessment":
        possible_strings = ["airways", "breathing", "circulation", "disability", "exposure", "mental", "type"]
        for identifier in possible_strings:
            ret = occur_in_bag_assessment(identifier, str)
            if ret == 1:
                return ret, identifier
        return ret, str


    elif field == "status":
        ret, res = occur_in_bag_status(str, type)
        return ret, res

    else:
        print("field not found")


# search available options from start
def occur_in_bag_start(str):
    possible_fields = ["first assessment"]
    for identifier in possible_fields:
        print(str)
        print("first assessment")
        if difflib.SequenceMatcher(None, identifier, str).ratio() > 0.7:
            return 1, identifier
        else:
            return 0, str


# search in bag of words for similar words for ABCDE words
def occur_in_bag_assessment(identifier, str):

    if str == None:
        return 0
    # use bag of words
    bag_of_words_airways = ["airways", "airway", "highways", "highway", "always", "ways"]
    bag_of_words_breathing = ["breathing", "braiding", "braving" "printing", "trading", "living", "ing"]
    bag_of_words_circulation = ["circulation", "circ", "lation"]
    bag_of_words_disability = ["disability", "stability", "civility", "ability", "ility"]
    bag_of_words_exposure = ["exposure", "expo", "show", "sure"]
    bag_of_words_type = ["type", "top"]
    bag_of_words_mental = ["mental", "menthol"]

    # airways
    if identifier is "airways":
        if str in bag_of_words_airways:
            #print("The word: %s is found" % (str, identifier))
            return 1
        else:
            # check for substrings
            for val in bag_of_words_airways:
                #print("looking for %s in %s" % (val, str))
                if(str.find(val) != -1):
                    return 1
            return 0

    # breathing
    elif identifier is "breathing":
        if str in bag_of_words_breathing:
            #print("The word: %s is found in the %s bag" % (str, identifier))
            return 1
        else:
            # check for substrings
            for val in bag_of_words_breathing:
                #print("looking for %s in %s" % (val, str))
                if(str.find(val) != -1):
                    return 1
            return 0

    # circulation
    elif identifier is "circulation":
        if str in bag_of_words_circulation:
            #print("The word: %s is found" % (str, identifier))
            return 1
        else:
            # check for substrings
            for val in bag_of_words_circulation:
                #print("looking for %s in %s" % (val, str))
                if(str.find(val) != -1):
                    return 1
            return 0


    # disability
    elif identifier is "disability":
        if str in bag_of_words_disability:
            #print("The word: %s is found" % (str, identifier))
            return 1
        else:
            # check for substrings
            for val in bag_of_words_disability:
                #print("looking for %s in %s" % (val, str))
                if(str.find(val) != -1):
                    return 1
            return 0


    # exposure
    elif identifier is "exposure":
        if str in bag_of_words_exposure:
            #print("The word: %s is found" % (str, identifier))
            return 1
        else:
            # check for substrings
            for val in bag_of_words_exposure:
                #print("looking for %s in %s" % (val, str))
                if(str.find(val) != -1):
                    return 1,
            return 0


    # type
    elif identifier is "type":
        if str in bag_of_words_type:
            #print("The word: %s is found" % (str, identifier))
            return 1
        else:
            # check for substrings
            for val in bag_of_words_type:
                #print("looking for %s in %s" % (val, str))
                if(str.find(val) != -1):
                    return 1,
            return 0


    # mental
    elif identifier is "mental":
        if str in bag_of_words_mental:
            #print("The word: %s is found" % (str, identifier))
            return 1
        else:
            # check for substrings
            for val in bag_of_words_mental:
                #print("looking for %s in %s" % (val, str))
                if(str.find(val) != -1):
                    return 1,
            return 0

    else:
        return 0

# find stable, unstable, critical
def occur_in_bag_status(str, type):
    bag_ABCDE = ["stable", "unstable", "critical"]
    bag_mental = ["alert", "verbal response", "painful stimuli", "unresponsive"]
    bag_type = ["medicine", "trauma", "maternity", "cardiac arrest", "deceased", "transport"]
    list = ["airways", "breathing", "circulation", "disability", "exposure"]


    if type in list:

        for val in bag_ABCDE:
            #if difflib.SequenceMatcher(None, val, str).ratio() > 0.7:
            #    print("returning")
            #    return 1, val
            if val == str:
                return 1, val

        return 0, str


    elif type == "mental":
        for val in bag_mental:
            if difflib.SequenceMatcher(None, val, str).ratio() > 0.7:
                return 1, val

        return 0, str


    elif type == "type":
        for val in bag_type:
            if difflib.SequenceMatcher(None, val, str).ratio() > 0.7:
                return 1, val

        return 0, str


    else:
        print("Type not found")
        print("Type: %s" % type)
        return 0, str
