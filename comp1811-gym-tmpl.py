#########################################################
# COMP1811 CW1:
#  1st member : Your name               Your ID 
#  2nd member : Your partner's name     Your partner's ID
#  
#  LAB        : Mon 12:00-14:00 KW015   (Replace your lab)
##########################################################

from dataclasses import dataclass
from csv import reader

# We have to deal with
# basic data-types, loops, procedures,
# I/O , structs (@dataclass), assertions.
#
#


#1
# topic: structs defining data types
class Athlete:
    def __init__(self,name,weight,number_of_sessions_attended,training_plan):
        self.name=name
        self.weight=weight
        self.number_of_sessions_attended=number_of_sessions_attended
        self.training_plan=training_plan
    

#2
# topic: dictionaries Collection Data Types.
fees = {
"beginner":25,
"intermediate":30,
"elite":35,

        
}


#3
# I/O(tuple(Atheltes))
# Pre: Existent path
# topic: I/O , str prefeniend functions.
def io_ld_athletes(path: str):
    athletes = []
    
    with open(path) as f:
        csv_reader = reader(f)
        for athlete_data in csv_reader:
            new_athlete = Athlete(name=athlete_data[0], weight=athlete_data[1], number_of_sessions_attended=int(athlete_data[2]), training_plan=athlete_data[3])
            athletes.append(new_athlete)
        
        
    return tuple(athletes)

#4
# Topic: while (maximum algorithm)
# Pre  : Non empty tuple
# Post : Maximum athlete
def heaviest_athlete(aa):
    max_athlete=aa[0]
    for athlete in aa:
        if athlete.weight > max_athlete.weight:
            max_athlete=athlete
            
    return max_athlete       



#5
# topics : loops,I/O,
# computation(expressions), formatted strings.

def io_audit(aa: tuple):
    row_header=f"{'Name':^15}|{'Weight':^10}|{'Session':^10}|{'training':^15}|{'fee':^10}|{'Amount due':^15}"
    
    print(row_header)
    
    total=0
    
    for athlete in aa:
        name=athlete.name
        weight=athlete.weight
        sessions=int(athlete.number_of_sessions_attended)
        training=athlete.training_plan
        
        fee= fees[training]
        
        amount_due= sessions * fee
        total += amount_due
        
        print(f"{name:^15}|{weight:^10}|{sessions:^10}|{training:^15}|{fee:^10}|{amount_due:^15}")
    
   
    print(f"Total audit: {total}")
    
    

#6
# Topic: while (linear search algorithm)
# Post : Maybe(Athlete)
def find_athlete(aa: tuple, name):
    for athlete in aa:
        if athlete.name == name:
            return athlete
        
    return None


#7
# for and filter
# Topic for and complex expresion
def fltr_athletes(aa: tuple, trn_plan: str, sessions : int):
    matched_athlete = []
    for athlete in aa:
        if athlete.training_plan == trn_plan and athlete.number_of_sessions_attended >= sessions:
            matched_athlete.append(athlete)
    return matched_athlete


#8
# Topic: dictionaries.
def athletes_by_trn_pln(aa: tuple) -> dict :
    counts = {}
    for athlete in aa:
        counts[athlete.training_plan] = counts.get(athlete.training_plan, 0) + 1
    return counts

#9
# topic : formatted strings, saving text files, lists?, 
#         typing conversions
def io_dump_into_txt( path :str, aa: tuple, no_sessions):
    
    res = []
    with open(path, 'w') as fd:
        for athlete in aa:
            if athlete.number_of_sessions_attended > no_sessions:
                res.append(athlete)
                fd.write(f"Name: {athlete.name} Weight: {athlete.weight} Sessions: {athlete.number_of_sessions_attended} \n")
        
    return len(res),len(aa)
            
    


#10 
# IO : paint an stack
def io_draw_stack(N):
    pass # TODO
    return

aa = io_ld_athletes("athletes_100.csv")

io_audit(aa)

print("Heaviest athlete:", heaviest_athlete(aa).name)

test= fltr_athletes(aa, "elite", 99)
print(test)

test_9=io_dump_into_txt('/Users/jams/Downloads/jaziya.txt', aa, 10)

