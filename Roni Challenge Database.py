import csv
import matplotlib.pyplot as plt
import numpy as np

file_names = ['april_2024.csv', 'may_2024.csv', 'june_2024.csv', 'july_2024.csv', 'august_2024.csv', 'september_2024.csv', 'october_2024.csv']

month_orders = []
hours = []

alfredo_count = 0
cheddar_count = 0
pepperjack_count = 0 

nomeat_count = 0
chicken_count = 0
pork_count = 0
brisket_count = 0
bacon_count = 0
ham_count = 0

notoppings_count = 0
broccoli_count = 0
corn_count = 0
onion_count  = 0
jalapeno_count = 0
tomato_count = 0
pepper_count = 0
mushroom_count = 0
pineapple_count = 0
parmesan_count = 0
breadcrumbs_count = 0

nodrizzle_count = 0
bbq_count = 0
garlicparm_count = 0
buffalo_count = 0
pesto_count = 0
ranch_count = 0
hothoney_count = 0

#track frequency in hour
def hours_inMonth(index):
    order_time = sent_date[index].split()
    order_hour = order_time[1].split(":")[0]
    hours.append(order_hour)


for name in file_names:
    order_num = []
    sent_date = []
    modifiers = []
    option = []
    parent_menu = []
    orderID = []

    # opens each file and fills arrays with data
    with open(name, 'r') as file:
        reader = csv.reader(file)
        header = next(reader, None)

        for row in reader:
            if(row[5] == "0-0"):
                break
            
            order_num.append(row[0])
            sent_date.append(row[1])
            modifiers.append(row[2])
            option.append(row[3])
            parent_menu.append(row[4])
            orderID.append(row[5])


    # tracks monthly orders
    index_tracker = -1
    prev_num = 0
    current_month_orders = 0
    for num in order_num:
        index_tracker += 1
        curr_num = int(num)
        
        if(curr_num != prev_num):
            current_month_orders += 1
            hours_inMonth(index_tracker)
            prev_num = curr_num
        
    month_orders.append(current_month_orders)

    
    for modifier in modifiers:
        # tracks cheese frequencies
        if (modifier == "Alfredo"):
            alfredo_count += 1
        if (modifier == "Cheddar"):
            cheddar_count += 1
        if (modifier == "Pepper Jack"):
            pepperjack_count += 1

        # tracks meat frequencies
        if (modifier == "No Meat"):
            nomeat_count += 1
        if (modifier == "Grilled Chicken"):
            chicken_count += 1
        if (modifier == "Pulled Pork"):
            pork_count += 1
        if (modifier == "Brisket"):
            brisket_count += 1
        if (modifier == "Bacon"):
            bacon_count += 1
        if (modifier == "Ham"):
            ham_count += 1

        # tracks topping frequencies
        if (modifier == "No Toppings"):
            notoppings_count += 1
        if (modifier == "Broccoli"):
            broccoli_count += 1
        if (modifier == "Corn"):
            corn_count += 1
        if (modifier == "Onions"):
            onion_count += 1
        if (modifier == "Jalapenos"):
            jalapeno_count += 1
        if (modifier == "Tomatoes"):
            tomato_count += 1
        if (modifier == "Bell Peppers"):
            pepper_count += 1
        if (modifier == "Mushrooms"):
            mushroom_count += 1
        if (modifier == "Pineapple"):
            pineapple_count += 1
        if (modifier == "Parmesan"):
            parmesan_count += 1
        if (modifier == "Breadcrumbs"):
            breadcrumbs_count += 1

        #track drizzle frequencies
        if (modifier == "No Drizzle"):
            nodrizzle_count += 1
        if (modifier == "BBQ"):
            bbq_count += 1
        if (modifier == "Garlic Parmesan"):
            garlicparm_count += 1
        if (modifier == "Buffalo"):
            buffalo_count += 1
        if (modifier == "Pesto"):
            pesto_count += 1
        if (modifier == "Ranch"):
            ranch_count += 1
        if (modifier == "Hot Honey"):
            hothoney_count += 1


        



for i in range(0, len(hours)):
    hours[i] = int(hours[i])

print(hours)

unique, counts = np.unique(hours, return_counts = True)
plt.bar(unique, counts)
plt.show()

print(month_orders)

cheese_counts = [alfredo_count, cheddar_count, pepperjack_count]
print(cheese_counts)

meat_counts = [nomeat_count, chicken_count, pork_count, brisket_count, bacon_count, ham_count]
print(meat_counts)

toppings_counts = [notoppings_count, broccoli_count, corn_count, onion_count, jalapeno_count, tomato_count,
                  pepper_count, mushroom_count, pineapple_count, parmesan_count, breadcrumbs_count]
print(toppings_counts)

drizzle_counts = [nodrizzle_count, bbq_count, garlicparm_count, buffalo_count, pesto_count, ranch_count, hothoney_count]
print (drizzle_counts)
