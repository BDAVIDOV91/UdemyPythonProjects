import json
import getpass

# Prompt the user for the master password and return it.
def get_master_password():
    return getpass.getpass('Enter your master password: ')

# Load the passwords from the file and decrypt using the master password.
def load_passwords(filename, master_password):
    try:
        with open(filename, 'r') as file:
            encrypted_data = file.read()
            decrypted_data = decrypt_data(encrypted_data, master_password)
            return json.loads(decrypted_data)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Encrypt and save the passwords to the file.
def save_passwords(filename, master_password, passwords):
    encrypted_data = encrypt_data(json.dumps(passwords), master_password)
    with open(filename, 'w') as file:
        file.write(encrypted_data)

        
# Encrypt the data using a simple XOR encryption.
def encrypt_data(data, key):
    encrypted_chars = []
    for i, char in enumerate(data):
        key_char = key[i % len(key)]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        encrypted_chars.append(encrypted_char)
    return ''.join(encrypted_chars)

# Decrypt the data using a simple XOR encryption.
def decrypt_data(data, key):
    return encrypt_data(data, key)

# Add a new password entry to the manager.
def add_password(filename, master_password):
    service = input('Enter the service name: ')
    username = input('Enter the username: ')
    password = getpass.getpass('Enter the password: ')
    
    passwords = load_passwords(filename, master_password)
    passwords[service] = {'username' : username, 'password' : password}
    save_passwords(filename, master_password, passwords)
    print('Password added successfully!')
    
# Retrieve a passsword from the manager.
def get_password(filename, master_password):
    service = input('Enter the service name: ')
    passwords = load_passwords(filename, master_password)
    
    if service in passwords:
        username = passwords[service]['username']
        password = passwords[service]['password']
        print(f'Service: {service}')
        print(f'Username: {username}')
        print(f'Password: {password}')
    else:
        print('Service not found.')
        
# Main program loop
def main():
    filename = 'passwords.txt'
    master_password = get_master_password()
    
    while True:
        print('\n1. Add a password')
        print('2. Get a password')
        print('3.Exit')
    
        choice = input('Enter your choice(1-3): ')
    
        if choice == "1":
            add_password(filename, master_password)
        elif choice == "2":
            get_password(filename, master_password)
        elif choice == "3":
            break
        else:
            print('Invalid choice. Please try again.')
        
if __name__ == '__main__':
    main() 