import pyodbc

connection_string = "DRIVER={ODBC Driver 18 for SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=ClinicalTrialDB;Trusted_Connection=yes;TrustServerCertificate=yes;"
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()
print("Database connection successful")


cursor.execute("select status, count(*) as query_count from queries group by status")
result = cursor.fetchall()

for status,query_count in result:
    print(status,query_count)

#Total Queries
cursor.execute("select count(*) from queries ")
result= cursor.fetchone()
total_queries = result[0]
print(f"Total Queries : {total_queries}")

#closed Queries
cursor.execute("select count (*) from queries where status='closed'")
result = cursor.fetchone()
closed_queries = result[0]
print(f"Closed Queries : {closed_queries}")

#query closure rate
closure_rate = (closed_queries/total_queries) * 100 
print(f"Query Closure Rate : {closure_rate:.1f}%")


#queries by field
cursor.execute("select field_name, count(*) as query_count from queries group by field_name")
result = cursor.fetchall()
for field_name, query_count in result:
    print(f"{field_name}:{query_count} queries")


#find the highest query field
query_counts =[]
for field_name, query_count in result:
    query_counts.append(query_count)
max_queries= max(query_counts)


#get the field name associalted with that maximum
query_counts =[]
for field_name, query_count in result:
    if query_count == max_queries:
        print(f"Highest Query Field: {field_name} ({query_count} queries)")


#queries by subject
cursor.execute("select subject_id, count(*) as query_count from queries group by subject_id")
result = cursor.fetchall()
for subject_id, query_count in result:
    print(f"{subject_id}: {query_count} queries")


#find the highest query subject 
query_counts =[]
for subject_id, query_count in result:
    query_counts.append(query_count)
max_queries = max(query_counts)


#find which subject has those 8 queries
for subject_id,query_count in result:
    if query_count == max_queries:
        print(f"Highest Query Subject: {subject_id} ({query_count} queries)")


#query domain classification
cursor.execute("""
select field_name,
case
when field_name in ('medication_name', 'end_date') then 'Medication data'
when field_name in ('systolic_bp','vitalsigns','weight_kg') then 'Vital signs'
when field_name in ('patient_result','test_name','Creatinine') then 'Lab results'
when field_name = 'visit_date' then 'Visits'
when field_name = 'subject_id' then 'Data Consistency'
when field_name = 'event_term' then 'Adverse Events'
end as data_domain
from queries """)
result = cursor.fetchall()
for field_name, data_domain in result:
    print(f"{field_name}:{data_domain}")


#count queries by domain
domain_counts={}
for field_name, data_domain in result:
    if data_domain in domain_counts:
        domain_counts[data_domain]+=1
    else:
        domain_counts[data_domain]=1
print(domain_counts)

max_counts= max(domain_counts.values())


for data_domain, query_count in domain_counts.items():
    if query_count == max_counts:
        print(f"Highest Query Domain: {data_domain} ({query_count} queries)")

#domain percentage
for data_domain, query_count in domain_counts.items():
    percentage = (query_count/total_queries)*100
    print(f"{data_domain}:{percentage:.1f}%")


#average queries per affected subject
cursor.execute("""
select subject_id, count(*) as query_count 
from queries
group by subject_id""")
result = cursor.fetchall()

query_counts =[]
for subject_id, query_count in result:
   query_counts.append(query_count)
average=sum(query_counts)/len(query_counts)
print(f"Average Queries per Subject:{average:.1f}")

subject_count=[]
for r in result:
    subject_id,query_count=r
    subject_count.append(subject_id)



#subject with queries
cursor.execute("select count(*) from subjects")
result= cursor.fetchone()
total_subjects= result[0]


percentage = (len(subject_count)/total_subjects)*100
print(f"Subjects with Queries: {percentage:.1f}%")