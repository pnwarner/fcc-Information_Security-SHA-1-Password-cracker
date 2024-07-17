import hashlib

def make_byte_list(file):
    byte_list = []
    # open file, and read as 'bytes' for hashlib.sha1()
    with open(file, 'rb') as f:
        # remove EOL characters with .strip()
        line = f.readline().strip()
        while line:
            byte_list.append(line)
            line = f.readline().strip()
    return byte_list

def crack_sha1_hash(hash, use_salts = False):
    pw_list = make_byte_list('top-10000-passwords.txt')
    salt_list = make_byte_list('known-salts.txt') if use_salts else None
    hash_dict = {}

    #Hash each password in pw_list, and add it to hash_dict
    for pw in pw_list:
        pw_string = pw.decode('utf-8')
        hash_dict[hashlib.sha1(pw).hexdigest()] = pw_string
        if use_salts:
            for salt in salt_list:
                # Add password prepended, and appended to hash_dict
                hash_dict[hashlib.sha1(salt + pw).hexdigest()] = pw_string
                hash_dict[hashlib.sha1(pw + salt).hexdigest()] = pw_string

    if hash in hash_dict:
        return hash_dict[hash]
    return 'PASSWORD NOT IN DATABASE'