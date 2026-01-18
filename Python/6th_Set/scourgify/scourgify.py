import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if not input_file.lower().endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        with open(input_file, newline="") as in_file, open(output_file, "w", newline="") as out_file:
            reader = csv.DictReader(in_file)
            writer = csv.DictWriter(out_file, fieldnames = ["first", "last", "house"])
            writer.writeheader()

            for row in reader:
                last_name, first_name = row["name"].split(", ")
                house = row["house"]
                writer.writerow({"first": first_name, "last": last_name, "house": house})

    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")



if __name__ == "__main__":
    main()
