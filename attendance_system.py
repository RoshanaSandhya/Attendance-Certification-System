import pandas as pd

df1 = pd.read_csv("meetinglistdetails_2026_05_29_2026_05_29.csv")
df2 = pd.read_csv("meetinglistdetails_2026_05_30_2026_05_30.csv")

print("FILE 1 Columns:")
print(df1.columns)

print("\nFILE 2 Columns:")
print(df2.columns)

print("\nFILE 1 Topics:")
print(df1["Topic"].unique())

print("\nFILE 2 Topics:")
print(df2["Topic"].unique())


import pandas as pd

# CSV files
file1 = "meetinglistdetails_2026_05_29_2026_05_29.csv"
file2 = "meetinglistdetails_2026_05_30_2026_05_30.csv"

# Read files
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# Combine both files
df = pd.concat([df1, df2], ignore_index=True)

# Required columns only
df = df[[
    "Topic",
    "Name (original name)",
    "Email",
    "Duration (minutes)",
    "Duration (minutes).1"
]]

# Convert duration columns to numbers
df["Duration (minutes)"] = pd.to_numeric(df["Duration (minutes)"], errors="coerce")
df["Duration (minutes).1"] = pd.to_numeric(df["Duration (minutes).1"], errors="coerce")

# Student attendance percentage per meeting
df["Attendance Percentage"] = (
    df["Duration (minutes).1"] / df["Duration (minutes)"]
) * 100

# Eligibility status
df["Certificate Status"] = df["Attendance Percentage"].apply(
    lambda x: "Eligible for Certificate" if x >= 75 else "Not Eligible for Certificate"
)

# Final result columns
result = df[[
    "Topic",
    "Name (original name)",
    "Email",
    "Duration (minutes)",
    "Duration (minutes).1",
    "Attendance Percentage",
    "Certificate Status"
]]

# Round percentage
result["Attendance Percentage"] = result["Attendance Percentage"].round(2)

# Save output
result.to_csv("attendance_certificate_result.csv", index=False)

print(result.head(20))
print("\nResult file created: attendance_certificate_result.csv")
