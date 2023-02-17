import math as m

def bobyn(step_w, step_h, bobin_type):
    d_current = d_min #задаємо поточний діаметр ущільнювача на кожному оберті
    w_current = 0 #поточна ширина намотки ущільнювача на кожному слої
    l = 0 #довжина ущільнювача на бобіні
    i = 0
    j = 0
    while d_max >= d_current:
        while w_wind >= w_current:
            w_current = w_current + step_w
            i=i+1


        l = ((w_wind/step_w) * m.sqrt((m.pi*d_current)**2 + step_w**2)) + l
        d_current = d_current+step_h*2
        j = j+1
    print("Кількість рядків", i)
    print("Кількість слоїв", j)
    return print(l)

# округлить значения до 10-х

while True:
    bobin_type = input('''
    Вкажіть тип бабіни:
    1 - D750
    2 - D500
    ''')
    step_x = float(input("Вкажіть шаг намотки:\n"))
    step_y = float(input("Вкажіть висоту ущільнювача (як він буде лягати на бабіну):\n"))
    # Описуєм параметри катушки D750
    if bobin_type == 'D750' or '1':
        d_max = 720  # 750 - 3 слоя обечайки (наружный диаметр)
        d_min = 420  # Внутренний деаметр
        w_wind = 249  # Ширина катушки

    bobyn(step_x, step_y, bobin_type)
