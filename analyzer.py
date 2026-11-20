from collections import Counter

def analyze_logs(file_path):
    severity_counts = Counter()
    critical_events = []

    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) < 4:
                continue
            timestamp = f"{parts[0]} {parts[1]}"
            level = parts[2]
            message = " ".join(parts[3:])

            severity_counts[level] += 1
            if level in ("ERROR", "CRITICAL"):
                critical_events.append(f"[{timestamp}] {level}: {message}")

    print("=== SERVER LOG SUMMARY ===")
    for level, count in severity_counts.items():
        print(f"{level}: {count}")

    print("\n=== ACTIONABLE ALERTS (ERROR & CRITICAL) ===")
    for event in critical_events:
        print(event)

if __name__ == "__main__":
    analyze_logs("server.log")
