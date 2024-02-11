car_info = {}
def car_data(manufacturer, model, **extra):
    car_info['manufacturer'] = manufacturer
    car_info["model"] = model
    return extra

car_data("Opel", "Corsa", gpl = "Yes")

print(car_info)
