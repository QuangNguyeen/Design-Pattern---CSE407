class BenhNhan:
    def __init__(self, ten):
        self.ten = ten
        self.danh_sach_bac_si = []

    def them_bac_si(self, bac_si):
        if bac_si not in self.danh_sach_bac_si:
            self.danh_sach_bac_si.append(bac_si)
            bac_si.them_benh_nhan(self)

    def hien_thi_danh_sach_bac_si(self):
        if self.danh_sach_bac_si:
            print(f"Benh nhan {self.ten} duoc dieu tri boi cac bac si: ")
            for bac_si in self.danh_sach_bac_si:
                print(bac_si.ten)
        else:
            print("Benh nhan chua duoc cac bac si dieu tri")


class BacSi:
    def __init__(self, ten):
        self.ten = ten
        self.danh_sach_benh_nhan = []

    def them_benh_nhan(self, benh_nhan):
        if benh_nhan not in self.danh_sach_benh_nhan:
            self.danh_sach_benh_nhan.append(benh_nhan)
            benh_nhan.them_bac_si(self)

    def hien_thi_danh_sach_benh_nhan(self):
        if self.danh_sach_benh_nhan:
            print(f"Bac si {self.ten} dang phu trach cac benh nhan: ")
            for benh_nhan in self.danh_sach_benh_nhan:
                print(benh_nhan.ten)
        else:
            print("Bac si chua dang phu trach benh nhan nao")


# Minh hoa
bac_si_1 = BacSi("Lan")
bac_si_2 = BacSi("Huan")

benh_nhan_1 = BenhNhan("Quang")
benh_nhan_2 = BenhNhan("Kien")
benh_nhan_3 = BenhNhan("Tuan")

bac_si_1.them_benh_nhan(benh_nhan_1)
bac_si_1.them_benh_nhan(benh_nhan_2)
bac_si_2.them_benh_nhan(benh_nhan_3)

bac_si_1.hien_thi_danh_sach_benh_nhan()
bac_si_2.hien_thi_danh_sach_benh_nhan()
