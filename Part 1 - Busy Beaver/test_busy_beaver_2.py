# -*- coding: utf-8 -*-
from turing_machine import TuringMachine


bbeaver2 = TuringMachine(
    { 
        # TODO: Part III c) - Write your transition rules for the 2-card Busy Beaver program here
        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('b', '1', 'L'),
        ('b', '0'): ('a', '1', 'L'),
        ('b', '1'): ('h', '1', 'R'),
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)
bbeaver3 = TuringMachine(
    {
        # TODO: Part III e) - Write your own transition rules for the 3-card Busy Beaver program here
        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('h', '1', 'R'),
        ('b', '0'): ('c', '0', 'R'),
        ('b', '1'): ('b', '1', 'R'),
        ('c', '0'): ('c', '1', 'L'),
        ('c', '1'): ('a', '1', 'L'),
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)
bbeaver4 = TuringMachine(
    {
        # TODO: Part III e) - Write your own transition rules for the 4-card Busy Beaver program here
        ('a', '0'): ('b', '1', 'R'),
        ('a', '1'): ('b', '1', 'L'),
        ('b', '0'): ('a', '1', 'L'),
        ('b', '1'): ('c', '0', 'L'),
        ('c', '0'): ('h', '1', 'R'),
        ('c', '1'): ('d', '1', 'L'),
        ('d', '0'): ('d', '1', 'R'),
        ('d', '1'): ('a', '0', 'R'),
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)
bbeaver5 = TuringMachine(
    {
        # TODO: Part III f) - Write your own transition rules for the 5-card Busy Beaver program here
        ('a', '0'): ('b', '1', 'L'),
        ('a', '1'): ('a', '1', 'L'),
        ('b', '0'): ('c', '1', 'R'),
        ('b', '1'): ('b', '1', 'R'),
        ('c', '0'): ('a', '1', 'L'),
        ('c', '1'): ('d', '1', 'R'),
        ('d', '0'): ('a', '1', 'L'),
        ('d', '1'): ('e', '1', 'R'),
        ('e', '0'): ('h', '1', 'R'),
        ('e', '1'): ('c', '0', 'R'),
    },
    start_state='a', accept_state='h', reject_state='r', blank_symbol='0'
)

def count_ones_from_machine(machine, input_):
    last_config = None
    for action, config in machine.run(input_):
        last_config = config
        if action in ('Accept', 'Reject'):
            break
    if last_config:
        tape = last_config['left_hand_side'] + [last_config['symbol']] + last_config['right_hand_side']
        return sum(1 for ch in tape if ch == '1')
    return 0

if __name__ == "__main__":
    def run(input_):
        w = input_
        # the same as mine 4 ones
        # This is an optimal BB-2. 4 is the maximum number of 1s you can get for 2 states
        print("BB with 2 states")
        bbeaver2.debug(w, step_limit=1000)
        print()

        count_ones_2 = count_ones_from_machine(bbeaver2, w)
        print(f"count: {count_ones_2}")
        print()
        # 6
        print("BB with 3 states")
        bbeaver3.debug(w, step_limit=1000)
        print()
        count_ones_3 = count_ones_from_machine(bbeaver3, w)
        print(f"count: {count_ones_3}")
        print()
        # 13
        print("BB with 4 states")
        bbeaver4.debug(w, step_limit=1000)
        print()
        count_ones_4 = count_ones_from_machine(bbeaver4, w)
        print(f"count: {count_ones_4}")
        print()
        # This machine runs for 47176870 steps, writing 4098 1s, and then halts. So BB(5) is at least 47176870
        # print("BB with 5 states")
        # bbeaver5.debug(w, step_limit=10000)
        # print()
        # count_ones_5 = count_ones_from_machine(bbeaver5, w)
        # print(f"count: {count_ones_5}")
        # print()


        # به همین ترتیب برای ۳، ۴ و ۵
        ...


    

    run('00000000000000')  # 14 0

# bbeaver.debug('00000000000000', step_limit=1000)
def count_ones_from_machine(machine, input_):
    last_config = None
    for action, config in machine.run(input_):
        last_config = config
        if action in ('Accept', 'Reject'):
            break
    if last_config:
        tape = last_config['left_hand_side'] + [last_config['symbol']] + last_config['right_hand_side']
        return sum(1 for ch in tape if ch == '1')
    return 0