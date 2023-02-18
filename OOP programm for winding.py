import math as m


class Bobyn:

    def __init__(self, d_max, d_min, w_wind):

        self.d_max = d_max
        self.d_min = d_min
        self.w_wind = w_wind

    def length(self, step_w, step_h):
        loss_percentage_w = 7 #додано відсоток втрат так-як на бобіну він кладеться не "впритик"
        loss_percentage_h = 10 #додано відсоток втрат так-як кожен слой кладеться не впритик, а трішки заломлює поверхню ущільнювача

        step_w = step_w + step_w*loss_percentage_w / 100 #шаг ущільнювача по ширині намотки з відсотком втрат
        step_h = step_h + step_h * loss_percentage_h / 100 #шаг ущільнювача по висоті намотки з відсотком втрат

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
        culc_dict = {
            'row' : i,
            'column' : j
        }
        return culc_dict, l

###########################################################################################
#D750:
    #d_max = 720   # 750 - 3 слоя обечайки (наружный диаметр)
    #d_min = 420   # 400 + слой + сгиб Внутренний деаметр
    #w_wind = 249  # Ширина катушки
D750 = Bobyn(730, 420, 249)
###########################################################################################
#D500:
    #d_max = 490  # 500 - 1 слоя обечайки (наружный диаметр)
    #d_min = 230  # + сгиб Внутренний деаметр
    #w_wind = 150  # Ширина катушки
D500 = Bobyn(490, 240, 150)
###########################################################################################
#D800:
    #d_max = 800  # 500 - 1 слоя обечайки (наружный диаметр)
    #d_min = 321  # + слои Внутренний деаметр
    #w_wind = 180  # Ширина катушки
D800 = Bobyn(800, 330, 180)
###########################################################################################
#D290:!
    #d_max = 490  # 500 - 1 слоя обечайки (наружный диаметр)
    #d_min = 230  # Внутренний деаметр
    #w_wind = 150  # Ширина катушки
D290 = Bobyn(290, 130, 60)

def question_en():
    bobin_type = int(input('''Enter coil type:
1 - D750
2 - D500
3 - D800 (Export)
4 - D250 (For tests)
'''))

    step_x = float(input("Enter winding pitch:\n"))
    step_y = float(input("Вкажіть висоту ущільнювача (як він буде лягати на бабіну):\n"))
    return bobyn_taker(bobin_type, step_x, step_y)

def question_ua():
    bobin_type = int(input('''Вкажіть тип бабіни:
1 - D750
2 - D500
3 - D800 (Export)
4 - D250 (Для тестів)
'''))

    step_x = float(input("Вкажіть шаг намотки:\n"))
    step_y = float(input("Вкажіть висоту ущільнювача (як він буде лягати на бабіну):\n"))
    return bobyn_taker(bobin_type, step_x, step_y)



def bobyn_taker(bobin_type, step_x, step_y):

    if bobin_type == 1:
        result_1, result_2  = D750.length(step_x, step_y)

    elif bobin_type == 2:
        result_1, result_2 = D500.length(step_x, step_y)

    elif bobin_type == 3:
        result_1, result_2 = D800.length(step_x, step_y)

    elif bobin_type == 4:
        result_1, result_2 = D290.length(step_x, step_y)



    return result_1, result_2




def answer_ua(result_1, result_2):
    ans = (f"Кількість рядків на одному слої: {result_1['row']}; \nКількість слоїв: {result_1['column']}.\n"
          f"Довжина намотки = {round((result_2/1000), 2)}м.")

    return ans




while True:
    result_1, result_2 = question_ua()
    print(answer_ua(result_1, result_2))



    input()

