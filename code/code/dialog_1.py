import json


# Opening JSON file
f1 = open('dialogues_001.json', "r")
 
# Loading JSON file
data = json.load(f1) 

with open("newdata1.json", "w") as n1:
    n1.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n1.write(i["dialogue_id"])
            n1.write("\t")
            n1.write(k["turn_id"])
            n1.write("\t")
            n1.write(k["utterance"])
            n1.write("\n")
            
f1.close()
n1.close()


#2
f2 = open('dialogues_002.json', "r")
data = json.load(f2)

with open("newdata2.json", "w") as n2:
    n2.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n2.write(i["dialogue_id"])
            n2.write("\t")
            n2.write(k["turn_id"])
            n2.write("\t")
            n2.write(k["utterance"])
            n2.write("\n")
            
f2.close()
n2.close()


#3
f3 = open('dialogues_003.json', "r")
data = json.load(f3)

with open("newdata3.json", "w") as n3:
    n3.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n3.write(i["dialogue_id"])
            n3.write("\t")
            n3.write(k["turn_id"])
            n3.write("\t")
            n3.write(k["utterance"])
            n3.write("\n")
            
f3.close()
n3.close()


#4
f4 = open('dialogues_004.json', "r")
data = json.load(f4)

with open("newdata4.json", "w") as n4:
    n4.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n4.write(i["dialogue_id"])
            n4.write("\t")
            n4.write(k["turn_id"])
            n4.write("\t")
            n4.write(k["utterance"])
            n4.write("\n")
            
f4.close()
n4.close()


#5
f5 = open('dialogues_005.json', "r")
data = json.load(f5)

with open("newdata5.json", "w") as n5:
    n5.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n5.write(i["dialogue_id"])
            n5.write("\t")
            n5.write(k["turn_id"])
            n5.write("\t")
            n5.write(k["utterance"])
            n5.write("\n")
            
f5.close()
n5.close()


#6
f6 = open('dialogues_006.json', "r")
data = json.load(f6)

with open("newdata6.json", "w") as n6:
    n6.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n6.write(i["dialogue_id"])
            n6.write("\t")
            n6.write(k["turn_id"])
            n6.write("\t")
            n6.write(k["utterance"])
            n6.write("\n")
            
f6.close()
n6.close()


#7
f7 = open('dialogues_007.json', "r")
data = json.load(f7)

with open("newdata7.json", "w") as n7:
    n7.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n7.write(i["dialogue_id"])
            n7.write("\t")
            n7.write(k["turn_id"])
            n7.write("\t")
            n7.write(k["utterance"])
            n7.write("\n")
            
f7.close()
n7.close()


#8
f8 = open('dialogues_008.json', "r")
data = json.load(f8)

with open("newdata8.json", "w") as n8:
    n8.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n8.write(i["dialogue_id"])
            n8.write("\t")
            n8.write(k["turn_id"])
            n8.write("\t")
            n8.write(k["utterance"])
            n8.write("\n")
            
f8.close()
n8.close()


#9
f9 = open('dialogues_009.json', "r")
data = json.load(f9)

with open("newdata9.json", "w") as n9:
    n9.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n9.write(i["dialogue_id"])
            n9.write("\t")
            n9.write(k["turn_id"])
            n9.write("\t")
            n9.write(k["utterance"])
            n9.write("\n")
            
f9.close()
n9.close()


#10
f10 = open('dialogues_010.json', "r")
data = json.load(f10)

with open("newdata10.json", "w") as n10:
    n10.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n10.write(i["dialogue_id"])
            n10.write("\t")
            n10.write(k["turn_id"])
            n10.write("\t")
            n10.write(k["utterance"])
            n10.write("\n")
            
f10.close()
n10.close()


#11
f11 = open('dialogues_011.json', "r")
data = json.load(f11)

with open("newdata11.json", "w") as n11:
    n11.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n11.write(i["dialogue_id"])
            n11.write("\t")
            n11.write(k["turn_id"])
            n11.write("\t")
            n11.write(k["utterance"])
            n11.write("\n")
            
f11.close()
n11.close()


#12
f12 = open('dialogues_012.json', "r")
data = json.load(f12)

with open("newdata12.json", "w") as n12:
    n12.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n12.write(i["dialogue_id"])
            n12.write("\t")
            n12.write(k["turn_id"])
            n12.write("\t")
            n12.write(k["utterance"])
            n12.write("\n")
            
f12.close()
n12.close()


#13
f13 = open('dialogues_013.json', "r")
data = json.load(f13)

with open("newdata13.json", "w") as n13:
    n13.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n13.write(i["dialogue_id"])
            n13.write("\t")
            n13.write(k["turn_id"])
            n13.write("\t")
            n13.write(k["utterance"])
            n13.write("\n")
            
f13.close()
n13.close()


#14
f14 = open('dialogues_014.json', "r")
data = json.load(f14)

with open("newdata14.json", "w") as n14:
    n14.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n14.write(i["dialogue_id"])
            n14.write("\t")
            n14.write(k["turn_id"])
            n14.write("\t")
            n14.write(k["utterance"])
            n14.write("\n")
            
f14.close()
n14.close()


#15
f15 = open('dialogues_015.json', "r")
data = json.load(f15)

with open("newdata15.json", "w") as n15:
    n15.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n15.write(i["dialogue_id"])
            n15.write("\t")
            n15.write(k["turn_id"])
            n15.write("\t")
            n15.write(k["utterance"])
            n15.write("\n")
            
f15.close()
n15.close()


#16
f16 = open('dialogues_016.json', "r")
data = json.load(f16)

with open("newdata16.json", "w") as n16:
    n16.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n16.write(i["dialogue_id"])
            n16.write("\t")
            n16.write(k["turn_id"])
            n16.write("\t")
            n16.write(k["utterance"])
            n16.write("\n")
            
f16.close()
n16.close()


#17
f17 = open('dialogues_017.json', "r")
data = json.load(f17)

with open("newdata17.json", "w") as n17:
    n17.write("Dialogue_id\tTurn_id\tUtterance\n")
    for i in data:  

        print(i['dialogue_id'])
        turns = i["turns"]
        for k in turns:       
            print(k["turn_id"])
            print(k["utterance"])
            n17.write(i["dialogue_id"])
            n17.write("\t")
            n17.write(k["turn_id"])
            n17.write("\t")
            n17.write(k["utterance"])
            n17.write("\n")
            
f17.close()
n17.close()


