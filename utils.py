import sys


def to_base(i,base):
    """
        converts a number <i> to base <base>
        returns a list representation of the converted base
        ex:
            to_base(255,2) ==> [1,1,1,1,1,1,1,1,1]
            to_base(145,10) ==> [1,4,5]
                146 = 1*(100) + 4*(10) + 5*(1)
            to_base(1000,36] ==> [27,28]
                1000 = 27*(36**1) + 28*(36**0)
    """

    res = []

    leftover = i

    while i > 0:
        remainder = i % base
        leftover = i / base
        res.append(remainder)
        i = leftover

    return list(reversed(res))


def pad_list(alist, padding = 5):
    """
        returns a padded list, such that the resulting list is
        atleast <padding> long:
        pad_list([2,3,5], padding = 5) ==> [0,0,2,3,5]
        pad_list([1,2,3,4,5], padding = 5) ==> [1,2,3,4,5]
        pad_list(['X'], padding = 7) ==> [0,0,0,0,0,0,'X']
    """

    padded = []

    for i in range(padding - len(alist)):
        padded.append(0)

    padded.extend(alist)

    return padded




def n_to_imgur(num):
    """
        convert a number to an appropriate imgur sequence
        (basically this converts an int to a base-62 number,
        and returns a string representation of it)
        >>> n_to_imgur(0)
        '00000'
        >>> n_to_imgur(62)
        '00010'
        >>> n_to_imgur(61*(62**4))
        'z0000'
        >>> n_to_imgur(61*(62**4) + 61*(62**3))
        'zz000'
        >>> n_to_imgur(5*(62**4) + 5*(62**3) + 5*(62**2) + 5*(62**1) + 5*(62 ** 0))
        '55555'
        >>> n_to_imgur(52*(62**4) + 53*(62**3) + 54*(62**2) + 55*(62**1) + 56*(62 ** 0))
        'qrstu'
    """

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    res = pad_list(to_base(num,62), padding=5)
    return ''.join([alphabet[x] for x in res])


def imgur_to_n(string):
    """
        The inverse of n_to_imgur(num) -- this function treats the argument as a 
        base62 number and returns a base10 representation of that number
        >>> imgur_to_n('00000')
        0
        >>> imgur_to_n('00008')
        8
        >>> imgur_to_n('0000L')
        21
        >>> imgur_to_n('0001L')
        83
        >>> imgur_to_n('ZZZZZ')
        525649985
    """

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    total = 0
    pos = 0
    for i in reversed(string):
        total += alphabet.find(i) * (len(alphabet) ** pos)
        pos += 1
    return total

