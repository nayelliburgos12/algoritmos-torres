Algoritmo OperacionesYComparaciones
    Definir num1, num2 Como Real
    Definir suma, resta, multiplicacion, division Como Real
	
    Escribir "Ingrese el primer n�mero: "
    Leer num1
    Escribir "Ingrese el segundo n�mero: "
    Leer num2
	
    suma <- num1 + num2
    resta <- num1 - num2
    multiplicacion <- num1 * num2
    division <- num1 / num2
	
    Escribir "Suma: ", suma
    Escribir "Resta: ", resta
    Escribir "Multiplicaci�n: ", multiplicacion
    Escribir "Divisi�n: ", division
	
    Si suma > multiplicacion Entonces
        Escribir "La suma es mayor que la multiplicaci�n."
    Sino
        Escribir "La multiplicaci�n es mayor o igual que la suma."
    FinSi
FinAlgoritmo
