class parking_spot:
    # you have to implement 'constructor(생성자)' and 'get' method
    def __str__(self): # 변경금지 
        item = self.__item 
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s 

    def __init__(self,name,city,district,ptype,longitude,latitude): # 객체를 만들기 위한 생성자
        self.__item = {
            'name': name,
            'city': city, 
            'district': district, 
            'ptype': ptype, 
            'longitude': float(longitude), 
            'latitude' : float(latitude)
            } 

    def get(self,keyword = 'name'):
        return self.__item[keyword] #keyword에 해당하는 value를 반환 

def str_list_to_class_list(str_list): #받아온 str_list를 클래스 리스트로 변환 하기 위한 함수
    class_list = [] # 객체 append를 위해서 먼저 빈 리스트 선언
    
    for item in str_list: 
        split_lsit = item.split(',') 
        class_list.append(parking_spot(split_lsit[1],split_lsit[2],split_lsit[3],split_lsit[4],split_lsit[5],split_lsit[6])) #객체생성후 append
    return class_list
        
def print_spots(spots): #주차장을 print 하기 위한 함수
    list_len = len(spots) 
    print(f"---print elements({list_len})---") 
    for item in spots:
        print(item.__str__()) 

def filter_by_name(spots, name):
    filter_by_name_list = [ item for item in spots if name in item.get('name')] #get 함수를 이용해서 spots객체리스트의 객체에 접근후 데이터 핕터링
    return filter_by_name_list

def filter_by_city(spots, city):
    filter_by_city_list = [ item for item in spots if city in item.get('city')] #get 함수를 이용해서 spots객체리스트의 객체에 접근후 데이터 핕터링
    return filter_by_city_list

def filter_by_district(spots, district):
    filter_by_district_list = [ item for item in spots if district in item.get('district')] #get 함수를 이용해서 spots객체리스트의 객체에 접근후 데이터 핕터링
    return filter_by_district_list

def filter_by_ptype(spots, ptype):
    filter_by_ptype_list = [ item for item in spots if ptype in item.get('ptype')] #get 함수를 이용해서 spots객체리스트의 객체에 접근후 데이터 핕터링
    return filter_by_ptype_list

def filter_by_location(spots, locations): #index로 locations튜플에 접근후 데이터 필터링
    filter_by_location_list  =  [
                                item for item in spots
                                if  item.get('latitude')  > locations[0]
                                and item.get('latitude')  < locations[1]
                                and item.get('longitude') > locations[2]
                                and item.get('longitude') < locations[3]
                                ]
    return filter_by_location_list 

def sort_by_keyword(spots,keyword): #내장함수인 sorted함수를 통해서 객체리스트의 객체들의 __item 의 key값에 맞는 value들을 참고해 객체 정렬
    sorted_by_keyword_list = sorted(spots,key = lambda x:x.get(keyword)) 
    return sorted_by_keyword_list


# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
#if __name__ == '__main__':
    #import file_manager
    #str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    #spots = str_list_to_class_list(str_list)
    #print_spots(spots)

    #version#3
    #spots = filter_by_district(spots, '동작')
    #print_spots(spots)
    
    #version#4
    #spots = sort_by_keyword(spots, 'name')
    #print_spots(spots)