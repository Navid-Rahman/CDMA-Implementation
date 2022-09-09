import numpy as np
from logo_CDMA import logo

print(logo)

def walsh_code(order):
    # Walsh Code Generator

    W = np.array([1])
    for i in range(order):
        W = np.tile(W, [2, 2])
        half = 2 ** i
        W[half:, half:] = np.negative(W[half:, half:])
    return W


print("Walsh code:\n", walsh_code(3))

# Transforming into lists
catch_on_list = walsh_code(3)
transfer_to_list = catch_on_list.tolist()

starting_range = 0
ending_range = len(transfer_to_list)

c1, c2, c3, c4, c5, c6, c7, c8 = [transfer_to_list[i] for i in (0, 1, 2, 3, 4, 5, 6, 7)]


# Get the data bits for the 8 stations
d1 = int(input("Enter D1 for Station 1:"))
d2 = int(input("Enter D2 for Station 2:"))
d3 = int(input("Enter D3 for Station 3:"))
d4 = int(input("Enter D4 for Station 4:"))
d5 = int(input("Enter D5 for Station 5:"))
d6 = int(input("Enter D6 for Station 6:"))
d7 = int(input("Enter D7 for Station 7:"))
d8 = int(input("Enter D8 for Station 8:"))

# Resultant for each Station
r1 = np.multiply(c1, d1)
r2 = np.multiply(c2, d2)
r3 = np.multiply(c3, d3)
r4 = np.multiply(c4, d4)
r5 = np.multiply(c5, d5)
r6 = np.multiply(c6, d6)
r7 = np.multiply(c7, d7)
r8 = np.multiply(c8, d8)

# Sum of total Resultant
resultant_channel = r1 + r2 + r3 + r4 + r5 + r6 + r7 + r8
print("Resultant Channel", resultant_channel)
Channel = int(input("Enter  the station to listen for C1=1 ,C2=2, C3=3, C4=4, C5=5, C6=6, C7=7, C8=8 : "))

if Channel == 1:
    rc = c1
elif Channel == 2:
    rc = c2
elif Channel == 3:
    rc = c3
elif Channel == 4:
    rc = c4
elif Channel == 5:
    rc = c5
elif Channel == 6:
    rc = c6
elif Channel == 7:
    rc = c7
elif Channel == 8:
    rc = c8
inner_product = np.multiply(resultant_channel, rc)

print("Inner Product", inner_product)
res1 = sum(inner_product)

data = res1 / len(inner_product)
print("Data bit that was sent", data)
