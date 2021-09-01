"""
Program:               annual_insurance_cost_calculator.py
Author:                Noah Allan Ertz
Last Date Modified:    2021-08-31

Calculates the annual insurance cost of each driver.
"""

from custom_exceptions.driver_exception import InvalidNameException, InvalidAgeException, InvalidCoverageLevelException
from constants.coverages import AGE_0, AGE_1, AGE_2, AGE_3, AGE_4, AGE_5, STATE_MINIMUM_0, STATE_MINIMUM_1, STATE_MINIMUM_2, STATE_MINIMUM_3, STATE_MINIMUM_4, STATE_MINIMUM_5, LIABILITY_COVERAGE_0, LIABILITY_COVERAGE_1, LIABILITY_COVERAGE_2, LIABILITY_COVERAGE_3, LIABILITY_COVERAGE_4, LIABILITY_COVERAGE_5, FULL_COVERAGE_0, FULL_COVERAGE_1, FULL_COVERAGE_2, FULL_COVERAGE_3, FULL_COVERAGE_4, FULL_COVERAGE_5, ACCIDENT_RATE_INCREASE


def get_driver_dictionary(driver_id):
    """
    Gets driver information for input and returns driver dictionary.

    :param driver_id: ID number for driver dictionary
    :return: driver dictionary
    """

    # Acceptable characters for name and age.
    name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ")
    age_characters = set('1234567890')

    # Get and check driver name.
    driver_name = input('Enter Driver Name: ')
    if not name_characters.issuperset(driver_name):
        raise InvalidNameException(driver_name)

    # Get and check driver string.
    driver_age_string = input('Enter Driver Age: ')
    if not age_characters.issuperset(driver_age_string):
        raise ValueError
    else:
        driver_age = int(driver_age_string)
        if driver_age < AGE_0:
            raise InvalidAgeException(driver_age)

    # Get and check desired coverage level.
    desired_coverage_level = input('Enter Driver\'s desired_coverage_level: ')
    if desired_coverage_level.lower() != 'sm' and desired_coverage_level.lower() != 'l' and desired_coverage_level.lower() != 'f':
        raise InvalidCoverageLevelException(desired_coverage_level)

    # Determine coverage cost from age and desired coverage level.
    coverage_cost = 0
    if AGE_0 <= driver_age < AGE_1:
        if desired_coverage_level.lower() == 'sm':
            coverage_cost = STATE_MINIMUM_0
        elif desired_coverage_level.lower() == 'l':
            coverage_cost = LIABILITY_COVERAGE_0
        elif desired_coverage_level.lower() == 'f':
            coverage_cost = FULL_COVERAGE_0
    elif AGE_1 <= driver_age < AGE_2:
        if desired_coverage_level.lower() == 'sm':
            coverage_cost = STATE_MINIMUM_1
        elif desired_coverage_level.lower() == 'l':
            coverage_cost = LIABILITY_COVERAGE_1
        elif desired_coverage_level.lower() == 'f':
            coverage_cost = FULL_COVERAGE_1
    elif AGE_2 <= driver_age < AGE_3:
        if desired_coverage_level.lower() == 'sm':
            coverage_cost = STATE_MINIMUM_2
        elif desired_coverage_level.lower() == 'l':
            coverage_cost = LIABILITY_COVERAGE_2
        elif desired_coverage_level.lower() == 'f':
            coverage_cost = FULL_COVERAGE_2
    elif AGE_3 <= driver_age < AGE_4:
        if desired_coverage_level.lower() == 'sm':
            coverage_cost = STATE_MINIMUM_3
        elif desired_coverage_level.lower() == 'l':
            coverage_cost = LIABILITY_COVERAGE_3
        elif desired_coverage_level.lower() == 'f':
            coverage_cost = FULL_COVERAGE_3
    elif AGE_4 <= driver_age < AGE_5:
        if desired_coverage_level.lower() == 'sm':
            coverage_cost = STATE_MINIMUM_4
        elif desired_coverage_level.lower() == 'l':
            coverage_cost = LIABILITY_COVERAGE_4
        elif desired_coverage_level.lower() == 'f':
            coverage_cost = FULL_COVERAGE_4
    elif AGE_5 <= driver_age:
        if desired_coverage_level.lower() == 'sm':
            coverage_cost = STATE_MINIMUM_5
        elif desired_coverage_level.lower() == 'l':
            coverage_cost = LIABILITY_COVERAGE_5
        elif desired_coverage_level.lower() == 'f':
            coverage_cost = FULL_COVERAGE_5

    # Create list of driver information.
    driver_information = [driver_name, driver_age, desired_coverage_level, coverage_cost]

    # Create driver dictionary from driver ID and driver information list
    driver_dictionary = {driver_id: driver_information}

    return driver_dictionary


if __name__ == '__main__':
    # Initialize driver input answer variable for while loop
    is_there_driver_answer = 'y'
    # ID number
    new_id = 0
    # Initialize drivers dictionary.
    drivers = {}

    # Execute while there is another driver.
    while is_there_driver_answer[0].lower() == 'y':
        # Prompt user.
        is_there_driver_answer = input('Enter driver? (y/N) ')
        # Determine if there is another driver from user input.
        if is_there_driver_answer[0].lower() == 'y':
            # Check for exceptions.
            try:
                # Get driver dictionary.
                driver = get_driver_dictionary(new_id)
                # Update dictionary of multiple drivers.
                drivers.update(driver)

                # Prompt user for any accidents from driver.
                accidents_answer = input('Have you had any accidents? (y/n) ')
                # Continue to request valid answer if invalid.
                while accidents_answer[0].lower() != 'y' and accidents_answer[0].lower() != 'n':
                    accidents_answer = input('Invalid answer. Have you had any accidents? (y/n) ')

                # Determine if driver had accidents.
                if accidents_answer[0].lower() == 'y':
                    # Add accident rate increase to driver
                    drivers.get(new_id)[3] += int(drivers.get(new_id)[3] * ACCIDENT_RATE_INCREASE)
            except InvalidNameException as message:
                print(message)
            except InvalidAgeException as message:
                print(message)
            except InvalidCoverageLevelException as message:
                print(message)
            except ValueError:
                print('ValueError encountered.')
            else:
                # Increment driver ID.
                new_id += 1
        else:
            break

    # Print all of the drivers' annual insurance coverage costs if there are any.
    if drivers != {}:
        print('\nAnnual Insurance Coverage Costs')
        for driver in drivers.values():
            print(f'{driver[0]}: ${driver[3]}')
