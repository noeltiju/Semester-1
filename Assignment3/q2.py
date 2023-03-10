#d = {name; {current={},entries[{},{}]}}

def make_dictionary(data):
    details = {}
    for entry in data:
        l = entry.split(", ")
        name = l[0]; status = l[1]; gate = l[2]; time = l[3]
        d = {'status':status, "gate":gate, "time":time}

        if name not in details:
            details[name] = {"current":d, "entries":[d]}

        else:
            k = details[name]
            current = k["current"]
            if current:
                if current["status"] == "EXIT" and status == "ENTER":
                    k["current"] = d
                    k["entries"].append(d)

                elif current["status"] == "EXIT" and status == "EXIT":
                    k["current"] = d
                    l = k["entries"]
                    l[-1] = d
                    k["entries"] = l


                elif current["status"] == "ENTER" and status == "ENTER":
                    pass
                    
                elif current["status"] == "ENTER" and status == "EXIT":
                    k["current"] = d
                    k["entries"].append(d)
            else:
                k["current"] = d
                k['entries'].append(d)

            details[name] = k
    return details

def query1(details,sname,time):
    for name in details:
        #Prints overall status of the user
        if name  == sname:
            val = details[name]
            if val["current"]=={}:
                print("Student has exited the college")

            else:
                print(f"Current status is {val['current']}")

            
        #Prints status at a time
            state = ""
            d = {}
            for entry in val["entries"]:
                if entry["time"] <= time:
                    state = entry["status"]
                    d = entry

            print(d)

def query2(details,start,end):
    ans = []
    for name in details:
        val = details[name]
        entries = val['entries']
        state = ""
        time = ""
        gate=""
        d={}
        for i in entries:
            if start<=i["time"]<=end:
                if i["status"]=="ENTRY" and state=="ENTRY":
                    pass
                elif i["status"]=="EXIT" and state=="EXIT":
                    gate = i["gate"]; time = i["time"]
                    d = i
                
                else:
                    state = i["status"];gate = i["gate"]; time = i["time"]
                    d = i
        if d!= {}:
            d["name"] = name
            ans.append(d)
    
    return ans

def query2_sort(ans):
    f = open("output_q2.txt","w")
    ans = sorted(ans, key=lambda x: x['time'])
    for i in ans:
        state  = i["status"]; name = i["name"]; time = i["time"]; gate = i["gate"]
        if state == "ENTER":             
            s = f"{name} has entered college at {time} using gate {gate}\n"

        else:
            s = f"{name} has exited college at {time} using gate {gate}\n"
        f.write(s)
    
def query3(details,gate):
    entry_count=0; exit_count=0
    for name in details:
        d = details[name]
        for entry in d["entries"]:
            g = int(entry["gate"])
            if gate == g and entry["status"] == 'ENTER':
                entry_count+=1
            elif gate == g and entry["status"] == 'EXIT':
                exit_count+=1
    return (entry_count,exit_count)

if __name__ == "__main__":
    myfile = open('sorted_data.txt',"r")
    data= myfile.read().splitlines()
    data = data[1:]

    details = make_dictionary(data)
    query1(details,"Sahil Goyal","00:40:05")
    ans = query2(details,"02:00:00","06:00:00")
    query2_sort(ans)
    print(query3(details, 3))