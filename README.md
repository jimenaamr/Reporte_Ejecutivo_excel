# REPORTE EJECUTIVO EXCEL

En este repositorio se encuentran los archivos necesarios para hacer un excel con un reporte ejecutivo acerca de las ventas de Maven Pizzas en 2016.

## Archivos Adjuntados

- order_details.csv: Detalles sobre los pedidos que se han realizado a lo largo del año. En él encontramos el identificador del pedido, el identificador de la pizza pedida y la cantidad pedida. Deberemos limpiar los datos, ya que no están en el formato correcto.

- orders.csv: Detalles sobre los pedidos que se han realizado a lo largo del año. En él encontramos el identificador del pedido, la fecha en la que se realizó y la hora. Deberemos limpiar los datos, ya que no están en el formato correcto.

- pizza_types.csv: Detalles sobre las pizzas disponibles en la pizzaría. En él encontramos el identificador del tipo de pizza, su nombre completo, la categoría en la que está y los ingredientes necesarios para prepararla.

- pizzas.csv: Detalles sobre las pizzas disponibles en la pizzaría. En él encontramos el identificador del tipo de pizza, su tipo, su tamaño y su precio.

- pizzas_pedidas_2016.csv: Dataframe creado tras ejecutar el archivo pizzas_año.py. Te ofrece un cálculo de cada tipo de pizza a lo largo de todo 2016.

- dinero_ganado_2016.csv: Dataframe con el dinero ganado durante el año 2016 por la venta de cada tipo de pizza.

- prediccion_ingredientes16.csv: Dataframe que te ofrece una predicción de los ingredientes que la pizzería debería comprar semanalmente en función de los datos de 2016 analizados.

- requirements.txt: En este archivo encontramos las librerías que se necesitan instalar para poder ejecutar los archivos.

- crear_excel.py: En este archivo encontramos el código necesario para crear el excel del reporte ejecutivo de la pizzería. En él añadimos una predicción de los ingredientes que se tendrán que comprar cada semana, que se obtiene de prediccion_ingredientes16.csv, dos gráficas con el dinero ganado por cada pizza en el año, que se obtienen de dinero_ganado_2016.csv y una gráfica con los pedidos de cada tipo de pizza en todo el año, que se obtiene de pizzas_pedidas_2016.csv.

- ganacias_año.py: Código neceario para crear un dataframe con los tipos de pizza que hay y las ganancias que se han conseguido con cada tipo a lo largo del año. Es el dinero_ganado_2016.csv

- reporte_pizzas.xlsx: Reporte ejecutivo en formato excel de la pizzería Maven Pizzas en el año 2016 creado al ejecutar crear_excel.py. Encontramos tres hojas, la primera con un reporte ejecutivo acerca del dinero ganado, la segunda con un reporte de la predicción de ingredientes y la tercera con un reporte de la cantidad de pizzas de cada tipo. En las tres hojas encontramos gráficas creadas con excel, mientras que en la última encontramos también una imagen añadida de una gráfica creada con seaborn.

- grafica_pizzas_año.jpeg: Imagen de la gráfica con los datos de pizzas_pedidas_2016.csv añadida al excel.


## Modo de Ejecución

1- Instalar el requirements.txt

2- Ejecutar el archivo ganancias_año.py para obtener el csv dinero_ganado_2016.csv.

3- Ejecutar el archivo crear_excel.py para obetener el reporte ejecutivo en formato excel.