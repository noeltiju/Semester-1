def f1(data):
    data = data.lower()
    word = ""
    count_unique = 0
    count_total = 0
    for c in data:
        if c.isalpha():
            word+=c
        
        else:
            if word.isalpha():
                if word not in words:
                    words[word]=1
                    count_unique+=1

                else:
                    words[word]+=1
                count_total+=1
                word=""

    if word.isalpha() and word!= "":
        if word not in words:
            words[word]=1
            count_unique+=1

        else:
            words[word]+=1
        count_total+=1

    return count_unique / count_total

def f2(data):
    vals = list(words.values())
    vals.sort(reverse=True)
    top_vals = vals[0:5]
    count = 0
    for w in words:
        if words[w] in top_vals:
            count+=1

    return count/sum(list(words.values()))

def f3(data):
    data.replace("?","")
    sentences = data.split(".")
    count = 0
    for s in sentences:
        if len(s.split()) > 35 or len(s.split()) > 5:
            count+=1

    return count / len(sentences)

def f4(data):
    prev = ""
    count=0
    for i in range(1,len(data)):
        e = data[i]
        if e == "." and prev == "." and data[i-1] != ".":
            count+=1
        elif e == "," and prev == "," and data[i-1] != ",":
            count+=1
        
        elif e == ":" and prev == ":" and data[i-1] != ":":
            count+=1
        elif e == ";" and prev == ";" and data[i-1] != ";":
            count+=1
        
        prev = e
    return count/sum(list(words.values()))
            
def f5():
    if sum(list(words.values())) > 750:
        return 1
    return 0

def words5():
    vals = list(words.values())
    vals.sort(reverse = True)
    ans = []
    try:
        vals = vals[0:5]
        count = 0
        while count < 5:
            for w in words:
                if d[w] == vals[count]:
                    ans.append(w)
                    count+=1
        return ans

    except:
        return ans

        
        



if __name__ == "__main__":
   n = int(input())
   from random import randint
   for i in range(1,n+1):
    fname = f"File{i}.txt"
    words = {}
    with open(f"/Users/NOEL/Desktop/Python/IP/Assignment3/Files/{fname}") as myfile:
        d = myfile.read()
        f1_val = f1(d)
        f2_val = f2(d)
        f3_val = f3(d)
        f4_val = f4(d)
        f5_val = f5()

        f = open("/Users/NOEL/Desktop/Python/IP/Assignment3/Files/scores.txt","a")
        f.write(f"{fname}:\n")
        score = 4 + f1_val*6 + f2_val*6 - f3_val - f4_val - f5_val
        f.write(f"Score: {score}\n")
        f.write(f"Top 5 words: ")
        l = words5()
        for i in l:
            f.write(i+" ")
            f.write("\n")

        w = list(words.keys())
        f.write("5 random words: ")
        for i in range(5):
            r = randint(0,len(w)-1)
            f.write(f"{w[r]} ")

        f.write("\n")


        

        





    