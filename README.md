# Clinical Trial Data Quality & Validation System

A Python and SQL-based project that simulates clinical trial data
management and data quality validation workflows.

The project uses synthetic clinical trial data to identify data
discrepancies, manage queries, validate corrected data, and generate
data quality reports.

## Project Objectives

- Simulate a clinical trial data management workflow using synthetic data.
- Store clinical trial data in a relational database.
- Perform SQL-based data validation and consistency checks.
- Identify missing, invalid, and inconsistent clinical data.
- Create and manage data queries for identified discrepancies.
- Track query resolution and closure.
- Analyse data quality using Python.
- Generate an Excel-based data quality report.

## Project Workflow

Clinical Trial Data
        ↓
Database Storage
        ↓
SQL Data Validation
        ↓
Discrepancy Identification
        ↓
Query Creation
        ↓
Site Response / Data Correction
        ↓
Query Verification
        ↓
Query Closure
        ↓
Python Data Quality Analysis
        ↓
Excel Quality Report

## Technologies Used

- Python
- SQL Server
- SQL
- pyodbc
- openpyxl
- Git
- Excel

## Validation Checks

The project includes validation checks across multiple clinical data domains:

### Vital Signs
- Invalid weight values
- Implausible systolic blood pressure values
- Missing vital sign records

### Laboratory Results
- Invalid laboratory values
- Missing laboratory results
- Subject and visit reconciliation

### Visits
- Subject and visit mismatches
- Visit date inconsistencies
- Missing expected visit data

### Adverse Events
- Missing event information
- Subject and visit consistency
- Date validation

### Medication Data
- Missing medication information
- Invalid medication date ranges
- Subject and visit consistency

### Cross-Table Validation
- Subject ID consistency across related tables
- Visit and clinical data reconciliation
- Identification of inconsistencies between related records

## Query Management

Discrepancies identified during validation were recorded as queries.

Each query contains:

- Query ID
- Subject ID
- Visit ID
- Field name
- Issue description
- Query text
- Status
- Resolution

### Query Lifecycle

Open → Answered → Closed

The project tracks queries from discrepancy identification through
resolution and final closure.

A total of **12 queries** were created and all **12 queries were closed**,
resulting in a **100% query closure rate**.

## Project Results

The synthetic clinical trial dataset contained **10 subjects**.

The validation process identified **12 data queries** across multiple
clinical data domains.

Key findings:

- Total queries: **12**
- Closed queries: **12**
- Open queries: **0**
- Query closure rate: **100%**
- Subjects with queries: **2 of 10 (20%)**
- Average queries per affected subject: **6.0**
- Highest query count by subject: **SUB003 (8 queries)**
- Highest query domains: **Vital Signs** and **Lab Results**
  with **3 queries each**

The results were analysed using Python and exported into an Excel-based
data quality report.

## Project Structure

```text
clinical-trial-data-quality/
│
├── documentation/
│   ├── clinical_data_flow.md
│   ├── validation_rules.md
│   └── query_management.md
│
├── python/
│   ├── data_quality_analysis.py
│   └── create_quality_report.py
│
├── reports/
│   └── data_quality_report.xlsx
│
├── src/
│   └── clinical_trial_data_quality/
│
├── README.md
├── pyproject.toml
└── uv.lock

## Documentation

The project includes documentation covering:

- **Clinical Data Flow** — overview of the clinical data review and query process.
- **Validation Rules** — validation checks used to identify data quality issues.
- **Query Management** — query lifecycle, statuses, and resolution process.

## Key Skills Demonstrated

- Clinical data validation
- Data quality review
- Query management and resolution
- SQL data analysis
- Cross-table data reconciliation
- Missing and inconsistent data identification
- Python-based data quality analysis
- Excel reporting
- Data documentation
- Quality-focused analytical thinking

## Data Privacy

This project uses completely synthetic clinical trial data created for
learning and demonstration purposes.

No real patient data, protected health information, or confidential
clinical trial data is used in this project.