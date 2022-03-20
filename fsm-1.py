from statemachine import StateMachine, State


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
