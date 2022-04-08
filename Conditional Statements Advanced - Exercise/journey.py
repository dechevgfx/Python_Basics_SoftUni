budget = float(input())
season = input()
type_of_housing = ""
final_sum = 0

if budget <= 100:
    if season == "summer":
        type_of_housing = "Camp"
        final_sum = budget * 0.30
        print("Somewhere in Bulgaria")
        print(f"{type_of_housing} - {final_sum:.2f}")
    elif season == "winter":
        type_of_housing = "Hotel"
        final_sum = budget * 0.70
        print("Somewhere in Bulgaria")
        print(f"{type_of_housing} - {final_sum:.2f}")
elif budget <= 1000:
    if season == "summer":
        type_of_housing = "Camp"
        final_sum = budget * 0.40
        print("Somewhere in Balkans")
        print(f"{type_of_housing} - {final_sum:.2f}")
    elif season == "winter":
        type_of_housing = "Hotel"
        final_sum = budget * 0.80
        print("Somewhere in Balkans")
        print(f"{type_of_housing} - {final_sum:.2f}")
elif budget > 1000:
    type_of_housing = "Hotel"
    final_sum = budget * 0.90
    print("Somewhere in Europe")
    print(f"{type_of_housing} - {final_sum:.2f}")
