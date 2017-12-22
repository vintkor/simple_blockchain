from hashlib import sha256
from os import listdir, curdir
from json import dumps


CHAIN_DIR = curdir + '/chains/'


def get_last_file():
    files = listdir(CHAIN_DIR)
    sort_files = sorted(files, key=int)
    return sort_files[-1]


def make_new_filename():
    last_file_name = int(get_last_file())
    new_file_name = last_file_name + 1
    return str(new_file_name)


def get_hash(filename):
    file = open(CHAIN_DIR + filename, 'rb').read()
    return sha256(file).hexdigest()


def write_chain():
    prev_hash = get_hash(get_last_file())
    data = {
        "name": "Pupkin 2",
        "to": "Noname",
        "amount": 10,
        "hash": prev_hash,
    }

    with open(CHAIN_DIR + make_new_filename(), 'w') as file:
        file.write(dumps(data, indent=4))


if __name__ == '__main__':
    write_chain()
