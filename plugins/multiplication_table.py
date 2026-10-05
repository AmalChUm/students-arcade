AUTHOR = "Shayan Shoukat"
APP_NAME = "Multiplication Table Generator"

def run():
    print("=== Multiplication Table Generator ===")
    try:
        number = int(input("Enter a number to generate its table: "))
        limit = int(input("Enter range limit (default 10): ") or "10")
        
        print(f"\nMultiplication Table for {number}:")
        for i in range(1, limit + 1):
            print(f"{number} x {i} = {number * i}")
    except ValueError:
        print("Invalid input! Please enter valid integers.")

if __name__ == "__main__":
    run()