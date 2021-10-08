import hashlib

class encoder():

    def encode(self,str):
        encoded_data = hashlib.md5(str.encode())
        return encoded_data.hexdigest()


if __name__ == "__main__":
    str = "dudi"
    encoder = encoder()
    encoded_string = encoder.encode(str)
    print(encoded_string)
