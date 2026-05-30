# Individual Flask Assignment - LLM Energy Consumption API

## Overview

This Flask application provides API routes for analyzing energy consumption data from large language model training. The project uses a PostgreSQL database created from a curated LLM energy consumption dataset. The API allows users to compare energy consumption across data center regions and view detailed model-level energy data for a selected region.

The purpose of this project is to connect a real dataset to a database-backed web application. The database stores information about LLM model training, including model size, training tokens, GPU type, number of GPUs, training hours, data center region, power usage effectiveness, hardware power draw, carbon intensity, total energy consumption, and total carbon footprint.

## Repository Structure

text Data/   createtable.sql   llmenergy.csv  ProductionCode/   app.py   API.py   datasource.py   psqlConfig.py  README.md 

## Database Setup

The database table is created using the script in the Data folder:

bash psql -d [database_name] -f Data/createtable.sql 

After creating the table, I used the following copy command to import the cleaned dataset into PostgreSQL:

sql \copy llm_energy (model_name, model_parameters_billion, training_tokens_billion, gpu_type, num_gpus, training_hours, data_center_region, PUE, hardware_power_draw_watts_per_gpu, carbon_intensity_gco2_per_kwh, total_energy_kwh, total_carbon_footprint_kgco2e) FROM 'Data/llmenergy.csv' WITH (DELIMITER ',', NULL 'NULL', FORMAT csv, HEADER TRUE); 

## How to Run the Routes

### Prerequisites

- Python 3.8 or higher
- Flask installed
- psycopg2 installed
- PostgreSQL database set up on stearns

Install required libraries if needed:

bash pip install flask psycopg2-binary 

### Starting the Application

Navigate to the project directory:

bash cd ind-flask-zhouy2-110 

Run the Flask application:

bash python3 ProductionCode/app.py 

The server will start at:

text http://127.0.0.1:5001 

## User Stories

### User Story 1

As an environmental researcher, I want to compare total energy consumption across data center regions so that I can identify which regions are associated with the highest LLM training energy usage.

### User Story 2

As a sustainability analyst, I want to compare average energy consumption by region so that I can understand how energy usage differs across data center locations.

### User Story 3

As a machine learning researcher, I want to view detailed model-level records for a specific region so that I can determine which models contribute most to energy consumption in that region.

## Route 1: Get Energy Summary by Region

### Purpose

This route returns total and average energy consumption grouped by data center region. The results are sorted from highest to lowest total energy consumption.

### URL Pattern

text /api/energy_by_region 

### HTTP Method

text GET 

### Parameters

None.

### Example Request

text http://127.0.0.1:5001/api/energy_by_region 

### Example Using curl

bash curl http://127.0.0.1:5001/api/energy_by_region 

### Example Output

text Energy Consumption by Data Center Region  Region                         Total Energy (kWh)   Average Energy (kWh) Memphis Tennessee                     154,000,000        154,000,000 US East (Northern Virginia)            45,532,815          9,106,563 US Central (Iowa)                       4,346,063            869,213 Not specified                           1,390,000            695,000 US East (South Carolina)                1,123,598          1,123,598 Europe (Finland)                          433,196            433,196 China                                      15,360             15,360 

## Route 2: Get Detailed Data for a Specific Region

### Purpose

This route returns a detailed breakdown of energy consumption by individual model for a selected data center region.

### URL Pattern

text /api/region/<region_name> 

### HTTP Method

text GET 

### Parameters

region_name is required. It should match one of the region names in the dataset. Spaces should be written as %20 in the URL.

### Valid Region Names

text US East (Northern Virginia) US Central (Iowa) US East (South Carolina) Europe (Finland) China France Memphis Tennessee Not specified 

### Example Requests

text http://127.0.0.1:5001/api/region/US%20East%20(Northern%20Virginia) 

text http://127.0.0.1:5001/api/region/US%20Central%20(Iowa) 

text http://127.0.0.1:5001/api/region/Europe%20(Finland) 

text http://127.0.0.1:5001/api/region/China 

### Example Using curl

bash curl "http://127.0.0.1:5001/api/region/US%20East%20(Northern%20Virginia)" 

### Example Output

text Region: US East (Northern Virginia) Total: 45,532,815 kWh Models:   GPT-3: 1,287,000 kWh   GPT-4: 16,099,378 kWh   Llama 3.1: 24,841,800 kWh   Claude 3 Opus: no data   Claude 3 Sonnet: no data   Claude 3 Haiku: no data   XLM: 82,637 kWh   Falcon 180B: 3,222,000 kWh 

### Example Output for Region With No Matching Data

text No data found for region: Invalid Region Name 

## Part 3: Database Design Process

The original dataset contains information about large language model training, including model specifications, training tokens, GPU hardware, number of GPUs, training hours, data center region, power usage effectiveness, hardware power draw, regional carbon intensity, total energy consumption, and total carbon footprint. I chose to represent the curated dataset using one table because each row describes one model-training record. I did not split the data into multiple tables because the dataset is relatively small and the main user stories focus on comparing complete training records rather than managing separate entities such as models, regions, and hardware types. A single table also makes the two required queries more direct and reduces unnecessary complexity for this project.

I included the columns that were most relevant to the user stories and to environmental analysis of LLM training. I kept model identity, model size, training scale, GPU information, location, energy consumption, and carbon footprint because these fields allow users to compare both technical and environmental aspects of model training. I excluded extraneous data that did not help answer the user stories or support the planned queries. The primary key is an id column with type SERIAL PRIMARY KEY, which gives each row a unique identifier even if model names or other values are repeated.

I selected data types based on how each field is used. Text-based fields such as model_name, gpu_type, and data_center_region use VARCHAR because they store names and categories. Quantitative fields such as parameters, tokens, GPU counts, training hours, PUE, power draw, carbon intensity, energy consumption, and carbon footprint were cleaned so that they could be stored consistently and used in calculations. This matters because the queries use numeric values for aggregation, comparison, and filtering. Missing or unavailable values from the original dataset were handled during cleaning so that the data could be imported successfully and queried consistently.

## Part 3: Query Design and User Stories

The first query supports the user stories about comparing energy consumption across regions. It groups the dataset by data_center_region and calculates total and average energy consumption for each region. This matches the environmental researcher user story because it identifies which regions have the highest total energy usage. It also matches the sustainability analyst user story because average energy consumption gives another way to compare regional patterns. This query provides a high-level summary of the dataset and shows how energy consumption differs by location.

The second query supports the user story about viewing model-level details within a specific region. It filters the dataset by a selected data_center_region and returns the models associated with that region along with their energy consumption values. This allows a user to move from the regional summary to a more detailed view of the individual model records behind that total. Thus, the two queries are designed to show different ranges of the dataset: the first query summarizes across all regions, while the second query drills down into specific model records for one region.

Together, the two queries support different but related levels of analysis. The first query answers a broad comparison question across the whole dataset, while the second query answers a more specific investigative question about one region. This design makes the API useful for both summary-level environmental analysis and detailed model-level exploration.