from flask import Flask
from ProductionCode.API import load_data, may_user_story
import sys
from io import StringIO


app = Flask(__name__)
load_data()


def calculate_region_energy(data, region_name, region_idx, energy_idx, model_idx):
    """
    Calculate total energy consumption and collect model data for a specific region.
    
    Args:
        data: List of data rows from CSV
        region_name: Name of the region to filter
        region_idx: Column index for region names
        energy_idx: Column index for energy values
        model_idx: Column index for model names
    
    Returns:
        tuple: (total_energy, list_of_model_strings)
    """
    total = 0
    models = []
    
    for row in data[1:]:  # Skip header row
        # Skip rows that are too short
        if len(row) <= max(region_idx, energy_idx, model_idx):
            continue
        
        # Filter by region
        if row[region_idx] != region_name:
            continue
        
        # Extract model name
        model_name = row[model_idx] if row[model_idx] else ""
        
        # Parse energy value
        energy_str = row[energy_idx] if row[energy_idx] else ""
        
        if energy_str and energy_str not in ["Not disclosed", "Not specified"]:
            try:
                energy = float(energy_str)
                total += energy
                models.append(f"{model_name}: {energy:,.0f} kWh")
            except ValueError:  # Specific exception instead of bare except
                models.append(f"{model_name}: error")
        else:
            models.append(f"{model_name}: no data")
    
    return total, models


def format_region_output(region_name, total, models):
    """
    Format region energy data into readable string output.
    
    Args:
        region_name: Name of the region
        total: Total energy consumption
        models: List of model strings
    
    Returns:
        Formatted string with region summary
    """
    output = f"Region: {region_name}\nTotal: {total:,.0f} kWh\nModels:\n"
    for m in models:
        output += f"  {m}\n"
    return output


@app.route('/api/energy_by_region')
def energy_by_region():
    """
    API endpoint that returns energy analysis data.
    
    Captures and returns the console output from the may_user_story()
    function, displaying it in an HTML preformatted block.
    """
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        may_user_story()
        output = sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout
    
    return f"<pre>{output}</pre>"


@app.route('/api/region/<region_name>')
def region_data(region_name):
    """
    API endpoint that returns detailed energy consumption data for a specific region.
    
    Retrieves data from the loaded dataset, filters by the requested region name,
    calculates total energy usage, and formats the results with individual model details.
    
    Args:
        region_name: Name of the data center region to query (e.g., "us-east", "eu-west")
    
    Returns:
        HTML response with preformatted text containing region energy summary
    """
    from ProductionCode.API import data
    
    # Find column indices
    header = data[0]
    region_index = header.index("data_center_region")
    energy_index = header.index("total_energy_kwh")
    model_index = header.index("Model name")
    
    # Calculate and format results
    total, models = calculate_region_energy(
        data, region_name, region_index, energy_index, model_index
    )
    output = format_region_output(region_name, total, models)
    
    return f"<pre>{output}</pre>"


if __name__ == '__main__':
    app.run()