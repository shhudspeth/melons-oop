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
        self.is_bestseller = is_bestseller
        self.name = name

        self.pairings = []

        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        # is pairing a list or a string --> TBD
        # Fill in the rest
        # if it is a list, unpacks and adds
        self.pairings.extend(pairing)
        # dirself.pairings.append(pairing)

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
                        is_seedless=False, name="Crenshaw")
    crenshaw.add_pairing(['proscuitto'])
   

    yellow_water = MelonType(code='yw', first_harvest = 2013, color='yellow', is_bestseller=False, 
                        is_seedless=False, name="Yellow Watermelon")
    yellow_water.add_pairing(['ice cream'])

    all_melon_types.extend([muskmelon, casaba, crenshaw, yellow_water])

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest
    for melon in melon_types:
        print(f"{melon.name} pairs with")
        for pair in melon.pairings:
            print(f"  - {pair}")
        print(f"\n")

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_code_dict = {}
    # Fill in the rest
    for melon in melon_types:
        melon_code_dict[melon.code] = melon_code_dict.get(melon.code, melon)
    return melon_code_dict

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, melon_type, shape_rating, color_rating, harvest_field, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvest_field = harvest_field
        self.harvested_by = harvested_by
        self.can_sell= self.is_sellable()

    def is_sellable(self):
        return (self.shape_rating > 5 and self.color_rating > 5 and self.harvest_field !=3)

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest
    # dictionary of melon types
    melons_by_id = make_melon_type_lookup(melon_types)
    melon_1 = Melon(melons_by_id['yw'], 8,7, 2, 'Sheila')
    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Sheila')
    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Sheila')
    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Sheila')
    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Sheila')

    return [melon_1, melon_2, melon_3, melon_4, melon_5, melon_6, melon_7, melon_8, melon_9]

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 
    for melon in melons:
        if melon.can_sell:
            sell_yes_or_no = "(CAN BE SOLD)"
        else:
            sell_yes_or_no = "(NOT SELLABLE)" 

        print(f"Harvested by{melon.harvested_by} from Field {melon.harvest_field} {sell_yes_or_no}")


