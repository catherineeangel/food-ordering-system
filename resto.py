from collections import Counter

#goal: creates a system that can take orders from customer(s) in a restaurant

#creates menu list
class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price 
    
    #returns the menu info
    def info(self):
        return self.name + " : $" + str(self.price)                 
    
    def get_name(self):
        return self.name 
    
    def get_price(self):
        return self.price 

#creates class Food
#inherits class Menu
class Food(Menu):
    def __init__(self, name, price):
        super().__init__(name, price)

    #mayb add some functions only for Food 

#creates class Drink
class Drink(Menu):
    def __init__(self, name, price):
        super().__init__(name, price)


#checks if customer's input is a number
def is_digit(check_input):
    if check_input.isdigit():
        return True
    return False

#checks if user input is a letter 
def is_string_only(check_input):
    if check_input.isalpha():
        return True
    return False

#check whether the names inputed are == num of peops eating
def is_name(check_input_names, number_of_people):
    if len(check_input_names) == int(number_of_people):
        return True
    return False 

#checks whether customer's input order is in the menu list
def is_in_menu(item_order, item_list):
    if item_order in range(len(item_list)+1):
        return True
    return False
    #print(len(item_list))
#creates a function that asks for customer(s)'s orders
def customer_order():
    #print greetings
    print("Hi, welcome to Home Cafe!")

    #asks user to input number of people eating
    number_of_people = input("How many people are eating? : ")
    #if input is not int, keeps asking user to input int 
    while not is_digit(number_of_people):
        print("Please input a number.")
        number_of_people = input("How many people are eating? : ")


    #asks for name
    names = [number_of_people for number_of_people in input("Enter your name(s): ").split(", ")]
    while not is_name(names, number_of_people):
        print("Please input ", number_of_people, "name(s")
        names = [number_of_people for number_of_people in input("Enter your name(s): ").split(", ")]

    print_menu()

    for name in names:
        print("---------------------------------------")
        print(name + ", please input your order number.")
        
        food_order = int(input("What do you want to eat?: "))

        while not is_in_menu(food_order, foods):
            print(name + ", please input the specified order number.")
            food_order = int(input("What do you want to eat?: "))
            
        if food_order > 0:
            food_name = foods[(food_order-1)]
            selected_food.append(food_name)
            selected_price.append(food_name.get_price())

        drink_order = int(input("What do you want to drink?: "))

        while not is_in_menu(drink_order, drinks):
            print(name + ", please input the specified order number.")
            drink_order = int(input("What do you want to drink?: "))

        if drink_order > 0:
            drink_name = drinks[(drink_order-1)]
            selected_drink.append(drink_name)
            selected_price.append(drink_name.get_price())

        #split_bill(names) 
        #creates a function that prints out the selected menu   
    print("\n---------------------------------------")

def print_orders():
    #basic idea : doesn't work if there are more than 1 items --> the output will be print twice/more
    #for x in range(len(selected_menu)):
    #    print(selected_menu[x].get_name()
    print("Here are your orders:")
    for item in selected_menu: #item represents either food/ drink
        #total price 
        #to avoid double listing
        c = Counter(item) #lists each [selected_menu with its number_of_orders] in an element
        #print(c)
        for n, v in c.items(): #c.items() access the elements within the element mentioned above
            name = n.get_name()
            print(v, name)
    count_total_price()    
      

def print_menu():
    print("\n---------------------------------------\n")
    #print the menu
    print("~FOOD~")
    #index here refers to menu number that starts from 1
    index = 1
    for food in foods:
        print(str(index) + "." + food.info())
        index += 1
    print() #creates a space

    index = 1
    print("~BEVARAGE~")
    for drink in drinks:
        print(str(index) + "." + drink.info())
        index += 1
    print() #creates a space

#counts total price
def count_total_price():
    print("---------------------------------------")
    print("Total price: $" +  str(sum(selected_price)))


#TEST
#split bill function
#def split_bill(names):
#    for name in names:
#        print(name + "'s order: ")
#        for x in range(len(selected_menu)):
#            print(food_name.get_name())


    
#TEST      
#--makes class customer where it inputs the customer and num of people
#class Customer:
#    def __init__(self, name, number):
#        self.name = name 
#        name = 
#        self.number = number
#
#    def greetings():
#        print("Hi, welcome to Home Cafe!")
#    def number_of_people():

#to simplify the food and drink lists,, create some function....
#creates food list 

foods =[
    Food("Carbonara", 8),
    Food("Fish Burger", 6),
    Food("Steak", 12),
    Food("Nasi Goreng", 5)
    ]


#creates drink list

drinks = [
    Drink("Ice Tea", 2),
    Drink("Coffee", 2),
    Drink("Orange Juice", 3),
    Drink("Soda", 1)
    ]

#creates a list for the selected food and drink,, then puts both in a list
selected_food = []
selected_drink = []
selected_menu = [selected_food, selected_drink]

#PRICE
selected_price = []

#creates main function
def main():
    #asks each indiviual for their choice of menu
    customer_order()
    #printing out the selected menus
    print_orders()

if __name__ == "__main__":
    main()


