#condition
#short if

a = 3
b = 7

print("A ya") if a > b else print("B aja")

print('=========TIPE DATA========')
#tipe data
#int, string, float, boolean, complex, ctypes

#tipe data int: angka satuan
int_data = 10
print("data: ", int_data)
print("data ini bertipe: ", type(int_data))

#tipe data string: kumpulan karakter
string_data = "binar"
print("data: ", string_data)
print("data ini bertipe: ", type(string_data))

#tipe data float: angka dengan koma
float_data = 11.2
print("data: ", float_data)
print("data ini bertipe: ", type(float_data))

#tipe data boolean: bilangan biner true/false
bool_data = False
print("data: ", bool_data)
print("data ini bertipe: ", type(bool_data))

## tipe data khusus
# bilangan complex
complex_data = complex(2,3)
print("data: ", complex_data)
print("data ini bertipe: ", type(complex_data))

# di python banyak tipe bahasa yg tidak dipakai
# tipe data dari bahasa C

from ctypes import c_double, c_char, c_long

c_double = c_double(22.2)
print("data: ", c_double)
print("data ini bertipe: ", type(c_double))
