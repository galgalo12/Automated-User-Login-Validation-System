This Python script automates a simple login validation process by checking:

    Approved Usernames and Devices: It uses two parallel lists:

    approved_users contains names of authorized users.

    approved_devices contains the corresponding approved device for each user (indexed the same).

Login Function:

    Validates if the entered username exists.

    If valid, it retrieves the corresponding device and compares it with the one the user inputs.

Displays appropriate messages:

    ✅ If login is successful (correct user and device).

    ❌ If login fails due to an incorrect device or unknown username.

User Interaction:

    Prompts the user to enter their username.

    If valid, it informs them of their assigned device and prompts for the device ID.

    Displays the final login result.
