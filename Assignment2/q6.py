dataset = [(10, 15), (20, 25), (100, 40), (40, 20)]

writing_file = open("IPgrade.txt","w")

with open("IPmarks.txt","r") as myfile:
    marks = myfile.readlines()
    for _ in marks:
        total = 0
        line = _.replace("\n","")
        val = line.split(", ")
        rollno = val[0]

        for i in range(1,len(val)):
            max_ = dataset[i-1][0] ; weight_ = dataset[i-1][1]
            mark = int(val[i])
            value = mark / max_

            final_val = value * weight_
            total += final_val

        print(total)
        if total > 80:
            grade = 'A'

        elif total > 70:
            grade = 'A-'
        
        elif total > 60:
            grade = 'B'

        elif total > 50:
            grade = 'B-'

        elif total > 40:
            grade = 'C'

        elif total > 35:
            grade = 'C-'

        elif total > 30:
            grade = 'D'

        else:
            grade = "F"

        writing_file.write(f"{rollno}, {total}, {grade}\n")

writing_file.close()