def descuentos(descuento,valor):

    total = float(valor) * descuento/100
    return valor - total
        

precio = float(input("Precio Articulo:"))
descuen = float(input("Descuento") or 10)
print(descuen)
print(f"El valor con descuento es: {descuentos(descuen,precio)}")