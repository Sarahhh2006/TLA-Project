# -*- coding: utf-8 -*-
from turing_machine import TuringMachine
from test_turing_machine_example1 import print_states

#create the Turing machine
transitions = {
        ('q0','1'):('qs','y','R'),
        ('q0','0'):('q10','0','R'),
        ('qs','1'):('qs','y','R'),
        ('qs','0'):('qs2','0','R'),
        ('qs2',''):('qs3','','L'),
        ('qs3','0'):('qs3','0','L'),
        ('qs3','y'):('qs3','','L'),
        ('qs3',''):('qs4','','R'),
        ('qs4',''):('qs4','','R'),
        ('qs4','0'):('qs5','0','R'),
        ('qs5',''):('qa','','L'),
        ('qs2','1'):('qs6','1','L'),

        ('qs6','0'):('q1','0','R'),

        ('q1','x'):('q1','x','R'),
        ('q1','1'):('q2','x','L'),
        ('q2','x'):('q2','x','L'),
        ('q2','0'):('q2','0','L'),

        ('q2','y'):('q3','Y','L'),
        ('q3','1'):('q3','1','L'),
        ('q3','y'):('q3','y','L'),
        ('q3',''):('q4','1','R'),
        ('q4','1'):('q4','1','R'),
        ('q4','y'):('q4','y','R'),   
        ('q4','Y'):('q5','Y','L'),
        ('q5','1'):('q9','1','R'),
        ('q5','y'):('q3','Y','L'),
        ('q9','Y'):('q9','y','R'),
        ('q9','0'):('q1','0','R'),
        ('q1',''):('q7','','L'),
        ('q7','x'):('q7','','L'),
        ('q7','0'):('q7','','L'),
        ('q7','y'):('q7','','L'),
        ('q7','1'):('q7','1','L'),
        ('q7',''):('qa','','R'),


        ('q10','1'):('q10','','R'),
        ('q10',''):('q10','','L'),
        ('q10','0'):('q11','','L'),
        ('q11',''):('qa','','R'),

}
if __name__ == "__main__":
    print_states(transitions)
    machine = TuringMachine(transitions)

    def run(input_):
        w = input_
        print("Input:",w)
        print("Accepted" if machine.accepts(w) else "Rejected")
        machine.debug(w, step_limit=1000)

        print()

    # SHOULD ACCEPT
    run("110111")
    # outputs 111111

    # SHOULD ACCEPT
    run("11101111")
    # outputs 111111111111

    run("01111")
