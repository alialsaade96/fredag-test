# kitty.py

import os

# Define the path to check
path = "target/"

# Print a welcome message
print("🐱 Hello from kitty.py!")

# Check if the path exists
if os.path.exists(path):
    print(f"✅ The path '{path}' exists.")
    
    # List contents of the folder
    files = os.listdir(path)
    if files:
        print("📂 Contents of the folder:")
        for file in files:
            print(f" - {file}")
    else:
        print("📁 The folder is empty.")
else:
    print(f"❌ The path '{path}' does not exist.")