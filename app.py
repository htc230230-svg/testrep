import sys

def main():
    print("Hello from Docker! This script is running inside a container.")
    print(f"Python version: {sys.version}")

if __name__ == "__main__":
    main()
