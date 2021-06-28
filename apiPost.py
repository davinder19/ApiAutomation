import requests
# ******* ADD BOOK ******************
addBook_response = requests.post('http://216.10.245.166/Library/Addbook.php', json={
    "name": "Learn From Udemy",
    "isbn": "xyz21",
    "aisle": "991",
    "author": "D-Dev"
}, headers={"Content-Type": "application/json"},)
# we can use .json method to get response directly in Json Format
print(addBook_response.json())
# add into variable
response_json = addBook_response.json()
# printing book ID
book_ID = response_json['ID']
messageAdd = response_json["Msg"]
print(messageAdd)
print("Book ID is ", book_ID)
# how to check the Status Code
status_code = addBook_response.status_code
print("Status Code is", status_code)
# use assert method to check the assertion
assert status_code == 200
# ******* Delete BOOK ******************
response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={
"ID": book_ID
},headers={"Content-Type": "application/json"},)
delete_statusCode = response_deleteBook.status_code
print(" Status Code is", delete_statusCode)
assert delete_statusCode == 200
# we can use .json method to get response directly in Json Format
resDel_json = response_deleteBook.json()
messageDel = resDel_json['msg']
print(messageDel)
assert messageDel == "book is successfully deleted"
