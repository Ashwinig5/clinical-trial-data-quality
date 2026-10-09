import pyodbc
from openpyxl import Workbook
from openpyxl.styles import Font


connection_string = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=ClinicalTrialDB;Trusted_Connection=yes;TrustServerCertificate=yes;"

connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

print("Database connection successful")

cursor.execute("select count(*) from queries")
result = cursor.fetchone()
total_queries = result[0]

cursor.execute("SELECT COUNT(*) FROM Queries WHERE status = 'Closed'")
result = cursor.fetchone()
closed_queries = result[0]
closure_rate = (closed_queries / total_queries) * 100

workbook = Workbook()
worksheet = workbook.active
worksheet.title = "Quality Summary"

worksheet["A1"] = "Clinical Trial Data Quality Report"
worksheet["A1"].font = Font(size=16, bold=True)

worksheet["A3"] = "Total Queries"
worksheet["B3"] = total_queries

worksheet["A4"] = "Closed Queries"
worksheet["B4"] = closed_queries

worksheet["A5"] = "Query Closure Rate"
worksheet["B5"] = closure_rate/100
worksheet["B5"].number_format="0.0%"


cursor.execute("select count(*) from queries where status = 'Open'")
result = cursor.fetchone()
open_queries = result[0]

worksheet["A6"] = "Open Queries"
worksheet["B6"] = open_queries


cursor.execute("""
SELECT
    CASE
        WHEN field_name IN ('medication_name', 'end_date') THEN 'Medication Data'
        WHEN field_name IN ('systolic_bp', 'vitalsigns', 'weight_kg') THEN 'Vital Signs'
        WHEN field_name IN ('patient_result', 'test_name', 'Creatinine') THEN 'Lab Results'
        WHEN field_name = 'visit_date' THEN 'Visits'
        WHEN field_name = 'subject_id' THEN 'Data Consistency'
        WHEN field_name = 'event_term' THEN 'Adverse Events'
    END AS data_domain,
    COUNT(*) AS query_count
FROM Queries
GROUP BY
    CASE
        WHEN field_name IN ('medication_name', 'end_date') THEN 'Medication Data'
        WHEN field_name IN ('systolic_bp', 'vitalsigns', 'weight_kg') THEN 'Vital Signs'
        WHEN field_name IN ('patient_result', 'test_name', 'Creatinine') THEN 'Lab Results'
        WHEN field_name = 'visit_date' THEN 'Visits'
        WHEN field_name = 'subject_id' THEN 'Data Consistency'
        WHEN field_name = 'event_term' THEN 'Adverse Events'
    END
""")

domain_results = cursor.fetchall()

worksheet["A8"] = "Queries by Data Domain"
worksheet["A8"].font = Font(bold=True)
worksheet["A9"] = "Data Domain"
worksheet["A9"].font = Font(bold=True)
worksheet["B9"] = "Query Count"
worksheet["B9"].font = Font(bold=True)

row = 10

for data_domain, query_count in domain_results:
    worksheet[f"A{row}"] = data_domain
    worksheet[f"B{row}"] = query_count
    row += 1

highest_domain_count = max(query_count for data_domain, query_count in domain_results)

for data_domain, query_count in domain_results:
    if query_count == highest_domain_count:
        print(f"Highest Query Domain: {data_domain} ({query_count} queries)")

for data_domain, query_count in domain_results:
    print(f"{data_domain}: {query_count} queries")


cursor.execute("""
SELECT subject_id, COUNT(*) AS query_count
FROM Queries
GROUP BY subject_id
""")

subject_results = cursor.fetchall()

for subject_id, query_count in subject_results:
    print(f"{subject_id}: {query_count} queries")

worksheet["D8"] = "Queries by Subject"
worksheet["D8"].font = Font(bold=True)
worksheet["D9"] = "Subject ID"
worksheet["D9"].font = Font(bold=True)
worksheet["E9"] = "Query Count"
worksheet["E9"].font = Font(bold=True)

row = 10

for subject_id, query_count in subject_results:
    worksheet[f"D{row}"] = subject_id
    worksheet[f"E{row}"] = query_count
    row += 1

highest_subject_count = max(
    query_count for subject_id, query_count in subject_results
)

for subject_id, query_count in subject_results:
    if query_count == highest_subject_count:
        print(
            f"Highest Query Subject: {subject_id} "
            f"({query_count} queries)"
        )

query_counts = []

for subject_id, query_count in subject_results:
    query_counts.append(query_count)

average_queries = sum(query_counts) / len(query_counts)


print(f"Average Queries per Affected Subject: {average_queries:.1f}")

cursor.execute("SELECT COUNT(*) FROM Subjects")
result = cursor.fetchone()
total_subjects = result[0]

print(f"Total Subjects: {total_subjects}")

subjects_with_queries = len(subject_results)

subjects_with_queries_percentage = (
    subjects_with_queries / total_subjects
) * 100

print(
    f"Subjects with Queries: "
    f"{subjects_with_queries_percentage:.1f}%"
)

# Add summary metrics to Excel
worksheet["A20"] = "Subjects with Queries"
worksheet["B20"] = subjects_with_queries

worksheet["A21"] = "Subjects with Queries (%)"
worksheet["B21"] = subjects_with_queries_percentage/100
worksheet["B21"].number_format="0.0%"

worksheet["A22"] = "Average Queries per Affected Subject"
worksheet["B22"] = average_queries

worksheet.column_dimensions["A"].width = 32
worksheet.column_dimensions["B"].width = 18
worksheet.column_dimensions["D"].width = 20
worksheet.column_dimensions["E"].width = 18

workbook.save("reports/data_quality_report.xlsx")

print("Quality report created successfully")