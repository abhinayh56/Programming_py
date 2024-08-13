from abc import ABC, abstractmethod

class Servo(ABC):
    @abstractmethod
    def enable(self):
        pass
    
    @abstractmethod
    def disable(self):
        pass
    
    @abstractmethod
    def set_mode(self, mode):
        pass

    @abstractmethod
    def set_angle(self, angle):
        pass

    @abstractmethod
    def set_speed(self, speed):
        pass

    @abstractmethod
    def set_torque(self, torque):
        pass

    @abstractmethod
    def e_stop(self):
        pass

    @abstractmethod
    def quick_stop(self):
        pass

class Servo_1(Servo):
    def enable(self):
        print("servo 1: enable")
    
    def disable(self):
        print("servo 1: disable")
    
    def set_mode(self, mode):
        print(f"servo 1: mode {mode}")

    def set_angle(self, angle):
        print(f"servo 1: set_angle {angle}")

    def set_speed(self, speed):
        print(f"servo 1: set_speed {speed}")

    def set_torque(self, torque):
        print(f"servo 1: set_torque {torque}")

    def e_stop(self):
        print("servo 1: e_stop")

    def quick_stop(self):
        print("servo 1: quick_stop")

class Servo_2(Servo):
    def enable(self):
        print("servo 2: enable")
    
    def disable(self):
        print("servo 2: disable")
    
    def set_mode(self, mode):
        print(f"servo 2: mode {mode}")

    def set_angle(self, angle):
        print(f"servo 2: set_angle {angle}")

    def set_speed(self, speed):
        print(f"servo 2: set_speed {speed}")

    def set_torque(self, torque):
        print(f"servo 2: set_torque {torque}")

    def e_stop(self):
        print("servo 2: e_stop")

    def quick_stop(self):
        print("servo 2: quick_stop")

class Servo_3(Servo):
    def enable(self):
        print("servo 3: enable")
    
    def disable(self):
        print("servo 3: disable")
    
    def set_mode(self, mode):
        print(f"servo 3: mode {mode}")

    def set_angle(self, angle):
        print(f"servo 3: set_angle {angle}")

    def set_speed(self, speed):
        print(f"servo 3: set_speed {speed}")

    def set_torque(self, torque):
        print(f"servo 3: set_torque {torque}")

    def e_stop(self):
        print("servo 3: e_stop")

    def quick_stop(self):
        print("servo 3: quick_stop")

class Servo_4(Servo):
    def enable(self):
        print("servo 4: enable")
    
    def disable(self):
        print("servo 4: disable")
    
    def set_mode(self, mode):
        print(f"servo 4: mode {mode}")

    def set_angle(self, angle):
        print(f"servo 4: set_angle {angle}")

    def set_speed(self, speed):
        print(f"servo 4: set_speed {speed}")

    def set_torque(self, torque):
        print(f"servo 4: set_torque {torque}")

    def e_stop(self):
        print("servo 4: e_stop")

    def quick_stop(self):
        print("servo 4: quick_stop")

class Servo_5(Servo):
    def enable(self):
        print("servo 5: enable")
    
    def disable(self):
        print("servo 5: disable")
    
    def set_mode(self, mode):
        print(f"servo 5: mode {mode}")

    def set_angle(self, angle):
        print(f"servo 5: set_angle {angle}")

    def set_speed(self, speed):
        print(f"servo 5: set_speed {speed}")

    def set_torque(self, torque):
        print(f"servo 5: set_torque {torque}")

    def e_stop(self):
        print("servo 5: e_stop")

    def quick_stop(self):
        print("servo 5: quick_stop")

class Servo_6(Servo):
    def enable(self):
        print("servo 6: enable")
    
    def disable(self):
        print("servo 6: disable")
    
    def set_mode(self, mode):
        print(f"servo 6: mode {mode}")

    def set_angle(self, angle):
        print(f"servo 6: set_angle {angle}")

    def set_speed(self, speed):
        print(f"servo 6: set_speed {speed}")

    def set_torque(self, torque):
        print(f"servo 6: set_torque {torque}")

    def e_stop(self):
        print("servo 6: e_stop")

    def quick_stop(self):
        print("servo 6: quick_stop")

s_1 = Servo_1()
s_2 = Servo_2()
s_3 = Servo_3()
s_4 = Servo_4()
s_5 = Servo_5()
s_6 = Servo_6()

s_1.enable()
s_2.enable()
s_3.enable()
s_4.enable()
s_5.enable()
s_6.enable()