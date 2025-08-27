import random

def get_difficulty():
    print("🎮 Number Guesser: Stats and Glory Edition™")
    print("Choose your difficulty:")
    print("1 - Easy (1-100, 7 guesses)")
    print("2 - Medium (1-500, 10 guesses)")
    print("3 - Hard (1-1000, 15 guesses)")
    print("4 - Impossible (1-9999, 30 guesses)")
    print("5 - IM-IM-IM-POSSIBLE (1-999999, 40 guesses)")

    while True:
        try:
            choice = int(input("Enter difficulty (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("🛑 Pick between 1 and 5, bruh.")
        except ValueError:
            print("💀 Not a number. Try again.")

def set_range_and_attempts(difficulty):
    settings = {
        1: (1, 100, 7),
        2: (1, 500, 10),
        3: (1, 1000, 15),
        4: (1, 9999, 30),
        5: (1, 999999, 40)
    }
    return settings[difficulty]

def save_stats(win, attempts_used, difficulty, total_guesses, secret_number):
    with open("ng_stats.txt", "a") as f:
        f.write(f"{'WIN' if win else 'LOSS'} | Difficulty {difficulty} | Guesses: {attempts_used} | "
                f"Secret: {secret_number} | Avg Distance: {round(total_guesses/attempts_used, 2)}\n")

def play_game():
    difficulty = get_difficulty()
    low, high, max_attempts = set_range_and_attempts(difficulty)
    secret_number = random.randint(low, high)
    total_distance = 0
    guesses = []

    print(f"\n🤖 I'm thinking of a number between {low} and {high}. You get {max_attempts} guesses.\n")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Guess #{attempt}: "))
            guesses.append(guess)
            distance = abs(guess - secret_number)
            total_distance += distance

            if guess < secret_number:
                print("📉 Too low.")
            elif guess > secret_number:
                print("📈 Too high.")
            else:
                print(f"\n🎯 CORRECT! You guessed the number {secret_number} in {attempt} tries!")
                avg_distance = round(total_distance / attempt, 2)
                print(f"📊 Average Distance from target: {avg_distance}")
                save_stats(True, attempt, difficulty, total_distance, secret_number)
                return
        except ValueError:
            print("⚠️ Please enter a valid number.")
    
    print(f"\n💀 Game over! You used all {max_attempts} guesses.")
    print(f"The number was: {secret_number}")
    avg_distance = round(total_distance / max_attempts, 2)
    print(f"📊 Average Distance from target: {avg_distance}")
    save_stats(False, max_attempts, difficulty, total_distance, secret_number)

if __name__ == "__main__":
    play_game()
