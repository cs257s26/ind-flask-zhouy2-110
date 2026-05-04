DROP TABLE IF EXISTS llm_energy;
CREATE TABLE llm_energy (
    id SERIAL PRIMARY KEY,
    model_name VARCHAR(100) NOT NULL,
    model_parameters_billion DECIMAL,
    training_tokens_billion DECIMAL,
    gpu_type VARCHAR(50),
    num_gpus INT,
    training_hours DECIMAL,
    data_center_region VARCHAR(100),
    pue DECIMAL,
    hardware_power_draw_watts_per_gpu INT,
    carbon_intensity_gco2_per_kwh INT,
    total_energy_kwh DECIMAL,
    total_carbon_footprint_kgco2e DECIMAL
);