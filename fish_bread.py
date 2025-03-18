#
#
#
#
# stock(변수/딕셔너리) : 팥붕어빵 10개, 슈크림붕어빵 8개, 초코붕어빵 5개
stock = {
    "팥붕어빵" : 10,
    "슈크림붕어빵" : 8,
    "초코붕어빵" : 5
}

sales = {
    "팥붕어빵": 0,
    "슈크림붕어빵": 0,
    "초코붕어빵": 0
}

prices = {
    "팥붕어빵": 1000,
    "슈크림붕어빵": 1200,
    "초코붕어빵": 1500,
}

# 주문 기능
def order_bread():
    while True:
        bread_type = input("주문할 붕어빵을 선택하세요. (팥붕어빵, 슈크림붕어빵, 초코붕어빵) 또는 '뒤로가기' 입력: ")
        if bread_type == "뒤로가기":
            break
    
        # 메뉴 주문
        if bread_type in stock:
            bread_count = int(input("주문할 개수를 입력하세요.: "))
            if stock[bread_type] >= bread_count > 0:
                stock[bread_type] -= bread_count # 업데이트 된 재고 : 현재재고 - 주문 개수
                sales[bread_type] += bread_count # 현재 판매한 총 개수 : 현재판매한개수 - 판매 개수 
                print(f"{bread_type}을 {bread_count}개 판매했습니다.")
            else:
                print(f"재고가 부족합니다. 현재 {stock[bread_type]}개만 주문 가능합니다.")
        else:
            print(f"팥붕어빵, 슈크림붕어빵, 초코붕어빵 중 하나의 맛을 선택해주세요.")
         
# 관리자 모드
def admin_mode():
    while True:
        bread_type = input("재고를 추가할 붕어빵을 선택하세요. (팥붕어빵, 슈크림붕어빵, 초코붕어빵) 또는 '종료' 입력 : ")
        if bread_type == "종료":
            break
        if bread_type in stock:
            bread_count = int(input("재고를 추가할 개수를 입력하세요. : "))
            stock[bread_type] += bread_count # stock[bread_type] =  stock[bread_type] + bread_count
            print(f"{bread_type}의 재고가 {bread_count}개 추가되어 현재 {stock[bread_type]}개 입니다.")
        else :
            print("재고를 추가할 올바른 메뉴를 입력하세요.")

# 메인 기능 선택
while True:
    mode = input("원하는 모드를 선택하세요 (주문, 관리자, 종료) : ")
    if mode == "종료":
        break

    elif mode == "주문":
        order_bread()

    elif mode == "관리자":
        admin_mode()

    elif mode == "데이터 분석":
        pass

