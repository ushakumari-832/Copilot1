import subprocess

def print_system_uptime():
    try:
        # Run the 'uptime' command on Unix/Linux/Mac systems
        uptime = subprocess.check_output(['uptime'], encoding='utf-8')
        print("System Uptime:", uptime.strip())
    except Exception as e:
        print("Could not get system uptime:", e)

if __name__ == "__main__":
    print_system_uptime()
