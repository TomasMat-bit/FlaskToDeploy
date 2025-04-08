# Skyrius 1: [ Obuolys, Bananai, Tuščia ]
# Skyrius 2: [ Tuščia, Tuščia, Tuščia ]
# Skyrius 3: [ Tuščia, Tuščia, Tuščia ]

warehouse = [["" for _ in range(3)] for _ in range(3)]

def display_warehouse():
    print('SANDELIO BUKLE:')
    for i, section in enumerate(warehouse):
        display = [item if item != '' else 'Tuscia' for item in section]
        print(f'Skyrius {i+1}: {display}')
    print()

def is_section_full(section_index):
    return all(i != '' for i in warehouse[section_index])

def is_warehouse_full():
    return all(is_section_full(i) for i in range(3))

while not is_warehouse_full():
    display_warehouse()
    try:
        section_input = int(input('Iveskite skyriaus numeri (1-3): ')) - 1
        shelf_input = int(input('Iveskite lentynos numeri (1-3): ')) - 1
        item = input('Iveskite prekes pavadinima: ').strip()

        if not (0 <= section_input < 3 and 0 <= shelf_input < 3):
            print('Neteiisingas skyriaus arba lentynos numeris!')
            continue

        if item and warehouse[section_input][shelf_input] != '':
            print('Si lentyna jau uzimta!')
            continue

        if item and is_section_full(section_input):
            print(f'Skyrius {section_input + 1} dabar yra pilnas!')
            continue

        warehouse[section_input][shelf_input] = item
        if item:
            print(f'Preke "{item}" prideta i skyriu {section_input + 1}, lentyna {shelf_input + 1}')
        else:
            print(f'Preke isimta is skyriaus {section_input + 1}, lentynos {shelf_input + 1}')

    except ValueError:
        print('Ivestys turi buti skaiciai!')

display_warehouse()
print('Visi skyriai pilni. Sandelis uzpildytas!')
