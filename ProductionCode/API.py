import argparse
import sys
import csv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILENAME = os.path.join(BASE_DIR, 'Data', 'llmenergy.csv')

data = []


def load_data():
    """Loads in data from a CSV file and stores it in `data`"""
    if len(data) == 0:
        with open(FILENAME, newline='') as datafile:
            csv_file = csv.reader(datafile)
            for row in csv_file:
                data.append(row)


def region_energy_consumption():
    """
    Analyzes energy consumption by region.
    """

    def map_energy_values_to_regions():
        """
        Maps each region to a list of energy values.
        """
        try:
            region_index = data[0].index("data_center_region")
            energy_index = data[0].index("total_energy_kwh")
        except:
            print("Error")
            return {}

        region_energy = {}

        for row in data[1:]:
            region = row[region_index].strip()

            if not region:
                continue

            energy_str = row[energy_index].strip()

            if not energy_str:
                continue

            try:
                energy = float(energy_str)
            except ValueError:
                continue

            if region not in region_energy:
                region_energy[region] = []

            region_energy[region].append(energy)

        return region_energy

    def calculate_total_energy(energy_values):
        """
        Calculates total energy for a region.
        """
        return sum(energy_values)

    def calculate_average_energy(energy_values):
        """
        Calculates average energy for a region.
        """
        return calculate_total_energy(energy_values) / len(energy_values)

    if len(data) == 0:
        load_data()

    region_energy = map_energy_values_to_regions()

    results = []

    for region, energies in region_energy.items():
        total_energy = calculate_total_energy(energies)
        average_energy = calculate_average_energy(energies)

        results.append({
            "region": region,
            "total_energies": total_energy,
            "average_energies": average_energy
        })

    results.sort(
        key=lambda x: x["total_energies"],
        reverse=True
    )

    print("Energy Consumption by Data Center Region")
    print(
        f"{'Region':<30} "
        f"{'Total Energy (kWh)':<20} "
        f"{'Average Energy (kWh)':<18}"
    )

    for result in results:
        print(
            f"{result['region']:<30} "
            f"{result['total_energies']:>18,.0f}   "
            f"{result['average_energies']:>16,.0f}"
        )


def main():
    load_data()

    parser = argparse.ArgumentParser(
        usage="Type first initial in lowercase of team member who wrote a user story to access their assigned user story",
        description="CLI API for our second deliverable"
    )

    parser.add_argument("user_story", action="store", default="n", help="access team member's user story")
    parser.add_argument("input", action="store", default="n", help="state required argument")

    args = parser.parse_args()

    if args.user_story == "m":
        region_energy_consumption()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()