cantidad = int(input())
i = 0
cont1 = 0
cont2 = 0
cont3 = 0
cont4 = 0
sumaAcidez = 0
sumaMateria = 0
a = 4  # "sumamente apto"
b = 3  # "moderadamente apto"
c = 2  # "marginalmente apto"
d = 1  # "no apto"
while i < cantidad:
    acidez = float(input())
    materiaOrganica = float(input())
    sumaAcidez += acidez
    sumaMateria += materiaOrganica

    # categoria acidez
    if 5.5 < acidez <= 6.5:
        catAcidez = a
    elif (6.5 < acidez <= 7.0) or (5.0 < acidez <= 5.5):
        catAcidez = b
    elif (7.0 < acidez <= 8.0) or (4.5 <= acidez <= 5.0):
        catAcidez = c
    elif acidez > 8.0 or acidez < 4.5:
        catAcidez = d

    # categoria materia organica
    if materiaOrganica < 3:
        catMateria = d
    elif materiaOrganica <= 4:
        catMateria = c
    elif materiaOrganica <= 5:
        catMateria = b
    elif materiaOrganica > 5:
        catMateria = a

    # si son iguales
    if catMateria == catAcidez:
        categoriaDefinitiva = catAcidez
    else:
        # si son diferentes
        if catAcidez < catMateria:
            categoriaDefinitiva = catAcidez
        else:
            categoriaDefinitiva = catMateria

    # conteo por categorias
    if categoriaDefinitiva == 4:
        cont1 += 1
    elif categoriaDefinitiva == 3:
        cont2 += 1
    elif categoriaDefinitiva == 2:
        cont3 += 1
    elif categoriaDefinitiva == 1:
        cont4 += 1

    # incremento
    i += 1

print("{:.2f}".format(sumaAcidez / cantidad, 2))
print("{:.2f}".format(sumaMateria / cantidad, 2))
print(f"sumamente apto {cont1}")
print(f"moderadamente apto {cont2}")
print(f"marginalmente apto {cont3}")
print(f"no apto {cont4}")
