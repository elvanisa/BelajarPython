#casting

#integer
print('=====INTEGER====')
int_data = 11
print(int_data)
print("tipe datanya adalah", type(int_data))

float_data = float(int_data)
string_data = str(int_data)
boolean_data = bool(int_data) #false kalau 0

print("ini data ", float_data, "tipenya adalah", type(float_data))
print("ini data ", string_data, "tipenya adalah", type(string_data))
print("ini data ", boolean_data, "tipenya adalah", type(boolean_data))

#float
print('=====FLOAT====')
float_data = 11.9
print(float_data)
print("tipe datanya adalah", type(float_data))

int_data = int(float_data)
string_data = str(float_data)
boolean_data = bool(float_data) #false kalau 0

print("ini data ", int_data, "tipenya adalah", type(int_data))
print("ini data ", string_data, "tipenya adalah", type(string_data))
print("ini data ", boolean_data, "tipenya adalah", type(boolean_data))

#string
print('=====STRING====')
string_data = "55"
print(string_data)
print("tipe datanya adalah", type(string_data))

int_data = int(string_data)
float_data = float(string_data)
boolean_data = bool(string_data) #false kalau 0

print("ini data ", int_data, "tipenya adalah", type(int_data))
print("ini data ", float_data, "tipenya adalah", type(float_data))
print("ini data ", boolean_data, "tipenya adalah", type(boolean_data))

#boolean
print('=====BOOLEAN====')
boolean_data = False
print(boolean_data)
print("tipe datanya adalah", type(boolean_data))

int_data = int(boolean_data)
float_data = float(boolean_data)
string_data = str(boolean_data)

print("ini data ", int_data, "tipenya adalah", type(int_data))
print("ini data ", float_data, "tipenya adalah", type(float_data))
print("ini data ", string_data, "tipenya adalah", type(string_data))


#input data by user
print('=====INPUT DATA====')
data = input("masukkan data: ")
print("data", data, "tipenya adalah", type(data))

int_data = int(input("masukkan angka: "))
print("data", int_data, "tipenya adalah", type(int_data))

float_data = float(input("masukkan angka desimal: "))
print("data", float_data, "tipenya adalah", type(float_data))

bool_data = bool(input("masukkan nilai boolean: "))
print("data", bool_data, "tipenya adalah", type(bool_data))

print('=====ARITMATIC====')

a = 10
b = 5

hasil = a - b
print('hasil dari', a, '-', b, 'adalah', hasil)