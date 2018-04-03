text = input("Unesite tekst: ")

xor = []
xor2 = []
for key in range(1,6):
    xor_text = ""
    for i in text:
        xor_text += (chr(ord(i)^key))
    xor.append(xor_text)

for key2 in range(6,10):
    for j in xor:
        xor_text2 = ""
        for k in j:
            xor_text2 += (chr(ord(k)^key2))
        xor2.append(xor_text2)

print(xor2)