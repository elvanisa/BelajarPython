print('=========PRINT========')
#display a line of text using the  print()  function
print('Hello, saya Elva!')
print('Hello, saya Elva!')

#print two lines of text by using the new line symbol
print('Ini baris pertama\nIni baris kedua')

print('=========VARIABLE========')
#declare variable
a = "test"
b = 20
c = 3.5

#print variable
print("we want to", a, "number", b, "and number", c)

#using format function
print('saya suka {0} dan {2}'.format('buah','sayur','permen'))

print('=========ARITMATIC========')
#aritmatic
a = 5
#addition
b = a + 2  
#subtraction
c = b - 3   
#multiplication
d = c * 2   
#division
e = d / 4  
#exponentiation
f = e ** 2  
#modulo (returns the remainder)
g = f % 2   

print('Nilai dari a, b, c, d, e, f, dan g \nadalah: {0}, {1}, {2}, {3}, {4}, {5}, dan {6}.'.format(a, b, c, d, e, f, g))

print('=========COMPARISON========')
#comparison
x = 5
print(x == 3) #cek apakah x samadengan 3
print(x != 7) 
print(x > 14) #cek apakah x lebih besar dari 14
print(x < 23)
print(x >= 9)
print(x <= 5)

print('=========LIST========')
#list
list_int = [1,2,2,3,4]
list_buah = ['anggur','pepaya','mangga']

print(list_int[4])
print(list_buah[2])