import time
import os

def get_uptime():
    if os.name == "posix":
        # For Linux/Unix systems
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
        return uptime_seconds
    elif os.name == "nt":
        # For Windows systems
        import ctypes
        kernel32 = ctypes.windll.kernel32
        uptime_ms = kernel32.GetTickCount64()
        return uptime_ms / 1000.0
    else:
        raise NotImplementedError("Unsupported OS")

if __name__ == "__main__":
    uptime = get_uptime()
    print(f"System Uptime: {uptime:.2f} seconds")
