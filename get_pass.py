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
        python get_pass.py -i users.txt -p passwords_list.txt"""
    parser = argparse.ArgumentParser(description="Storing Hashing passwords",
                                     epilog=example_usage,
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument("-i", "--input", required=True,
                        help="Input users file")
    parser.add_argument("-p", "--passwords", required=True,
                        help="Passwords list file")

    return parser.parse_args()



def main(passwords: str, users: str) -> None:
    """
    Main function opens files and check hashes

    Args:
        passwords (str): txt file with common passwords
        users (str): txt file containing usernames with passwords
    """
    with open(users, 'r') as u:
        for user_line in u.readlines():
            with open(passwords, 'r') as p:
                for password in p.readlines():
                    user_name, user_pass = user_line.split('\n')[0].split(':')[0], user_line.split('\n')[0].split(':')[1]
                    encoded = password.strip().encode()
                    hashed = hashlib.sha256(encoded).hexdigest()
                    if user_pass == hashed:
                        print(f'Password for user: {user_name} found and is {password.strip()}!')
                        with open(user_name + '.txt', 'w') as f:
                            f.write(f'{user_name}:{password.strip()}')
                        break



if __name__ == "__main__":
    args = parse_arguments()
    input_file = args.input
    if not os.path.isfile(input_file):
        raise Exception(f'File {input_file} not found!')
    passwords_file = args.passwords
    if not os.path.isfile(input_file):
        raise Exception(f'File {input_file} not found!')
    main(passwords_file, input_file)
