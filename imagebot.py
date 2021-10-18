#!/usr/bin/env python3

# By Trond Hauklien
import requests  # You might have to tun "pip install requests"
import getpass
import os

# INFORMATION
print("############################################")
print("# Upload script for galleries at timini.no #")
print("############################################")
print("")

# ASK USER FOR PATHS
print("Example url: https://www.timini.no/gallery/upload/130341")
gallery = input("Link to gallery UPLOAD page: ")
print("All files in folder will be uploaded.")
folder = input("Path to image folder (Drag and drop is possible): ").replace(
    "\\", "/").replace("'", "").replace("& ", "")

# VERIFY
print(f"These files will be uploaded to {gallery}")
ls = os.listdir(folder)
for filename in ls:
    print(f"{folder}/{filename}")
print("")
success = True if input(
    "Proceed and start upload? (Y/n) ").lower() == "n" else False


def upload():
    # CREDENTIALS
    username = input("username (timini.no): ")
    password = getpass.getpass("Enter your password, then hit enter: ")

    # PREPARE URLS
    loginurl = "https://www.timini.no/"
    uploadurl = gallery + "/nodisp"

    logindata = {'password': password, 'username': username}

    # INITIATE SESSION
    with requests.Session() as session:
        post = session.post(loginurl, data=logindata)  # Log in
        for i, filename in enumerate(ls):
            file = {"image1": open(folder + "/" + filename, 'rb')}
            r = session.post(uploadurl, files=file)
            if len(r.text) > 10000:
                print("Error while uploading. Check credentials.")
                return False
            print(f"Uploaded ({i+1}/{len(ls)}): {folder}{filename}")
    return True


while success == False:
    success = upload()
    if not success:
        success = True if input(
            "Do you want to try again? (Y/n) ").lower() == "n" else False
