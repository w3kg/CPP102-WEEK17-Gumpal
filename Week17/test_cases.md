# Test Cases – Greenhouse Climate Monitoring System

Tested by: (William Elis K. Gumpal)        Date: (10/12/2026)

Each test was run in a fresh program session, starting from the initial data
(temperatures 28, 31, 35, 37, 29 and humidity 55, 60, 65, 70, 58).

| Test Case | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|
| TC01 | Choose 1 | Five readings: 28, 31, 35, 37, 29 | Showed Reading 1 to 5: 28, 31, 35, 37, 29 °C with their humidity values | Pass |
| TC02 | Choose 2, enter 33, then humidity 60 | "Reading added successfully." | "Reading added successfully." Choosing 1 then showed 6 readings, with 33 °C as Reading 6 | Pass |
| TC03 | Choose 2, enter abc | Rejected; list unchanged | "Invalid input. Enter a whole number only." Choosing 1 still showed 5 readings | Pass |
| TC04 | Choose 2, enter -5 | Rejected; list unchanged | "Invalid temperature. Enter a value from 0 to 100." Choosing 1 still showed 5 readings | Pass |
| TC05 | Choose 2, enter 120 | Rejected; list unchanged | "Invalid temperature. Enter a value from 0 to 100." Choosing 1 still showed 5 readings | Pass |
| TC06 | Choose 2, add 30 (humidity 60), then choose 3 | 30 °C -> WARNING | "Reading 6 : 30 °C -> WARNING \| 60 % humidity -> WITHIN TARGET" | Pass |
| TC07 | Choose 3 | 35 °C -> WARNING | "Reading 3 : 35 °C -> WARNING \| 65 % humidity -> WITHIN TARGET" | Pass |
| TC08 | Choose 4 (initial data) | Total 160, Avg 32.00, Min 28, Max 37, status ATTENTION REQUIRED | Number of readings 5, Total 160, Average 32.00 °C, Min 28 °C, Max 37 °C, NORMAL 2 (40.00%), WARNING 2 (40.00%), CRITICAL 1 (20.00%), Overall Status: ATTENTION REQUIRED | Pass |
| TC09 | Enter 9 at the menu | Error message; menu shown again | "Invalid choice. Please enter a number from 1 to 5." The menu was shown again | Pass |
| TC10 | Choose 5 | Exit message; program ends | "Thank you for using the Greenhouse Climate Monitoring System." The program ended | Pass |

## Bugs Found and Fixed

- I first tried to use separate functions,
  `get_initial_readings()` and `get_initial_humidity()`, to supply the two lists,
  it worked when the functions had return values of the index, but to lessen the line codes, I removed them
  and put `readings` and `humidity` on the first lines of the program, as the
  laboratory exercise instructs. And `main()` reads those lists directly.
- **Empty input showed the wrong message.** Pressing Enter with nothing typed
  said "Enter a whole number only." I added a separate empty-input check that
  shows "The reading cannot be empty." before the whole-number check.
- **Wrong success wording.** The message said "Readings added successfully."
  but the test expects "Reading added successfully." I changed it to singular.