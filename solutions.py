"""
Practice problems to get the hang of converting among data types.
In this case, we focus on converting numeric data types to strings and vice-versa.
"""


def calculate_profit():
    """
    Imagine this scenario: a company has determined that its annual profit is typically 23 percent of total sales.
    Complete this function so that it asks the user to enter in the projected amount of total sales and then displays the profit that will be made from that amount.
    You can assume the user will enter only numeric characters, e.g. "3000", not "$3,000.00"
    The output should match the format of the following examples: "Profit: $690.00" for sales of $3,000, or "Profit: $2,300.00" for sales of $10,000, etc.
    """
    projected_amount_of_sales = input("What is the Projected Amount of Total Sales?")
    projected_sales_int = int(projected_amount_of_sales)
    profit_unformatted=int(0.23 * projected_sales_int)
    profit = f"{profit_unformatted:,.2f}"
    print("profit: $" + profit)

def calculate_quotient_and_remainder():
    """
    Complete this function so that it asks the user to input two integers.
    You program should calculate and output the quotient and remainder when the first number is divided by the second.
    Here's an example run of the function:
      Enter number #1: 5
      Enter number #2: 2
      2 goes into 5 a total of 2 times with a remainder of 1
    """
    number_one = input("Enter number #1: ")
    number_two = input("Enter number #2: ")
    x = int(number_one)
    y = int(number_two)
    print(number_two + " goes into " + number_one + " a total of " + str(x // y) + " times with a remainder of " + str(x % y))

def calculate_miles_per_gallon():
    """
    A car's Miles Per Gallon (MPG) can be calculated using the following formula:
      MPG = Miles driven / Gallons of Gas Used
    Complete this function so that it asks the user for the number of miles driven and the gallons of gas used.
    It should calculate the car's MPG and display the result in the format indicated in this example run of the program:

      Miles driven: 100
      Gas used (gallons): 25
      Miles per gallon: 2.2
    """
    miles_driven = input("How many miles did you drive?")
    gallons_gas = input("How many gallons of gas did you use?")
    m = int(miles_driven)
    g = int(gallons_gas)
    miles_per_gallon = m / g
    print("Miles driven: " + str(m) + "\nGas used (gallons): " + str(g) + "\nMiles per gallon: " + str(miles_per_gallon))


def align_text():
    """
    Complete this function such that it asks the user to enter in 3 price values (as floating point numbers).
    The print out the price values so that they are formatted to two decimal places. Also make sure that the price values are right aligned and line up at the decimal point.
    Here's a sample running of the program:

      Enter price #1: 1.55
      Enter price #2: 10
      Enter price #3: 9532.6

      Here are your prices!

      Price #1: $    1.55
      Price #2: $   10.00
      Price #3: $ 9532.60
    """
    price_number_one = input("Enter price #1: ")
    price_number_two = input("Enter price #2: ")
    price_number_three = input("Enter price #3: ")
    price_one_float = float(price_number_one)
    price_two_float = float(price_number_two)
    price_three_float = float(price_number_three)

    import locale
    locale.setlocale(locale.LC_ALL, '')
    price_one = format(price_one_float, '0.2f')
    price_two = format(price_two_float, '0.2f')
    price_three = format(price_three_float, '0.2f')
    print("\nHere are your prices!\n")
    print(
        f"{'Price #1: $'}{price_one:>8}",
        f"{'Price #2: $'}{price_two:>8}",
        f"{'Price #3: $'}{price_three:>8}",
        sep="\n"
    )