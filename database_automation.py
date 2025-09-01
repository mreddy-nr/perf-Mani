import psycopg2

try:
    conn = psycopg2.connect(
        dbname="ayasdi",
        user="ayasdi",
        password="rFt9f7YcvzZlI7kL",
        host="10.233.64.14",
        port="5432"
    )
    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    sql_statements = """
    truncate table subject_content cascade; 
    truncate table subject_data cascade;
    truncate table subject_events cascade; 
    truncate table subject_narrative cascade; 
    truncate table subject_relationships cascade; 
    truncate table subject_task_logs cascade; 
    truncate table subject_tasks cascade; 
    truncate table subjects cascade;
    truncate table detections cascade;
    truncate table detections cascade;
    truncate table subject_tasks cascade;
    truncate table subject_data cascade;
    """

    cur.execute(sql_statements)

    # Print all server notices (like pgAdmin)
    for notice in conn.notices:
        print(notice.strip())

    print(cur.statusmessage)  # Shows "TRUNCATE TABLE"
    print("Query returned successfully.")

except Exception as e:
    print("Error executing SQL statements:", e)
finally:
    if conn:
        conn.close()