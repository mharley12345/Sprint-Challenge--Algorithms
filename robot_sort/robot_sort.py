class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"
    
    #Helper Functions to use
    def right_swap(self):
        """
        Swap element to right of current position
        """

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out
        
        # Robot needs to sort a list, based on its functions -> moving, swapping, comparing and turn light on/off
        # Robot move right or left until it has stop
        # Algorithm to use  -> selection sort
        
        #You can loop around the list endlessly, has to be stopped when sorting is complete

        self.set_light_on() #initialize the robot sorting state and will allow us to break out of it

        #lets loop through the list
        while self.light_is_on() == True:
            
            #Robot starts at position [0] of the list 
            #When the robot initially picks item, it leaves 'None' in the list
            #We can use 'None' of the list as pivot to divide the list into left side as sorted while right side of pivot needs to sorted
            #This may result multiple passes of list before it is done
            #Performance could be slow
            self.swap_item() #Initial Pickup
            #Keep moving to the right to find smallest item 
            while self.can_move_right():
                self.move_right()
                #Lets check the item being held is larger than item in the list
                if self.compare_item() == 1:
                    #Swapped it out for a smaller item
                    self.swap_item()
                #Lets keep going to right to see if we can another smaller item from the list
            
            #If we end up reaching end of right side of list, then we are carrying smallest item in the list, lets go place back where we pick the first item and swapped with 'None'

            while self.can_move_left() == True and self.compare_item() != None:
                self.move_left()

            #We have now reach 'None' Our pivot, where we can swapped the smallest item in the List

            self.swap_item()

            #Now we move to right and swap the next item, and set 2nd position as new pivot and continue the loop. However, we will eventually reach the end of right side. 

            #Move to next item right of pivot 'None' and start the process again
            if self.can_move_right() == True:
                self.move_right()
            else:
                #If we reach end of right side, then we have swapped all items correctly and robot is not holding anything, can finally rest
                self.set_light_off()

                    




if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [5,4,6,9]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)