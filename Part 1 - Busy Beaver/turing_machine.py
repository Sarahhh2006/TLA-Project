

import logging
from itertools import islice


class TuringMachine:


    def __init__(self, transitions, start_state='q0', accept_state='qa', reject_state='qr', blank_symbol=''):

        self.transitions=transitions
        self.start_state=start_state
        self.accept_state=accept_state
        self.reject_state=reject_state
        self.blank_symbol=blank_symbol
        



    def run(self, input_):

        right_hand_side=list(input_) if isinstance(input_, (str, list)) else []
        left_hand_side=[]
        state=self.start_state
        symbol=self.blank_symbol
        if right_hand_side:
            symbol=right_hand_side.pop(0)
        flag=False

        while 1:
            action,config=configg(state,left_hand_side,right_hand_side,symbol,self.accept_state,self.reject_state)
            yield (action,config)  

            flag=False          
            for (curr_state,read),(next_state,write,move) in self.transitions.items():
                if curr_state==state and read==symbol:
                    flag=True
                    state=next_state
                    symbol=write
                    symbol=find_next_symbol(symbol,move,left_hand_side,right_hand_side,self.blank_symbol)
                    break
  
            if action in {"Accept","Reject"}:
                break          
            if flag==False:
                yield ("Reject",config)
            

    def accepts(self, input_, step_limit=150):
        step=0
        run=self.run(input_)
        while(step<step_limit): 
            (action,config)=next(run)
            step+=1
            if action=="Accept":
                return True
            if action=="Reject":
                return False
                
        return None


    def rejects(self, input_, **kwargs):

        return not self.accepts(input_)


    def debug(self, input_, step_limit=152, colored=True):

        step=0
        run=self.run(input_)
        while(step<step_limit): 
            (action,config)=next(run)
            step=step+1
            if action in {"Accept","Reject"}:
                if action=="Accept":
                    if(colored):
                        colored_config=colored_configg(config)
                        print(colored_config)
                    else:
                        norm_config=normal_config(config)
                        print(norm_config)
                    print("input accepted")
                    break
                else:
                    if(colored):
                        colored_config=colored_configg(config)
                        print(colored_config)
                    else:
                        norm_config=normal_config(config)
                        print(norm_config)
                    print("input rejected")
                    break
            if(colored):
                colored_config=colored_configg(config)
                print(colored_config)
            else:
                norm_config=normal_config(config)
                print(norm_config)
            

def colored_configg(config):
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    result=""
    result+=config["state"]
    result+=' '
    n1=len(config["left_hand_side"])
    n2=len(config["right_hand_side"])

    for i in range(n1):
        result+=f"{GREEN} {config['left_hand_side'][i]} {RESET}"
    result+=f"{RED} {config['symbol']} {RESET}"

    for j in range(n2):
        result+=f"{YELLOW} {config['right_hand_side'][j]} {RESET}"

    return result

def normal_config(config):
    result=""
    result+=config["state"]
    result+=' '
    n1=len(config["left_hand_side"])
    n2=len(config["right_hand_side"])
    for i in range(n1):
        result+=config['left_hand_side'][i]
    result+='['
    result+=config['symbol']
    result+=']'
    for i in range(n2):
        result+=config['right_hand_side'][i]



    return result
# def make_tape(input_):
#     n=len(input_)
#     right_hand_side=[]
#     left_hand_side=[]
#     for i in range((n//2),n):
#         right_hand_side.append(input_[i])
#     for i in range(0,n//2):
#         left_hand_side.append(input_[(n//2)-i-1])
#     return left_hand_side,right_hand_side


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
        "left_hand_side":left_hand_side,
        "symbol":symbol,
        "right_hand_side": right_hand_side
    }

    return action,config


def find_next_symbol(symbol,move,left_hand_side,right_hand_side,blank):
    next_sym=blank
    if move=='R':
        left_hand_side.append(symbol)
        if right_hand_side:
            next_sym=right_hand_side.pop(0)
    if move=='L':
        if not left_hand_side:
            logging.warning("Singly-infinite tape boundary crossed (moving left from position 0).")
        right_hand_side.insert(0,symbol)
        if left_hand_side:
            next_sym=left_hand_side.pop()
    
    return next_sym

# def reverse(left_hand_side):
#     result=[]
#     n=len(left_hand_side)
#     for i in range(n):
#         result.append(left_hand_side[n-i-1])
#     return result