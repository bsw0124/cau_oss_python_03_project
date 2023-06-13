class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method
    def __str__(self): #교수님께서 미리 구현해 놓으신 것으로 절대 변경하지 말것. 
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s 

    def __init__(self,name,city,district,ptype,longitude,latitude): # 변수명
        self.__item = {
            'name': name,
            'city': city, 
            'district': district, 
            'ptype': ptype, 
            'longitude': float(longitude), 
            'latitude' : float(latitude)
            } 

    def get(self,keyword = 'name'):
        return self.__item[keyword] #keyword에 해당하는 value(리스트)를 반환 
    

def str_list_to_class_list(str_list):
    class_list = []
    
    for item in str_list:
        split_lsit = item.split(',')
        class_list.append(parking_spot(split_lsit[1],split_lsit[2],split_lsit[3],split_lsit[4],split_lsit[5],split_lsit[6]))
    
    return class_list
        


def print_spots(spots):
    list_len = len(spots)
    print(f"---print elements({list_len})---") 
    for item in spots:
        print(item.__str__())


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
#if __name__ == '__main__':
    #import file_manager
    #str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    #spots = str_list_to_class_list(str_list)
    #print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)
    
    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)