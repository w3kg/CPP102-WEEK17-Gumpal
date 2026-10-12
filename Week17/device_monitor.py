readings = [28, 31, 35, 37, 29]
humidity = [55, 60, 65, 70, 58]


def is_whole_number(text):
    """Check whether text represents a whole number."""
    if text == "":
        return False

    if text[0] == "-":
        return len(text) > 1 and text[1:].isdigit()

    return text.isdigit()


def display_menu():
    """Display the main menu."""
    print("\nGREENHOUSE CLIMATE MONITORING SYSTEM")
    print("------------------------------------")
    print("[1] View Readings")
    print("[2] Add Reading")
    print("[3] Classify Readings")
    print("[4] Generate Summary")
    print("[5] Exit")


def display_readings(temperatures, humidities):
    """Display all temperature and humidity readings."""
    print("\nGREENHOUSE READINGS")
    print("-------------------")

    for i in range(len(temperatures)):
        print(
            "Reading", i + 1,
            ":", temperatures[i], "°C |",
            "Humidity:", humidities[i], "%"
        )


def add_reading(temperatures, humidities):
    """Add a temperature and humidity reading if both are valid."""
    temperature_text = input("Enter temperature in °C: ")

    if len(temperature_text) == 0:
        print("Invalid input. The reading cannot be empty.")
        return

    if not is_whole_number(temperature_text):
        print("Invalid input. Enter a whole number only.")
        return

    temperature = int(temperature_text)

    if temperature < 0 or temperature > 100:
        print("Invalid temperature. Enter a value from 0 to 100.")
        return

    humidity_text = input("Enter relative humidity (0-100%): ")

    if len(humidity_text) == 0:
        print("Invalid humidity input. The reading cannot be empty.")
        return

    if not is_whole_number(humidity_text):
        print("Invalid humidity input. Enter a whole number only.")
        return

    humidity_value = int(humidity_text)

    if humidity_value < 0 or humidity_value > 100:
        print("Invalid humidity. Enter a value from 0 to 100.")
        return

    temperatures.append(temperature)
    humidities.append(humidity_value)

    print("Reading added successfully.")


def classify_temperature(temperature):
    """Return the temperature classification."""
    if temperature < 30:
        return "NORMAL"
    elif temperature <= 35:
        return "WARNING"
    else:
        return "CRITICAL"


def classify_humidity(humidity_value):
    """Classify humidity using this project's example target range."""
    if humidity_value < 40:
        return "LOW"
    elif humidity_value <= 70:
        return "WITHIN TARGET"
    else:
        return "HIGH"


def classify_readings(temperatures, humidities):
    """Display the classifications for both measurements."""
    print("\nCLIMATE CLASSIFICATION")
    print("----------------------")

    for i in range(len(temperatures)):
        temperature_status = classify_temperature(temperatures[i])
        humidity_status = classify_humidity(humidities[i])

        print(
            "Reading", i + 1, ":",
            temperatures[i], "°C ->", temperature_status,
            "|", humidities[i], "% humidity ->", humidity_status
        )


def compute_total(values):
    """Calculate the total using a loop."""
    total = 0

    for value in values:
        total += value

    return total


def compute_average(values):
    """Calculate the average of the values."""
    if len(values) == 0:
        return 0

    return compute_total(values) / len(values)


def find_minimum(values):
    """Find the smallest value using a loop."""
    minimum = values[0]

    for value in values:
        if value < minimum:
            minimum = value

    return minimum


def find_maximum(values):
    """Find the largest value using a loop."""
    maximum = values[0]

    for value in values:
        if value > maximum:
            maximum = value

    return maximum


def count_category(temperatures, category):
    """Count temperatures belonging to a classification."""
    count = 0

    for temperature in temperatures:
        if classify_temperature(temperature) == category:
            count += 1

    return count


def determine_overall_status(warning_count, critical_count):
    """Determine the overall temperature monitoring status."""
    if critical_count >= 1:
        return "ATTENTION REQUIRED"
    elif warning_count >= 1:
        return "MONITOR"
    else:
        return "NORMAL"


def display_summary(temperatures, humidities):
    """Display temperature statistics and humidity statistics."""
    total_readings = len(temperatures)

    normal_count = count_category(temperatures, "NORMAL")
    warning_count = count_category(temperatures, "WARNING")
    critical_count = count_category(temperatures, "CRITICAL")

    print("\nTEMPERATURE SUMMARY")
    print("-------------------")
    print("Number of readings :", total_readings)
    print("Total of readings  :", compute_total(temperatures))
    print("Average temperature: {:.2f} °C".format(
        compute_average(temperatures)
    ))
    print("Minimum temperature:", find_minimum(temperatures), "°C")
    print("Maximum temperature:", find_maximum(temperatures), "°C")

    print("\nNORMAL   : {} ({:.2f}%)".format(
        normal_count, normal_count / total_readings * 100
    ))
    print("WARNING  : {} ({:.2f}%)".format(
        warning_count, warning_count / total_readings * 100
    ))
    print("CRITICAL : {} ({:.2f}%)".format(
        critical_count, critical_count / total_readings * 100
    ))

    print("\nOverall Status:",
          determine_overall_status(warning_count, critical_count))

    print("\nHUMIDITY SUMMARY")
    print("----------------")
    print("Average humidity: {:.2f}%".format(
        compute_average(humidities)
    ))
    print("Minimum humidity:", find_minimum(humidities), "%")
    print("Maximum humidity:", find_maximum(humidities), "%")


def main():
    """Run the greenhouse climate monitoring menu."""
    temperatures = readings
    humidities = humidity

    while True:
        display_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            display_readings(temperatures, humidities)

        elif choice == "2":
            add_reading(temperatures, humidities)

        elif choice == "3":
            classify_readings(temperatures, humidities)

        elif choice == "4":
            display_summary(temperatures, humidities)

        elif choice == "5":
            print("Thank you for using the Greenhouse Climate Monitoring System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()