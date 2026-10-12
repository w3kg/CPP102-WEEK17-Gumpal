# Greenhouse Climate Monitoring System

**Student Name:** William Elis K. Gumpal
**Student Number:** 2601168
**Section:** 1CPE-A

## Project Description

This program monitors simulated greenhouse temperature and humidity readings.
It classifies each temperature as NORMAL, WARNING, or CRITICAL and each humidity
reading as LOW, WITHIN TARGET, or HIGH. It then prints a numerical summary with
an overall monitoring status. It was built for CPP102 Laboratory Exercise 17 and
uses only Python 3 built-in features.

## Features

- View all stored temperature and humidity readings
- Add a new reading (whole numbers from 0 to 100 only, for both temperature and humidity)
- Classify every reading
- Generate a summary: count, total, average, minimum, maximum, category counts and percentages, and overall status
- Show an average, minimum, and maximum for humidity
- Reject invalid menu choices and invalid readings without crashing

## Requirements

- Python 3 (no external packages)

## How to Run

1. Open a terminal inside the Week17 folder.
2. Type: `python device_monitor.py`
   (On macOS or Linux, type: `python3 device_monitor.py`)

## Sample Output

```
GREENHOUSE CLIMATE MONITORING SYSTEM
------------------------------------
[1] View Readings
[2] Add Reading
[3] Classify Readings
[4] Generate Summary
[5] Exit
Enter choice: 4

TEMPERATURE SUMMARY
-------------------
Number of readings : 5
Total of readings  : 160
Average temperature: 32.00 °C
Minimum temperature: 28 °C
Maximum temperature: 37 °C

NORMAL   : 2 (40.00%)
WARNING  : 2 (40.00%)
CRITICAL : 1 (20.00%)

Overall Status: ATTENTION REQUIRED

HUMIDITY SUMMARY
----------------
Average humidity: 61.60%
Minimum humidity: 55 %
Maximum humidity: 70 %
```

## Test Cases

I performed 10 tests. 10 passed and 0 failed. Full details are in
[test_cases.md](test_cases.md).

## Known Limitations

- Readings are lost when the program closes, because nothing is saved to a file.
- The temperature rules (below 30 NORMAL, 30 to 35 WARNING, above 35 CRITICAL) are
  classroom values for this simulation, not real safety or climate standards.
- The humidity ranges (below 40 LOW, 40 to 70 WITHIN TARGET, above 70 HIGH) are my own
  example values.
- The overall status uses temperature only, not humidity.
- Readings cannot be edited or deleted after they are added.
- Only whole numbers are accepted, so a reading such as 31.5 is rejected.

## Reflection

The hardest part was making all the functions work together by passing data through parameters. My program first crashed because two functions were empty, and I fixed it by letting `main()` read the lists directly. Testing also showed that empty input gave the wrong message, so I added a separate check for it. Next, I would like to save the readings so they aren't lost when the program closes.