"""
Attempt to mix SimPy python-statemachine
"""
from statemachine import StateMachine, State
from random import randint
import simpy


class EV:
    def __init__(self, _env):
        self.env = _env
        self.drive_proc = env.process(self.drive())
        self.bat_ctrl_proc = env.process(self.bat_ctrl())
        self.bat_ctrl_reactivate = env.event()

    def drive(self):
        while True:
            # Drive for 20-40 min
            yield self.env.timeout(randint(20, 40))

            # Park for 1–6 hours
            print('Start parking at', self.env.now)
            self.bat_ctrl_reactivate.succeed()  # "reactivate"
            self.bat_ctrl_reactivate = env.event()
            yield env.timeout(randint(60, 360))
            print('Stop parking at', self.env.now)

    def bat_ctrl(self):
        while True:
            print('Bat. ctrl. passivating at', self.env.now)
            yield self.bat_ctrl_reactivate  # "passivate"
            print('Bat. ctrl. reactivated at', self.env.now)

            # Intelligent charging behavior here …
            yield env.timeout(randint(30, 90))


env = simpy.Environment()
ev = EV(env)
env.run(until=150)
"""
class TrafficLightMachine(StateMachine):
    green = State('Green', initial=True)
    yellow = State('Yellow')
    red = State('Red')

    slowdown = green.to(yellow)
    stop = yellow.to(red)
    go = red.to(green)

    # transitions
    # @staticmethod
    def on_slowdown(self):
        print('on_slowdown')

    # @staticmethod
    def on_stop(self):
        print('on_stop.')

    # @staticmethod
    def on_go(self):
        print('on_go')

    # on_enter
    # @staticmethod
    def on_enter_green(self):
        print('on_enter_green')

    # @staticmethod
    def on_enter_yellow(self):
        print('on enter yellow.')

    # @staticmethod
    def on_enter_red(self):
        print('on enter red!')

    # on_exit
    # @staticmethod
    def on_exit_green(self):
        print('on_exit_green!')

    # @staticmethod
    def on_exit_yellow(self):
        print('on_exit_yellow')

    # @staticmethod
    def on_exit_enter_red(self):
        print('on_exit_enter_red!')


traffic_light = TrafficLightMachine()
# print(traffic_light.current_state)
# print(traffic_light.is_green)
traffic_light.slowdown()

"""
