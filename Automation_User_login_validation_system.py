# List of approved users and their corresponding devices
approved_users = ["AbdiRahman", "Reyes", "John", "Raha"]
approved_devices = ["Mac-pro", "Windows", "PC", "Mac-Air"]

def login(username, device_id):
    """
    Function to validate user login based on approved users and devices.
    """
    result = ""

    if username in approved_users:
        result += f"The user {username} is approved.\n"
        ind = approved_users.index(username)
        assigned_device = approved_devices[ind]
        result += f"Assigned device for {username}: {assigned_device}\n"

        if device_id == assigned_device:
            result += f"✅ Login successful: You are using the correct device ({device_id}).\n"
        else:
            result += f"❌ Login failed: {device_id} is not the assigned device.\n"
    else:
        result += f"❌ The username '{username}' is not approved to access the system.\n"

    return result

# Prompt user for username
user_input = input("Enter your username: ").strip()

# Check if username is approved
if user_input in approved_users:
    assigned_device = approved_devices[approved_users.index(user_input)]
    print(f"Hello {user_input}, your assigned device is: {assigned_device}")
    device_input = input("Enter your device ID: ").strip()
    print(login(user_input, device_input))
else:
    # Skip asking for device if username is invalid
    print(login(user_input, ""))
