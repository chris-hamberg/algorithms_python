from types import SimpleNamespace
import random, string, sys

'''
To execute the testing function run the code with command line argument test
ex. ~$ python change_making.py test

For normal usage run the script with an amount as a command line argument
ex. ~$ python change_making.py 23.62
'''
class InvalidInputError(Exception):
    def __init__(self):
        super().__init__()

# Initialize denomination definitions (as integers less than 100 for precision)
DENOMINATIONS = {
        'quarter': 25, 
        'dime': 10,
        'nickel': 5, 
        'penny': 1
        }

def make_change(amount):
    '''
    Optimized Greedy Change Making Algorithm.
    '''
    # Initialize data structure.
    namespace = SimpleNamespace(
                is_valid = True,
                amount   = amount, 
                dollars  = 0, 
                cents    = 0, 
                change   = SimpleNamespace(
                                dollar  = 0, 
                                quarter = 0, 
                                dime    = 0, 
                                nickel  = 0, 
                                penny   = 0)
                )
    # remove leading $ sign from input string, if it exists
    namespace = text_process(namespace)
    
    try:
        # Validate input.
        namespace = validate(namespace)
    except InvalidInputError:
        namespace.change = ('Amount must be a positive real number, '
                            'and in a valid format.')
    else:
        
        namespace.change.dollar = namespace.dollars

        # The Greedy Change Making Algorithm
        for denomination, value in DENOMINATIONS.items():
            while namespace.cents >= value:
                namespace.change.__dict__[denomination] += 1
                namespace.cents -= value
    finally: 
        return namespace

def text_process(namespace):
    '''
    Removes any leading '$' from amount.
    '''
    try:
        # remove $ sign, if there is one
        index = namespace.amount.index('$')+1
        namespace.amount = namespace.amount[index:]
    except ValueError: # $ wasn't in the string
        pass
    finally:
        return namespace

def validate(namespace):
    '''
    The input validation function..

    rejects character strings, negative decimal values, decimals that have 
    nonzero digits in place values exceeding hundreths, and empty strings
    '''
    try:
        assert float(namespace.amount) >= 0 # digital and nonnegative
        partition = namespace.amount.split('.')
        decimal_part = partition[1]
        # nonzero digits in place-values exceeding the hundredths place
        assert int(decimal_part) == 0 or len(decimal_part) <= 2
    except (ValueError, TypeError, AssertionError):
        namespace.is_valid = False
        raise InvalidInputError
    except IndexError: # input was not floating-point
        namespace.dollars = int(namespace.amount)
    else: # input was of the form x.yz
        namespace.dollars, namespace.cents = int(partition[0]), int(decimal_part)
    return namespace

def display(namespace):

    if namespace.is_valid:

        length = len(str(namespace.change.dollar))
        fill = ' '*length
        namespace.amount = float(namespace.amount)
        print(''' 
 input :   ${namespace.amount:.2f}
 output:

    {namespace.change.dollar}  dollars
    {namespace.change.quarter}{fill} quarters
    {namespace.change.dime}{fill} dimes
    {namespace.change.nickel}{fill} nickels
    {namespace.change.penny}{fill} pennies
'''.format_map(vars()))
    
    else:
        print(''' 
 input :   {namespace.amount}
 output:   {namespace.change}'''.format_map(vars()))

def test():
    '''
    Test cases are developed and executed here.
     - test_1 : charater input > error
     - test_2 : negative real number input > error
     - test_3 : the empty string > error
     - test_4 : nonzero digits in place values exceeding hundredths > error
     - test_5 : the integer zero > a multiset that is the empty set
     - test_6 : a pseudorandom nonnegative real number less than or equal to one 
                million. > a populated multiset
    '''
    test_1 = random.choice(string.ascii_letters + string.punctuation)
    test_2 = -1 * (random.randint(0, 1000000) + round(random.random(), 2)) 
    test_3 = ''
    test_4 = random.randint(0, 1000000) + random.random()
    test_5 = 0
    test_6 = random.randint(0, 1000000) + round(random.random(), 2)

    # normalize test case data types
    cases = list(map(str, [test_1, test_2, test_3, test_4, test_5, test_6]))

    # add set membership information for each case
    sets = ['non-numeric character', 'negative real number', 'empty string',
            'nonzero digits in place-values exceeding hundredths', 
            'zero integer',
            'a correct input value']
    cases = list(zip(cases, sets))

    # process test cases
    for index, case in enumerate(cases):
        amount, set_membership = case[0], case[1]
        test_number = index +1
        # execute the algorithm
        namespace   = make_change(amount)
        print('\n[Test Case {test_number} ({set_membership})]:'.format_map(
                vars()))
        display(namespace)        

def main():
    try:
        amount = sys.argv[1]
    except IndexError:
        print('Must enter an amount.')
    else:
        if amount == 'test':
            test()
        else:
            namespace = make_change(amount)
            display(namespace)

if __name__ == '__main__':
    main()
