#!/usr/bin/env python3

# By Trond Hauklien and Henrik T. Kaarbø
import requests  # You might have to tun "pip install requests"
import getpass
import os

# Import generic path handling object for cross platform compatibility
from pathlib import Path 

def main():
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
    paths = Path(folder)
    for filename in paths.iterdir():
        print(f"{filename}")
    print("")

    # define upload modes
    modes =  {
        "default" : "Default implementation",
        "chronological" : "Upload chonologically by picture creation time (works on Windows)",
        "q" : "\tQuit the script"}

    # Print mode explanation neatly
    linelength = 60 
    print(f"Please select mode. The available modes are")
    
    print("-"*linelength)
    for mode, explanation in modes.items():
        print(f"\n{mode}: \t{explanation}")

    print("-"*linelength)
    
    while not (userInput :=  input("Select mode: ").lower()) in modes:
        print(f"{userInput} not recognized, availible modes are {list(modes.keys())}")
    
    if userInput == "q":
        return None

    success = True if input(
        "Proceed and start upload? (Y/n) ").lower() == "n" else False
    
    while success == False:
        success = upload(paths, galleryurl=gallery, mode = userInput)
        if not success:
            success = True if input(
                "Do you want to try again? (Y/n) ").lower() == "n" else False

def upload(path : Path, galleryurl : str,  mode : str = "default"):
    """
    Uploading script for timini.no. Requests username and password safely and initiates an upload request to 
    selected galleryurl.
    
    args:
        path        :   Path  ->   path to the directory containing the images
        galleryurl  :   str   ->   target gallery url for upload 
        mode        :   str   ->   function upload mode, currently only "chronological", "default" implemented
    """
    # CREDENTIALS
    username = input("username (timini.no): ")
    password = getpass.getpass("Enter your password, then hit enter: ")

    # PREPARE URLS
    loginurl = "https://www.timini.no/"
    uploadurl = galleryurl + "/nodisp"

    logindata = {'password': password, 'username': username}

    if mode == "chronological":
        path = sorted(path.iterdir(), key=os.path.getctime)
    
    else:
        path = list(path.iterdir())

    # INITIATE SESSION 
    with requests.Session() as session:
        # Log in
        post = session.post(loginurl, data=logindata) 
        for i, filepath in enumerate(path):

            with open(filepath, 'rb') as picture:
                file = {"image" + str(i) : picture}
                r = session.post(uploadurl, files=file)

            # a "wtf-response" condition:    
            if len(r.text) > 10000:
                print("Error while uploading. Check credentials.")
                return False

            print(f"Uploaded ({i+1}/{len(path)}): {filepath}")
    return True

if __name__ == "__main__":
    main()
