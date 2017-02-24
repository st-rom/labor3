class Property:
    '''
    Represents the property
    '''
    def __init__(self, square_feet='', beds='',
                 baths='', **kwargs):
        '''
        Initiates Property class's parameters
        :param square_feet: str
        :param beds: str
        :param baths: str
        :param kwargs: str
        '''
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        '''
        Prints property details
        :return: None
        '''
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        '''
        Inputs dictionary variables
        :return: dict
        '''
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))

    prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    '''
    This function gets valid input and returns it for further usage
    :param input_string: string
    :param valid_options: string/list
    :return: string which is in input_string
    '''
    input_string += " ({}) ".format((", ".join(valid_options)))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Apartment(Property):
    '''
    Represents apartment which is child of class Property
    '''
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        '''
        Initiates some variables
        :param balcony: string
        :param laundry: string
        :param kwargs: string
        '''
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        '''
        Prints information about Apartment
        :return: None
        '''
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: {}".format(self.laundry))
        print("has balcony: {}".format(self.balcony))

    def prompt_init():
        '''
        Creates and returns dictionary with some description of the apartment
        :return: dict
        '''
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does "
            "the property have? ",
            Apartment.valid_laundries)
        balcony = get_valid_input(
            "Does the property have a balcony?",
            Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    '''
    Represents House class, child of Property class
    '''
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='',
                 garage='', fenced='', **kwargs):
        '''
        Initiates House parameters
        :param num_stories: str,
        :param garage: str
        :param fenced: str
        :param kwargs: str
        '''
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        '''
        Prints information about House
        :return: None
        '''
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        '''
        Returns some information about House
        :return: dict
        '''
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How many stories? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    '''
    Represents Purchase class
    '''
    def __init__(self, price='', taxes='', **kwargs):
        '''
        Initiates arguments of Purchase class
        :param price: str
        :param taxes: str
        :param kwargs: str
        '''
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        '''
        Prints some information about Purchase
        :return: None
        '''
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        '''
        Creates dict which contains information about purchase
        :return: dict
        '''
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    '''
    Represents Rental with information about it
    '''
    def __init__(self, furnished='', utilities='',
                 rent='', **kwargs):
        '''
        Initiates arguments of Rental class
        :param furnished: str
        :param utilities: str
        :param rent: str
        :param kwargs: str
        '''
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        '''
        Prints some information about Rental
        :return: None
        '''
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        '''
        Creates dictionary with some information about Rental
        :return: dict
        '''
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ",
                                      ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    '''
    Represents class HouseRental which is child of classes Rental and House
    '''
    def prompt_init():
        '''
        Creates dictionary which contains details about House and Rental
        :return: dict
        '''
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    '''
    Represents class ApartmentRental which is child of classes Rental and Apartment
    '''
    def prompt_init():
        '''
        Creates dictionary which contains details about Apartment and Rental
        :return: dict
        '''
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    '''
    Represents class ApartmentPurchase which is child of classes Purchase and Apartment
    '''
    def prompt_init():
        '''
        Creates dictionary which contains details about Apartment and Purchase
        :return: dict
        '''
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    '''
    Represents class HousePurchase which is child of classes Purchase and House
    '''
    def prompt_init():
        '''
        Creates dictionary which contains details about House and Purchase
        :return: dict
        '''
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    '''
    Represent class Agent
    '''
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def __init__(self):
        '''
        Initiates property list
        '''
        self.property_list = []

    def display_properties(self):
        '''
        Shows information about properties
        :return: None
        '''
        for property in self.property_list:
            property.display()

    def add_property(self):
        '''
        Adds property and payment type
        :return: None
        '''
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()

        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))


