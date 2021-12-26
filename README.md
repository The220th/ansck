# ansck

ansck (any numeral system convertek) - скрипт, который переводит из любой системы счисления в любую другую.

# Использование

Чтобы запустить, выполните:

``` bash
> python ansck.py {number}_{suf1} {suf2}

# number - число, которое переводится в другую систему счисления

# suf1 - система счисления числа number

# suf2 - система счисления результата
```

Например:

``` bash
python ansck.py 10011011_2 10
```

сконвертирует число `10011011` в двоичной системе счисления в десятичную, то есть в `155`.

Также возможно указывать цифры поразрядно. Например:

``` bash
python ansck.py "[14 120 53 0 1]_123" 9
```

сконвертирует число `[14 120 53 0 1]` в системе счисления `123` в девятиричную, то есть в `8757323621`.


Или можно так:

``` bash
python ansck.py DE2_17 5
# или
python ansck.py "[13 14 2]_17" 5
# или
python ansck.py "[13, 14, 2]_17" 5
```

сконвертирует число `DE2` в системе счисления `17` в пятиричную, то есть в `111442`.

# Использование как модуль

Можно пользовать как модуль. Например:

``` python
# -*- coding: utf-8 -*-
import ansck

if __name__ == '__main__':
    ansck.dec2sn(2, 25) # вернёт [1, 0, 0, 1, 1]

    ansck.dec2sn(16, 10447) # вернёт [15, 12, 8, 2]

    ansck.sn2dec(2, [1, 0, 0, 1, 1]) # вернёт 25

    ansck.sn2dec(16, [15, 12, 8, 2]) # вернёт 10447

    ansck.letter2num([15, 12, 8, 2]) # вернёт 28CF

    ansck.num2letter("28CF") # вернёт [15, 12, 8, 2]

    #...
```