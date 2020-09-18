f=open("complete.csv","r")
Final={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[1].lower()
    confirmed=data[4]
    Death=data[5]
    recovered=data[6]
    if(state not in Final):
        Final[state]={"state":state,"confirmed":confirmed,"death":Death,"recovered":recovered}
    else:
        Final[state]={"state": state, "confirmed": confirmed, "death": Death, "recovered": recovered}

def fetchdata(**kwargs):
    state=(kwargs["state"])
    if("parameter" in kwargs):
        value=kwargs["parameter"]
        print(Final[state][value])
    else:
        print(Final[state]["confirmed"])
a=input("Choose 1 if only state otherwise 2")
if(a=="1"):
    state1=input("state name")
    if state1 not in Final:
        print("There is no state with this name")
    else:
        fetchdata(state=state1)
elif(a=="2"):
    state1 = input("state name")
    if state1 not in Final:
        print("There is no state with this name")
    else:
         parameter1= input("Enter parameter")
         fetchdata(state=state1,parameter=parameter1)
else:
     print("invalid Number")
