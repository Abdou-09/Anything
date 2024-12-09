from datetime import datetime
from netmiko import ConnectHandler
import os
import socket
import shutil
import requests

# Main Menu function to display options
def main_menu():
    print("\nMain Menu")
    print("Option 1 : Show the date and time")
    print("Option 2 : Show the IP address")
    print("Option 3 : Show the Remote Home Directory Listing")
    print("Option 4 : Backup the Remote File")
    print("Option 5 : Save the Web page")
    print("Option Q : Exit")

# Show the current date and time in a readable format
def current_date():
    try:
        my_datetime = datetime.now()
        formatted_datetime = my_datetime.strftime("%m/%d/%Y %H:%M:%S")
        print("Current Date and Time: ", formatted_datetime)
    except Exception as e:
        print(f"An error occurred: {e}")

# Show the IP address of the local machine
def ip_address():
    try:
        hostname = socket.gethostname()
        my_ip = socket.gethostbyname(hostname)
        print("My IP address is: ", my_ip)
    except Exception as e:
        print(f"An error occurred during the IP address retrieval: {e}")

# Connect to the Ubuntu VM and display the system infodef show_system_info():
try:
    ubuntu_device = {
        device_type:= "linux",
        host:="10.0.2.15",
        username:="vboxuser",
        password:="changeme",
        port:=22,
        secret:="changeme",
    }
    # Simulating some operation
    print("Device setup successful:", ubuntu_device)
except Exception as e:
    print(f"An error occurred: {e}")



def get_remote_home_directory():
    try:
        # Establish SSH connection to the remote device
        connection = ConnectHandler(ubuntu_device)
        
        # Fetch the home directory path using the 'echo $HOME' command
        output = connection.send_command("echo $HOME")
        
        # Display the result
        print("Linux VM Home Directory: ", output.strip())
        
        # Disconnect from the remote device
        connection.disconnect()
    except Exception as e:
        print(f"An error occurred during the SSH connection: {e}")

# Backup a file on the remote machine
def backup_file():
    try:
        # Ask the user for the full path to the file
        file_path = input("Please enter the full path to the file on the remote computer: ")

        if not os.path.isfile(file_path):
            print("The file does not exist. Please check the path and try again.")
            return

        # Create the backup file path with a '.old' suffix
        backup_path = file_path + ".old"
        
        # Copy the file to the backup location
        shutil.copy(file_path, backup_path)
        print(f"Backup successful! File copied to: {backup_path}")
    except Exception as e:
        print(f"An error occurred during the backup: {e}")

# Save a webpage to a file
def backup_webpage():
    try:
        # Ask the user for the full URL of the webpage
        url = input("Please enter the full URL of the webpage: ")
        
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        if response.status_code == 200:
            print(f"Successfully fetched the webpage: {url}")
            
            # Create a filename based on the URL
            filename = url.replace("https://", "").replace("http://", "").replace("/", "_") + ".html"
            
            # Write the content to a file
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(response.text)
            print(f"Webpage saved successfully as '{filename}'")
        else:
            print(f"Failed to fetch the webpage. HTTP Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while trying to fetch the webpage: {e}")

# Main function to handle the menu and user input
def output():
    while True:
        main_menu()
        choice = input("Please enter your choice: ").strip().upper()

        if choice == "1":
            current_date()
        elif choice == "2":
            ip_address()
        elif choice == "3":
            get_remote_home_directory()
        elif choice == "4":
            backup_file()
        elif choice == "5":
            backup_webpage()
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("An error has occurred, please try again.")

if __name__ == "__main__":
    output()
