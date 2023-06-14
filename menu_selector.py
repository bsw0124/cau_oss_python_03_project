import file_manager
import parking_spot_manager

def start_process(path):
    str_list = file_manager.read_file(path)
    spots = parking_spot_manager.str_list_to_class_list(str_list)
    while True:
        print("---menu---")
        print("[1] print")
        print("[2] filter")
        print("[3] sort")
        print("[4] exit")
        #str_list = file_manager.read_file(path)
        #spots = parking_spot_manager.str_list_to_class_list(str_list)
        select = int(input('type:'))
        if select == 1:
            parking_spot_manager.print_spots(spots)
            # fill this block
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
                spots = parking_spot_manager.filter_by_name(spots, keyword)
                continue #데이터 필터링후 출력하지 않고 바로 다시 메뉴 셀렉터로 올리기
                # fill this block
            elif select == 2:
                keyword = input('type city:')
                spots = parking_spot_manager.filter_by_city(spots, keyword)
                continue #데이터 필터링후 출력하지 않고 바로 다시 메뉴 셀렉터로 올리기
                # fill this block
            elif select == 3:
                keyword = input('type district:')
                spots = parking_spot_manager.filter_by_district(spots, keyword)
                continue #데이터 필터링후 출력하지 않고 바로 다시 메뉴 셀렉터로 올리기
                # fill this block
            elif select == 4:
                keyword = input('type ptype:')
                spots = parking_spot_manager.filter_by_ptype(spots, keyword)
                continue #데이터 필터링후 출력하지 않고 바로 다시 메뉴 셀렉터로 올리기
                # fill this block
            elif select == 5:
                min_lat = float(input('type min lat:'))
                max_lat = float(input('type max lat:'))
                min_lon = float(input('type min long:'))
                max_lon = float(input('type max long:'))
                spots = parking_spot_manager.filter_by_location(spots,(min_lat,max_lat,min_lon,max_lon))
                continue #데이터 필터링후 출력하지 않고 바로 다시 메뉴 셀렉터로 올리기
                
                
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
            print("Exit")
            break;
            # fill this block
        else:
            print("invalid input")