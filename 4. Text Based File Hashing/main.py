import hashlib

def generate_hash(file_name):
    try:
        with open(file_name, 'rb') as file:
            #create sha256 object
            sha256 = hashlib.sha256()
            #read file in chunk to avoid memory overflow
            while chunk := file.read(4096):
                sha256.update(chunk)
            return sha256.hexdigest()
        
    except FileExistsError:
        return "File not found!"
    
if __name__ == "__main__":
    file_name = input("Enter file name: ")
    hash_value = generate_hash(file_name)
    print(f"SHA-256 Hash: {hash_value}")