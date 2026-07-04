# -*- coding: utf-8 -*-
"""A Turing machine simulator skeleton.

    Accepting '#'
    =============

    >>> from turing_machine import TuringMachine

    Instantiate the machine with particular transitions.

    >>> one_hash = TuringMachine(
    ...     {
    ...         ('q0', '#'): ('saw_#', '#', 'R'),
    ...         ('saw_#', ''): ('qa', '', 'R'),
    ...     }
    ... )

    Check whether it accepts a string:

    >>> one_hash.accepts('#')
    True

    >>> one_hash.accepts('##')
    False

    Check whether it rejects a string:

    >>> one_hash.rejects('#')
    False

    >>> one_hash.rejects('##')
    True

"""

import logging
from itertools import islice


class TuringMachine:
    """Turing machine simulator class.

    A machine is instantiated with transitions, start, accept and reject states
    and a blank symbol. We assume that the input and the tape alphabet can be
    deducted from the transitions.

    :param dict transitions: a mapping from (state, symbol) tuples to (state,
    symbol, direction) tuple. Directions are either 'L' (for left) or 'R' (for right).

    :param start_state: the initial state of the machine.

    :param accept_state: the accept state.

    :param reject_state: the reject state.

    :blank_symbol: the special symbol that marks the tape cell to be empty.

    """

    def __init__(self, transitions, start_state='q0', accept_state='qa', reject_state='qr', blank_symbol=''):
        # TODO: Implement the constructor. Initialize transitions, start_state, accept_state,
        # reject_state, blank_symbol, and any other helpful structures.
        self.transitions=transitions
        self.start_state=start_state
        self.accept_state=accept_state
        self.reject_state=reject_state
        self.blank_symbol=blank_symbol
        
        ##pass


    def run(self, input_):
        """Execute the Turing machine for a particular input.

        :param input_: the input that is written on the tape. It can be a list
        of strings, or just a string, in which case each letter is treated as a symbol.

        This method MUST be a Python generator. It should yield a (action, configuration) tuple
        at each step of the computation.
        
        The action is either 'Accept', 'Reject' or None. 
        
        Configuration is a dictionary with the following keys:
        - 'state': the current state,
        - 'left_hand_side': list of symbols on the left hand side of the current position (closest first),
        - 'symbol': the current symbol under the head,
        - 'right_hand_side': list of symbols on the right hand side of the current position.

        """
        # TODO: Implement the simulator loop as a Python generator.
        # 1. Initialize the tape using two lists (left_hand_side and right_hand_side) and the current symbol.
        # 2. Yield the current step (action, configuration).
        # 3. Read transitions and update state, write symbols, and move the head ('L' or 'R').
        # 4. Handle tape expansion dynamically for both left and right directions (double-sided infinite tape).
        # 5. Log a warning using logging.warning() if the singly-infinite tape boundary is crossed before Part III.
        left_hand_side,right_hand_side=make_tape(input_)
        state=self.start_state
        symbol=input_[0]
        if(len(left_hand_side)>0):
            head=(len(left_hand_side)*-1)
        else:
            head=0
        flag=False
        while 1:
            halt,action,config=configg(state,left_hand_side,right_hand_side,symbol,self.accept_state,self.reject_state)
            yield (action,config,head)  
            flag=False          
            for (curr_state,read),(next_state,write,move) in self.transitions.items():
                if curr_state==state and read==symbol:
                    flag=True
                    state=next_state
                    change_tape(write,head,left_hand_side,right_hand_side)
                    head,symbol=find_next_symbol(move,head,left_hand_side,right_hand_side,self.blank_symbol)
                    break
  
            if action in {"Accept","Reject"}:
                break          
            if flag==False:
                yield ("Reject",config,head)
            


        ##pass

    def accepts(self, input_, step_limit=150):
        """Check whether the Turing machine accepts a string.

        :param input_: the input string or list.
        :param step_limit: the maximum number of steps to simulate before stopping.
        :return: True if the machine halts in accept_state, False if it rejects,
                 or None if the step limit is reached without halting.
        """
        # TODO: Run the generator up to step_limit and check the action of the final yielded state.
        # Remember to log a warning if the step_limit is reached without halting.


        step=0
        run=self.run(input_)
        while(step<step_limit): 
            (action,config,head)=next(run)
            step+=1
            if action=="Accept":
                return True
            if action=="Reject":
                return False
                
        return None

        ##pass

    def rejects(self, input_, **kwargs):
        """Check whether the Turing machine rejects a string.

        :param input_: the input string or list.
        :return: True if the machine rejects the string, False if it accepts.
        """
        # TODO: Determine rejection by checking if accepts() returns False.

        return not self.accepts(input_)
        ##pass

    def debug(self, input_, step_limit=152, colored=True):
        """Print the execution configuration of the machine per transition for debugging.

        :param input_: the input string or list.
        :param step_limit: the maximum number of steps to output.
        :param colored: True to output colored boundaries in terminal.
        """
        # TODO: Loop over the steps yielded by run() up to step_limit and print the tape configuration.
        # E.g., print the state and the tape with the head highlighted in brackets like: left[symbol]right
        step=0
        run=self.run(input_)
        while(step<step_limit): 
            (action,config,head)=next(run)
            step=step+1
            if action in {"Accept","Reject"}:
                if action=="Accept":
                    if(colored):
                        colored_config=colored_configg(config,head)
                        print(colored_config)
                    else:
                        norm_config=normal_config(config,head)
                        print(norm_config)
                    print("input accepted")
                    break
                else:
                    if(colored):
                        colored_config=colored_configg(config,head)
                        print(colored_config)
                    else:
                        norm_config=normal_config(config,head)
                        print(norm_config)
                    print("input rejected")
                    break
            if(colored):
                colored_config=colored_configg(config,head)
                print(colored_config)
            else:
                norm_config=normal_config(config,head)
                print(norm_config)
            
            
        ##pass

def colored_configg(config,head):
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    result=""
    result+=config["state"]
    result+=' '
    n1=len(config["left_hand_side"])
    n2=len(config["right_hand_side"])
    if(head<0):
        index=(n1)-(-head)
        for i in range(0,index):
            result+=f"{GREEN} {config['left_hand_side'][i]} {RESET}"
        result+=f"{RED} {config['left_hand_side'][index]} {RESET}"
        for i in range(index+1,n1):
            result+=f"{GREEN} {config['left_hand_side'][i]} {RESET}"
        for j in range(n2):
            result+=f"{YELLOW} {config['right_hand_side'][j]} {RESET}"

    else:
        index=head
        for j in range(n1):
            result+=f"{GREEN} {config['left_hand_side'][j]} {RESET}"        
        for i in range(0,index):
            result+=f"{YELLOW} {config['right_hand_side'][i]} {RESET}"
        result+=f"{RED} {config['right_hand_side'][index]} {RESET}"
        for i in range(index+1,n2):
            result+=f"{YELLOW} {config['right_hand_side'][i]} {RESET}"

    return result

def normal_config(config,head):
    result=""
    result+=config["state"]
    result+=' '
    n1=len(config["left_hand_side"])
    n2=len(config["right_hand_side"])
    if(head<0):
        index=(n1)-(-head)
        for i in range(0,index):
            result+=config['left_hand_side'][i]
        result+='['
        result+=config['left_hand_side'][index]
        result+=']'
        for i in range(index+1,n1):
            result+=config['left_hand_side'][i]
        for j in range(n2):
            result+=config['right_hand_side'][j]

    else:
        index=head
        for j in range(n1):
            result+=config['left_hand_side'][j]       
        for i in range(0,index):
            result+=config['right_hand_side'][i]
        result+='['
        result+=config['right_hand_side'][index]
        result+=']'
        for i in range(index+1,n2):
            result+=config['right_hand_side'][i]

    return result
def make_tape(input_):
    n=len(input_)
    right_hand_side=[]
    left_hand_side=[]
    for i in range((n//2),n):
        right_hand_side.append(input_[i])
    for i in range(0,n//2):
        left_hand_side.append(input_[(n//2)-i-1])
    return left_hand_side,right_hand_side


def configg(state,left_hand_side,right_hand_side,symbol,accept,reject):
    if state==accept:
        action="Accept"
        halt=True
    elif state==reject:
        action="Reject"
        halt=True
    else:
        action=None
        halt=False

    config={
        "state":state,
        "left_hand_side":reverse(left_hand_side),
        "symbol":symbol,
        "right_hand_side": right_hand_side
    }

    return halt,action,config


def change_tape(write,head,left_hand_side,right_hand_side):
    if(head<0):
        index=-head
        left_hand_side[index-1]=write
    else:
        right_hand_side[head]=write


def find_next_symbol(move,head,left_hand_side,right_hand_side,blank):
    if move=='R':
        head=head+1
    if move=='L':
        if head==0:
            logging.warning("Singly-infinite tape boundary crossed (moving left from position 0).")
        head=head-1
    next_sym=blank
    if(head>=0):
        if head>=len(right_hand_side):
            right_hand_side.append(blank)
        
        next_sym=right_hand_side[head]

    if(head<0):
        index=(head*-1)-1
        if index>=len(left_hand_side):
            left_hand_side.append(blank)
        
        next_sym=left_hand_side[index]
    return head,next_sym

def reverse(left_hand_side):
    result=[]
    n=len(left_hand_side)
    for i in range(n):
        result.append(left_hand_side[n-i-1])
    return result