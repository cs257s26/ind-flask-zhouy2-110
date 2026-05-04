CREATE TABLE IF NOT EXISTS llm_energy (
    id SERIAL PRIMARY KEY,
    model_name VARCHAR(100) NOT NULL,
    model_parameters_billion DECIMAL(10,2),
    training_tokens_billion DECIMAL(12,2),
    gpu_type VARCHAR(50),
    num_gpus INT,
    training_hours DECIMAL(10,2),
    data_center_region VARCHAR(100),
    pue DECIMAL(4,2),
    hardware_power_draw_watts_per_gpu INT,
    carbon_intensity_gco2_per_kwh INT,
    total_energy_kwh DECIMAL(15,2),
    total_carbon_footprint_kgco2e DECIMAL(15,2)
);