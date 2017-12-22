import hashlib
import os
import json
import random
import string


CHAIN_DIR = os.curdir + '/chains/'


def get_hash(filename):
    file = open(CHAIN_DIR + filename, 'rb').read()
    return hashlib.sha256(file).hexdigest()


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_prev_filename(firts_file):
    stop = True
    filename = firts_file
    while stop:
        with open(CHAIN_DIR + filename, 'r') as file:
            next_link = json.load(file)['next']
            if next_link is '':
                stop = False
                return filename
            filename = next_link


def set_next_link_in_prev_file(filename, prev_filename):
    with open(CHAIN_DIR + prev_filename, 'r+') as file:
        f = json.load(file)
        f.update({'next': filename})
        file.seek(0)
        file.write(json.dumps(f, indent=4))


def write_chain():
    current_filename = random_string_generator(10)

    if len(os.listdir(CHAIN_DIR)) == 1:
        prev_filename = '1'
    else:
        prev_filename = get_prev_filename('1')

    set_next_link_in_prev_file(current_filename, prev_filename)
    prev_hash = get_hash(prev_filename)

    data = {
        "name": "Pupkin 2",
        "to": "Noname",
        "amount": 10,
        "hash": prev_hash,
        "next": "",
        "prev": prev_filename,
    }

    with open(CHAIN_DIR + current_filename, 'w') as file:
        file.write(json.dumps(data, indent=4))


if __name__ == '__main__':
    write_chain()
