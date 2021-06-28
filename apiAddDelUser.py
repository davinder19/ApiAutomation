import requests
# from payLoad file import all
from payLoad import *
from utilities.configration import *
from utilities.resources import *

# access getConfig method
config = getConfig()['API']['endpoint']
User = ApiResources.urlUser
noUser = ApiResources.noUser
url = config + User
url2 = config + noUser
headers = {"Content-Type": "application/json"}
# ******* not Found User ******************
ntUserRes = requests.get(url2)
ntStatusCode = ntUserRes.status_code
print("User Not Found Status Code is ", ntStatusCode)
assert ntStatusCode == 404
# ******* Found User ******************

findUserRes = requests.get(url)
addStatusCode = findUserRes.status_code
print("Found User Status Code is ", addStatusCode)
assert addStatusCode == 200
print(findUserRes.json())
# ******* ADD User ******************
print("Adding New User")
addUser_response = requests.post(url,
                                 json=addUserData(),
                                 headers=headers, )
# we can use .json method to get response directly in Json Format
print(addUser_response.json())
# add into variable
response_json = addUser_response.json()
# printing user ID
user_ID = response_json['id']
messageAdd = response_json['Name']
print("User", messageAdd, "Added")
assert messageAdd == 'inder'
print("User ID is ", user_ID)
# how to check the Status Code
status_code = addUser_response.status_code
print("Add User Status Code is", status_code)
# use assert method to check the assertion
assert status_code == 201
# ******* Delete User******************
print("Deleting User")

response_deleteUser = requests.delete(url, json={
    "id": user_ID
}, headers=headers, )

delete_statusCode = response_deleteUser.status_code
print("Delete User Status Code is", delete_statusCode)
assert delete_statusCode == 204
# we can use .json method to get response directly in Json Format
# resDel_json = response_deleteBook.json()

# *********************************************************************************************************
