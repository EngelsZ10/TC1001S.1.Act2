# TC1001S.1.Act2
Actividad 2. Juego de la Víbora: Modificamos script snake.py del paquete de python freegames para agregar lo siguiente:
- La comida se movera al azar un paso a la vez sin salirse de la ventana
- La víbora y la comida deben tener un color diferente y aleatorio entre negro, naranja, amarillo, azul y verde.

Integrantes:
- Engels Emiliano Miranda Palacios A01423398
- Ronaldo Jesús Ruíz Álvarez A01424337

Log de Ronaldo:

En la línea 36 agregué una condición que comparaba si el objeto de la comida excedía los límites de la pantalla,
al ser cierto este if, regresaba el objeto a las coordenadas 0,0.

En la línea 39 y 40 agregué el movimiento aleatorio que tenía la comida en (x,y), utilizando un randrange que 
nos arrojara números tal como el -1 y 1 para de esta forma multiplicarlo por 10 y que la fruta se mueva
en los mismos intervalos que el cuerpo de la serpiente para que al comparar su colisión esta se efectúe de 
forma correcta.

Log de Emiliano:

En lineas de 19 a 21 inicialise los indices (de la lista de colores) que representan el color de la comida y de la serpiente en un integrer random entre \[0,5) y cree una lista con los 5 colores posibles

En lineas 65 y 66 cambia el indice del color la comida a un integrer random entre \[0,5) hasta que sea diferente del indice del color de la serpiente

En lineas 59 y 61 asigna el color correspondiente de la lista de colores a la comida y la serpiente
