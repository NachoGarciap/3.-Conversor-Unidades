import sys


class ConversorUnidades:

    # METODOS PARA MEDIDAS DE TIEMPO
    def convertir_min_a_seg(self, minutos):
        return minutos * 60  # 1 min = 60 seg

    def convertir_seg_a_min(self, segundos):
        return segundos / 60  # 60 seg = 1 min

    def convertir_horas_a_min(self, horas):
        return horas * 60  # 1 h = 60 min

    # METODOS PARA MEDIDAS DE LONGITUD

    def convertir_metros_a_km(self, metros):
        return metros / 1000  # 1m = 0.001km
    def convertir_km_a_metros(self, km):
        return km * 1000  # 1km = 1000m
    def convertir_cm_a_metros(self, cm):
        return cm / 100  # 100cm = 0.01m

    #METODOS PARA MEDIDAS DE TEMPERATURA

    def convertir_celsius_a_fahrenheit(self, celsius):
        return (celsius * 9 / 5) + 32

    def convertir_fahrenheit_a_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5 / 9


    def menu_tiempo(self):
        while True:
            print('-----Conversion de Tiempo-----')
            print('1.De minutos a segundos')
            print('2.De segundos a minutos')
            print('3.De horas a minutos')
            print('4.Volver')

            opcion = int(input('Elige una opción: '))

            if opcion == 1:
                minutos = float(input('Introduce los minutos: '))
                segundos = self.convertir_min_a_seg(minutos)
                print(f'{minutos} minutos son {segundos} segundos')
            elif opcion == 2:
                segundos = float(input('Introduce los segundos: '))
                minutos = self.convertir_seg_a_min(segundos)
                print(f'{segundos} segundos son {minutos} minutos')
            elif opcion == 3:
                horas = float(input('Introduce los horas: '))
                minutos = self.convertir_horas_a_min(horas)
                print(f'{horas} horas son {minutos} minutos')
            elif opcion == 4:
                break
            else:
                print('Opción no valida. Intentalo de nuevo')

    def menu_longitud(self):
        while True:
            print('-----Conversion de Longitud-----')
            print('1.De metros a kilometros')
            print('2.De kilometros a metros')
            print('3.De centimetros a metros')
            print('4.Volver')

            opcion = int(input('Elige una opción: '))

            if opcion == 1:
                metros = float(input('Introduce los metros: '))
                km = self.convertir_metros_a_km(metros)
                print(f'{metros} metros son {km} kilometros')
            elif opcion == 2:
                km = float(input('Introduce los kilometros: '))
                metros = self.convertir_km_a_metros(km)
                print(f'{km} kilometros son {metros} metros')
            elif opcion == 3:
                centimetros = float(input('Introduce los centimetros: '))
                metros = self.convertir_cm_a_metros(centimetros)
                print(f'{centimetros} centimetros son {metros} metros')
            elif opcion == 4:
                break
            else:
                print('Opción no valida. Intentalo de nuevo')

    def menu_temperatura(self):
        while True:
            print('-----Conversion de Temperatura-----')
            print('1. Celsius a Fahrenheit')
            print('2. Fahrenheit a Celsius')
            print('3. Volver')

            opcion = int(input('Elige una opción: '))

            if opcion == 1:
                celsius = float(input('Introduce los grados Celsius: '))
                print(f'{celsius}°C son {self.convertir_celsius_a_fahrenheit(celsius)}°F')
            elif opcion == 2:
                fahrenheit = float(input('Introduce los grados Fahrenheit: '))
                print(f'{fahrenheit}°F son {self.convertir_fahrenheit_a_celsius(fahrenheit)}°C')
            elif opcion == 3:
                break
            else:
                print('Opción no valida. Intentalo de nuevo')

    def ejecutar(self):
        while True:
            print('-----Conversor-----')
            print('1.Tiempo')
            print('2.Longitud')
            print('3.Temperatura')
            print('4.Salir')

            opcion = int(input('Elige una opción: '))

            if opcion == 1:
                self.menu_tiempo()
            elif opcion == 2:
                self.menu_longitud()
            elif opcion == 3:
                self.menu_temperatura()
            elif opcion == 4:
                sys.exit('Saliendo del programa...')
            else:
                print('Opción incorrecta, prueba de nuevo')


