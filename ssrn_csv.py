import csv
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the website
url = "http://ssrn.aviyaan.com/traffic_controller"
driver.get(url)

# Find the <select> element by using a different selector
location_select = Select(driver.find_element("css selector", 'select[name="location"]'))

# Open a CSV file for writing
csv_file_path = "ssrnTables.csv"
with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the header row to the CSV file
    header_row = [
        "Station No",
        "Road Link",
        "Location",
        "AADT",
        "AADT excluding MC & Rickshaws",
        "AADT in PCUs",
        "AADT in PCUs excluding MC & Rickshaws",
        "Year",
        "More info",
    ]
    csv_writer.writerow(header_row)

    # Iterate through each option starting from the second one (index 1)
    for index in range(1, len(location_select.options)):
        # Re-find the <select> element inside the loop
        location_select = Select(
            driver.find_element("css selector", 'select[name="location"]')
        )

        # Select the option
        selected_option = location_select.options[index].text
        location_select.select_by_index(index)

        # Print a message to the console with the selected option name
        print(
            f"Processing Option: {selected_option} ({index}/{len(location_select.options)-1})..."
        )

        # Find the form and submit it
        form = driver.find_element("css selector", "form")
        form.submit()

        # Find the table with class 'link-table'
        table = driver.find_element(By.CSS_SELECTOR, "table.link-table.column.span-24")

        # Iterate through each row (excluding the header row)
        for row in table.find_elements(By.XPATH, ".//tbody/tr[position()>1]"):
            # Extract data from the row
            data_row = [cell.text for cell in row.find_elements(By.XPATH, ".//td")]

            # Append data to the CSV file
            csv_writer.writerow(data_row)

        # Wait for a moment to ensure all data is loaded
        time.sleep(2)

# Close the browser window
driver.quit()

print(f"Data has been saved to: {csv_file_path}")
