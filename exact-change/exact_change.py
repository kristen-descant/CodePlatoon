def exact_change(amount_paid, item_cost, currency='USD'):
    if currency == "pesos":
        change = change_pesos(amount_paid,item_cost)
    elif currency == "yen":
        change = change_yen(amount_paid,item_cost)
    elif currency == "euros":
        change = change_euros(amount_paid,item_cost)
    elif currency == "ruble":
        change = change_ruble(amount_paid,item_cost)
    else:
        change = amount_paid - item_cost

    change_map = {
        100:'$100 bill',
        50: '$50 bill',
        20: '$20 bill',
        10: '$10 bill',
        5: '$5 bill',
        1: '$1 bill',
        .25: 'quarter',
        .10: 'dime',
        .05: 'nickel',
        .01: 'penny',
    }
    result = f'The exact change for an item that costs ${item_cost:.2f} with an amount paid of ${amount_paid} is '
    
    demonination = 0
    if change > 0:
        for key in change_map:
            counter = 0
            if change >= key:
                counter = int(change // key)
                change -= key * counter
                demonination += 1
                if change < 0.01 and demonination > 1:
                    result += "and "  
                if counter > 1:
                    label = change_map[key]+'s'
                    if key == .01:
                        label = 'pennies'
                    result += f'{counter} {label}, '
                elif counter == 1:
                    result += f'{counter} {change_map[key]}, '
        result = result[:-2]   
        result += "."  
        return result
    elif change == 0:
        return 'You paid the exact amount, no change due.'
    else:
        return "Insuficient funds."

  


def change_pesos(amount_paid, item_cost):
    pesos_to_usd = amount_paid * 0.058
    return item_cost - pesos_to_usd

def change_yen(amount_paid, item_cost):
    yen_to_usd = amount_paid * 0.0072
    return item_cost - yen_to_usd 

def change_euros(amount_paid, item_cost):
    euros_to_usd = amount_paid * 1.08
    return item_cost - euros_to_usd 

def change_ruble(amount_paid, item_cost):
    ruble_to_usd = amount_paid * 0.012
    return item_cost - ruble_to_usd 


