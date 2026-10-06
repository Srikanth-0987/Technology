"""
DAY 2 — DATA GENERATOR
Run this ONCE. It creates your own personal dataset: day02_usage.csv

Every student gets the SAME COLUMNS and DIFFERENT NUMBERS.
Your answers will not match your neighbour's. Copying is pointless.

HOW TO RUN
  1. Save this file as generate_app_usage.py
  2. Change ROLL_NUMBER below to YOUR roll number
  3. python generate_app_usage.py
  4. Confirm day02_usage.csv appeared in the same folder
"""

import matplotlib.pyplot as plt
import csv
import random

# ---------------------------------------------------------------
# CHANGE THIS LINE ONLY
ROLL_NUMBER = "25245A6627"
# ---------------------------------------------------------------

APPS = ["Chat", "Video", "Study", "Games"]

# Personality profiles: (weekday_base, weekend_base, spread)
PROFILES = {
    "Chat":  (55, 80, 22),
    "Video": (70, 130, 35),
    "Study": (95, 45, 30),
    "Games": (30, 90, 28),
}


def build_rows(seed_text):
    rng = random.Random(seed_text)
    rows = []
    for day in range(1, 31):
        weekend = (day % 7) in (6, 0)
        row = {"Day": day}
        for app in APPS:
            weekday_base, weekend_base, spread = PROFILES[app]
            base = weekend_base if weekend else weekday_base
            value = int(rng.gauss(base, spread))
            # a few realistic zero days
            if rng.random() < 0.05:
                value = 0
            row[app] = max(0, value)
        rows.append(row)
    return rows


def main():
    rows = build_rows(ROLL_NUMBER)
    with open("day02_usage.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Day"] + APPS)
        writer.writeheader()
        writer.writerows(rows)

    print("Created day02_usage.csv")
    print("Rows:", len(rows), " Columns:", ["Day"] + APPS)
    print("Seed used:", ROLL_NUMBER)
    print()
    print("First 3 rows:")
    for r in rows[:3]:
        print(r)


if __name__ == "__main__":
    main()