import json
from avl_tree import module

locations = [
    {
        "name": "신정문 주차장",
        "latitude": 36.60924342720994,
        "longitude": 127.28889446545843,
        "scooters": [
            {
                "id": "scooter001",
                "battery": 70,
                "repair": False
            }
        ]
    },
    {
        "name": "학술정보원",
        "latitude": 36.60987854046684,
        "longitude": 127.28710841905747,
        "scooters": [
            {
                "id": "scooter002",
                "battery": 50,
                "repair": False
            },
                        {
                "id": "scooter002",
                "battery": 50,
                "repair": True
            }
        ]
    },
    {
        "name": "과기2관",
        "latitude": 36.61087905080802,
        "longitude": 127.28700593927432,
        "scooters": [
            {
                "id": "scooter003",
                "battery": 30,
                "repair": True
            }
        ]
    },
    {
        "name": "ICT 융합관",
        "latitude": 36.60913903276567,
        "longitude": 127.28358476879771,
        "scooters": [
        ]
    }
]

#장소 필터링
processed_locations = []

for location in locations:
    scooters = location['scooters']
    num_scooters = len(scooters)

    # scooter 정보가 없거나 모든 scooter의 repair 값이 True인 경우 제외
    if num_scooters == 0 or all(scooter['repair'] for scooter in scooters):
        continue

    processed_locations.append(location)

locations = processed_locations

#AVL-Tree 초기화
location_avl_tree = module.LocationAVLTree()

for location in locations:
    location_avl_tree.insert(location)

#AVL-Tree에서 이름으로 Node찾기
search_result_node = location_avl_tree.search("신정문 주차장")
print("=============== found node =================")
print(f"location: {search_result_node.location}")
print(f"scooters: {search_result_node.scooters}")

#AVL-Tree를 이용해 가장 가까운 그룹 찾기
target_location = {
    "latitude": 36.60857621133895,
    "longitude": 127.28904846065954
}

nearest_location = None
min_distance = float('inf')

for location in locations:
    distance = location_avl_tree._distance(location, target_location)
    if distance < min_distance:
        min_distance = distance
        nearest_location = location

print("============ nearest location ==============")
if nearest_location == None:
    print("No available scooter found.")
print(f"The nearest location is {nearest_location['name']} with {min_distance}m")
print("============================================")

location_avl_tree.visualize()
