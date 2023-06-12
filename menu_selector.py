import file_manager
import parking_spot_manager
# file_manager 모듈을 import한 이유는 read_file을 시용하기 위해서 import
# parking_spot_manager는 구현 사항(version2, 3, 4)을 실행하기 위해서 모듈을 import
def start_process(path):
    str_list = file_manager.read_file(path)
    spots = parking_spot_manager.str_list_to_class_list(str_list)
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        select = int(input('type:'))
        if select == 1:
            # version2: menu의 1번을 구현
            # 1번 옵션을 선택하였을 경우 parking_spot_manager 모듈의 print_spots 함수를 호출한다.
            parking_spot_manager.print_spots(spots)

        elif select == 2:
            print("---filter by---")
            print("[1] name")
            print("[2] city")
            print("[3] district")
            print("[4] ptype")
            print("[5] location")
            select = int(input('type:'))
            if select == 1:
                keyword = input('type name:')
                print("not implemented yet")
                # fill this block
            elif select == 2:
                keyword = input('type city:')
                print("not implemented yet")
                # fill this block
            elif select == 3:
                keyword = input('type district:')
                print("not implemented yet")
                # fill this block
            elif select == 4:
                keyword = input('type ptype:')
                print("not implemented yet")
                # fill this block
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                print("not implemented yet")
                # fill this block
            else:
                print("invalid input")
        elif select == 3:
            keywords = ['name', 'city', 'district', 'ptype', 'latitude', 'longitude']
            print("---sort by---")
            print(keywords)
            keyword = input('type keyword:')
            if keyword in keywords:
                print("not implemented yet")
                # fill this block
            else: print("invalid input")
        elif select == 4:
            # version2: 4번을 선택
            # "Exit"을 출력하고 반복을 종료한다.
            # 4번이 선택되면 break를 실행하여 while loop가 종료되게 됩니다.
            print("Exit")
            break

        else:
            print("invalid input")