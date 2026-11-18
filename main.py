import numpy as np

prices = np.array([120, 250, 500, 750, 1000])
quantities = np.array([5, 3, 8, 2, 4])
discounts = np.array([10, 15, 0, 20, 5])


def show_array_info(array):
    print("Масив:", array)
    print("Тип масиву:", type(array))
    print("Тип елементів:", array.dtype)
    print("Форма масиву:", array.shape)
    print("Кількість елементів через len():", len(array))
    print("Кількість елементів через size:", array.size)


print("Ціни товарів")
show_array_info(prices)

print("\nКількість проданих товарів")
show_array_info(quantities)

print("\nЗнижки")
show_array_info(discounts)

print("\nРозрахунки вартості та знижок")

sales_amounts = prices * quantities
print("Виручка за кожним товаром без знижки:", sales_amounts)

discounts = discounts + 3
print("Оновлені знижки (%):", discounts)

discounted_prices = prices - prices * discounts / 100
print("Ціни за одиницю після знижки:", discounted_prices)

print("\n Порівняння цін")

print("Дорожчі за 500 грн:", prices[prices > 500])
print("Від 200 до 800 грн:", prices[(prices >= 200) & (prices <= 800)])
print("Рівно 500 грн:", prices[prices == 500])

print("\nЛогічні оператори")

low_or_high = (prices < 300) | (prices > 800)
print("Ціни менші за 300 або більші за 800 грн:", prices[low_or_high])

at_most_500 = ~(prices > 500)
print("Ціни не вище 500 грн:", prices[at_most_500])

price_and_quantity = (prices > 200) & (quantities > 3)
print("Ціни товарів дорожчих за 200 грн, яких продали більше ніж 3 шт.:",
      prices[price_and_quantity])

print("\n Суми знижок та кінцеві ціни")

discount_amounts_20 = prices * 20 / 100
print("Сума знижки 20% для кожного товару:", discount_amounts_20)

individual_discount_amounts = prices * discounts / 100
print("Сума індивідуальної знижки:", individual_discount_amounts)

prices_after_20 = prices - discount_amounts_20
print("Ціни після знижки 20%:", prices_after_20)

prices_after_individual_discounts = prices - individual_discount_amounts
print("Ціни після індивідуальних знижок:", prices_after_individual_discounts)

print("\n Індексація та зрізи")

print("Ціна першого товару:", prices[0])
print("Ціна останнього товару:", prices[-1])
print("Перші три ціни:", prices[:3])

prices[1] = 300
print("Ціни після зміни другого товару:", prices)

print("Ціни у зворотному порядку:", prices[::-1])

print("\n8. Зміна та доповнення масиву")

prices = np.append(prices, 1500)
print("Додали 1500 у кінець:", prices)

prices = np.insert(prices, 2, 400)
print("Вставили 400 на третю позицію:", prices)

prices = np.delete(prices, 3)
print("Видалили четверту ціну:", prices)

print("\n Додаткові оператори та функції NumPy")

prices += 100
print("Ціни після збільшення на 100 грн:", prices)

quantities *= 2
print("Кількість товарів після подвоєння:", quantities)

print("Кількість повних сотень у кожній ціні:", prices // 100)
print("Залишки від ділення цін на 100:", prices % 100)

prices = np.where(prices < 300, 300, prices)
print("Ціни після заміни значень менше 300 грн:", prices)

print("Унікальні ціни:", np.unique(prices))
print("Ціни за зростанням:", np.sort(prices))
print("Ціни в межах від 200 до 800 грн:", np.clip(prices, 200, 800))