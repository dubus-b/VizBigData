id_file = []
i = 0
with open('StudentsPerformance.csv') as f:
    for line in f:
        id_file.append(str(i) +',' + line)
        i = i + 1
f.close()
with open('data.csv', 'w') as f:
    for item in id_file:
        f.write("%s" % item)
f.close()