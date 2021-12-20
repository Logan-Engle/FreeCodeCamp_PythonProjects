import copy
import random
# Consider using the modules imported above.

class Hat:
    """
    Instantiates an object of the type hat
    """
    def __init__(self, **balls_dict):
        """
        Initialises instance variables
        """
        self.contents = []
        for key, val in balls_dict.items():
            for i in range(val):
                self.contents.append(key)

    def draw(self, amount):
        """
        Returns a list of balls removed from the hat
        equal to the amount passed in
        """
        if amount > len(self.contents):
            return self.contents
        else:
            removed_list = []
            for i in range(amount):
                random_index = random.randint(0, (len(self.contents) - 1))
                removed_list.append(self.contents[random_index])
                self.contents.remove(self.contents[random_index])
        return removed_list

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    Returns an approximate probability of drawing certain balls
    using the results from a specified number of tests
    """
    count = 0
    for i in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        drawn_balls = copy_hat.draw(num_balls_drawn)
        success = True
        for key, val in expected_balls.items():
            if drawn_balls.count(key) < val:
                success = False
                break
            else:
                success = True
        if  success:
            count += 1
    return count/num_experiments