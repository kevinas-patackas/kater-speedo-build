mapping = {
    "min": {
        "reading": 0,
        "value": 0,
    },
    "max": {
        "reading": 1000,
        "value": 100,
    },
    "ranges": [
        {
            "reading": 200,
            "value": 50,
        },
        {
            "reading": 400,
            "value": 90,
        },
        {
            "reading": 300,
            "value": 70
        }
    ]
}

mapping_sorted = {
    **mapping,
    "ranges": sorted(mapping["ranges"], key=lambda x: x["reading"]),
}


def find_value_by_range(reading):
    upper_range_index = -1
    for i in range(len(mapping_sorted["ranges"])):
        if mapping_sorted["ranges"][i]["reading"] > reading:
            upper_range_index = i
            break

    if upper_range_index == -1:
        upper_range = mapping_sorted["max"]
        lower_range = mapping_sorted["ranges"][-1] if len(
            mapping_sorted["ranges"]) > 0 else mapping_sorted["min"]
    else:
        upper_range = mapping_sorted["ranges"][upper_range_index]
        lower_range = mapping_sorted["ranges"][upper_range_index -
                                               1] if upper_range_index > 0 else mapping_sorted["min"]

    value = (reading - lower_range["reading"]) / (upper_range["reading"] - lower_range["reading"]) * (
        upper_range["value"] - lower_range["value"]) + lower_range["value"]

    return round(value)


print(find_value_by_range(-100))
print(find_value_by_range(0))
print(find_value_by_range(100))
print(find_value_by_range(250))
print(find_value_by_range(350))
print(find_value_by_range(400))
print(find_value_by_range(450))
print(find_value_by_range(600))
print(find_value_by_range(1000))
print(find_value_by_range(1100))


# -25
# 0
# 25
# 60
# 80
# 90
# 84
# 65
