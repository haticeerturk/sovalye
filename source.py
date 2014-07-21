sovalyeSayisi = input("Sovalye sayisini girin : ")
sovalyeler = []

j = 0
for i in range(sovalyeSayisi) :
	sovalyeler.append(i+1)

while len(sovalyeler) != 1 :
	while j + 1 <= len(sovalyeler) : 
		if len(sovalyeler) != 1 :
			sovalyeler.pop((j+1) % len(sovalyeler))
			j+=1
			print j, "---" ,sovalyeler
	j = 0
