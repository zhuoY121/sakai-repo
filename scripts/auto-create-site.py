import requests
from bs4 import BeautifulSoup

# Set the URL of the login page
login_url = 'https://trunk-mysql8.nightly.sakaiproject.org/portal'

# Set the username and password
username = 'admin'
password = 'admin'

# Set the login credentials in a dictionary
login_data = {
    'username': username,
    'password': password
}

# Send a POST request to the login page with the login credentials
response = requests.post(login_url, data=login_data)

# Check the response status code to see if the login was successful
if response.status_code == 200:
    print('Login successful!')
else:
    print('Login failed.')

print(response.text)
# Print or process the data as needed
# print(response.text)
    
session_cookies = {
    'session_id': "9a8b4c61-1658-4e17-a1e7-43c690936a2a"
}
    
upload_url = "https://trunk-mysql8.nightly.sakaiproject.org/portal/site/~admin/tool/~admin-210/sakai.filepicker.helper/sakai.resource.type.helper.helper"
response = requests.get(upload_url, cookies=session_cookies)
print(response.text)

logout_url = "https://trunk-mysql8.nightly.sakaiproject.org/portal/logout"

# Send a GET request to the logout endpoint
response = requests.get(logout_url)

# Check the response status code to see if the logout was successful
if response.status_code == 200:
    print('Logout successful!')
else:
    print('Logout failed.')