import simpy
from statemachine import StateMachine, State
import Logging.log as log
import Exceptions.OutOfStock as oos
import numpy as np
from math import trunc


class MfcStateMachine(StateMachine):
    def __init__(self, _env):
        self.__env = _env
        self.__controlArea = State('Checkin', initial=True)
        self.__orderArea = State("Ordering")
        self.__pickArea = State('Picking')
        self.__packArea = State('Packing')
        self.__labelArea = State('Labeling')
        self.__deliverArea = State('Delivering')
        self.__restArea = State('Resting')

        self.__getOrder = self.controlArea.to(self.orderArea)
        self.__pickOrder = self.orderArea.to(self.pickArea)
        self.__packOrder = self.pickArea.to(self.packArea)
        self.__labelOrder = self.packArea.to(self.labelArea)
        self.__deliverOrder = self.labelArea.to(self.deliverArea)
        self.__takeBreak = self.controlArea.to(self.restArea)
        self.__gotoControl = self.orderArea.to(self.controlArea) \
                             | self.pickArea.to(self.controlArea) \
                             | self.packArea.to(self.controlArea) \
                             | self.labelArea.to(self.controlArea) \
                             | self.deliverArea.to(self.controlArea) \
                             | self.restArea.to(self.controlArea)

    @property
    def gotoControl(self):
        return self.__gotoControl

    @gotoControl.setter
    def gotoControl(self, value):
        self.__gotoControl = value

    @property
    def takeBreak(self):
        return self.__takeBreak

    @takeBreak.setter
    def takeBreak(self, value):
        self.__takeBreak = value

    @property
    def deliverOrder(self):
        return self.__deliverOrder

    @deliverOrder.setter
    def deliverOrder(self, value):
        self.__deliverOrder = value

    @property
    def labelOrder(self):
        return self.__labelOrder

    @labelOrder.setter
    def labelOrder(self, value):
        self.__labelOrder = value

    @property
    def packOrder(self):
        return self.__packOrder

    @packOrder.setter
    def packOrder(self, value):
        self.__packOrder = value

    @property
    def pickOrder(self):
        return self.__getOrder

    @pickOrder.setter
    def pickOrder(self, value):
        self.__pickOrder = value

    @property
    def getOrder(self):
        return self.__getOrder

    @getOrder.setter
    def getOrder(self, value):
        self.__getOrder = value

    @property
    def restArea(self):
        return self.__restArea

    @restArea.setter
    def restArea(self, value):
        self.__restArea = value

    @property
    def deliverArea(self):
        return self.__deliverArea

    @deliverArea.setter
    def deliverArea(self, value):
        self.__deliverArea = value

    @property
    def labelArea(self):
        return self.__labelArea

    @labelArea.setter
    def labelArea(self, value):
        self.__labelArea = value

    @property
    def packArea(self):
        return self.__packArea

    @packArea.setter
    def packArea(self, value):
        self.__packArea = value

    @property
    def pickArea(self):
        return self.__pickArea

    @pickArea.setter
    def pickArea(self, value):
        self.__pickArea = value

    @property
    def orderArea(self):
        return self.__orderArea

    @orderArea.setter
    def orderArea(self, value):
        self.__orderArea = value

    @property
    def controlArea(self):
        return self.__controlArea

    @controlArea.setter
    def controlArea(self, value):
        self.__controlArea = value

    @property
    def env(self):
        return self.__env

    @env.setter
    def env(self, value):
        self.__env = value

    def controller(self):
        while True:
            yield self.getOrder(self)
            yield self.pickOrder(self)
            yield  self.packOrder(self)
            yield self.labelOrder(self)
            yield  self.deliverOrder(self)
            yield  self.gotoControl(self)

    def on_enter_control_area(self):
        # start counting entering the control area
        simulation_status = True
        station_start = self.env.now
        log.show_bread_crumbs(self.env.now, "Arrive at the Control")

        # do something
        op_time = MfcStateMachine.get_random()
        yield self.env.timeout(op_time)

        station_time = self.env.now - station_start
        log.log_op_time(station_time, "Did something after arriving at the Control")

        return simulation_status

    def on_exit_control_area(self):
        # start counting exiting the control area
        simulation_status = True
        station_start = self.env.now
        log.show_bread_crumbs(self.env.now, "Leaving the Control")

        # do something
        op_time = MfcStateMachine.get_random()
        yield self.env.timeout(op_time)

        station_time = self.env.now - station_start
        log.log_op_time(station_time, "Did something before leaving at the Control")

        return simulation_status

    def on_enter_order_area(self):
        # start counting entering the Order
        simulation_status = True
        station_start = self.env.now
        log.show_bread_crumbs(self.env.now, "Arriving at the Order")

        # do something
        op_time = MfcStateMachine.get_random()
        yield self.env.timeout(op_time)

        station_time = self.env.now - station_start
        log.log_op_time(station_time, "Did something after arriving at the Order")

        return simulation_status

    def on_exit_order_area(self):
        # start counting leaving the Order
        simulation_status = True
        station_start = self.env.now
        log.show_bread_crumbs(self.env.now, "Leaving the Order")

        # do something
        op_time = MfcStateMachine.get_random()
        yield self.env.timeout(op_time)

        station_time = self.env.now - station_start
        log.log_op_time(station_time, "Did something before leaving at the Order")

        return simulation_status

    def on_enter_pick_area(self):
        # start counting entering the Pick
        simulation_status = True
        station_start = self.env.now
        log.show_bread_crumbs(self.env.now, "Arriving at the Pick")

        # do something
        op_time = MfcStateMachine.get_random()
        yield self.env.timeout(op_time)

        station_time = self.env.now - station_start
        log.log_op_time(station_time, "Did something after arriving at the Pick")

        return simulation_status

    def on_exit_pick_area(self):
        # start counting leaving the Pick
        simulation_status = True
        station_start = self.env.now
        log.show_bread_crumbs(self.env.now, "Leaving the Pick")

        # do something
        op_time = MfcStateMachine.get_random()
        yield self.env.timeout(op_time)

        station_time = self.env.now - station_start
        log.log_op_time(station_time, "Did something before leaving at the Pick")

        return simulation_status

    def on_enter_pack_area(self):
        # start counting entering the Pack
        simulation_status = True
        station_start = self.env.now
        log.show_bread_crumbs(self.env.now, "Arriving at the Pack")

        # do something
        op_time = MfcStateMachine.get_random()
        yield self.env.timeout(op_time)

        station_time = self.env.now - station_start
        log.log_op_time(self.env.now, "Did something after arriving at the Pack")

        return simulation_status

    def on_exit_pack_area(self):
        # start counting leaving the Pack
        simulation_status = True
        station_start = self.env.now
        log.show_bread_crumbs(self.env.now, "Leaving the Pack")

        # do something
        op_time = MfcStateMachine.get_random()
        yield self.env.timeout(op_time)

        station_time = self.env.now - station_start
        log.log_op_time(station_time, "Did something before leaving at the Pack")

        return simulation_status

    def on_enter_label_area(self):
        # start counting entering the Label
        simulation_status = True
        station_start = self.env.now
        log.show_bread_crumbs(self.env.now, "Arriving at the Label")

        # do something
        op_time = MfcStateMachine.get_random()
        yield self.env.timeout(op_time)

        station_time = self.env.now - station_start
        log.log_op_time(station_time, "Did something after arriving at the Label")

        return simulation_status

    def on_exit_label_area(self):
        # start counting leaving the Label
        simulation_status = True
        station_start = self.env.now
        log.show_bread_crumbs(self.env.now, "Leaving the Label")

        # do something
        op_time = MfcStateMachine.get_random()
        yield self.env.timeout(op_time)

        station_time = self.env.now - station_start
        log.log_op_time(station_time, "Did something before leaving at the Label")

        return simulation_status

    def on_enter_delivery_area(self):
        # start counting entering the Delivery
        simulation_status = True
        station_start = self.env.now
        op_time = MfcStateMachine.get_random()
        log.show_bread_crumbs(self.env.now, "Arriving at the Delivery")

        # do something
        yield self.env.timeout(op_time)

        station_time = self.env.now - station_start
        log.log_op_time(station_time, "Did something after arriving at the Delivery")

        return simulation_status

    def on_exit_delivery_area(self):
        # start counting leaving the Delivery
        simulation_status = True
        station_start = self.env.now
        log.show_bread_crumbs(self.env.now, "Leaving the Delivery")

        # do something
        op_time = MfcStateMachine.get_random()
        yield self.env.timeout(op_time)

        station_time = self.env.now - station_start
        log.log_op_time(station_time, "Did something before leaving at the Delivery")

        return simulation_status


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
                yield self.env.process(self.cleaning())
                yield self.env.process(self.receiving())
                yield self.env.process(self.cycle_count())
                yield self.env.process(self.parcel_level_scanning())
            except OOS as err:
                # perform any action on YourException instance
                print("Message:", err.message)

    def cleaning(self):
        # start counting  cleaning area time
        simulation_status = True
        station_start = self.env.now

        # Simulate cleaning receiving
        print('Starting cleaning at %s' % self.env.now)
        area_time = self.get_random(1, 10)
        yield self.env.timeout(area_time)
        print('End cleaning at %s' % self.env.now)

        return simulation_status

    def receiving(self):
        # start counting  receiving area time
        simulation_status = True
        station_start = self.env.now

        # Simulate cleaning receiving
        print('Starting receiving at %s' % self.env.now)
        area_time = self.get_random(1, 10)
        yield self.env.timeout(area_time)
        print('End receiving at %s' % self.env.now)

        return simulation_status

    def cycle_count(self):
        # start counting cycle count area time
        simulation_status = True
        station_start = self.env.now

        # Simulate cleaning receiving
        print('Starting cycle count at %s' % self.env.now)
        area_time = self.get_random(1, 10)
        if self.env.now > 80:
            raise OOS('Time is higher than 80')
        yield self.env.timeout(area_time)
        print('End cycle count at %s' % self.env.now)

        return simulation_status

    def parcel_level_scanning(self):
        # start counting  parcel level scanning area time
        simulation_status = True
        station_start = self.env.now

        # Simulate cleaning receiving
        print('Starting parcel level scanning at %s' % self.env.now)
        area_time = self.get_random(1, 10)
        yield self.env.timeout(area_time)
        print('End parcel level scanning at %s' % self.env.now)

        return simulation_status

    @staticmethod
    def get_random(low, high):
        random = np.random.default_rng().random()
        return trunc((high - low) * random + low)


# Set up and run the simulation
# simulation_environment = simpy.Environment()  # one environment for the whole simulation
# ppp = PPP(simulation_environment)
# ppp_process = simulation_environment.process(ppp.checkin(simulation_environment))
# simulation_environment.run(until=150)

# Set up and run the simulation using state machines
simulation_environment = simpy.Environment()  # one environment for the whole simulation
pppStateMachine = MfcStateMachine(simulation_environment)
pppStateMachine_process = simulation_environment.process(pppStateMachine.controller())
simulation_environment.run(until=150)
