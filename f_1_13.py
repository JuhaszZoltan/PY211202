MIN = 1000
MAX = 300000

print('Bankjegyautomata\n')
print(f'Legkisebb címlet {MIN} ft, maximálisan felvehető összeg {MAX} Ft.\n')
osszeg = int(input('Adja meg mekkora összeget kíván felvenni! '))
if osszeg % 1000 != 0:
    print('csak 1000el osztható összeget tud felvenni!')
elif osszeg < MIN:
    print(f'a minimálisan felvehető összeg: {MIN} Ft')
elif osszeg > MAX:
    print(f'a maximálisan felvehető összeg {MAX} Ft')
else:
    te = osszeg // 10000
    osszeg = osszeg % 10000
    oe = osszeg // 5000
    osszeg = osszeg % 5000
    ee = osszeg // 1000

    print(f'{te} * 10 000 = {te * 10000}')
    print(f' {oe} *  5 000 =   {oe *  5000}')
    print(f' {ee} *  1 000 =   {ee *  1000}')
    print( '--------------------')
    print(f'Összeg:       {te * 10000 + oe * 5000 + ee * 1000} Ft')