
###Madlib Story###
#Today I went to the zoo. I saw a(n) ___________(adjective)_____________(Noun) jumping up and down in its tree. 
#He _____________(verb, past tense) __________(adverb)through the large tunnel that led to its _______(adjective) __________(noun).
#I got some peanuts and passed  them through the cage to a gigantic gray _______(noun)towering above my head.
#Feeding that animal made  me hungry.
#I went to get a __________(adjective) scoop  of ice cream.
#It filled my stomach. Afterwards I had to __________(verb) __________ (adverb) to catch our bus.  
#When I got home I __________(verb, past tense)my  mom for a __________(adjective) day at the zoo. 


def mad_libs_input():
    adjective_one = input("Please input an adjective: ")
    noun_one = input("Please input a noun: ")
    verb_one = input("Please input a verb: ")
    adverb_one = input("Please input an adverb: ")
    adjective_two = input("Please input another adjective: ")
    noun_two = input("Please input another noun: ")
    noun_three = input("Please input the last noun: ")
    adjective_three = input("Please input a 3rd adjective: ")
    verb_two = input("Please input another verb: ")
    adverb_two = input("Please input another adverb: ")
    verb_three = input("Please input the last verb: ")
    adjective_four = input("Please input the last adjective: ")
       
    return adjective_one, noun_one, verb_one, adverb_one, adjective_two, noun_two, noun_three, adjective_three, verb_two, adverb_two, verb_three, adjective_four
    
    

def mad_libs_print():
    madlib_adjective_one, madlib_noun_one, madlib_verb_one, madlib_adverb_one, madlib_adjective_two, madlib_noun_two, madlib_noun_three, madlib_adjective_three, madlib_verb_two, madlib_adverb_two, madlib_verb_three, madlib_adjective_four = mad_libs_input()
    print("Today I went to the zoo. I saw a(n) " + madlib_adjective_one + madlib_noun_one + " jumping up and down in its tree.")
    print("He " + madlib_verb_one + madlib_adverb_one + " through the large tunnel that led to its " + madlib_adjective_two + madlib_noun_two)
    print("I got some peanuts and passed them through the cage to a gigantic gray " + madlib_noun_three + " towering above my head.")
    print("Feeding that animal made me hungry.")
    print("I went to get a " + madlib_adjective_three + " scoop of ice cream.")
    print("It filled my stomach. Afterwards I had to " + madlib_verb_two + madlib_adverb_two + " to catch our bus.")
    print("When I got home I " + madlib_verb_three + " my mom for a " + madlib_adjective_four + " day at the zoo.")


mad_libs_print()







