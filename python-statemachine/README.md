# python-statemachine
Learning [python-statemachine](https://pypi.org/project/python-statemachine/) by playing around with it.

# Observations
## Callbacks
The documentation does not provide any `on_exit` examples. This works:
```python
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
traffic_light.slowdown()
```
This works, as shown below:
 ```bash
$ python3 fsm-1.py
on_slowdown
on_exit_green!
on enter yellow.
```

## Static methods do not work for TrafficLightMachine
If we declare the callback methods as static and attempt to use them, we get the `AttributeError: 'NoneType' object has no attribute 'current_state'`;

# Experimenting with integrating it with SimPy
Unable to integrate SimPy and python-statemachine easily. I'll come back to it later.