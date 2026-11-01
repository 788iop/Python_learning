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


import time
class Timer:
    def __init__(self):
        pass
    def __enter__(self):
        self.start_time = time.time()
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        end_time = time.time()
        timered = end_time - self.start_time
        print(f'Время работы: {timered:.4f} сек')
with Timer():
    sum(range(100000000)) 
