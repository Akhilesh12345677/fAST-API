import pandas as pd
import sqlite3

# 1️⃣ Excel file ka path
excel_file = "smart_hr_system.xlsx"   # apni file ka naam yaha likho

# 2️⃣ Excel file read karo
df = pd.read_excel(excel_file)

print("Excel Data:")
print(df)

# 3️⃣ SQLite database create/connect
conn = sqlite3.connect("mydatabase.db")

# 4️⃣ Excel data ko SQLite table me save karo
df.to_sql("students", conn, if_exists="replace", index=False)

print("\nData successfully stored in SQLite!")

# 5️⃣ SQLite se data read karke show karo
query = "SELECT * FROM students"
result = pd.read_sql(query, conn)

print("\nData from SQLite:")
print(result)

# 6️⃣ Connection close karo
conn.close()
