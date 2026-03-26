import os
import time

def monitor_system():
    print("CyberTrace Engine Started...\n")
    
    while True:
        print("Monitoring system processes...")
        processes = os.popen('tasklist').read()
        
        if "cmd.exe" in processes:
            print("[ALERT] Command Prompt detected!")
        
        time.sleep(5)

if __name__ == "__main__":
    monitor_system()
