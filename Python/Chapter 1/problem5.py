# Import the external moudule
import os

# Select the current directory
directory = "/"

# Each file is shown through a loop.
for item in os.listdir(directory):
    print(item)