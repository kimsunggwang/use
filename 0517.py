print("파이썬 피자에 오신것을 환영합니다!")
small_pizza_price = 15000
medium_pizza_price = 20000
large_pizza_price = 30000
pepperoni_price = 2000
cheese_price = 3000

size=(input("원하는 피자 사이즈는: S,M,L "))
add_pepperoni = input("페퍼로니를 추가하시겠습니까? (Y/N): ")
add_cheese = input("치즈를 추가하시겠습니까? (Y/N): ")
total_price = 0

if size == 'S':
    total_price += small_pizza_price
elif size == 'M':
    total_price += medium_pizza_price
elif size == 'L':
    total_price += large_pizza_price

if add_pepperoni == 'Y':
    total_price += pepperoni_price

if add_cheese == 'Y':
    total_price += cheese_price

print(f"총 지불하실 금액은{total_price}원 입니다")