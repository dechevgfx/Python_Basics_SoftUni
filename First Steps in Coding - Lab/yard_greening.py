sq_m_green = float(input())
price_for_all_sq_m = 7.61 * sq_m_green
discount = price_for_all_sq_m * 0.18
total_price = price_for_all_sq_m - discount

print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")

