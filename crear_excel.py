import xlsxwriter as xlsx
import pandas as pd

df_ganancias = pd.read_csv('dinero_ganado_2016.csv',sep = ",", encoding = "LATIN_1")
df_prediccion_ingredientes = pd.read_csv('prediccion_ingredientes16.csv',sep = ",", encoding = "LATIN_1")
df_pizzas_pedidas = pd.read_csv('pizzas_pedidas_2016.csv',sep = ",", encoding = "LATIN_1")

reporte = xlsx.Workbook('reporte_pizzas.xlsx')

hoja1 = reporte.add_worksheet('Reporte_Ejecutivo')

titulo1 = reporte.add_format({'bold':True, 'font_size':50, 'font_color':'green'})
hoja1.merge_range(1,5,1,20,'REPORTE EJECUTIVO',titulo1)

tit1 = list(df_ganancias.columns)
titulos1 = []

for i in range(1,len(tit1)):
    titulos1.append(tit1[i])

hoja1.write_row('B5',titulos1)
hoja1.write_column('B6',df_ganancias['Pizza'])
hoja1.write_column('C6',df_ganancias['Dinero Ganado'])

grafico1 = reporte.add_chart({'type':'column'})
grafico1.set_size({'width': 2000, 'height': 600})
grafico1.set_x_axis({'name':'Tipos de Pizza'})
grafico1.set_y_axis({'name':'Dinero Ganado'})

grafico1.add_series({'categories':'=Reporte_Ejecutivo!$B$6:$B$101','values': '=Reporte_Ejecutivo!$C$6:$C$101'})

hoja1.insert_chart('F5',grafico1)


hoja2 = reporte.add_worksheet('Reporte_Ingredientes')

titulo2 = reporte.add_format({'bold':True, 'font_size':50, 'font_color':'green'})
hoja2.merge_range(1,5,1,20,'REPORTE DE INGREDIENTES',titulo2)

tit2 = list(df_prediccion_ingredientes.columns)
titulos2 = []

for i in range(1,len(tit2)):
    titulos2.append(tit2[i])

hoja2.write_row('B5',titulos2)
hoja2.write_column('B6',df_prediccion_ingredientes['Ingrediente'])
hoja2.write_column('C6',df_prediccion_ingredientes['Cantidad a comprar'])

grafico2 = reporte.add_chart({'type':'column'})
grafico2.set_size({'width': 1500, 'height': 600})
grafico2.set_x_axis({'name':'Ingredientes'})
grafico2.set_y_axis({'name':'Cantidad a Comprar por Semana'})

grafico2.add_series({'categories':'=Reporte_Ingredientes!$B$6:$B$70','values': '=Reporte_Ingredientes!$C$6:$C$70'})

hoja2.insert_chart('F5',grafico2)


hoja3 = reporte.add_worksheet('Reporte_Pedidos')

titulo3 = reporte.add_format({'bold':True, 'font_size':50, 'font_color':'green'})
hoja3.merge_range(1,5,1,20,'REPORTE DE PEDIDOS',titulo3)

tit3 = list(df_pizzas_pedidas.columns)
titulos3 = []

for i in range(1,len(tit3)):
    titulos3.append(tit3[i])

hoja3.write_row('B5',titulos3)
hoja3.write_column('B6',df_pizzas_pedidas['Pizza'])
hoja3.write_column('C6',df_pizzas_pedidas['Cantidad pedida'])

grafico3 = reporte.add_chart({'type':'pie'})
grafico3.set_size({'width': 1000, 'height': 900})
grafico3.set_x_axis({'name':'Tipos de Pizza'})
grafico3.set_y_axis({'name':'Cantidad Pedida'})

grafico3.add_series({'categories':'=Reporte_Pedidos!$B$6:$B$37','values': '=Reporte_Pedidos!$C$6:$C$37'})

hoja3.insert_chart('F5',grafico3)
hoja3.insert_image('W5','grafica_pizzas_año.jpeg')

reporte.close()