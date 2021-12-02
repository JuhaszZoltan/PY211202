print('"gyümölcs"pult:\n')

print('alma:        360 Ft/Kg')
print('körte:      1100 Ft/Kg')
print('szilva:      800 Ft/Kg')
print('bazsalikom: 2500 Ft/ g')

zvz = input('mi kéne ha volna? ')

if zvz == 'gyümölcs':
    gyumi = input('milyen gyümölcsöt szeretnél? ')
    if gyumi == 'alma':
        kg = float(input('ennyit (kg): '))
        print(f'{kg} Kg alma {360 * kg} Ft')
    elif gyumi == 'körte':
        kg = float(input('ennyit (kg): '))
        print(f'{kg} Kg körte {1100 * kg} Ft')
    elif gyumi == 'szilva':
        kg = float(input('ennyit (kg): '))
        print(f'{kg} Kg szilva {800 * kg} Ft')
    else: print('ilyet nem árulunk, bocsi :(')
elif zvz == 'bazsalikom':
    cs = float(input('hány g-t kérsz? '))
    print(f'{cs * 2500} Ft lesz.')
else: print('bocs, olyan nincs')



