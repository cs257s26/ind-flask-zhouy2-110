1. Database Design Decisions
I chose one table because each row represents a unique LLM model, and there is no repeating data. The dataset contains 27 LLM models with  model name, parameter count, GPU type, training hours, data center region, and energy consumption metrics. Data Cleaning: I delete all "Not specified" and "Not disclosed" data since these were replaced with empty strings (NULL in the database) in order to maintain data type integrity.

2. User Stories and Query Mapping
User Story 1 (Energy by Region): As a researcher studying AI environmental impact, I want to see total and average energy consumption by data center region so that I can identify which geographic areas have the highest energy usage for LLM training.
Query: the query selects all records with non-empty energy consumption values, groups them by data center region, calculates the sum of total_energy_kwh for each region, and sorts the results from highest to lowest total energy.

User Story 2: As an AI model developer, I want to know which LLM models have the largest parameter counts so that I can understand the relationship between model size and energy consumption.
Query: The query selects all records with non-null parameter count values, sorts them by model_parameters_billion in descending order (from largest to smallest), and returns the top 5 records with their model names and parameter counts.
