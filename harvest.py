############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller
        self.name = name

        self.pairings = []

        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        # is pairing a list or a string --> TBD
        # Fill in the rest
        # if it is a list, unpacks and adds
        self.pairings.extend(*pairing)
        # self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    # file_of_melons = open(melons_list.txt)
    # melon_names = {}
    # for line in file_of_melons:
    #     if line.startswith('Name: '):
    #         melon_names[line[6:]=.set_default({})

    # def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 # name):
    # Fill in the rest
    muskmelon = MelonType('musk', first_harvest=1998, color ='green', is_seedless=True, 
                          is_bestseller=True, name='Muskmelon')
    muskmelon.add_pairing(['mint'])
                        
    casaba = MelonType(code='cas', first_harvest = 2003, color='orange', is_bestseller=False, 
                        is_seedless=False, name = "Casaba")
    casaba.add_pairing(['strawberries', 'mint'])

    crenshaw = MelonType(code='cren', first_harvest = 1996, color='green', is_bestseller=False, 
                        is_seedless=False, name = "Crenshaw")
    crenshaw.add_pairing(['proscuitto'])

    yellow_water = MelonType(code='yw', first_harvest = 2013, color='yellow', is_bestseller=False, 
                        is_seedless=False, name = "Yellow Watermelon")
    crenshaw.add_pairing(['ice cream'])



    


    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 


