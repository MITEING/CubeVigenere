# -*- coding: utf-8 -*- 
import re
import math

"""
第二の鍵として、(直前の文字でなくて)平文最初のｎ文字を使う。
このとき、最初のn文字は単に二倍されてしまうので、alphabetが偶数個しかない状態だと復号できない。空白を入れることでこれを回避。
因みに、最初のn文字は通常のkeyのみで暗号化するのでもよい。空白を一文字と考えるのは無理になることがありそうではある。
また、もう一つのアイデアとして、和ではなくて積を使うことを考えると剰余体をなしていて欲しい。
小文字+空白の27文字は非素数なのでダメだが、小文字+大文字+空白の53文字なら剰余体をなしてくれる。
（実際には積を使わないので、ここでは奇数でさえあればよい)
"""

alphabet = "aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ ";

def Main():

    message = "Mankind in its present state has been around for a quarter of a million years, yet only the last 4,000 have been of any significance. So, what did we do for nearly 250,000 years? We huddled in caves and around small fires, fearful of the things that we didn't understand. It was more than explaining why the sun came up, it was the mystery of enormous birds with heads of men and rocks that came to life. So we called them 'gods' and 'demons', begged them to spare us, and prayed for salvation. In time, their numbers dwindled and ours rose. The world began to make more sense when there were fewer things to fear, yet the unexplained can never truly go away, as if the universe demands the absurd and impossible. Mankind must not go back to hiding in fear. No one else will protect us, and we must stand up for ourselves. While the rest of mankind dwells in the light, we must stand in the darkness to fight it, contain it, and shield it from the eyes of the public, so that others may live in a sane and normal world. We secure. We contain. We protect. - The Administrator"

    message = re.sub(r'[.,!?\']', "", message).replace("-", "")    #erase symbol

    key = "SecureContainProtect"

    N = len(key) + 1
    
    code = CodeMessage(message, key, N)

    print(code)
    print(DecodeMessage(code, key, N))
    
    return

#major functions#
def CodeMessage(message, key, n):
    #'alphabet' only
    if math.gcd(len(key), n) != 1:
        print("It cant code : KEY LENGTH AND N ARE NOT RELATIVE PRIME.")
        return
    
    key2 = message[0:n-1] #first n charactor

    code = Code(Code(message, key), key2)
    
    return code

def DecodeMessage(code, key, n):
    de1 = Decode(code, key)

    #key2 wo eru
    ini = de1[0:n-1]
    key2 = ""
    for i in range(len(ini)):
        c = alphabet.find(ini[i])
        if c % 2 == 0:
            key2 += alphabet[int(c / 2)]
        else:
            key2 += alphabet[int((c + len(alphabet)) / 2)]

    #decode
    de2 = Decode(de1, key2)
    return de2

#minor#
def Code(target, key):
    answer = ""
    for i in range(len(target)):
        if re.match(r"[0-9]", target[i]):
            answer += target[i]
        else:
            answer += alphabet[(alphabet.find(target[i]) + alphabet.find(key[i % len(key)]))% len(alphabet)]

    return answer

def Decode(target, key):
    answer = ""
    for i in range(len(target)):
        if re.match(r"[0-9]", target[i]):
            answer += target[i]
        else:
            answer += alphabet[(alphabet.find(target[i]) - alphabet.find(key[i % len(key)]))%len(alphabet)]

    return answer

    
Main()
