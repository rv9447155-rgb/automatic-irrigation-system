Row-Based Automatic Irrigation System (Python)

**Created By:

Raj verma

Project Description

This project is a simple Python program that simulates an **automatic irrigation system** used in farming.
Each crop row has a small sensor wire:

* **0 = Row is dry (needs water)**
* **1 = Row is wet (fully watered)**

The program waters each row one by one.
When the sensor shows `1`, the program stops watering that row and moves to the next.
After all rows are watered, the **motor turns OFF automatically**.


**Features**

* Motor turns ON at the start
* Waters rows one-by-one
* Stops watering when row becomes wet
* Moves automatically to next row
* Turns OFF motor after all rows are complete
* Easy for beginners and great for school projects

 **How It Works (Simple Steps)**

1. User enters number of rows
2. Motor starts
3. For each row:

   * If sensor = 0 → water the row
   * If sensor = 1 → row is complete
4. After last row → motor turns OFF

 **Python Code**

python

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


**How to Run the Program**

1. Install Python on your computer
2. Save the code in a file like:

   ```
   irrigation.py
   ```
3. Open terminal / command prompt
4. Run the program using:

   python irrigation.py
5. Enter sensor values (0 or 1) when asked
 **Advantages**

* Saves water
* Reduces manual work
* Simple and easy to understand
* Good for school/college projec
*
*   **Conclusion**

This project shows how Python can help in agriculture by automating irrigation row by row.
It saves time, water, and effort while keeping farming simple and smart.
