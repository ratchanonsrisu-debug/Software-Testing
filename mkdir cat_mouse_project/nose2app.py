def cat_and_mouse(x, y, z):
    dist_a = abs(z - x)  # ระยะห่างแมว A กับหนู C
    dist_b = abs(z - y)  # ระยะห่างแมว B กับหนู C

    if dist_a < dist_b:
        return "Cat A"
    elif dist_b < dist_a:
        return "Cat B"
    else:
        return "Mouse C"