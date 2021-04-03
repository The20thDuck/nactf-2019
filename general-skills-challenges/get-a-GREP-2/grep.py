import random
f = open("flag.txt", "w")
flag = "r3gul4r_3xpr3ss10ns_ar3_m0r3_th4n_r3gul4r_euaiooa"
chars = "abcdefghijklmnopqrstuvwxyz0123456789_"
chars = list(chars)
length = len(flag)
for i in range(100000):
    text = ""
    if i == 67369:
        f.write("nactf{" + flag + "}\n")
        continue
    for i in range(length):
        text += random.choice(chars)
    f.write("nactf{" + text + "}\n")
