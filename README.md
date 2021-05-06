# TC1001S.1-Actividad2
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
