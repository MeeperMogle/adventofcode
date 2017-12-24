def passphrase_is_valid(passphrase):
    found_already = []

    words = passphrase.split(' ')

    for word in words:
        if word in found_already:
            return False
        found_already.append(word)

    return True


def passphrase_is_valid_no_anagrams(passphrase):
    words = passphrase.split(' ')

    for i in range(len(words)):
        words[i] = ''.join(sorted(words[i]))

    return passphrase_is_valid(' '.join(words))
