"""
 This program calculates the total amount of a meal purchased at a restaurant. 
 The program asks the user to enter the charge for the food.
 Then calculate the amounts with an 18 percent tip and 7 percent sales tax. 
 Then displays each of these amounts and the total price.
"""

# The percentage of a bill that should be added for tip
TIP_PERCENT = .18 

# The percentage of a bill that should be added for sales tax
SALES_TAX_PERCENT = .07


def main():
    food_cost = float(input("How much did the food cost?: "))
    tip_amount = food_cost * TIP_PERCENT
    sales_tax = food_cost * SALES_TAX_PERCENT

    total = food_cost + tip_amount + sales_tax

    print("Meal cost\t: ${:>12.2f}".format(food_cost))
    print("Tip ({}%)\t: ${:>12.2f}".format(int(TIP_PERCENT*100),tip_amount))
    print("Sales tax ({}%)\t: ${:>12.2f}".format(int(SALES_TAX_PERCENT*100),sales_tax))
    print("Total Cost\t: ${:>12.2f}".format(total))

    


if __name__ == "__main__":
    main()