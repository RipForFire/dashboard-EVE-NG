# Run the command to install python3-pip 
# Install the required packages in the requirements.txt file
# Print success message or error message

# Import the required packages
import os

# Command to install python3-pip
os.system("sudo apt-get install python3-pip")

# Install the required packages in the requirements.txt file
os.system("pip3 install -r requirements.txt")

# Print message to tell the user that the installation is complete
# And how to run the program
print("Installation complete. To run the program, type 'python3 main.py'")