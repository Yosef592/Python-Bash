import subprocess

def get_saved_wifi_passwords():
    # Run the command to get the list of profiles
    command = ['netsh', 'wlan', 'show', 'profiles']
    networks = subprocess.check_output(command, encoding='utf-8').split('\n')
    
    # Extract the profile names
    profiles = [line.split(':')[1].strip() for line in networks if "All User Profile" in line]

    wifi_details = []

    for profile in profiles:
        # Run the command to get the profile details, including the password
        command = ['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']
        result = subprocess.check_output(command, encoding='utf-8').split('\n')
        
        # Extract the password
        password_line = [line.split(':')[1].strip() for line in result if "Key Content" in line]
        password = password_line[0] if password_line else None
        
        wifi_details.append({'Profile': profile, 'Password': password})

    return wifi_details

if __name__ == "__main__":
    wifi_passwords = get_saved_wifi_passwords()
    
    for wifi in wifi_passwords:
        with open("Wifi_Pass.txt", "x") as file:
        	file.close()
        with open("Wifi_Pass.txt", "w") as file:
        	file.write(f"Profile: {wifi['Profile']}, Password: {wifi['Password']}")

