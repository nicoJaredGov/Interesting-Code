#finite automaton
import itertools

''' INSTRUCTIONS:
# The FA must be initialized with a set of alphabets and a set of states (both strings)
# Afterwards, use the respective functions to set the initial state and set the accept state/s
# You can then call the setTransition function to set the transition function or
directly set it using a dictionary like in the example below
# Finally, call readString(<input string>) to see if it is accepted or rejected by the FA
'''

class FA:
    def __init__(self,alphabet,states):
        self.alphabet = alphabet
        self.states = states
        self.initialState = "N/A"
        self.acceptanceStates = set()
        self.function = dict()
        self.items = itertools.product(states,alphabet)

    def setInitState(self,new_state):
        new_state = str(new_state)
        if new_state in self.states:
            self.initialState = new_state
        else:
            print("state does not exist in FA")

    def setAcceptState(self,state):
        state = str(state)
        if state in self.acceptanceStates:
            print("state already an accept state")
        elif state in self.states:
            self.acceptanceStates.add(state)
        else:
            print("state does not exist in FA")
        

    def setTransition(self):
        print("setting transition function")
        for i in self.items:
            print(i)
            self.function[i] = input(": ")

    def readString(self,word):
        if self.initialState == "N/A":
            print("initial state not set")
        else:
            curr_state = self.initialState
            for i in word:
                if i in alphabet:
                    item = (curr_state,i)
                    print(item)
                    curr_state = self.function[item]
            if curr_state in self.acceptanceStates:
                print("accepted")
            else:
                print("rejected")
                    
	
    #def addState():
    #def addAcceptState():

#EXAMPLE - accepts even number of a's and odd number of b's            
'''
alphabet = {'a','b'}
states = {'1','2','3','4'}
m1 = FA(alphabet,states)
m1.function = {('1','a'):'2',('1','b'):'3',('2','a'):'1',('2','b'):'4',
               ('3','a'):'4',('3','b'):'1',('4','a'):'3',('4','b'):'2'}
m1.setInitState(1)
m1.setAcceptState(3)
m1.readString("abbababab")
'''

        
