import os
import shlex
import zipfile
from time import time

def bruteforce_zip(file_path, word_list):

    try:
        with zipfile.ZipFile(file_path) as zip_file:

            attempts = 0
            start_time = time()

            with open(word_list, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:

                    attempts += 1
                    password = line.strip()

                    try:
                        zip_file.extractall("output", pwd=password.encode())

                        total_time = time() - start_time

                        print("\n[+] Password Found")
                        print("[+] Password:", password)
                        print("[+] Time: %.2f seconds | %.2f attempts/sec"
                              % (total_time, attempts / total_time))

                        print("[+] Archive extracted to 'output/'")

                        return password

                    except RuntimeError:
                        continue

    except zipfile.BadZipFile:
        print(f"[!] Not a valid zip: {file_path}")
        return None

    print(f"[X] Password not found for {file_path}")
    return None


def extract_command(user_input_value):

    parts = shlex.split(user_input_value)

    if len(parts) < 2:
        print("[!] Usage: extract <archive_path> [password | wordlist]")
        return

    archive_path = parts[1]
    option = parts[2] if len(parts) == 3 else None

    if not os.path.isfile(archive_path):
        print(f"[!] Archive '{archive_path}' not found")
        return

    try:
        with zipfile.ZipFile(archive_path) as zip_ref:

            if option and os.path.isfile(option):

                print("[*] Starting bruteforce using wordlist:", option)
                password = bruteforce_zip(archive_path, option)

                if password:
                    print("[+] Extraction completed")

            elif option:

                zip_ref.extractall("output", pwd=option.encode())
                print(f"[+] Extracted using password: {option}")

            else:

                try:
                    zip_ref.extractall("output")
                    print("[+] Extracted without password")

                except RuntimeError:
                    print("[!] Archive requires a password")

    except zipfile.BadZipFile:
        print("[!] Invalid zip file")

    except RuntimeError:
        print("[!] Wrong password")

    except Exception as e:
        print("[!] Unexpected error:", e)