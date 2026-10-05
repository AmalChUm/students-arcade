import time

AUTHOR = "Shayan Shoukat"
APP_NAME = "Countdown Message"

def run():
    print("=== Countdown Message ===")
    try:
        seconds = int(input("Enter countdown time in seconds: "))
        message = input("Enter completion message (or press Enter for default): ") or "Time's up!"
        
        print("Starting countdown...")
        for i in range(seconds, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        print(f"🎉 {message}")
    except ValueError:
        print("Invalid input! Please enter a valid integer for seconds.")

if __name__ == "__main__":
    run()