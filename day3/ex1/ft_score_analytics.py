import sys


if __name__ == "__main__":
    usage = "No scores provided. Usage: python3 " \
        "ft_score_analytics.py <score1> <score2> ..."
    print("=== Player Score Analytics ===")
    if len(sys.argv) == 1:
        print(usage)
    else:
        scores: list[int] = []

        i = 1
        while i < len(sys.argv):
            try:
                score = int(sys.argv[i])
                scores = scores + [score]
            except ValueError:
                print(f"Invalid parameter: '{sys.argv[i]}'")
            i += 1
        if len(scores) == 0:
            print(usage)
        else:
            print(f"Scores processed: {scores}")
            print(f"Total players: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {(sum(scores) / len(scores)):.2f}")
            print(f"High score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
