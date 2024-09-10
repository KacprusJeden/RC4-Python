class RC4Coding:
    def __init__(self, msg: str, key: str):
        self._msg = msg
        self._key = key

    @property
    def msg(self):
        return self._msg

    @msg.setter
    def msg(self, value):
        self._msg = value

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value

    def ord_key_array(self, word):
        return [ord(letter) for letter in word]

    def KSA(self):
        S = list(range(256))
        key_array = self.ord_key_array(self._key)
        key_length = len(key_array)

        j = 0
        for i in range(len(S)):
            j = (j + S[i] + key_array[i % key_length]) % 256
            S[i], S[j] = S[j], S[i]

        return S

    def PRGA(self):
        S = self.KSA()
        msg_length = len(self._msg)

        i = 0
        j = 0
        key2tab = []

        while msg_length > 0:
            msg_length -= 1
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            K = S[(S[i] + S[j]) % 256]
            key2tab.append(K)

        return key2tab

    def rc4Encrypt(self):
        keyStream = self.PRGA()
        msg_array = self.ord_key_array(self._msg)

        cipher = [keyStream[i] ^ msg_array[i] for i in range(len(msg_array))]

        return ''.join([format(c, '02x') for c in cipher])



#Test
rc4Coding = RC4Coding('Mission Accomplished', 'KACPER')
print(rc4Coding.rc4Encrypt())