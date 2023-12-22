import collections

import math
import random

from decimal import Decimal, getcontext

e = math.e


class FunctionRepo(object):
    handlers = None

    def __init__(self):
        self.handlers = collections.defaultdict(set)

    def register(self, event, callback):
        self.handlers[event].add(callback)

    def fire(self, event, **kwargs):
        for handler in self.handlers.get(event, []):
            handler(**kwargs)


def f1_rastrigins_function(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension):
        x = list_of_values[i]
        res += (x * x - 10 * math.cos(2 * math.pi * x))
    res *= 10
    return res


def f2_schwefels_function(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension):
        x = list_of_values[i]
        res -= x * math.sin(math.sqrt(math.fabs(x)))
    return res


def f3_griewanks_function(list_of_values):
    dimension = len(list_of_values)
    sumpart = float(0)
    multpart = float(1)
    for i in range(0, dimension):
        x = list_of_values[i]
        sumpart += (x * x) / 4000
        multpart *= math.cos(x / math.sqrt(i+1))
    res = 1 + sumpart - multpart
    return res


def f4_sine_envelope_sine_wave_function(list_of_values):
    dimension = len(list_of_values)
    sumpart = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        sumpart += 0.5 + (math.pow(math.sin(x * x + y * y - 0.5), 2) / math.sqrt(1 + 0.001 * (x * x + y * y)))
    res = -1 * sumpart
    return res


def f5_stretched_v_sine_wave_function(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        multiplicand1 = ((x * x + y * y) ** 0.25)
        multiplicand2 = math.pow(math.sin(50 * ((x * x + y * y) ** 0.1)), 2)
        res += multiplicand1 * multiplicand2 + 1
    return res


def f6_ackleys_function_ii(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        exponent1 = 0.2 * math.sqrt(0.5 * (x * x + y * y))
        exponent2 = 0.5 * math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y)
        res += 20 + e - (20 / (e ** exponent1) - (e**exponent2))
    return res


def f7_egg_holder(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        minuend = -1 * x * math.sin(math.sqrt(math.fabs(x - y - 47)))
        subtrahend = (y + 47) * math.sin(math.sqrt(math.fabs(y + 47 + x / 2)))
        res += - minuend - subtrahend
    return res


def f8_ranas_function(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        multiplicand1 = math.sin(math.sqrt(math.fabs(y + 1 - x)))
        multiplicand2 = math.cos(math.sqrt(math.fabs(y + 1 + x)))
        addend1 = x * multiplicand1 * multiplicand2
        multiplicand3 = math.cos(math.sqrt(math.fabs(y + 1 - x)))
        multiplicand4 = math.sin(math.sqrt(math.fabs(y + 1 + x)))
        addend2 = (y + 1) * multiplicand3 * multiplicand4
        res += addend1 + addend2
    return res


def f9_michalewiczs_function(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        addend1 = math.sin(x) * math.pow(math.sin((x * x) / math.pi), 20)
        addend2 = math.sin(y) * math.pow(math.sin((2 * x * x) / math.pi), 20)
        res -= (addend1 + addend2)
    return res


def f10_masters_cosine_wave_function(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        exponent = (-1 * ((x * x) + (y * y) + (0.5 * x * y))) / 8
        multiplicand = math.cos(4 * math.sqrt((x * x) + (y * y) + (0.5 * x * y)))
        res += ((e ** exponent) * multiplicand)
    return res


def f11_bukin_function_n_6(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        addend1 = math.sqrt(math.fabs(y - (0.01 * x * x)))
        addend2 = math.fabs(x + 10)
        res += (100 * addend1) + (0.01 * addend2)
    return res


def f12_cross_in_tray_function(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        multiplicand1 = math.sin(x) * math.sin(y)
        exponent = math.fabs(100 - (math.sqrt(x * x + y * y) / math.pi))
        res += -0.0001 * ((math.fabs(multiplicand1 * (e ** exponent)) + 1) ** 0.1)
    return res


def f13_jednoducha_cosinova(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension):
        x = list_of_values[i]
        res += ((x / e) * math.cos(x))
    return res


def f14_holder_table_function(list_of_values):
    getcontext().prec = 50
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        exponent = 1 - (math.sqrt((x * x) + (y * y)) / math.pi)
        decimal_power = Decimal(e) ** Decimal(math.fabs(exponent))
        res -= math.fabs(math.sin(x) * math.cos(y) * float(decimal_power))
    return res


def f15_jezaty_bazenek(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension):
        x = list_of_values[i]
        dividend = x * math.sin(math.sqrt(math.fabs(math.pow(x, 3))))
        divisor = math.fabs(math.sin(x) * math.cos(x)) + 1
        res += dividend / divisor
    return res


def f16_lesoharmonika(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        dividend = math.sqrt((x * x) + (y * y))
        divisor = math.fabs(y) + 1
        multiplicand = dividend / divisor
        res += ((math.cos(math.pi * x) * multiplicand) - (e ** math.sin(x)))
    return res


def f17_kosmicka_lod(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        addend1 = math.sin(x) * math.pow(math.sin((x * x) / math.pi), 20)
        addend2 = math.sqrt(math.fabs(y - (x * x)))
        res += (addend1 + addend2)
    return res


def f18_misto_dopadu(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        minuend = math.sin(x) * math.pow(math.sin((x * x) / math.pi), 20)
        subtrahend = math.cos(4 * math.sqrt(x * x + y * y + 0.5 * x * y))
        res += (minuend - subtrahend)
    return res


def f19_sopka(list_of_values):
    dimension = len(list_of_values)
    getcontext().prec = 50
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        addend1 = math.sin(x) * math.pow(math.sin((x * x) / math.pi), 20)
        decimal_divisor = (Decimal(e) ** Decimal(0.2 * math.sqrt(0.5 * (x * x + y * y))))
        addend2 = 20 / decimal_divisor
        decimal_subtrahend = Decimal(e) ** Decimal(0.5 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y)))
        res += (addend1 + float(addend2) - float(decimal_subtrahend))
    return res


def f20_paralelni_koryta(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        minuend = math.sin(x) * math.cos(y)
        subtrahend = (y + 47) * math.sin(math.sqrt(math.fabs(y + 47 + (x / 2))))
        res -= math.fabs(minuend - subtrahend)
    return res


def f21_vlnity_ctyrlistek(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        fraction = (math.sqrt(x * x + y * y)) / math.pi
        res += (math.fabs(100 - fraction) * math.sin(x * y)) / 10
    return res


def f22_duny_s_horami(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        fraction = math.sin((x * x) + (x * y)) / (math.fabs(y) + 1)
        res += fraction * 100 * math.sqrt(math.fabs(y - (0.01 * x * x)))
    return res


def f23_fosilie(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        addend1 = (-1) * x * math.sin(x)
        addend2 = math.cos(math.pow(x, 3))
        addend3 = math.sin(math.pow(y, 2))
        subtrahend = math.cos(math.pow(y, 3))
        res += addend1 + addend2 - y + addend3 - subtrahend
    return res


def f24_vlnobiti(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        multiplicand1 = 1 - (0.1 * x * y)
        multiplicand2 = 2 * math.pow(math.cos(x), 20)
        addend = 4 * math.cos(y)
        res += (multiplicand1 * multiplicand2) + addend
    return res


def f25_vlnite_skluzavky(list_of_values):
    dimension = len(list_of_values)
    res = float(0)
    for i in range(dimension - 1):
        x = list_of_values[i]
        y = list_of_values[i + 1]
        multiplicand1 = y - (0.33 * x * x)
        multiplicand2 = 2 * math.pow(math.cos(x), 20)
        addend = 4 * math.sin(y)
        res += (multiplicand1 * multiplicand2) + addend
    return res


def create_filled_random_list(dimension, items_per_category):
    random_list = list()
    for _ in range(dimension):
        random_list.append(random.randint(0, items_per_category - 1))
    return random_list
