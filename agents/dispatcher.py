def assign_vehicle(emergency, severity):
    if emergency == "medical" and severity > 80:
        return "🚑 ICU Ambulance"
    elif emergency == "medical":
        return "🚑 Ambulance"
    elif emergency == "fire":
        return "🚒 Fire Truck"
    else:
        return "🚓 Police Vehicle"