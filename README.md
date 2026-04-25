1. View Energy Consumption by Region
This page shows the summary of total and average energy consumption for each center region in data.
URL: http://127.0.0.1:PORT/api/energy_by_region
Eg: http://127.0.0.1:8080/api/energy_by_region
Output:
Energy Consumption by Data Center Region
Region                         Total Energy (kWh)   Average Energy (kWh) 
Memphis Tennessee                     154,000,000        154,000,000
US East (Northern Virginia)            45,532,815          9,106,563
US Central (Iowa)                       4,346,063            869,213
Not specified                           1,390,000            695,000
US East (South Carolina)                1,123,598          1,123,598
Europe (Finland)                          433,196            433,196
China                                      15,360             15,360

2. View Specific Region Data
This page shows detailed energy consumption for a specific center region in data, including total energy and a list of models with their individual energy usage.
URL: http://127.0.0.1:PORT/api/region/REGION_NAME
Eg: http://127.0.0.1:8080/api/region/US%20East%20(Northern%20Virginia)
Output:
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