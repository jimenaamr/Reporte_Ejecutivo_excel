import pandas as pd

df_detalle_pedidos = pd.read_csv('order_details.csv',sep = ";", encoding = "LATIN_1")
df_pizzas = pd.read_csv('pizzas.csv',sep = ",", encoding = "LATIN_1")

df_detalle_pedidos['quantity'] = df_detalle_pedidos['quantity'].str.replace('one','1')
df_detalle_pedidos['quantity'] = df_detalle_pedidos['quantity'].str.replace('One','1')
df_detalle_pedidos['quantity'] = df_detalle_pedidos['quantity'].str.replace('two','2')
df_detalle_pedidos['quantity'] = df_detalle_pedidos['quantity'].str.replace('Two','2')


df_detalle_pedidos['pizza_id'] = df_detalle_pedidos['pizza_id'].str.replace('-','_')
df_detalle_pedidos['pizza_id'] = df_detalle_pedidos['pizza_id'].str.replace('@','a')
df_detalle_pedidos['pizza_id'] = df_detalle_pedidos['pizza_id'].str.replace('3','e')
df_detalle_pedidos['pizza_id'] = df_detalle_pedidos['pizza_id'].str.replace('0','o')
df_detalle_pedidos['pizza_id'] = df_detalle_pedidos['pizza_id'].str.replace(' ','_')

df_detalle_pedidos['quantity'].fillna(1, inplace = True)
df_detalle_pedidos = df_detalle_pedidos[df_detalle_pedidos['pizza_id'].notna()]

lista_cantidades_validas = list(df_detalle_pedidos['quantity'])
lista_tipos_pizza = list(df_pizzas['pizza_id'])
lista_precios_pizza = list(df_pizzas['price'])
lista_pizzas_pedidas = list(df_detalle_pedidos['pizza_id'])

dic_precios_pizza = {}
for i in range(len(lista_tipos_pizza)):
    dic_precios_pizza[lista_tipos_pizza[i]] = lista_precios_pizza[i]

for i in range(len(lista_cantidades_validas)):
        lista_cantidades_validas[i] = int(lista_cantidades_validas[i])
        if lista_cantidades_validas[i] < 0:
            lista_cantidades_validas[i] *= -1

dic_cantidad_pedida = {}
for tipo in lista_tipos_pizza:
    dic_cantidad_pedida[tipo] = 0

for i in range(len(lista_pizzas_pedidas)):
    dic_cantidad_pedida[lista_pizzas_pedidas[i]] += lista_cantidades_validas[i]

dic_precio_total = {}
for pizza in dic_cantidad_pedida:
    dic_precio_total[pizza] = dic_cantidad_pedida[pizza] * dic_precios_pizza[pizza]
    
df = pd.DataFrame([[key, dic_precio_total[key]] for key in dic_precio_total.keys()], columns=['Pizza','Dinero Ganado'])
df.to_csv('dinero_ganado_2016.csv')