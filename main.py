import random
nameVendor=None
products=[]


option=None

print("Mercadito chévere")
print("1. Crear lista de mercado")
print("2. Ver lista de mercado")
print("3. Editar producto de la lista")
print("4. Retirar producto de la lista")
print("5. Salir")

while option!=5:
    option=int(input("Digita una opción: "))
    if option == 1:
        product={}
        print("Has ingresado a CREAR TU LISTA DE MERCADO")
        product["id"]=random.randint(1000,9999)
        product["name"]=input("Digita el nombre del producto: ")
        product["price"]=int(input("Digita el precio del producto: "))
        product["quantity"]=int(input("Digita la cantidad del producto: "))

        products.append(product)
        print(products)


    elif option == 2:
        for i in products:
            print(i["name"])
    elif option == 3:
        productToChange = int(input("Digite el ID del producto a cambiar"))
        for i in products:
            if productToChange==i["id"]:
                print()
    elif option == 4:
        print()
    else:
        print("Opción no válida")