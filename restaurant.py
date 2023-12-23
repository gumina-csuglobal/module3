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