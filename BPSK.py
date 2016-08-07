import math
from PRNG import prng
from PRNG import gaussian_prng

max_len = 10000
my_prng = prng(120, 38, 74)

"""
Question 2a: Using uniform random number to produce random bits
- Anything above 0.5 is considered a 1
- Anything below 0.5 is considered a 0
"""
data = []
for i in range(max_len):
    if my_prng.random() >= 0.5:
        data.append(1)
    else:
        data.append(0)

print data

"""
Question 2b: Modulate the data using BPSK
"""
BPSK_data = []
for i in data:
    if i is 1:
        BPSK_data.append(1)
    else:
        BPSK_data.append(-1)

print BPSK_data

"""
QPSK_symbols = {"00": complex(0, 0), "01": complex(0, 1), "10": complex(-1, 0), "11": complex(0, -1)}
QPSK_data = []
for i in range(0, len(data), 2):
    tmp = "{0}{1}".format(data[i], data[i + 1])
    QPSK_data.append(QPSK_symbols[tmp])
print QPSK_data
"""

"""
Question 2c: Add noise to the symbols.
"""
SNR = 1
BPSK_sigma = 1/math.sqrt(math.pow(10, SNR * 1/10) * 2 * 1)
my_gaus = gaussian_prng(0, BPSK_sigma)
transmitted_data = []
for i in BPSK_data:
    transmitted_data.append(i + my_gaus.random())

print transmitted_data
print BPSK_sigma

"""
Convert symbols back to bits
"""
received_data = []
for r in transmitted_data:
    prob_1 = math.exp(-1*(abs(r - 1)**2)/(2 * BPSK_sigma ** 2))
    prob_2 = math.exp(-1*(abs(r - (-1))**2)/(2 * BPSK_sigma ** 2))

    alpha = 1/(prob_1 + prob_2)
    prob_1 *= alpha
    prob_2 *= alpha

    if prob_1 >= prob_2:            # If they are equal, always choose the second one.
        received_data.append(1)
    else:
        received_data.append(-1)

print received_data

"""
Compare transmitted bits to received bits and count the bit errors.
"""
index = 0
num_errors = 0
for symbol in received_data:
    if received_data[index] is not BPSK_data[index]:
        num_errors += 1
    index += 1
print num_errors
print num_errors * 1.0/max_len * 1.0
