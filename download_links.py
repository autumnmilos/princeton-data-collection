from selenium import webdriver
import time

#This code downloads all links and adds them to a folder corresponding to a name

driver_path = '/path/to/chromedriver'


driver = webdriver.Chrome(executable_path=driver_path)

# Read input data from a JSON file
input_filename = 'output.json'
with open(input_filename, 'r') as infile:
    data = json.load(infile)

# Store names and links in a dictionary
names_links_dict = {}

for entry in data:
    name = entry["name"]
    links = entry["links"]
    names_links_dict[name] = links


#print(json.dumps(names_links_dict, indent=2))

#Create a folder for each name and download links in that folder
for name, links in names_links_dict.items():
    folder_name = name.replace(" ", "_") 
    os.makedirs(folder_name, exist_ok=True) 

    for link_info in links:
        link_name = link_info["name"]
        link_url = link_info["link"]

        driver.get(link_url)


        current_directory = os.getcwd()


        file_path = os.path.join(current_directory, folder_name, f"{link_name}.pdf")  

   
        link_element = driver.find_element_by_xpath("//a[contains(text(), 'Download')]")
        link_element.click()


        time.sleep(5)  

        # Move the downloaded file to the correct folder
        downloaded_file_name = "download.pdf"  
        os.rename(downloaded_file_name, file_path)

# Close the webdriver
driver.quit()
