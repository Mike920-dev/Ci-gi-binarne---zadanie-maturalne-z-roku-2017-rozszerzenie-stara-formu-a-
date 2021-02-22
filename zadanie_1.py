def czy_dwucykliczny(napis):
    dlugosc = int(len(napis) / 2)

    czesc_1 = napis[0:dlugosc]
    czesc_2 = napis[dlugosc:]

    if czesc_1 == czesc_2:
        return True
    return False

with open("binarne.txt", "r", encoding="UTF-8") as file:
    napisy_binarne = []

    for line in file:
        napisy_binarne.append(line.strip())

# print(napisy_binarne)

ile_dwucykliczne = 0

for napis in napisy_binarne:
    if czy_dwucykliczny(napis):
        ile_dwucykliczne += 1

print(ile_dwucykliczne)


