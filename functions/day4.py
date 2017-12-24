def passphrase_is_valid(passphrase):
    found_already = []

    words = passphrase.split(' ')

    for word in words:
        if word in found_already:
            return False
        found_already.append(word)

    return True
