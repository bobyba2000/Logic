male(tranHap).
male(tranLy).
male(tranHoangNghi).
male(tranTuKhanh).
male(tranThua).
male(lyHueTong).
male(tranThuDo).
male(tranLieu).
male(tranThaiTong).
male(tranHungDao).
male(tranThanhTong).
male(tranQuangKhai).
male(tranNhatDuat).
male(tranBinhTrong).
male(tranQuocTang).
male(tranNhanTong).
male(tranAnhTong).

female(leThiThai).
female(tranThiDung).
female(tranThiNguyet).
female(lyThuanThien).
female(lyChieuHoang).
female(vuThiPhuong).
female(thienThanhCongChua).
female(nguyenThanhHoangHau).
female(phungDuongCongChua).
female(thuyBaoCongChua).
female(baoThanhHoangHau).
female(huyenTranCongChua).

parent(tranHap, tranLy).
parent(tranHap, tranHoangNghi).

parent(tranLy, tranTuKhanh).
parent(tranLy, tranThua).
parent(tranLy, tranThiDung).

parent(tranHoangNghi, tranThuDo).

parent(tranThua, tranLieu).
parent(tranThua, tranThaiTong).
parent(leThiThai, tranLieu).
parent(leThiThai, tranThaiTong).

parent(lyHueTong, lyThuanThien).
parent(lyHueTong, lyChieuHoang).
parent(tranThiDung, lyThuanThien).
parent(tranThiDung, lyChieuHoang).

parent(tranLieu, tranHungDao).
parent(tranLieu, nguyenThanhHoangHau).
parent(tranThiNguyet, tranHungDao).
parent(tranThiNguyet, nguyenThanhHoangHau).

parent(tranThaiTong, tranThanhTong).
parent(tranThaiTong, tranQuangKhai).
parent(tranThaiTong, tranNhatDuat).
parent(tranThaiTong, thuyBaoCongChua).
parent(lyThuanThien, tranThanhTong).
parent(lyThuanThien, tranQuangKhai).
parent(vuThiPhuong, tranNhatDuat).
parent(vuThiPhuong, thuyBaoCongChua).

parent(tranHungDao, tranQuocTang).
parent(tranHungDao, baoThanhHoangHau).
parent(thienThanhCongChua, tranQuocTang).
parent(thienThanhCongChua, baoThanhHoangHau).

parent(tranThanhTong, tranNhanTong).
parent(nguyenThanhHoangHau, tranNhanTong).

parent(tranNhanTong, huyenTranCongChua).
parent(tranNhanTong, tranAnhTong).
parent(baoThanhHoangHau, huyenTranCongChua).
parent(baoThanhHoangHau, tranAnhTong).

married(tranThua, leThiThai).
married(lyHueTong, tranThiDung).
married(tranThuDo, tranThiDung).
married(tranLieu, tranThiNguyet).
married(tranThaiTong, lyThuanThien).
married(tranThaiTong, lyChieuHoang).
married(tranThaiTong, vuThiPhuong).
married(tranHungDao, thienThanhCongChua).
married(tranThanhTong, nguyenThanhHoangHau).
married(tranQuangKhai, phungDuongCongChua).
married(tranBinhTrong, thuyBaoCongChua).
married(tranNhanTong, baoThanhHoangHau).
married(tranAnhTong, huyenTranCongChua).
