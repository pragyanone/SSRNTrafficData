# SSRN Traffic data
This repository contains python code and fetched traffic data from [http://ssrn.aviyaan.com/traffic_controller](http://ssrn.aviyaan.com/traffic_controller) as of 2080-09-29.

The python code was developed using ChatGPT.

- **ssrn.py** downloads the traffic data file *.xls* for each station throughout the recorded years consecutively.
- **ssrn_csv.py** fetches the traffic data table for each station and combines them into a combined *.csv* file. <br>*See **ssrn.traffic_controller.2080-09-29/ssrnTables.csv**. <br>This file was analysed and saved as **ssrnTables.xlsx***.
- There were missing data for several stations. A list of stations with missing data is provided in **ssrn.traffic_controller.2080-09-29/ssrnMissing.txt**.