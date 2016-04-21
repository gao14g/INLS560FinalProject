# Open Amarr.tsv file
with open("Amarr.tsv") as file:
    file_lines = file.readlines()

# Read through file and split based on tabs
amarr_table = []
for line in file_lines:
    amarr_table.append(line.split("\t"))


# Create a dictionary of dictionaries for each item with their statistics    
for row in amarr_table:
    del row[17:len(amarr_table)+1]    
amarr_dict = {}
for row in amarr_table[1:]:
    word = row[1]
    word = word.lower()
    if word not in amarr_dict:
        amarr_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}
    else:
        amarr_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}

# Open Jita.tsv file
with open("Jita.tsv") as file:
    file_lines = file.readlines()

# Read through file and split based on tabs
jita_table = []
for line in file_lines:
    jita_table.append(line.split("\t"))
 
# Create a dictionary of dictionaries for each item with their statistics  
for row in jita_table:
    del row[17:len(jita_table)+1]    
jita_dict = {}
for row in jita_table[1:]:
    word = row[1]
    word = word.lower()
    if word not in jita_dict:
        jita_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}
    else:
        jita_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}

# Open Dodixie.tsv file
with open("Dodixie.tsv") as file:
    file_lines = file.readlines()

# Read through the file and split based on tabs
dodixie_table = []
for line in file_lines:
    dodixie_table.append(line.split("\t"))
 
# Create a dictionary of dictionaries for each item with their statistics  
for row in dodixie_table:
    del row[17:len(dodixie_table)+1]    
dodixie_dict = {}
for row in dodixie_table[1:]:
    word = row[1]
    word = word.lower()
    if word not in dodixie_dict:
        dodixie_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}
    else:
        dodixie_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}

# Open Rens.tsv file
with open("Rens.tsv") as file:
    file_lines = file.readlines()

# Read through the file and split based on tabs
rens_table = []
for line in file_lines:
    rens_table.append(line.split("\t"))

# Create a dictionary of dictionaries for each item with their statistics  
for row in rens_table:
    del row[17:len(rens_table)+1]    
rens_dict = {}
for row in rens_table[1:]:
    word = row[1]
    word = word.lower()
    if word not in rens_dict:
        rens_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}
    else:
        rens_dict[word] = {"ID":row[2],"Buy Vol":row[3],"Buy Avg":row[4],"Buy Max":row[5],"Buy Min":row[6],"Buy StdDev":row[7],"Buy Median":row[8],"Buy Percentile":row[9],"Sell Vol":row[10],"Sell Avg":row[11],"Sell Max":row[12],"Sell Min":row[13],"Sell StdDev":row[14],"Sell Median":row[15],"Sell Percentile":row[16]}

# Create options for choosing a certain station
trade_stations = """Option 1 - Amarr
Option 2 - Dodixie
Option 3 - Jita
Option 4 - Rens """
  
# Create options for choosing to see certain types of statistics 
station_options = """Option 1 - Search for All Statistics for Specific Items
Option 2 - Search for Specific Statistics for Specific Items
Option 3 - Search for Buy Order Statistics for Specific Items
Option 4 - Search for Sell Order Statistics for Specific Items"""

# define function to show all statistics for a certain item
def all_stats(trade_station):
    going = True
    while going:
        answer = input("Please input an item name: ")
        answer = answer.lower()
        try:
            print_list(trade_station,answer)
            answer = input("If you want to search for another item, type '1'. If you want to go back to the menu, type '2': ")
            if answer == "1":
                going = True
            elif answer == "2":
                going = False
        except:
            print("Error: Item name not found. Please try again.")

def option2():
    print("You have chosen to see statistics for specific trade stations")
    print (trade_stations)
    station = input("Choose which station you would like to use: ")
    if station == "1":
        print("You have chosen Amarr.")
        print(station_options)
        choice = input("Choose one of the options above: ")
        if choice == "1":
            all_stats(amarr_dict)
    if station == "2":
        print("You have chosen Dodixie.")
        print(station_options)
        choice = input("Choose one of the options above: ")
        if choice == "1":
            all_stats(dodixie_dict)
    if station == "3":
        print("You have chosen Jita")
        print(station_options)
        choice = input("Choose one of the options above: ")
        if choice == "1":
            all_stats(jita_dict)
    if station == "4":
        print("You have chosen Rens.")
        print(station_options)
        choice = input("Choose one of the options above: ")
        if choice == "1":
            all_stats(rens_dict)


def print_list(dictionary,answer):
    id = dictionary[answer]["ID"]
    buy_vol = dictionary[answer]["Buy Vol"]
    buy_avg = dictionary[answer]["Buy Avg"]
    buy_max = dictionary[answer]["Buy Max"]
    buy_min = dictionary[answer]["Buy Min"]
    buy_sdv = dictionary[answer]["Buy StdDev"]
    buy_med = dictionary[answer]["Buy Median"]
    buy_perc = dictionary[answer]["Buy Percentile"]
    sell_vol = dictionary[answer]["Sell Vol"]
    sell_avg = dictionary[answer]["Sell Avg"]
    sell_max = dictionary[answer]["Sell Max"]
    sell_min = dictionary[answer]["Sell Min"]
    sell_sdv = dictionary[answer]["Sell StdDev"]
    sell_med = dictionary[answer]["Sell Median"]
    sell_perc = dictionary[answer]["Sell Percentile"]
    print ("ID:", id)
    print ("Buy Volume:", buy_vol)
    print ("Buy Average:", buy_avg)
    print ("Buy Max:", buy_max)
    print ("Buy Min:", buy_min)
    print ("Buy Standard Deviation:", buy_sdv)
    print ("Buy Percentile:", buy_perc)
    print ("Sell Volume:", sell_vol)
    print ("Sell Average:", sell_avg)
    print ("Sell Max:", sell_max)
    print ("Sell Min:", sell_min)
    print ("Sell Standard Deviation:", sell_sdv)
    print ("Sell Percentile:", sell_perc)



def option3():
    status = True
    while status:
        answer = input("Please input an item name: ")
        answer = answer.lower()
        try:
            amarr_dict[answer]
            print("Amarr:")
            print_list(amarr_dict,answer)
            print()
            print("Jita:")
            print_list(jita_dict,answer)
            print("Dodixie:")
            print_list(dodixie_dict,answer)
            print()
            print("Rens:")
            print_list(rens_dict,answer)
            print()
            answer = input("If you want to search for another item, type '1'. If you want to go back to the menu, type '2': ")
            if answer == "1":
                status = True
            elif answer == "2":
                status = False
        except:
            print("Error: Item name not found. Please try again.")

def spec_stats(trade_station):
    status = True
    while status:  
        item = input("Please input an item name: ")
        item = item.lower()
        try:
            trade_station[item]
            answer = input("Please input the statistics you want to see separated by commas with no spaces: ")
            answer_list = answer.split(",")
            for stat in answer_list:
                print(stat,":",trade_station[item][stat])
            answer = input("If you want to search for another item, type '1'. If you want to go back to the menu, type '2': ")
            if answer == "1":
                status = True
            elif answer == "2":
                status = False
        except:
            print("Error: Item doesn't exist. Please try again.")

def all_spec_stats():
    status = True
    while status:  
        item = input("Please input an item name: ")
        item = item.lower()
        try:
            amarr_dict[item]
            answer = input("Please input the statistics you want to see separated by commas with no spaces: ")
            answer_list = answer.split(",")
            print("Amarr:")
            for stat in answer_list:
                print(stat,":",amarr_dict[item][stat])
            print()
            print("Dodixie:")
            for stat in answer_list:
                print(stat,":",dodixie_dict[item][stat])
            print()
            print("Jita")
            for stat in answer_list:
                print(stat,":",jita_dict[item][stat])
            print()
            print("Rens:")
            for stat in answer_list:
                print(stat,":",rens_dict[item][stat])
            print()
            answer = input("If you want to search for another item, type '1'. If you want to go back to the menu, type '2': ")
            if answer == "1":
                status = True
            elif answer == "2":
                status = False
        except:
            print("Error: Item doesn't exist. Please try again.")
    
def option4():
    status = True
    while status:
        station = input("Type '1' if you want to see items from a specific station, type '2' if you want to see items from all stations, or type '3' to go back to the main menu: ")
        if station == "1":
            print (trade_stations)
            station_name = input("Choose the station you want to see: ")
            if station_name == "1":
                spec_stats(amarr_dict)
            if station_name == "2":
                spec_stats(dodixie_dict)
            if station_name == "3":
                spec_stats(jita_dict)
            if station_name == "4":
                spec_stats(rens_dict)
        if station == "2":
            all_spec_stats()
        if station == "3":
            status = False
        
                
            # item = input("Please input an item name: ")
            # item = item.lower()
            # answer = input("Please input the statistics you want to see separated by commas with no spaces: ")
            # answer_list = answer.split(",")
            # print (answer_list)
            # for stat in answer_list:
            #     print(amarr_dict[item][stat])
        if station == "2":
            item = input("Please input an item name: ")
            item = item.lower()
            answer = input("Please input the statistics you want to see separated by commas with no spaces: ")
            answer_list = answer.split(",")
            print (answer_list)
            for stat in answer_list:
                print(amarr_dict[item][stat])

def help_message():
    message = """Here are some extra tips and information:
    The data is broken down into these main columns:
    - ID
    - Buy Vol
    - Buy Avg
    - Buy Max
    - Buy Min
    - Buy StdDev
    - Buy Median
    - Buy Percentile
    - Sell Vol
    - Sell Avg
    - Sell Max
    - Sell Min
    - Sell StdDev
    - Sell Median
    - Sell Percentile
    The 'Buy' statstics refer to buy orders and the 'Sell' statstics refer to sell orders.
    Some examples of items in this list include:
    - Isogen, Griffin, Tristan, Kestrel, Utu, Vangel, Small Arms, Lucent Compound"""
    print (message)
    print("Press 'enter' to go back to the menu.")
    input()
    