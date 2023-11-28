
    
cliente1 = Cliente("Pamela", "Gomez", "123456789", "27831234", "1234567890")
vendedor1 = Vendedor("Terre", "Neitor", "2627282930", "27831415", "004", 17000, 50)
product = Procesador( "Procesador", "123", "Core i7", "Intel","","",79,40,"","","","","","","","")        

factura = Factura(cliente1, product , vendedor1, "Adomicilio", "17/12/23", 100, float(100*1.12), "001200" )

factura.imprimirFactura()