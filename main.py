import Driver

def main():
    try:
        Driver.browser("chrome", "https://www.google.com/")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()