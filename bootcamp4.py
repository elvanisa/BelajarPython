# bilangan  biner BITWISE

a = 9
b = 5

#bitwise OR (|)
c = a | b
print("nilai dari", a, "binary", format(a,'08b'))
print("nilai dari", b, "binary", format(b,'08b'))
print("nilai dari", c, "binary", format(c,'08b'))

#bitwise AND (&)
print("====AND====")
c = a & b
print("nilai dari", a, "binary", format(a,'08b'))
print("nilai dari", b, "binary", format(b,'08b'))
print("nilai dari", c, "binary", format(c,'08b'))

#bitwise XOR (^)
print("====XOR====")
c = a ^ b
print("nilai dari", a, "binary", format(a,'08b'))
print("nilai dari", b, "binary", format(b,'08b'))
print("nilai dari", c, "binary", format(c,'08b'))

#bitwise NOT (~)
print("====NOT====")
c = ~b
print("nilai dari", b, "binary", format(b,'08b'))
print("nilai dari", c, "binary", format(c,'08b'))

#bitwise shift right (>>)
print("====>>====")
c = a >> 2
print("nilai dari", a, "binary", format(a,'08b'))
print("nilai dari", c, "binary", format(c,'08b'))

#bitwise shift left (<<)
print("====<<====")
c = a << 2
print("nilai dari", a, "binary", format(a,'08b'))
print("nilai dari", c, "binary", format(c,'08b'))