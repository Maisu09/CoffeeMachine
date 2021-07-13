#Globalzz

MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
    },
}

RESOURCES = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'money': 0,
}

def MoneyProblem():  #Veryfies the amount of money added by the user. Also askes the user for the money...
    print('Introduce the money: ')
    penny=input('Pennys: ')
    dime=input('Dimes: ')
    nickel=input('Nickels: ')
    quarter=input('Quarter: ')


def CappuccinoCheck():  #Check for ingredients and for the money. goes into making it.

    for ingredient in MENU['cappuccino']['ingredients']:
        if int(RESOURCES[ingredient]) < int(MENU['cappuccino']['ingredients'][ingredient]):
            # print(RESOURCES[ingredient])
            # print(MENU['cappuccino']['ingredients'][ingredient])
            print(f"we can't do this right now. Not enough {ingredient}")
            return 
    
    MoneyProblem()
    
        
def LatteCheck():  #Check for ingredients and for the money. goes into making it.

    for ingredient in MENU['latte']['ingredients']:
        if int(RESOURCES[ingredient]) < int(MENU['latte']['ingredients'][ingredient]):
            # print(RESOURCES[ingredient])
            # print(MENU['latte']['ingredients'][ingredient])
            print(f"we can't do this right now. Not enough {ingredient}")
            return
    
    MoneyProblem()

        
def EspressoCheck():  #Check for ingredients and for the money. goes into making it.

    for ingredient in MENU['espresso']['ingredients']:
        if int(RESOURCES[ingredient]) < int(MENU['espresso']['ingredients'][ingredient]):
            # print(RESOURCES[ingredient])
            # print(MENU['espresso']['ingredients'][ingredient])
            print(f"we can't do this right now. Not enough {ingredient}")
            return
    
    MoneyProblem()

        


button=input('What drink do you want? (espresso/cappuccino/latte) ')

if button == 'report':
    for name in RESOURCES:
        print(f"{name}: {RESOURCES[name]}")
else:
    if button == 'espresso':
        EspressoCheck()
    elif button=='latte':
        LatteCheck()
    elif button=='cappuccino':
        CappuccinoCheck()


    

