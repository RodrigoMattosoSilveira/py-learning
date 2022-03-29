import simpy
from math import trunc
import Logging.log as log


class OOS(Exception):
    def __init__(self, message):
        self.message = message


class PPP(object):
    """
    The PPP process (each ppp has a name) arrives at the order station (order_area), requests an order, fulfills the
    order and yells hooray
    """

    def __init__(self, _env):
        self.__env = _env
        self.__pppShiftTally = None
        self.__pppOrderTally = None
        self.__orderTabletResource = None
        self.__packingLocationResource = None
        self.__labelPrintersResource = None
        self.__orderTallyLog = None
        self.__pppActivityLog = None

    @property
    def env(self):
        return self.__env

    @env.setter
    def env(self, value):
        self.__env = value

    def checkin(self, _env):

        while True:
            try:
                yield self.env.process(self.cleaning_receiving())
                yield self.env.process(self.cycle_count())
                yield self.env.process(self.parcel_level_scanning())
            except OOS as err:
                # perform any action on YourException instance
                print("Message:", err.message)

    def cleaning_receiving(self):
        # start counting  cleaning receiving area time
        simulation_status = True
        station_start = self.env.now

        # Simulate cleaning receiving
        print('Starting cleaning receiving at %s',  self.env.now)
        area_time = 10
        yield self.env.timeout(area_time)
        print('End cleaning receiving at %s',  self.env.now)

        return simulation_status

    def cycle_count(self):
        # start counting cycle count area time
        simulation_status = True
        station_start = self.env.now

        # Simulate cleaning receiving
        print('Starting cycle count at %s',  self.env.now)
        area_time = 10
        if  self.env.now > 80:
            raise OOS('Time is higher than 80')
        yield self.env.timeout(area_time)
        print('End cycle count at %s',  self.env.now)

        return simulation_status

    def parcel_level_scanning(self):
        # start counting  parcel level scanning area time
        simulation_status = True
        station_start = self.env.now

        # Simulate cleaning receiving
        print('Starting parcel level scanning at %s',  self.env.now)
        area_time = 10
        yield self.env.timeout(area_time)
        print('End parcel level scanning at %s',  self.env.now)

        return simulation_status


# Set up the simulation
simulation_environment = simpy.Environment()  # one environment for the whole simulation
ppp = PPP(simulation_environment)
ppp_process = simulation_environment.process(ppp.checkin(simulation_environment))

# Run the simulation
simulation_environment.run(until=150)

