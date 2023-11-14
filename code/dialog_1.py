import json
import os

rootdir ='C:/Users/chen/Desktop/dialogue/'

with open("newdata.json", "w") as n1:

        n1.write("Dialogue_id\tTurn_id\tUtterance\tslot\n")

        for file in os.listdir(rootdir):

                # Opening JSON file
                f1 = open(os.path.join(rootdir, file), "r")

                # Loading JSON file
                data = json.load(f1)

                for i in data:

                        print(i['dialogue_id'])

                        turns = i["turns"]

                        for k in turns:

                                print(k["turn_id"])
                                print(k["utterance"])
                                n1.write(i["dialogue_id"])
                                slots=k["frames"]                                
                                Slot="NA"

                                for slot in slots:
                                        
                                        x=slot["slots"]
                                        #print(x)
                                        if len(x) != 0:
                                                for x1 in x:
                                                    print(x1["slot"])
                                                    Slot = x1["slot"]

                                n1.write("\t")
                                n1.write(k["turn_id"])
                                n1.write("\t")
                                n1.write(k["utterance"])                                
                                n1.write("\t")
                                n1.write(Slot)
                                n1.write("\n")
                                
                f1.close()
                
n1.close()
