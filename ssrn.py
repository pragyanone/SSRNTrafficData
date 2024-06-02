from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Open the website
url = 'http://ssrn.aviyaan.com/traffic_controller'
driver.get(url)

# Find the <select> element by using a different selector
location_select = Select(driver.find_element('css selector', 'select[name="location"]'))

# Iterate through each option starting from the second one (index 1)
for index in range(1, len(location_select.options)):
    # Re-find the <select> element inside the loop
    location_select = Select(driver.find_element('css selector', 'select[name="location"]'))

    # Select the option
    selected_option = location_select.options[index].text
    location_select.select_by_index(index)

    # Find the form and submit it
    form = driver.find_element('css selector', 'form')
    form.submit()

    # Find the table with class 'link-table'
    table = driver.find_element(By.CSS_SELECTOR, 'table.link-table.column.span-24')

    # Iterate through each row (excluding the header row)
    for row in table.find_elements(By.XPATH, './/tbody/tr[position()>1]'):
        try:
            # Extract parameters from the row
            first_param = row.find_element(By.XPATH, './/td[8]').text
            second_param = row.find_element(By.XPATH, './/td[2]').text

            # Find the link in the last column
            link = row.find_element(By.XPATH, './/td[last()]/a')

            # Get the URL from the link
            url = link.get_attribute('href')

            # Open the link in a new tab
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[-1])
            driver.get(url)
            # Click the download button using JavaScript with dynamic parameters
            script = f"exportToExcel('{first_param}', '{second_param}');"
            print(f'Getting {selected_option} {first_param}...')
            driver.execute_script(script)
          
        except:
            print(f'\t\tCannot get {selected_option} {first_param}')

        finally:
            # Close the new tab
            driver.close()

            # Switch back to the original tab
            driver.switch_to.window(driver.window_handles[0])  


# Close the browser window
driver.quit()
