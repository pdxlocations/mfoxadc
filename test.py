


OCV = [4190, 4050, 3990, 3890, 3800, 3720, 3630, 3530, 3420, 3300, 3100]
def show_voltage(voltage):
    for i in range(len(OCV)):
        if OCV[i] <= voltage:
            if i == 0:
                return 100.0
            else:
                return 100.0 / (len(OCV) - 1) * (len(OCV) - 1 - i + (voltage - OCV[i]) / (OCV[i - 1] - OCV[i]))
    return 0

print(show_voltage(4.2 * 1000))