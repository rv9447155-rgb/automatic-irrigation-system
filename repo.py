# Simple Irrigation System
# By Raj

rows = int(input("Enter number of rows: "))

print("\nMotor ON\n")

for r in range(1, rows + 1):
    print("Checking Row", r)

    sensor = int(input("Is the row wet? (0 = no, 1 = yes): "))

    while sensor == 0:
        print("Watering Row", r, "...")
        sensor = int(input("Is the row wet now? (0 = no, 1 = yes): "))

    print("Row", r, "is fully watered.\n")

print("All rows completed.")
print("Motor OFF")
