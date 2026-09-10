def process_revenue_report(order_list):
    total_revenue = 0
    successful_orders_count = 0

    for order in order_list:
        # Lọc bỏ đơn bom/hủy/hoàn và các khoản phí âm/0đ (Bẫy dữ liệu)
        if order.get("status") == "DELIVERED" and order.get("fee", 0) > 0:
            total_revenue += order["fee"]
            successful_orders_count += 1

    # Tính doanh thu trung bình trên mỗi đơn thành công (Tránh lỗi chia cho 0)
    if successful_orders_count > 0:
        average_revenue_per_order = total_revenue / successful_orders_count
    else:
        average_revenue_per_order = 0.0

    # In báo cáo tổng hợp cho Giám đốc
    print("=== BÁO CÁO DOANH THU ĐIỀU HÀNH (ĐÃ XỬ LÝ) ===")
    print(f"1. Tổng doanh thu thực tế: {total_revenue:,.0f}đ")
    print(f"2. Số đơn giao thành công: {successful_orders_count} đơn")
    print(
        f"3. Doanh thu TB/đơn thành công: {average_revenue_per_order:,.0f}đ/đơn")


# Dữ liệu thử nghiệm từ máy chủ (có chứa bẫy đơn hủy/hoàn)
order_data = [
    {"order_id": "01", "fee": 15000, "status": "DELIVERED"},
    {"order_id": "02", "fee": 20000, "status": "DELIVERED"},
    {"order_id": "03", "fee": 0, "status": "CANCELLED"},      # Bị loại bỏ bởi bộ lọc
    {"order_id": "04", "fee": -5000, "status": "RETURNED"},   # Bị loại bỏ bởi bộ lọc
    {"order_id": "05", "fee": 25000, "status": "DELIVERED"}
]

# Thực thi chương trình
process_revenue_report(order_data)
