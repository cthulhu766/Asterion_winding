import math as m


class Bobyn_D750:

    def __init__(self, d_max, d_min, w_wind):

        self.d_max = d_max
        self.d_min = d_min
        self.w_wind = w_wind

    def bobyn(self, step_w, step_h):
        d_current = self.d_min  # задаємо поточний діаметр ущільнювача на кожному оберті
        w_current = 0  # поточна ширина намотки ущільнювача на кожному слої
        l = 0  # довжина ущільнювача на бобіні
        i = 0
        j = 0
        while self.d_max >= d_current:
            while self.w_wind >= w_current:
                w_current = w_current + step_w
                i = i + 1

            l = ((self.w_wind / step_w) * m.sqrt((m.pi * d_current) ** 2 + step_w ** 2)) + l
            d_current = d_current + step_h * 2
            j = j + 1
        print("Кількість рядків", i)
        print("Кількість слоїв", j)
        return print(l)

#d_max = 720   # 750 - 3 слоя обечайки (наружный диаметр)
#d_min = 420   # Внутренний деаметр
#w_wind = 249  # Ширина катушки



D750 = Bobyn_D750(720, 420, 249)




D750.bobyn(13, 6)