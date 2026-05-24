DROP TABLE IF EXISTS llm_energy;
CREATE TABLE llm_energy (
    id SERIAL PRIMARY KEY,
    model_name VARCHAR(100) NOT NULL,
    model_parameters_billion TEXT,       
    training_tokens_billion TEXT,         
    gpu_type VARCHAR(50),
    num_gpus TEXT,                        
    training_hours TEXT,                  
    data_center_region VARCHAR(100),
    pue TEXT,                             
    hardware_power_draw_watts_per_gpu TEXT,  
    carbon_intensity_gco2_per_kwh TEXT,      
    total_energy_kwh TEXT,                
    total_carbon_footprint_kgco2e TEXT    
);