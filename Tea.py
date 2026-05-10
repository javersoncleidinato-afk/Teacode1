import time

tea_times = {
    "green": 2 * 60,
    "black": 4 * 60,
    "white": 3 * 60,
    "oolong": 5 * 60,
    "herbal": 7 * 60
}

print("Available teas:", ", ".join(tea_times.keys()))
tea = input("Choose your tea: ").lower()

if tea not in tea_times:
    print("Unknown tea type. Try again.")
else:
    seconds = tea_times[tea]
    print(f"Steeping {tea} tea for {seconds//60} minutes...")

    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("\nYour tea is ready! ☕")
