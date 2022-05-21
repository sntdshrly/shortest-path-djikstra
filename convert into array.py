# buat input matrix biar ga manual (unfinished)

def stringToList(string):
    listRes = list(string.split("\t"))
    return listRes

strA = "0	3	0	7	0	8	9	15	0	0	0	0	3	0	0	0	0	0	0	0	0	0"

listBaru = (stringToList(strA))

listKosong = []
listKosong.append(listBaru)

listKosong = [list(map(int, lst)) for lst in listKosong]

print(listKosong)