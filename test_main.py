from main import hitung_keliling_persegi, hitung_luas_persegi


def test_hitungluas():
    sisi = 3
    assert hitung_luas_persegi(sisi) == 9

def test_hitungkeliling():
    keliling = 2
    assert hitung_keliling_persegi(keliling) == 8