# Import the required packages
import os

# Command to update the package list
os.system("sudo apt-get update")

# Command to install python3-pip
os.system("sudo apt-get install python3-pip -y")

# Install the required packages in the requirements.txt file
os.system("pip3 install -r requirements.txt")

# Print message to tell the user that the installation is complete
print("Installation complete. To run the program, type 'python3 main.py'")