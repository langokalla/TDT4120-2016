
class HuffmanNode:

    def __init__(self, token=None, freq=None):
        self.token = token
        self.freq = freq
        self.left = None
        self.right = None

    def get_freq(self):
        return self.freq

    def get_token(self):
        return self.token


class HuffmanBinaryTree:

    def __init__(self):
        pass


def huffman(a):
    """
    Encode alphabet a  to bit strings.
    :param a: Alphabet with frequencies corresponding to letters/tokens.
    :return: Bitstring
    """
    n = len(a)
    Q = a
    for i in range(n-1):
        x = extract_min(a)
        y = extract_min(a)


def extract_min(d):
    x = min(d, key=d.get)
    xf = d[x]
    d.pop(x, None)
    return x, xf


c = {'q':4, 'e':5, 't':1, 'y':3}

print(huffman(c))