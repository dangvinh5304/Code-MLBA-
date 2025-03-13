import pandas as pd
import plotly.express as px

# Load the dataset
file_path = "dataset-416.xlsx"
xls = pd.ExcelFile(file_path)
df = pd.read_excel(xls, sheet_name='Sheet1')

# Filter out NaN values in 'Tên học phần' and 'Học Kỳ'
df_filtered = df[['Học Kỳ', 'Loại môn học', 'Tên học phần']].dropna()

# Convert semester numbers to string for better visualization
df_filtered['Học Kỳ'] = df_filtered['Học Kỳ'].astype(int).astype(str)

# Create a sunburst chart
fig = px.sunburst(df_filtered,
                  path=['Học Kỳ', 'Loại môn học', 'Tên học phần'],
                  title="Course Structure by Semester and Type",
                  width=900, height=900)

# Save the figure as an HTML file
chart_html = "sunburst_chart.html"
fig.write_html(chart_html)

# Generate the full HTML file
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nested Pie Chart</title>
</head>
<body>
    <h1>Course Structure by Semester and Type</h1>
    <iframe src="{chart_html}" width="100%" height="900px" style="border:none;"></iframe>
</body>
</html>
"""

# Save the full HTML file
full_html_file = "416_10k.html"
with open(full_html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML file generated: {full_html_file}")
