#Deterministic Turing Machine

import itertools

''' INSTRUCTIONS:
# The TM must be initialized with a set of alphabets and a set of states (must be chars if using serial set function)
# Afterwards, use the respective functions to set the initial state and set the accept state/s and reject state/s
# You can then call the setTransition function to set the transition function or
directly set it using a dictionary like in the example below
or call serialSetTransition for an even faster encoding of a TM

# NB!!!!!! A blank space character has to be explicit - by default it is 'b'. If you want to use another one, call setBlankSpaceCharacter.

# Finally, call read(<input string>) to see if it is accepted or rejected by the FA
'''

class TM:
    def __init__(self,alphabet,states):
        self.alphabet = alphabet
        self.states = states
        self.initState =  "N/A"
        self.acceptStates = set()
        self.rejectStates = set()
        self.function = dict()
        self.showStepsBool = False
        self.blankChar = 'b'
        self.items = itertools.product(states,alphabet)

    def setInitState(self,new_state):
        new_state = str(new_state)
        if new_state in self.states:
            self.initState = new_state
        else:
            print("state does not exist in machine")

    def setAcceptStates(self,new_states):
        for state in new_states:
            state = str(state)
            if state in self.acceptStates:
                print("state " + state + " already an accept state")
            elif state in self.rejectStates:
                print("state " + state + " already a reject state")
            elif state in self.states:
                self.acceptStates.add(state)
            else:
                print("state " + state + " does not exist in machine")

    def setRejectStates(self,new_states):
        for state in new_states:
            state = str(state)
            if state in self.rejectStates:
                print("state " + state + " already a reject state")
            elif state in self.acceptStates:
                print("state " + state + " already an accept state")
            elif state in self.states:
                self.rejectStates.add(state)
            else:
                print("state " + state + " does not exist in machine")

    def setTransition(self):
        print("setting transition function.")
        print("format: <next state> <replace symbol> <l (left) or r (right)>")
        for i in self.items:
            print(i)
            self.function[i] = input(": ").split(" ")

    #only useful when all symbols and state names are single characters   
	#FORMAT "transition1,transition2,..." where each transition has the format:
	# <current state><input char><next state><replace char><left or right on tape>
    def serialSetTransition(self,string):
        data = string.split(",")
        for i in data:
            self.function[(i[0],i[1])] = [i[2],i[3],i[4]]

    def setBlankSpaceCharacter(self,character):
        self.blankChar = character
        
    def printTape(self,tape,head):
        print("| ", end="")
        for i in tape:
            print(i + " | ",end="")
        print()

        print("  ",end="")
        for i in range(head):
            print("    ",end="")
        print("^")

    #Call these functions if you want to change the visibility of intermediate steps
    def showSteps(self):
        self.showStepsBool = True

    def hideSteps(self):
        self.showStepsBool = False
        
    def read(self,string):
        if self.initState == "N/A":
            print("initial state not set")
        else:
            tape = list(string)
            counter = 1
            
            tapeHead = 0
            curr_state = self.initState
            
            while True:
                if self.showStepsBool:
                    self.printTape(tape,tapeHead)
                
                if curr_state in self.acceptStates:
                    print("accepted")
                    print("numSteps:",counter)
                    print("final state:",curr_state)
                    break
                if curr_state in self.rejectStates:
                    print("rejected")
                    print("numSteps:",counter)
                    print("final state:",curr_state)
                    break
                
                item = (curr_state,tape[tapeHead])
                if item in self.function.keys():
                    counter += 1
                    action_data = self.function[item]
                    if self.showStepsBool:
                        print(item)
                        #print(item,"  replace with ",action_data[1])
                        #print(" ")
                    curr_state = action_data[0]
                    tape[tapeHead] = action_data[1]
                    if action_data[2] == 'l':
                        tapeHead -= 1
                        if tapeHead < 0:
                            print("error - negative index for head")
                    else:
                        tapeHead += 1
                    if tapeHead+1 > len(tape):
                        tape.append(self.blankChar)
                                       
                else:
                    print("rejected - no path")
                    print("numSteps:",counter)
                    print("final state:",curr_state)
                    break

    #read multiple strings, input is a list of strings            
    def multRead(self,inp):
        for i in inp:
            print("input:",i)
            self.read(i)
            print(" ")
        
                
#example 1
'''
alphabet = {'a','b','x'}
states = {'1','2','3','qa','qr'}
m1 = TM(alphabet,states)

m1.function = {('1','a'):['2','x','r'],('1','b'):['3','x','r'],
                 ('2','a'):['qa','x','r'],('2','b'):['3','x','r'],
                 ('3','a'):['2','x','r'],('3','b'):['qr','x','r']}
m1.setInitState('1')
m1.setAcceptStates(['qa'])
m1.setRejectStates(['qr'])
'''

#slides example = {0^n 1^n 2^n}
'''
m2 = TM({'0','1','2','x','y','z','$'},{'0','1','2','3','4','5'})

trans = "001xr,0y4yr,1y1yr,1010r,112yr,2z2zr,2121r,223zl,"
trans2 = "3030l,3131l,3y3yl,3z3zl,3x0xr,4y4yr,4z4zr,4$5$l"
m2.serialSetTransition(trans+trans2)

m2.setInitState('0')
m2.setAcceptStates(['5'])
m2.setBlankSpaceCharacter('$')
m2.showSteps()
'''

#test - powers of 2
'''
m3 = TM({'0','x','b'},{'1','2','3','4','5','a','r'})

trans = "102br,1brbr,1xrxr,2x2xr,2babr,203xr,"
trans2 = "3b5bl,3x3xr,3040r,403xr,4x4xr,4brbr,5050l,5x5xl,5b2br"
m3.serialSetTransition(trans+trans2)

m3.setInitState('1')
m3.setAcceptStates(['a'])
m3.setRejectStates(['r'])

m3.multRead(["0","00","1","0000"])
'''





                       




    
