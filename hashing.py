import os
import argparse
import hashlib

def parse_arguments():
    """
    Handling and parsing the command line arguments
    Returns:
        [argparse.Namespace]: The parsed arguments
    """
    example_usage = """Example of use:
        python3 hasing.py -i users.txt"""
    parser = argparse.ArgumentParser(description="Storing Hashing passwords",
                                     epilog=example_usage,
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-i", "--input", required=True,
                        help="Input user file")

    return parser.parse_args()


def store_hash(filename: str, username: str, password: str) -> None:
    """
    Storing usernames with hashed passwords

    Args:
        filename (str): txt file to store usernames with passwords
        username (str): username
        password (str): password of the corresponding user
    """
    encoded = password.encode()
    hashed = hashlib.sha256(encoded).hexdigest()
    with open(filename, 'a+') as f:
        f.write(f'{username}:{hashed}\n')


def main(filename: str) -> None:
    """
    Main function

    Args:
        filename (str): txt file to store username and hashed passwords
    """
    exit = False
    while not exit:
        print("Type username: ")
        username = str(input())
        print(f'Type password for {username}')
        password = str(input().strip())
        store_hash(filename, username, password)
        print('Do you want to continue: [y/n]?')
        choice = str(input())
        if choice.lower() == 'n' or choice.lower() == 'no':
            exit = True


if __name__ == "__main__":
    args = parse_arguments()
    input_file = args.input
    if not os.path.isfile(input_file):
        print(f'File {input_file} not found, Creating!')
    main(input_file)
