import codecs


def obfuscation(output):
    return codecs.encode(output, 'rot_13')
