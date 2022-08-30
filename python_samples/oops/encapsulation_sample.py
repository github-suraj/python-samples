'''
    Module File for Encapsulation sample class with:
        1. Private Variables
        2. Private Methods
'''


class Car:
    '''
        A Car class
            Private Instance Variable:
                __max_speed
    '''
    def __init__(self):
        self.__max_speed = 100

    def get_max_speed(self):
        '''
            Getter Method for car speed
        '''
        return self.__max_speed

    def set_max_speed(self, speed):
        '''
            Setter Method for car speed
        '''
        self.__max_speed = speed

    @staticmethod
    def __update_software():
        '''
            Private Method to Display, Car is getting Upgraded
        '''
        print('Updating Software')

    def drive(self):
        '''
            Method to drive car
        '''
        print('Driving at Maxspeed', self.__max_speed)


if __name__ == '__main__':
    redcar = Car()
    ## redcar.__update_software()
    #   Error: 'Car' object has no attribute '__update_software'
    ## redcar.__max_speed
    #   Error: 'Car' object has no attribute '__max_speed'

    # Access to a protected member _Car__max_speed of a client class
    print('MaxSpeed:', redcar._Car__max_speed)
    # Access to a protected member _Car__update_software of a client class
    redcar._Car__update_software()
    # Access to a protected member _Car__max_speed of a client class
    redcar._Car__max_speed = 200
    redcar.drive()
    redcar.set_max_speed(150)
    print('MaxSpeed:', redcar.get_max_speed())
