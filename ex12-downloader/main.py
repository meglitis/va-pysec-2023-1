from urllib.request import urlretrieve

url = "https://releases.ubuntu.com/23.04/ubuntu-23.04-desktop-amd64.iso"

filename = "ubuntu-23.04-desktop-amd64.iso"


def print_progress(block_num, block_size, total_size):
    print(round(block_num * block_size / total_size * 100, 3))


urlretrieve(url, filename, print_progress)
