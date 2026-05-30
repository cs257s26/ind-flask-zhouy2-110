# Individual Flask Assignment - LLM Energy Consumption API

## Overview

This Flask application provides two API endpoints for analyzing energy consumption data from LLM model training. The endpoints allow users to view aggregated energy statistics by region and detailed per-model energy breakdowns for specific data center regions.

## How to Run the Routes

### Prerequisites

- Python 3.8 or higher
- Flask library installed (`pip install flask`)

### Starting the Application

1. Navigate to the project directory:
   ```bash
   cd ind-flask-zhouy2-110
2. Run the Flask application:
   python3 app.py
3. The server will start at http://127.0.0.1:5001 

Route 1: Get Energy Summary by Region
Purpose: Returns total and average energy consumption grouped by data center region, sorted from highest to lowest total energy.

URL Pattern: /api/energy_by_region

HTTP Method: GET

Parameters: None

Example Request (copy and paste into browser): 
http://127.0.0.1:5000/api/energy_by_region

Example using curl:
curl http://127.0.0.1:5000/api/energy_by_region

Energy Consumption by Data Center Region
Region                         Total Energy (kWh)   Average Energy (kWh) 
Memphis Tennessee                     154,000,000        154,000,000
US East (Northern Virginia)            45,532,815          9,106,563
US Central (Iowa)                       4,346,063            869,213
Not specified                           1,390,000            695,000
US East (South Carolina)                1,123,598          1,123,598
Europe (Finland)                          433,196            433,196
China                                      15,360             15,360



Route 2: Get Detailed Data for a Specific Region
Purpose: Returns a detailed breakdown of energy consumption by individual model for a specific data center region.

URL Pattern: /api/region/<region_name>

HTTP Method: GET

Parameters:

region_name (required) - The name of the data center region. Replace spaces with %20 in the URL.

Valid region names (use exactly as shown):

US East (Northern Virginia)

US Central (Iowa)

US East (South Carolina)

Europe (Finland)

China

France

Memphis Tennessee

Example Requests (copy and paste into browser):

1. US East (Northern Virginia):
http://127.0.0.1:5000/api/region/US%20East%20(Northern%20Virginia)
2. US Central (Iowa):
http://127.0.0.1:5000/api/region/US%20Central%20(Iowa)
3. Europe (Finland):
http://127.0.0.1:5000/api/region/Europe%20(Finland)
4. China:
http://127.0.0.1:5000/api/region/China
Example using curl:
curl "http://127.0.0.1:5000/api/region/US%20East%20(Northern%20Virginia)"
Example Output (for US East Northern Virginia):
Region: US East (Northern Virginia)
Total: 45,532,815 kWh
Models:
  GPT-3: 1,287,000 kWh
  GPT-4: 16,099,378 kWh
  Llama 3.1: 24,841,800 kWh
  Claude 3 Opus: no data
  Claude 3 Sonnet: no data
  Claude 3 Haiku: no data
  XLM: 82,637 kWh
  Falcon 180B: 3,222,000 kWh
Example Output (for region with no data):
No data found for region: Invalid Region Name