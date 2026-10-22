# User Manual 
## Program for Calculating the Sum of Digits After the Decimal Separator 
### Purpose
The application is designed to calculate the sum of digits located after the decimal separator in a floating-point number entered by the user.

In addition, the software provides logging of calculations, backup creation, and restoration of log files. 

### Features 
The program allows the user to: 
- calculate the sum of digits after the decimal separator; 
- process numbers entered with either a dot or a comma; 
- display calculation results in a graphical user interface; 
- save calculation results to a log file; 
- create backup copies of logs; 
- restore logs from backup copies; 
- store the history of performed calculations. 

### System Requirements 
The following software is required: 
- Windows 10 or later; 
- Python 3.10 or later; 
- Tkinter library.

### Running the Application

To start the program:

1. Open the project in PyCharm.
2. Make sure all project files are available.
3. Open the file main.py.
4. Click the Run button.
5. Wait until the main window appears.

After startup, the graphical interface will become available.

### Using the Program

#### Performing a Calculation

To calculate the sum of digits after the decimal separator:

1. Enter a floating-point number.
2. Click the "Calculate" button.
3. View the displayed result.

**Example:**

Input:

15.378

Decimal part:

378

Result:

18

#### Creating a Backup

To create a backup copy:

1. Start the application.
2. Click the "Create Backup" button.
3. Wait for the confirmation message.

The backup file will be saved in the backup directory.

#### Restoring a Log File

To restore the log file:

1. Click the "Restore Log" button.
2. Wait until the restoration process is completed.
3. Verify that the log data has been restored correctly.
### Error Handling

If the entered value is invalid, the program displays an error message and requests correct input.

Examples of invalid input:

- abc
- test123
- 12.34.56

In such cases, the calculation will not be performed.

### Data Storage

All calculation results are automatically written to the log file.

Each log entry contains:

- date;
- time;
- input value;
- calculation result.
### Exiting the Program

To close the application, simply close the main window using standard operating system tools.

All saved data will remain available for future use.

_Author: Filatova Julia ISP-31_