DROP TABLE IF EXISTS llm_energy;
CREATE TABLE llm_energy (
    id SERIAL PRIMARY KEY,
    model_name VARCHAR(100) NOT NULL,
    model_parameters_billion VARCHAR(50),
    training_tokens_billion VARCHAR(50),
    gpu_type VARCHAR(50),
    num_gpus VARCHAR(20),
    training_hours VARCHAR(20),
    data_center_region VARCHAR(100),
    pue VARCHAR(20),
    hardware_power_draw_watts_per_gpu VARCHAR(20),
    carbon_intensity_gco2_per_kwh VARCHAR(20),
    total_energy_kwh VARCHAR(20),
    total_carbon_footprint_kgco2e VARCHAR(20)
);