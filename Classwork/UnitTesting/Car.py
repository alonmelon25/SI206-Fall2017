class SelfDrivingCar(object):
 
    def __init__(self):
 
        self.speed = 0
 
        self.destination = None
 
         
 
    def _accelerate(self):
 
        self.speed += 1
 
         
 
    def _decelerate(self):
 
        if self.speed > 0:
 
            self.speed -= 1
 
                     
 
    def _advance_to_destination(self):
 
        distance = self._calculate_distance_to_object_in_front()
 
        if distance < 10:
 
            self.stop()
 
 
 
        elif distance < self.speed / 2:
 
            self._decelerate()
 
        elif self.speed < self._get_speed_limit():
 
            self._accelerate()
 
     
 
    def _has_arrived(self):
 
        pass
 
         
 
    def _calculate_distance_to_object_in_front(self):
 
        pass
 
         
 
    def _get_speed_limit(self):
 
        pass
 
         
 
    def stop(self):
 
        self.speed = 0
 
         
 
    def drive(self, destination):
 
        self.destination = destination
 
        while not self._has_arrived():            
 
            self._advance_to_destination()
 
 
        self.stop()
 
    def __init__(self):
 
        self.speed = 0
 
        self.destination = None
 
         
 
    def _accelerate(self):
 
        self.speed += 1
 
         
 
    def _decelerate(self):
 
        if self.speed > 0:
 
            self.speed -= 1
 
                     
 
    def _advance_to_destination(self):
 
        distance = self._calculate_distance_to_object_in_front()
 
        if distance < 10:
 
            self.stop()
 
 
 
        elif distance < self.speed / 2:
 
            self._decelerate()
 
        elif self.speed < self._get_speed_limit():
 
            self._accelerate()
 
     
 
    def _has_arrived(self):
 
        pass
 
         
 
    def _calculate_distance_to_object_in_front(self):
 
        pass
 
         
 
    def _get_speed_limit(self):
 
        pass
 
         
 
    def stop(self):
 
        self.speed = 0
 
         
 
    def drive(self, destination):
 
        self.destination = destination
 
        while not self._has_arrived():            
 
            self._advance_to_destination()
 
        self.stop()


