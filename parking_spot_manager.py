# 구현은 혼자 하였고, 코드도 혼자 짰는데,
# 혹시나 특정 분들과 유사도에서 겹치는 부분이 있다면, 당연히 재시험에 응하도록 하겠습니다.
class parking_spot:
    #생성자 구현
    # setter가 존재하지 않는다
    # 그래서 __item 필드의 생성/설정은 생성자를 통해서만 이루어진다.
    # 생성자의 매개변수는 아래와 같이 name, city, district, ptype, longitude, latitude 총 6가지로 구성됐다.
    def __init__(self, name, city, district, ptype, longitude, latitude):
        #item은 class변수가 아니라 객체 변수로 생성합니다.
        # 클래스 변수로 생성을 하게 되면 어떤 문제가 생길 지 모르니, 객체 마다 private dictionary 객체를 생성 하도록 합니다.
        self.__item = {}
        #'name' 'city' 'district' 'ptype' 'longitude' 'latitude'
        # 문자열  문자열   문자열     문자열       실수         실수
        #최초 input parameter는 string값이 들어옵니다.
        # 위도와 경도는 float()를 활용하여 실수로 변환해 줍니다.
        self.__item['name'] = name
        self.__item['city'] = city
        self.__item['district'] = district
        self.__item['ptype'] = ptype
        self.__item['longitude'] = float(longitude)
        self.__item['latitude'] = float(latitude)

    #get 메소드는 keyword parameter에 __item의 key값으로 사용한다
    # parameter keyword를 통해서 __item[keyword] 값을 반환하고
    # default parameter는 'name'으로 지정한다. (아무것도 입력안하면 __item['name']이 return된다)
    def get(self, keyword='name'):
        return self.__item[keyword]

    #item의 값들을 출력해주는 역할을 하는데, print(parking_spot클래스의 객체)를 하면
    # __str__의 s값이 출력됩니다.
    def __str__(self):
        item = self.__item
        s  = f"[{item['name']}({item['ptype']})] "
        s += f"{item['city']} {item['district']}"
        s += f"(lat:{item['latitude']}, long:{item['longitude']})"
        return s

# str_list_to_class_list함수
# parameter: 문자열 리스트[str_list]
# return value:  parking_spot 클래스 객체의 리스트
#parameter로 들어온 문자열 리스트를 parking_spot의 객체로 변환해주고
#그것들을 spots리스트에 담아서 return 해준다.
def str_list_to_class_list(str_list):
    spots = []
    for string in str_list:
        _, name, city, district, ptype, longitude, latitude = string.split(",")
        spots.append(parking_spot(name, city, district, ptype, longitude, latitude))

    return spots

# 1. "---print elements([리스트의 길이])---"를 출력
# 2.  리스트에 저장된 모든 객체의 값을 출력한다.
#리스트의 길이는 len함수를 사용하면 됩니다
def print_spots(spots):
    print(f"---print elements({len(spots)})---")
    for i in spots:
        print(i)


#----------------version3----------------
#spots를 입력 받고, 각각에 맞는 parameter를 포함하는 parking spot object 리스트를 return하는 함수
def filter_by_name(spots, name):
    data = [s for s in spots if name in s.get('name')]
    return data

def filter_by_city(spots, city):
    data = [s for s in spots if city in s.get('city')]
    return data

def filter_by_district(spots, district):
    data = [s for s in spots if district in s.get('district')]
    return data
def filter_by_ptype(spots, ptype):
    data = [s for s in spots if ptype in s.get('ptype')]
    return data
#float를 처리하기 위해서 map을 사용
#처음에 들어오는 값은 string이기 때문에, float로 변환해줘야한다
def filter_by_location(spots, locations):
    min_lat, max_lat, min_long, max_long = map(float, locations)
    data = [s for s in spots if (min_lat < s.get('latitude') < max_lat)
            and (min_long < s.get('longitude') < max_long)]
    return data
# 각 단계별로 테스트 (테스트할때 주석해제 후 사용)
if __name__ == '__main__':
    print("Testing the module...")
    # version#2
    import file_manager
    str_list = file_manager.read_file("./input/free_parking_spot_seoul.csv")
    spots = str_list_to_class_list(str_list)
    print_spots(spots)

    # version#3
    # spots = filter_by_district(spots, '동작')
    # print_spots(spots)

    # version#4
    # spots = sort_by_keyword(spots, 'name')
    # print_spots(spots)