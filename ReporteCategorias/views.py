from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from FlujoEfectivo.models import FlujoModel
from Categorias.models import CategoriasModel
from django.http import JsonResponse

# Create your views here.

class ReporteCategoriasView(APIView):
    def get(self, request, mesUser,format = None):
        mesUser = int(mesUser)
        dataF = FlujoModel.objects.all()
        dataC = CategoriasModel.objects.all()
        semana = 0
        registros = False
        sumaCantidades = 0
        result = []
        ingresos = [
        [0,0,0,0,0], #fila de efectivo
        [0,0,0,0,0], #fila de depositos
        [0,0,0,0,0]] #fila de totales
        gastos = [
        [0,0,0,0,0], #fila de costo-venta
        [0,0,0,0,0], #fila de gasto-aoc
        [0,0,0,0,0]] #fila de totales

        diferencia = [0,0,0,0,0] #fila de Total utilidad
        rentabilidad = [0,0,0,0,0] #fila de margen de rentabilidad

        for f in dataF:
            categoria = dataC.filter(id=f.id_categoria.id).values()[0]['descripcion']
            subCategoria = dataC.filter(id=f.id_categoria.id).values()[0]['sub_categoria']
            dia = int(f.fecha[3:5])
            mes = int(f.fecha[:2])

            if(mes == mesUser):
                if(dia < 8 and mes == mesUser):
                    semana = 0
                if ((dia > 7 and dia < 15) and mes == mesUser):
                    semana = 1
                if((dia>14 and dia < 22) and mes == mesUser):
                    semana = 2
                if((dia>21) and mes == mesUser):
                    semana = 3

                if(subCategoria == "EFECTIVO"):
                    ingresos[0][semana] += f.cantidad
                elif(subCategoria == "DEPOSITO"):
                    ingresos[1][semana] += f.cantidad
                ingresos[2][semana] = ingresos[0][semana] + ingresos[1][semana]

                if(categoria == "COSTO-VENTA"):
                    gastos[0][semana] += f.cantidad
                elif(categoria == "GASTO-AOC"):
                    gastos[1][semana] += f.cantidad
                gastos[2][semana] = gastos[0][semana] + gastos[1][semana]      
        
        for registro in ingresos: #verificamos que exista almenos un registro sumando las cantidades, en caso de que no existan no se hará un reporte
            sumaCantidades = sum(registro)
        for registro in gastos:
            sumaCantidades += sum(registro)
        if(sumaCantidades>0):
            registros = True
        else:
            registros = False

        if(registros == True):
            for i in [0,1,2]: #indices de las filas que hay
                for cantidad in ingresos[i][0:4]: #buscar cada elemento de la fila
                    ingresos[i][4] += cantidad #hacer el total de los elementos de esa fila y guardarlo al final de la misma
                for cantidad in gastos[i][0:4]: #buscar cada elemento de la fila
                    gastos[i][4] += cantidad #hacer el total de los elementos de esa fila y guardarlo al final de la misma
            for i in [0,1,2,3,4]:
                diferencia[i] = ingresos[2][i] - gastos[2][i]
                rentabilidad[i] = round((diferencia[i]*100)/ingresos[2][i])
            result.append({
                    'cantidadEntrada' : ingresos,
                    'cantidadSalida' : gastos,
                    'utilidad' : diferencia,
                    'rentabilidad' : rentabilidad
                })
            return JsonResponse(result, safe=False)
        else:
            return JsonResponse({"message" : "No hay registros del mes seleccionado"}, safe=False)   
