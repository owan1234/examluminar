f=open("complete.csv","r")
Final={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[1]
    confirmed=data[4]
    Death=data[5]
    recovered=data[6]
    if(state not in Final):
        Final[state]={"state":state,"confirmed":confirmed,"death":Death,"recovered":recovered}
    else:
        Final[state]={"state": state, "confirmed": confirmed, "death": Death, "recovered": recovered}

def fetchdata(**kwargs):
    state=(kwargs["state"])
    if(state not in Final):
        print("There is no state")
        exit()
    if("parameter" in kwargs):
        value=kwargs["parameter"]
        print(Final[state][value])
    else:
        print(Final[state]["confirmed"])

fetchdata(state="Kerala",parameter="recovered")