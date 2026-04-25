import argparse
import sys
import csv


data = []
FILENAME = "/Users/zhouyuetong/ind-flask-zhouy2-110/ProductionCode/llmenergy.csv"

def load_data():
   """Loads in data from a CSV file and stores it in `data`"""
   if len(data) == 0:
       with open(FILENAME, newline='') as datafile:
           csv_file = csv.reader(datafile)
           for row in csv_file:
               data.append(row)


def may_user_story():
    """
    Analyzes energy consumption by region.
    
    Args:
        region_column: Name of the region column (default: "data_center_region")
    """
    if len(data) == 0:
        load_data()
    try:
        region_index = data[0].index("data_center_region")
        energy_index = data[0].index("total_energy_kwh")
    except:
        print("Error")
        return
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
    results = []
    for region, energies in region_energy.items():
        total = sum(energies)
        average = total / len(energies)
        results.append({'region': region,'total_energies': total,'average_energies': average,})
    results.sort(key=lambda x: x['total_energies'], reverse=True)
    print("Energy Consumption by Data Center Region")
    print(f"{'Region':<30} {'Total Energy (kWh)':<20} {'Average Energy (kWh)':<18} ")
    for r in results:
        print(f"{r['region']:<30} {r['total_energies']:>18,.0f}   {r['average_energies']:>16,.0f}")

def main():
    load_data()

    parser = argparse.ArgumentParser(
        usage= "Type first initial in lowercase of team member who wrote a user story to access their assigned user story",
        description="CLI API for our second deliverable"
    )

    parser.add_argument("user_story", action='store', default="n", help="access team member's user story")
    parser.add_argument("input", action='store', default="n", help="state required argument")

    args = parser.parse_args()

    if args.user_story == "m":
        may_user_story()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()