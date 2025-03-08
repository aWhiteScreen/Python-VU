import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

print("1.   Padalinkite intervalą nuo -1.3 iki 2.5 tolygiai į 64 dalis.")
array_one = np.linspace(-1.3, 2.5, 64)
for x in range(len(array_one)):
    print(f"{x+1} {array_one[x]}")

print("2. 	Sukonstruokite pasikartojantį masyvą pagal duotą N. \n "
"Duotas masyvas [1, 2, 3, 4] ir N = 3 \n "
"Rezultatas [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4] \n "
"Masyvas gali būti bet kokio dydžio ir atsitiktinai sugeneruojamas.")
array_two = np.random.rand(4)
N = 3
result_array = np.tile(array_two, N)
print(result_array)

print("3. 	Sukurkite masyvą iš pasikartojančių elementų.\n"
"Duotas sąrašas [3, 4] ir pasikartojimų skaičius 4.\n"
"Rezultatas [3, 3, 3, 3, 4, 4, 4, 4]")
array_three = [3, 4]
N = 4
repeated_elements = np.repeat(array_three, N)

print('4. 	Sukurkite masyvą dydžio 10 x 10 iš nulių "įrėmintų" vienetais. \
      Užuomina - pad.')
one_zero_array = np.pad(np.zeros((8,8), dtype=int), pad_width=1, mode='constant', constant_values=1)
print(one_zero_array)

print("5. 	Sukurkite masyvą dydžio 8 x 8, kur 1 ir 0 išdėlioti šachmatine tvarka.")
chessboard = np.zeros((8,8), dtype=int)
chessboard[1::2, ::2] = 1
chessboard[::2, 1::2] = 1
print(chessboard)

print("6. 	Sukurkite masyvą dydžio n×n , kurio (i,j)-oji pozicija lygi i+j.")
n = 4
ij_array = np.fromfunction(lambda i, j: i+j, (n, n), dtype=int)
print(ij_array)

print("7. 	Sukurkite atsitiktinį masyvą dydžio 5×5 naudodami np.random.rand(5, 5). Surūšiuokite eilutes pagal antrąjį stulpelį. \n"
"Užuominos - slicing, argsort, indexing.")
random_ordered_array = np.random.rand(5, 5)
random_ordered_array = random_ordered_array[random_ordered_array[:, 1].argsort()]
print(random_ordered_array)

print("8.   Apskaičiuokite matricos tikrines reikšmes ir tikrinį vektorių.")
matrix = np.random.rand(2,2)
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print(f"Values {eigenvalues}")
print(f"Vectors {eigenvectors}")

print("9.   Apskaičiuokite funkcijos 0.5*x**2 + 5 * x + 4 išvestines su numpy ir sympy paketais.\n"
"Užuominos - poly1d, deriv, diff")
numpy_derivative = np.poly1d([0.5, 5, 4]).deriv()
print(f"Numpy derivative: {numpy_derivative}")
x = sp.Symbol("x")
simpy_derivative = (0.5*x**2+5*x+4).diff(x)
print(f"Simpy derivative: {simpy_derivative}")

print("10. 	Apskaičiuokite funkcijos e-x apibrėžtinį, intervale [0,1], ir neapibrėžtinį integralus.")
definite_integral = sp.integrate(sp.E - x, (x,0,1))
indefinite_integral = sp.integrate(sp.E - x, x)
print(f"Definite integral: {definite_integral}")
print(f"Indefinite integral: {indefinite_integral}")

print("11. 	Pasinaudodami polinėmis koordinatėmis nupieškite kardioidę.")
theta = np.linspace(0, 2*np.pi, 1000)
r = 5 - 5 * np.sin(theta)
plt.polar(theta, r, 'r')
plt.title("Cardioid")
plt.show()

print("12. 	Sugeneruokite masyvą iš 1000 atsitiktinių skaičių, pasiskirsčiusių pagal normalųjį dėsnį su duotais vidurkiu V ir dispersija D. \n"
"Nupieškite jų histogramą")
V, D = 0, 1 
random_numbers = np.random.normal(V, np.sqrt(D), 1000)
plt.figure()
plt.hist(random_numbers, bins=30, density=True, alpha=0.6, color='g')
plt.title("Histogram")
plt.show()

