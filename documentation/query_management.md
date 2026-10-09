# Query Management

## Overview

Queries are raised when a discrepancy or inconsistency is identified during
clinical data review.

A query is used to request clarification, confirmation, or correction from
the clinical trial site.

## Query Lifecycle

The query management process used in this project follows these steps:

1. Identify a discrepancy during data validation.
2. Create a query describing the identified issue.
3. Send the query to the clinical trial site for clarification or correction.
4. Review the site response or corrected data.
5. Verify that the discrepancy has been appropriately resolved.
6. Record the resolution.
7. Close the query.

## Query Status

Queries in the project use the following statuses:

- **Open** — The discrepancy has been identified and the query is awaiting
  a response or resolution.
- **Answered** — A response has been received from the site and is ready
  for review.
- **Closed** — The response or correction has been reviewed and the issue
  has been appropriately resolved.

## Query Information

Each query contains information such as:

- Query ID
- Subject ID
- Visit ID
- Field name
- Issue description
- Query text
- Status
- Resolution

This information allows discrepancies to be tracked from identification
through resolution.

## Query Examples

Examples of queries identified in this project include:

- Invalid weight value.
- Implausible systolic blood pressure value.
- Invalid hemoglobin result.
- Missing laboratory result.
- Missing vital signs record.
- Subject and visit mismatch.
- Incorrect visit date.
- Missing adverse event information.
- Medication end date occurring before the start date.
- Missing medication name.
- Medication and subject mismatch.

## Query Analysis

After query resolution, the query data was analysed using Python to
understand overall data quality.

The analysis included:

- Total number of queries.
- Number of closed queries.
- Query closure rate.
- Queries by field.
- Queries by subject.
- Highest-query subject.
- Queries by data domain.
- Highest-query data domain.
- Average queries per affected subject.
- Percentage of subjects with queries.