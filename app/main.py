from pathlib import Path

PROJECT_NAME = "System & AI Analyst Knowledge Helper"

def main() -> None:
    root = Path.cwd()

    print(PROJECT_NAME)
    print(f"Project root: {root}")

if __name__ == "__main__":
    main()