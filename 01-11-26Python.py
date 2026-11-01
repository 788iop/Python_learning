def print_table(args):
    for name,price in products:
        print(f"{name:<10} {price:>10,.2f}") #Куда поставить разделитель , если его везде выплевывают???
products = [("Хлеб", 50), ("Сыр", 300.5), ("Икра", 10000.99)]
print_table(products)


def make_receipt(*items):
    result = ""
    for products in items:
        result += (f'{products:.<20}\n')
    result += f'Итого: {len(items)} шт.'
    return result
print(make_receipt("Хлеб", "Молоко"))
