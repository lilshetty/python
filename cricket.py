def calculate_run_rate(runs, balls):
    run_rate = (runs / balls) * 6
    return run_rate


def calculate_strike_rate(runs, balls):
    strike_rate = (runs / balls) * 100
    return strike_rate


def main():
    runs = 0
    balls = 0

    while True:
        score = input("Enter player score (enter 'q' to quit): ")
        if score.lower() == 'q':
            break

        runs += int(score)
        balls += 1

        run_rate = calculate_run_rate(runs, balls)
        strike_rate = calculate_strike_rate(runs, balls)

        print(f"Current Run Rate: {run_rate:.2f}")
        print(f"Current Strike Rate: {strike_rate:.2f}\n")

    print(f"Total Runs Scored: {runs}")
    print(f"Total Balls Faced: {balls}")
    print(f"Final Run Rate: {run_rate:.2f}")
    print(f"Final Strike Rate: {strike_rate:.2f}")


if __name__ == '__main__':
    main()
