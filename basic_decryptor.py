import hashlib
import random

class md5_worker():

    def encode(self,str):
        encoded_data = hashlib.md5(str.encode())
        return encoded_data.hexdigest()

    def decode(self, data, len):
        ranged = 10 ** len
        for num in range(ranged):
            str_num = str(num)
            encoded_str = self.encode(str_num)
            if encoded_str == data:
                return str_num




