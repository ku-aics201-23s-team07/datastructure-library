## AVL-Tree Libiray
- Github push date
  - 2023-05-16
- Development Team
  - Minse Kim, Hajun Myung, Park Min-chan\
- Presentation Team
  - Keunho Kim, Oh Tae-gyeom
---

### File Structure

- avl_tree
    - module.py → avl_tree main library
- .gitignore
- README.md
- requirements.txt -> python dependencies
- main.py → test code

---

### Progress

- 장소들을 AVL-Tree에 넣기전 리스트와 선형탐색을 이용해 필요없는 장소는 필터링합니다.
- AVL-Tree에 장소의 이름을 이용하여 삽입 및 정렬을 합니다.
- AVL-Tree를 이용해 정렬된 데이터를 가지고 target_location정보와 노드들의 location정보를 이용해 선형탐색후 가장 가까운 위치를 찾아냅니다.
- 장소의 이름을 이용해서 AVL-Tree내의 탐색 함수를 통해 노드를 찾아낼수 있습니다.
- 가장 가까운 장소를 구한후 장소내 scooters에서 가장 배터리가 많고 수리가필요없는 scooter를 heap구조를 이용해 구할수있습니다.

---

### Used

- AVL-Tree
- Stack
- Heap
- List