# ============================================
# CHƯƠNG TRÌNH QUẢN LÝ CỬA HÀNG SÁCH NHỎ
# Tác giả: [trần văn hùng]
# Ngôn ngữ: Python 3
# ============================================
# ----------------------------
# 1. KHỞI TẠO DỮ LIỆU
# ----------------------------
# Danh sách các cuốn sách trong cửa hàng (List of Dictionaries)
books = [
    {"ten": "Dế Mèn Phiêu Lưu Ký", "gia": 45000.0, "ton_kho": 15, "ban": 12},
    {"ten": "Tuổi Trẻ Đáng Giá Bao Nhiêu", "gia": 89000.0, "ton_kho": 5, "ban": 8},
    {"ten": "Đắc Nhân Tâm", "gia": 120000.0, "ton_kho": 20, "ban": 25},
    {"ten": "Nhà Giả Kim", "gia": 99000.0, "ton_kho": 2, "ban": 3},
    {"ten": "Harry Potter", "gia": 150000.0, "ton_kho": 10, "ban": 30}
]
# Thông tin khách hàng
khach_hang_ten = "An"
khach_hang_loai = "VIP"  # "thường" hoặc "VIP"
# ----------------------------
# 2. HÀM KIỂM TRA TỒN KHO
# ----------------------------
def check_stock(ten_sach, so_luong_mua):
    """
    Kiểm tra xem sách còn hàng hay không.
    Đồng thời phân loại theo mức giá.
    """
    for sach in books:
        if sach["ten"].lower() == ten_sach.lower():
            # Kiểm tra tồn kho
            if sach["ton_kho"] >= so_luong_mua:
                print(f" Sách '{ten_sach}' còn hàng ({sach['ton_kho']} quyển tồn).")
                stock_status = True
            else:
                print(f" Sách '{ten_sach}' hết hàng hoặc không đủ số lượng.")
                stock_status = False

            # Phân loại sách theo giá
            gia = sach["gia"]
            match gia:
                case gia if gia < 50000:
                    loai = "Sách giá rẻ"
                case gia if 50000 <= gia <= 100000:
                    loai = "Sách trung bình"
                case _:
                    loai = "Sách cao cấp"

            print(f"📘 Phân loại: {loai}\n")
            return stock_status, loai

    print("️ Không tìm thấy tên sách trong cửa hàng.\n")
    return False, None


# ----------------------------
# 3. HÀM TÍNH TOÁN HÓA ĐƠN
# ----------------------------
def calculate_bill(ten_sach, so_luong_mua, loai_khach):
    """
    Tính tổng tiền hóa đơn.
    Giảm 10% cho khách hàng VIP.
    """
    # Kiểm tra đầu vào
    if not isinstance(so_luong_mua, int) or so_luong_mua <= 0:
        print("⚠️ Số lượng mua phải là số nguyên dương.\n")
        return 0.0

    for sach in books:
        if sach["ten"].lower() == ten_sach.lower():
            if sach["ton_kho"] == 0:
                print(" Sách đã hết hàng.\n")
                return 0.0

            tong_tien = sach["gia"] * so_luong_mua

            # Giảm giá cho khách VIP
            if loai_khach.lower() == "vip":
                tong_tien *= 0.9  # giảm 10%

            print(f"💰 Tổng tiền cho {so_luong_mua} quyển '{ten_sach}': {tong_tien:,.0f} VNĐ\n")
            return tong_tien

    print(" Không tìm thấy sách trong danh sách.\n")
    return 0.0


# ----------------------------
# 4. LAMBDA TẠO MÃ GIẢM GIÁ
# ----------------------------
create_discount_code = lambda name, loai: name.upper() + ("_VIP" if loai.lower() == "vip" else "_REG")


# ----------------------------
# 5. THỐNG KÊ SÁCH BÁN CHẠY
# ----------------------------
def best_sellers():
    """
    In ra danh sách sách bán chạy (trên 10 quyển)
    và tìm cuốn bán chạy nhất bằng while loop.
    """
    print("Danh sách sách bán chạy (trên 10 quyển):")
    for sach in books:
        if sach["ban"] > 10:
            print(f"- {sach['ten']} ({sach['ban']} quyển đã bán)")

    # Tìm sách bán chạy nhất
    i = 0
    max_ban = 0
    best_book = None

    while i < len(books):
        if books[i]["ban"] > max_ban:
            max_ban = books[i]["ban"]
            best_book = books[i]
        i += 1

    print(f"\n Sách bán chạy nhất: '{best_book['ten']}' với {best_book['ban']} quyển đã bán.\n")


# ----------------------------
# 6. HÀM MAIN CHÍNH
# ----------------------------
def main():
    print("=========== CHƯƠNG TRÌNH QUẢN LÝ CỬA HÀNG SÁCH ===========\n")

    # Kiểm tra tồn kho
    check_stock("Harry Potter", 3)

    # Tính hóa đơn
    calculate_bill("Đắc Nhân Tâm", 2, khach_hang_loai)

    # Tạo mã giảm giá
    discount_code = create_discount_code(khach_hang_ten, khach_hang_loai)
    print(f" Mã giảm giá của khách hàng: {discount_code}\n")

    # Thống kê bán chạy
    best_sellers()


# ----------------------------
# 7. CHẠY CHƯƠNG TRÌNH
# ----------------------------
if __name__ == "__main__":
    main()
