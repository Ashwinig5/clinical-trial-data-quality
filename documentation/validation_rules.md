# Data Validation Rules

## Overview

Data validation was performed to identify discrepancies in clinical trial
data and ensure that the data is accurate, complete, consistent, and valid.

The project included validation checks across vital signs, laboratory
results, visits, adverse events, and medication data.

## Validation Checks

### 1. Vital Signs Validation

Vital sign values were checked for abnormal or clinically implausible
values.

Examples:

- Weight should not contain an invalid value such as 0.
- Systolic blood pressure should not contain an extreme or implausible value.

Discrepancies identified:

- SUB002 had a weight value of 0 for Visit 7.
- SUB003 had a systolic blood pressure value of 350 for Visit 12.

These discrepancies were queried and corrected.

### 2. Missing Data Validation

The database was checked for missing data that was expected for a
particular subject and visit.

Examples:

- Missing vital signs for a visit.
- Missing laboratory results.
- Missing medication information.
- Missing adverse event information.

### 3. Laboratory Results Validation

Laboratory results were checked for abnormal or invalid values and
missing results.

Example:

- SUB003 had a hemoglobin result of -5, which was identified as an invalid
  value and corrected to 13.2.

Laboratory data was also reconciled with the corresponding subject and visit
to identify inconsistencies.

### 4. Visit and Date Validation

Visit data was checked for inconsistencies between the recorded visit and
related data.

Examples:

- Subject and visit mismatches.
- Incorrect visit dates.
- Missing data expected for a particular visit.

### 5. Medication Data Validation

Medication records were checked for missing or inconsistent information.

Examples:

- Missing medication name.
- Medication end date occurring before the start date.
- Medication subject not matching the expected subject.

### 6. Cross-Table Validation

Related tables were compared to identify inconsistencies between records.

Examples:

- Subject ID in a clinical data record not matching the subject assigned to
  the corresponding visit.
- Clinical data associated with an incorrect visit.
- Laboratory results associated with the wrong subject or visit.

## Validation Outcome

The identified discrepancies were converted into queries. Site responses or
corrections were reviewed, and the queries were closed after the discrepancy
was appropriately resolved.

The validated data was then used for data quality analysis.