import sqlite3
from tabulate import tabulate


def fetch_results():
    conn = sqlite3.connect('benchmark_results.db')
    cursor = conn.cursor()

    cursor.execute('SELECT id, score, timestamp, processor_name, benchmark_type FROM results')
    rows = cursor.fetchall()

    conn.close()

    return rows


def display_results(results):
    headers = ["ID", "Score", "Timestamp", "Processor", "Benchmark Type"]
    print(tabulate(results, headers, tablefmt="pretty"))


if __name__ == "__main__":
    results = fetch_results()
    if results:
        display_results(results)
    else:
        print("No results found.")