# Step #3C: Information The Spreadsheet Calculates

Course: Step #11: Tracking
System: Personal System
Skool link: https://www.skool.com/leadgenerationacademy/classroom/aaa118a0?md=9a5e1c4cb86748b88d79a0cd3ad6fd8e

---
![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/6037c93820104f4cb4d54d4656b7781e683b6bb818b34ae089322a3e92db6023-md.png)

### Prerequisites

- [Step #3B: Information You Enter](https://www.skool.com/leadgenerationacademy/classroom/aaa118a0?md=422a0bc07efe418d89db88b4ff3d0ec7) (Current Course)

### Example

![image](https://assets.skool.com/f/1d97a8218f0840a8a65c7970ccdf40ce/0ec85eb23bb44da3a84afad559572bb3c252fad32cba4ad3879897cd7688d8c7-md.png)

- [Filled In Time Tracking Spreadsheet Example](https://docs.google.com/spreadsheets/d/1250Evn3hwWJYKTZDXWcABE9LrIdctnRzazbRuNdxjdQ/edit?gid=1274574573#gid=1274574573) [in this skill: assets/templates/filled-in-time-tracking-spreadsheet-example/]

### Framework & Criteria

1. **Total Hours:** A count of how many Hour Time cells you filled in that day.
2. **Average Hours:** Only calculated on the Week and Total rows. The daily cells stay empty on purpose, because one day's average is the same as that day's Total Hours.
3. **4h Consistency:** True or false for whether you completed four or more hours that day. On the Week and Total rows it becomes a count of how many days you hit four.
4. **4h Efficiency:** 5 hours 15 minutes divided by the time from waking up to finishing Hour 4. Capped at 100%, as is every efficiency column.
5. **Hour 1 Efficiency:** 1 hour 30 minutes divided by the time from waking up to finishing Hour 1. That allowance is a 30 minute morning routine plus the hour itself.
6. **Hour 2 Efficiency:** 2 hours 45 minutes divided by the time from waking up to finishing Hour 2. Every hour after the first adds 75 minutes, the hour plus a 15 minute break.
7. **Hour 3 Efficiency:** 4 hours divided by the time from waking up to finishing Hour 3.
8. **Hour 4 Efficiency:** 5 hours 15 minutes divided by the time from waking up to finishing Hour 4, which is the same figure as 4h Efficiency.
9. **Hour 5 to Hour 10 Efficiency:** The same pattern, adding 75 minutes of allowance for every hour past the fourth.
10. **Week Rows:** The purple row under every seven days. It sums your hours, averages the efficiency columns, and counts how many days you hit four.
11. **Total Row:** The red row at the bottom of the tab. The same treatment across the whole month, skipping the Week rows so nothing gets counted twice.

### Step-by-Step Instructions

1. **Do not type into the calculated columns.** Every one of them builds itself off the Wake Up Time and Hour Times you entered in Step #3B. Type over one and it stops being a formula.
2. **Copy the entire header row and paste it into ChatGPT.** The whole row, so what comes back is in the same column order and drops straight in.
3. **Ask it for five realistic rows of tab-separated fake data with every calculated field blank.** Blank calculated fields are the whole point, since you are testing whether the sheet fills them in by itself.
4. **Tell it to use valid times in chronological order.** Hour 3 landing before Hour 2 gives you nonsense percentages that tell you nothing about whether the sheet works.
5. **Tell it to leave the later hour fields blank on days with fewer completed hours.** You want a couple of three hour days and a couple of long ones in there, otherwise you never see 4h Consistency flip.
6. **Paste the fake data into the spreadsheet.** Into the daily rows only, and keep off the purple Week rows.
7. **Confirm Total Hours counts the completed hours correctly.** A day with six hour times filled in should read 6.
8. **Confirm 4h Consistency changes based on whether four hours were completed.** True on the four hour days, false on the short ones. This is why you asked for uneven days.
9. **Confirm every efficiency calculation populates correctly.** A filled hour time with an empty efficiency cell beside it means the formula in that column did not survive.
10. **Confirm the weekly and monthly totals update correctly.** The purple Week row, the red Total row, and the matching row on the Dashboard tab.
11. **Clear only the fake input data.** The times and the notes. Leave the formulas, the calculated cells, the Week rows and the Total row exactly where they are.

### Completion Audit

- Did you avoid typing into the calculated columns?
- Did you copy the entire header row and paste it into ChatGPT?
- Did you ask it for five realistic rows of tab-separated fake data with every calculated field blank?
- Did you tell it to use valid times in chronological order?
- Did you tell it to leave the later hour fields blank on days with fewer completed hours?
- Did you paste the fake data into the spreadsheet?
- Does Total Hours count the completed hours correctly?
- Does 4h Consistency change based on whether four hours were completed?
- Does every efficiency calculation populate correctly?
- Do the weekly and monthly totals update correctly?
- Did you clear only the fake input data?
