#!/usr/bin/env python3
# ============================================================
#   Tool    : ZipReaper
#   Author  : Tayyab Akhtar
#   Purpose : Educational Demonstration Only
#   Version : 1.0
#   Platform: Ubuntu
# ============================================================

import zipfile
import time
import sys
import os
from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

# ============================================================
#   COLORS
# ============================================================
RED     = Fore.RED    + Style.BRIGHT
GREEN   = Fore.GREEN  + Style.BRIGHT
YELLOW  = Fore.YELLOW + Style.BRIGHT
CYAN    = Fore.CYAN   + Style.BRIGHT
WHITE   = Fore.WHITE  + Style.BRIGHT
BLUE    = Fore.BLUE   + Style.BRIGHT
MAGENTA = Fore.MAGENTA + Style.BRIGHT
RESET   = Style.RESET_ALL

# ============================================================
#   LOGO
# ============================================================
def print_logo():
    os.system('clear')
    print(RED + r"""
███████╗██╗██████╗ ██████╗ ███████╗ █████╗ ██████╗ ███████╗██████╗ 
╚══███╔╝██║██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██╔══██╗
  ███╔╝ ██║██████╔╝██████╔╝█████╗  ███████║██████╔╝█████╗  ██████╔╝
 ███╔╝  ██║██╔═══╝ ██╔══██╗██╔══╝  ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
███████╗██║██║     ██║  ██║███████╗██║  ██║██║     ███████╗██║  ██║
╚══════╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
    """ + RESET) 

    print(CYAN + """
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║         ZIP FILE DICTIONARY ATTACK SIMULATOR             ║
    ║                                                          ║
    ╠══════════════════════════════════════════════════════════╣
    ║                                                          ║
    ║   Developer  :  Tayyab Akhtar                            ║
    ║   Purpose    :  Educational Demonstration Only           ║
    ║   Version    :  1.0                                      ║
    ║   Platform   :  Ubuntu                                   ║
    ║   Tool Name  :  ZipReaper                                ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """ + RESET)

# ============================================================
#   DISCLAIMER
# ============================================================
def print_disclaimer():
    print(YELLOW + """
    ╔══════════════════════════════════════════════════════════╗
    ║                   LEGAL DISCLAIMER                       ║
    ╠══════════════════════════════════════════════════════════╣
    ║                                                          ║
    ║   This tool is created for EDUCATIONAL PURPOSES ONLY.    ║
    ║                                                          ║
    ║   By using this tool you confirm that:                   ║
    ║                                                          ║
    ║   [✓]  You own the ZIP file you are testing              ║
    ║   [✓]  You have permission to test this file             ║
    ║   [✓]  You will not use this for illegal purposes        ║
    ║   [✓]  You understand unauthorized access is a crime     ║
    ║                                                          ║
    ║   Unauthorized use violates:                             ║
    ║   •  PAKISTAN — PECA 2016 Section 3,4,5,14,16            ║
    ║   •  Computer Fraud and Abuse Act (USA)                  ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """ + RESET)
    time.sleep(1)

# ============================================================
#   ATTACK CONFIGURATION
# ============================================================
def print_config(zip_file, wordlist, total):
    print(CYAN + """
    ╔══════════════════════════════════════════════════════════╗
    ║                  ATTACK CONFIGURATION                    ║
    ╠══════════════════════════════════════════════════════════╣""" + RESET)
    print(CYAN + f"    ║   Target ZIP   :  {zip_file:<40}║")
    print(CYAN + f"    ║   Wordlist     :  {wordlist:<40}║")
    print(CYAN + f"    ║   Total Pass   :  {total:<40,}║")
    print(CYAN + f"    ║   Attack Type  :  {'Dictionary Attack':<40}║")
    print(CYAN + f"    ║   Started At   :  {time.strftime('%Y-%m-%d %H:%M:%S'):<40}║")
    print(CYAN + """   ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """ + RESET)

# ============================================================
#   PROGRESS BAR
# ============================================================
def print_progress(attempts, total,
                   password, start_time):
    elapsed    = time.time() - start_time
    speed      = attempts / elapsed if elapsed > 0 else 0
    percentage = (attempts / total) * 100
    filled     = int(percentage / 5)
    bar        = "█" * filled + "░" * (20 - filled)

    print(GREEN +
          f"\r    [✗] [{bar}] "
          f"{percentage:.1f}% | "
          f"{attempts:,}/{total:,} | "
          f"{speed:,.0f}/sec | "
          f"Trying: {password:<15}"
          + RESET, end='', flush=True)

# ============================================================
#   SUCCESS BANNER
# ============================================================
def print_success(password, attempts,
                  elapsed, speed):
    print("\n")
    print(RED + """
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║   ██████╗ ██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗║
    ║  ██╔════╝ ██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗║
    ║  ██║      ██████╔╝███████║██║     █████╔╝ █████╗  ██║  ██║║
    ║  ██║      ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██║  ██║║
    ║  ╚██████╗ ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██████╔╝║
    ║   ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """ + RESET)

    print(RED + "    ╔══════════════════════════════════════════════════════════╗")
    print(RED + "    ║                    ATTACK RESULTS                        ║")
    print(RED + "    ╠══════════════════════════════════════════════════════════╣")
    print(RED + f"    ║   Status        :  PASSWORD FOUND!{' '*23}║")
    print(RED + f"    ║   Password      :  {password:<40}║")
    print(RED + f"    ║   Total Attempts:  {attempts:<40,}║")
    print(RED + f"    ║   Time Taken    :  {str(round(elapsed,2))+' seconds':<40}║")
    print(RED + f"    ║   Attack Speed  :  {str(round(speed))+' passwords/sec':<40}║")
    print(RED + "    ╠══════════════════════════════════════════════════════════╣")
    print(RED + "    ║                                                          ║")
    print(RED + "    ║   SECURITY LESSON:                                       ║")
    print(RED + "    ║   This password exists in the RockYou wordlist!          ║")
    print(RED + "    ║   Weak passwords can be cracked in seconds!              ║")
    print(RED + "    ║   NEVER use common or dictionary words as passwords!     ║")
    print(RED + "    ║                                                          ║")
    print(RED + "    ╚══════════════════════════════════════════════════════════╝")
    print(RESET)

# ============================================================
#   FAILURE BANNER
# ============================================================
def print_failure(attempts, elapsed, speed):
    print("\n")
    print(GREEN + """
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║   ███████╗ █████╗ ███████╗███████╗██╗                    ║
    ║   ██╔════╝██╔══██╗██╔════╝██╔════╝██║                    ║
    ║   ███████╗███████║█████╗  █████╗  ██║                    ║
    ║   ╚════██║██╔══██║██╔══╝  ██╔══╝  ╚═╝                    ║
    ║   ███████║██║  ██║██║     ███████╗██╗                    ║
    ║   ╚══════╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝                    ║
    ║                                                          ║
    ║         PASSWORD NOT FOUND — STRONG PASSWORD!            ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """ + RESET)

    print(GREEN + "    ╔══════════════════════════════════════════════════════════╗")
    print(GREEN + "    ║                    ATTACK RESULTS                        ║")
    print(GREEN + "    ╠══════════════════════════════════════════════════════════╣")
    print(GREEN + f"    ║   Status        :  PASSWORD NOT FOUND{' '*21}║")
    print(GREEN + f"    ║   Total Attempts:  {attempts:<40,}║")
    print(GREEN + f"    ║   Time Taken    :  {str(round(elapsed,2))+' seconds':<40}║")
    print(GREEN + f"    ║   Attack Speed  :  {str(round(speed))+' passwords/sec':<40}║")
    print(GREEN + "    ╠══════════════════════════════════════════════════════════╣")
    print(GREEN + "    ║                                                          ║")
    print(GREEN + "    ║   SECURITY LESSON:                                       ║")
    print(GREEN + "    ║   This password is NOT in the RockYou wordlist!          ║")
    print(GREEN + "    ║   Strong passwords successfully resist attacks!          ║")
    print(GREEN + "    ║   Always use complex passwords with 12+ characters!      ║")
    print(GREEN + "    ║                                                          ║")
    print(GREEN + "    ╚══════════════════════════════════════════════════════════╝")
    print(RESET)

# ============================================================
#   RECOMMENDATIONS
# ============================================================
def print_recommendations():
    print(MAGENTA + """
    ╔══════════════════════════════════════════════════════════╗
    ║                SECURITY RECOMMENDATIONS                  ║
    ╠══════════════════════════════════════════════════════════╣
    ║                                                          ║
    ║   [1]  Use passwords with 12+ characters                 ║
    ║   [2]  Mix uppercase, lowercase, numbers, symbols        ║
    ║   [3]  Never use dictionary words as passwords           ║
    ║   [4]  Use a password manager (Bitwarden, LastPass)      ║
    ║   [5]  Enable Two-Factor Authentication (2FA)            ║
    ║   [6]  Never reuse passwords across accounts             ║
    ║   [7]  Change passwords regularly                        ║
    ║   [8]  Use AES-256 encryption for ZIP files              ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """ + RESET)

# ============================================================
#   FOOTER
# ============================================================
def print_footer():
    print(WHITE + """
    ╔══════════════════════════════════════════════════════════╗
    ║                                                          ║
    ║       Thank you for using ZipReaper v1.0                 ║
    ║       Developed by  :  Tayyab Akhtar                     ║
    ║       Purpose       :  Educational Only                  ║
    ║       Remember      :  Stay Ethical. Stay Legal.         ║
    ║                                                          ║
    ╚══════════════════════════════════════════════════════════╝
    """ + RESET)

# ============================================================
#   MAIN ATTACK FUNCTION
# ============================================================
def dictionary_attack(zip_file, wordlist):

    # Check ZIP file
    if not os.path.exists(zip_file):
        print(RED +
              f"\n    [ERROR] ZIP file "
              f"'{zip_file}' not found!"
              + RESET)
        print(YELLOW +
              f"    [INFO]  Check the filename "
              f"and try again."
              + RESET)
        return None

    # Check wordlist
    if not os.path.exists(wordlist):
        print(RED +
              f"\n    [ERROR] Wordlist "
              f"'{wordlist}' not found!"
              + RESET)
        print(YELLOW +
              f"    [INFO]  Make sure rockyou.txt "
              f"is in the same folder."
              + RESET)
        return None

    # Open ZIP
    try:
        zf = zipfile.ZipFile(zip_file)
    except zipfile.BadZipFile:
        print(RED +
              "\n    [ERROR] Invalid ZIP file!"
              + RESET)
        return None

    # Load wordlist
    try:
        with open(wordlist, 'r',
                  encoding='latin-1') as f:
            passwords = f.readlines()
    except Exception as e:
        print(RED +
              f"\n    [ERROR] Could not open "
              f"wordlist: {e}"
              + RESET)
        return None

    total = len(passwords)

    # Print configuration
    print_config(zip_file, wordlist, total)

    # Info messages
    print(YELLOW +
          "    [*]  Wordlist loaded successfully"
          + RESET)
    print(YELLOW +
          "    [*]  Incorrect passwords shown "
          "in GREEN"
          + RESET)
    print(YELLOW +
          "    [*]  Correct password shown "
          "in RED"
          + RESET)
    print(YELLOW +
          "    [*]  Starting attack..."
          + RESET)
    print()

    # Countdown
    for i in range(3, 0, -1):
        print(CYAN +
              f"    [*]  Attack starts in {i}..."
              + RESET)
        time.sleep(1)

    print()

    # Start attack
    start_time = time.time()
    attempts   = 0

    for password in passwords:
        password = password.strip()
        attempts += 1

        # Show progress every 10000 attempts
        if attempts % 10000 == 0:
            print_progress(attempts, total,
                           password, start_time)

        try:
            zf.extractall(pwd=password.encode())

            # PASSWORD FOUND
            elapsed = time.time() - start_time
            speed   = (attempts / elapsed
                       if elapsed > 0 else 0)
            print_success(password, attempts,
                          elapsed, speed)
            return password

        except RuntimeError:
            continue
        except Exception:
            continue

    # PASSWORD NOT FOUND
    elapsed = time.time() - start_time
    speed   = (attempts / elapsed
               if elapsed > 0 else 0)
    print_failure(attempts, elapsed, speed)
    return None

# ============================================================
#   MAIN PROGRAM
# ============================================================
def main():

    # Print logo
    print_logo()
    time.sleep(1)

    # Print disclaimer
    print_disclaimer()

    # Get user input
    print(WHITE + """
    ╔══════════════════════════════════════════════════════════╗
    ║                    ENTER DETAILS                         ║
    ╚══════════════════════════════════════════════════════════╝
    """ + RESET)

    zip_file = input(CYAN +
                     "    [?]  Enter ZIP filename "
                     "(example: weak.zip): "
                     + RESET).strip()

    wordlist = "rockyou.txt"

    print()
    print(YELLOW +
          f"    [*]  Target   : {zip_file}"
          + RESET)
    print(YELLOW +
          f"    [*]  Wordlist : {wordlist}"
          + RESET)
    print()

    confirm = input(CYAN +
                    "    [?]  Start attack? "
                    "(yes/no): "
                    + RESET).strip().lower()

    if confirm != 'yes':
        print(RED +
              "\n    [!]  Attack cancelled "
              "by user."
              + RESET)
        print_footer()
        return

    print()

    # Run attack
    result = dictionary_attack(zip_file, wordlist)

    # Print recommendations
    print_recommendations()

    # Print footer
    print_footer()


# ============================================================
#   RUN
# ============================================================
if __name__ == "__main__":
    main()
