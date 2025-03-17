#
#
#
#
#
#
#
#

def order_bread():
    print("주문 완료")

def admin_mode():
    print("관리자 모드")


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

