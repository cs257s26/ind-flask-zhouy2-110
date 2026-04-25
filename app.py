from flask import Flask
from ProductionCode.API import load_data, may_user_story
import sys
from io import StringIO


app = Flask(__name__)
load_data()

@app.route('/api/energy_by_region')
def energy_by_region():
    """Call may_user_story function"""
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    may_user_story()
    
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    
    return f"<pre>{output}</pre>"

@app.route('/api/region/<region_name>')
def region_data(region_name):
    """Get specific region"""
    from ProductionCode.API import data
    header = data[0]
    region_index = header.index("data_center_region")
    energy_index = header.index("total_energy_kwh")
    model_index = header.index("Model name")
    total = 0
    model = []
    for row in data[1:]:
        if len(row) <= max(region_index, energy_index, model_index):
            continue
        if row[region_index] != region_name:
            continue
        
        model_name = row[model_index] if row[model_index] else ""
        energy_str = row[energy_index] if row[energy_index] else ""

        if energy_str and energy_str not in ["Not disclosed", "Not specified"]:
            try:
                energy = float(energy_str)
                total += energy
                model.append(f"{model_name}: {energy:,.0f} kWh")
            except:
                model.append(f"{model_name}: error")
        else:
            model.append(f"{model_name}: no data")
    
    output = f"Region: {region_name}\nTotal: {total:,.0f} kWh\nModels:\n"
    for m in model:
        output += f"  {m}\n"
    
    return f"<pre>{output}</pre>"

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    app.run(host='0.0.0.0', port=port)