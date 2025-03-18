# 붕어빵 가격
stock = {
    "팥붕어빵" : 10,      #10개
    "슈크림붕어빵" : 5,   # 5개
    "초코붕어빵" : 6     # 6개
}

sales = {
    "팥붕어빵" : 0,      #10개
    "슈크림붕어빵" : 0,   # 5개
    "초코붕어빵" : 0     # 6개
}

prices = {
    "팥붕어빵" : 1000,      #10개
    "슈크림붕어빵" : 1200,   # 5개
    "초코붕어빵" : 1500     # 6개
}


def calculate_salse():
    total_sales = 0

    for bread in sales:
        total_sales += (sales[bread] * prices[bread])
    print(f"총 매출은 {total_sales}원입니다.")


while True:
    mode = input("원하는 모드를 선택하세요 (주문, 관리자, 종료) : ")
    if mode == "종료":
        break

    elif mode == "주문":
        order_bread()

    elif mode == "관리자":
        admin_bread()

    elif mode == "데이터 분석":
        pass

calculate_salse()





