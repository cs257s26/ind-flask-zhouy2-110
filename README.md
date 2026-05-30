1. Database Design Decisions
I chose one table because each row represents a unique LLM model, and there is no repeating data. The dataset contains 27 LLM models with  model name, parameter count, GPU type, training hours, data center region, and energy consumption metrics. Data Cleaning: I delete all "Not specified" and "Not disclosed" data since these were replaced with empty strings (NULL in the database) in order to maintain data type integrity.

2. User Stories and Query Mapping
User Story 1 (Energy by Region): As a researcher studying AI environmental impact, I want to see total and average energy consumption by data center region so that I can identify which geographic areas have the highest energy usage for LLM training.
Query: the query selects all records with non-empty energy consumption values, groups them by data center region, calculates the sum of total_energy_kwh for each region, and sorts the results from highest to lowest total energy.

User Story 2: As an AI model developer, I want to know which LLM models have the largest parameter counts so that I can understand the relationship between model size and energy consumption.
Query: The query selects all records with non-null parameter count values, sorts them by model_parameters_billion in descending order (from largest to smallest), and returns the top 5 records with their model names and parameter counts.

3. Route 1: Get energy summary by region
    URL: /api/energy_by_region
    curl http://127.0.0.1:5000/api/energy_by_region
    Example Request (browser):
    http://127.0.0.1:5000/api/energy_by_region
    Region               Total Energy (kWh)
    US East (N. Virginia)   1,234,567
    EU West (Ireland)         987,654
    Asia Pacific (Tokyo)      456,789

Route 2: Get detailed data for a specific region
    URL: /api/region/<region_name>
    curl "http://127.0.0.1:5000/api/region/US%20East%20(Northern%20Virginia)"
    Parameter: region_name (use %20 for spaces)
    http://127.0.0.1:5000/api/region/US%20East%20(Northern%20Virginia)
    Region: US East (Northern Virginia)
    Total: 1,234,567 kWh
    Models:
        GPT-4: 500,000 kWh
        Llama 2: 300,000 kWh
        BLOOM: 234,567 kWh

How to Run the Application

- Python 3.8+
- Flask library

Instal:
 bash
pip install flask

 \copy llm_energy (model_name, model_parameters_billion, training_tokens_billion, gpu_type, num_gpus, training_hours, data_center_region, PUE, hardware_power_draw_watts_per_gpu, carbon_intensity_gco2_per_kwh, total_energy_kwh, total_carbon_footprint_kgco2e) FROM 'llmenergy.csv' WITH (DELIMITER ',', NULL 'NULL', FORMAT csv, HEADER TRUE);