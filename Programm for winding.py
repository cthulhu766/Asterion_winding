# !!!!Перезібрати функцію через ООП
# Додати катушку для тестів

def bobyn(step_w, step_h, bobin_type):
    # Описуєм параметри катушки D750
    if bobin_type == 'D750' or '1':
        d_max = 720  # 750 - 3 слоя обечайки (наружный диаметр)
        d_min = 400  # Внутренний деаметр
        w_wind = 240  # Ширина катушки

    # Описуєм параметри катушки D500
    elif bobin_type == 'D500' or '2':
        d_max = 490  # 500 - 1 слоя обечайки (наружный диаметр)
        d_min = 230  # Внутренний деаметр
        w_wind = 150  # Ширина катушки

    d_current = d_min
    w_current = 0
    sum_current_w = 0
    sum_current_h = 0
    i = 0
    j = 0

    # Розраховуєм кількість обертів на катушці
    while d_current < d_max - step_h * 2:
        d_current = d_current + step_h * 2
        l1 = d_current * 3.14

        sum_current_h = sum_current_h + l1
        i = i + 1
        # print(d_current)

    print(f'Кількість рядів: {i}')

    # Розраховуєм кількість стовбців на катушці
    while w_current < w_wind - step_w:
        w_current = w_current + step_w
        j = j + 1

        # print(w_current)
    print(f'Кількість стовбців: {j}')
    l = sum_current_h * j

    return print((l / 1000) * 0.88)  # 0.88 коэффіцієнт втрат


# округлить значения до 10-х

while True:
    bobin_type = input('''
    Вкажіть тип бабіни:
    1 - D750
    2 - D500
    ''')
    step_x = float(input("Вкажіть шаг намотки:\n"))
    step_y = float(input("Вкажіть висоту ущільнювача (як він буде лягати на бабіну):\n"))
    bobyn(step_x, step_y, bobin_type)
