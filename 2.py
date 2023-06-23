for index, row in df.iterrows():
    # Access row data using row[column_name]
    # Example: row['column_name']
    print(row['column_name'])
for column_name in df:
    # Access column data using df[column_name]
    # Example: df[column_name]
    print(df[column_name])
