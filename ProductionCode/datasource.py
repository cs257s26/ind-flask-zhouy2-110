import csv
import os

# Get the CSV file path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(BASE_DIR, 'Data', 'llmenergy.csv')

def load_csv_data():
    """Load data from CSV file"""
    data = []
    with open(CSV_PATH, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)
    return data

def get_energy_by_region():
    """Total energy consumption grouped by data center region.
    
    Returns:
        list - a list of (region, total_energy_kwh) tuples, or None if the query fails.
    """
    try:
        data = load_csv_data()
        header = data[0]
        
        # Find column indices
        region_idx = header.index("data_center_region")
        energy_idx = header.index("total_energy_kwh")
        
        region_energy = {}
        
        for row in data[1:]:  # Skip header
            region = row[region_idx] if region_idx < len(row) else ""
            energy_str = row[energy_idx] if energy_idx < len(row) else ""
            
            # Skip invalid data
            if not region or not energy_str:
                continue
            if energy_str in ["Not disclosed", "Not specified", ""]:
                continue
                
            try:
                energy = float(energy_str)
                if region not in region_energy:
                    region_energy[region] = 0
                region_energy[region] += energy
            except ValueError:
                continue
        
        # Sort by total energy descending
        results = sorted(region_energy.items(), key=lambda x: x[1], reverse=True)
        return results
    except Exception as e:
        print("Query error: ", e)
        return None

def get_top_models_by_parameters():
    """Retrieves the top 5 models with the largest parameter counts.
    
    Returns:
        list - a list of (model_name, model_parameters_billion) tuples, or None if the query fails.
    """
    try:
        data = load_csv_data()
        header = data[0]
        
        # Find column indices
        model_idx = header.index("Model name")
        param_idx = header.index("model_parameters_billion")
        
        models = []
        
        for row in data[1:]:  # Skip header
            model_name = row[model_idx] if model_idx < len(row) else ""
            param_str = row[param_idx] if param_idx < len(row) else ""
            
            # Skip invalid data
            if not model_name or not param_str:
                continue
            if param_str in ["Not disclosed", "Not specified", ""]:
                continue
                
            try:
                params = float(param_str)
                models.append((model_name, params))
            except ValueError:
                continue
        
        # Sort by parameters descending and get top 5
        models.sort(key=lambda x: x[1], reverse=True)
        return models[:5]
    except Exception as e:
        print("Something went wrong when executing the query: ", e)
        return None

def main():
    results1 = get_energy_by_region()
    if results1 is not None:
        print("Energy consumption by region: ")
        for region, total in results1:
            print(f"{region}: {total:,.0f} kWh")
    
    results2 = get_top_models_by_parameters()
    if results2 is not None:
        print("\nTop 5 models by parameter count: ")
        for model, params in results2:
            print(f"{model}: {params}B")

if __name__ == "__main__":
    main()