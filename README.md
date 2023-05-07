## AVL-Tree Libiray
- Github push date
  - 2023-05-07 (PM 10)
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
- test.py → test code for avl_tree

---

### Progress

- AVL-Tree에 장소의 이름을 이용하여 삽입 및 정렬을 합니다.
- AVL-Tree를 이용해 정렬된 데이터를 가지고 target_location정보와 노드들의 location정보를 이용해 선형탐색후 가장 가까운 위치를 찾아냅니다.
- 장소의 이름을 이용해서 AVL-Tree내의 탐색 함수를 통해 노드를 찾아낼수 있습니다.
- 데이터셋을 test.py내에서 AVL-Tree에 삽입전 장소 필터링을 하는데 이것을 AVL-Tree내의 insert함수에 내장시킬지 고민중입니다.
- AVL-Tree내의 visualize함수를 이용해 digraph로 변환하여 [사이트](http://magjac.com/graphviz-visual-editor/)에서 시각화 할수있습니다.
