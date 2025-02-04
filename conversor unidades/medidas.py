import sys


class ConversorUnidades:

    def convertir_min_a_seg(self, minutos):
        return minutos * 60  # 1 min = 60 seg

    def convertir_seg_a_min(self, segundos):
        return segundos / 60  # 60 seg = 1 min

    def convertir_horas_a_min(self, horas):
        return horas * 60  # 1 h = 60 min

    def ejecutar(self):
        while True:
            print('-----Conversor de unidades-----')
            print('1.De minutos a segundos')
            print('2.De segundos a minutos')
            print('3.De horas a minutos')
            print('4.Salir')

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
                sys.exit('Saliendo del programa...')
            else:
                print('Opción no valida. Intentalo de nuevo')


prueba = ConversorUnidades()
prueba.ejecutar()
