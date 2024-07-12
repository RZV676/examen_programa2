import os
import random
import csv
from random import randint
trabajadores = ["Juan Pérez","María García"
                ,"Carlos López","Ana Martínez","Pedro Rodríguez"
                ,"Laura Hernández","Miguel,Sánchez","Isabel Gómez"
                ,"Francisco Díaz","Elena Fernández"]

def ClasificacionDel_Sueldo():
    
    conSueldos=[]
    for t in trabajadores:
        conSueldos.append({'nombre':t, 'sueldo':randint(300000,2500000)})
    print (conSueldos)

sueldosTotales=[]
    



opc=6

while True:
    
    print('-'*40)
    print('1.-Asignar sueldos aleatorios')
    print('2.-Clasificar sueldos')
    print('3.-Ver estadísticas')
    print('4.-Reporte de sueldos')
    print('5.-Salir del programa')
    print('-'*40)
    opc=int(input('Se le selecciona tu opcion: '))
    
    match opc==1:
        case 1:
            # os.system('cls')
            # print('-'*40)
            # print (f'{randint}/{trabajadores}')
            ClasificacionDel_Sueldo()
        
        
        
        
        
        
    match opc==2:
        case 1:
            if ClasificacionDel_Sueldo():
                print ('Sueldos monores a $800.000 TOTAL')
            
                
            
        
        
        
        
        
    if opc==5:
        os.system('cls')
        print ('Finalizando programa...')
        print ('Desarrollado por Vicente Ramirez')
        print ('RUT: 22.014.713-4')
        break