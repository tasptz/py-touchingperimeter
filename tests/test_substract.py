from touchingperimeter import Rect

def test_tl_inside():
    assert sorted(Rect(2, 5, 12, 8).substracted(Rect(7, 6, 12, 8))) == [
        Rect(2, 5, 12, 1),
        Rect(2, 5, 5, 8),
    ]

def test_tr_inside():
    assert sorted(Rect(5, 7, 13, 8).substracted(Rect(3, 9, 6, 18))) == [
        Rect(5, 7, 13, 2),
        Rect(9, 7, 9, 8),
    ]
    
def test_bl_inside():
    assert sorted(Rect(7, 11, 13, 7).substracted(Rect(13, 3, 18, 12))) == [
        Rect(7, 15, 13, 3),
        Rect(7, 11, 6, 7),
    ]

def test_br_inside():
    assert sorted(Rect(9, 11, 18, 5).substracted(Rect(1, 5, 18, 8))) == [
        Rect(19, 11, 8, 5),
        Rect(9, 13, 18, 3),
    ]

def test_tl_tr_inside():
    assert sorted(Rect(1, 3, 14, 15).substracted(Rect(5, 7, 5, 30))) == [
        Rect(1, 3, 14, 4),
        Rect(1, 3, 4, 15),
        Rect(10, 3, 5, 15),
    ]

def test_tl_bl_inside():
    assert sorted(Rect(7, 3, 5, 4).substracted(Rect(8, 5, 10, 1))) == [
        Rect(7, 3, 1, 4),
        Rect(7, 6, 5, 1),
        Rect(7, 3, 5, 2),
    ]

def test_tr_br_inside():
    assert sorted(Rect(0, 0, 13, 15).substracted(Rect(-7, 9, 12, 3))) == [
        Rect(0, 12, 13, 3),
        Rect(0, 0, 13, 9),
        Rect(5, 0, 8, 15),
    ]

def test_bl_br_inside():
    assert sorted(Rect(5, 3, 8, 7).substracted(Rect(7, 1, 3, 5))) == [
        Rect(5, 3, 2, 7),
        Rect(10, 3, 3, 7),
        Rect(5, 6, 8, 4),
    ]

def test_overlap_right():
    assert Rect(5, 3, 8, 7).substracted(Rect(10, 1, 13, 25)) == [
        Rect(5, 3, 5, 7),
    ]

def test_overlap_top():
    assert Rect(5, 3, 8, 7).substracted(Rect(1, 7, 13, 25)) == [
        Rect(5, 3, 8, 4),
    ]

def test_overlap_left():
    assert Rect(5, 3, 8, 7).substracted(Rect(1, 1, 8, 25)) == [
        Rect(9, 3, 4, 7),
    ]

def test_overlap_bottom():
    assert Rect(5, 3, 8, 7).substracted(Rect(1, 1, 30, 4)) == [
        Rect(5, 5, 8, 5),
    ]

def test_exact_overlap():
    assert Rect(5, 3, 8, 7).substracted(Rect(5, 3, 8, 7)) == []