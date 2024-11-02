import pandas as pd

def querydatatypes(dtype):
    if "int" in str(dtype):
        return "INT"
    elif "float" in str(dtype):
        return "FLOAT"
    elif "object" in str(dtype):
        return "VARCHAR(255)"
    elif "datetime" in str(dtype):
        return "DATETIME"
    else:
        return "TEXT"

def op1NF(primary_keys, df):
    primary_key = primary_keys[0] if len(primary_keys) == 1 else primary_keys
    table_name = "_".join(primary_key) + "_table" if isinstance(primary_key, list) else primary_key + "_table"
    query = f"CREATE TABLE {table_name} (\n"

    for column, dtype in zip(df.columns, df.dtypes):
        if column in primary_keys:
            query += f"  {column} {querydatatypes(dtype)} PRIMARY KEY,\n"
        else:
            query += f"  {column} {querydatatypes(dtype)},\n"

    query = query.rstrip(',\n') + "\n);"
    print(query)

def op2_3_bcnf_4_5(relations):
    for relation_name, relation in relations.items():
        primary_keys = relation_name if isinstance(relation_name, tuple) else (relation_name,)
        table_name = "_".join(primary_keys) + "_table"

        query = f"CREATE TABLE {table_name} (\n"
        
        for column, dtype in zip(relation.columns, relation.dtypes):
            if column in primary_keys:
                query += f"  {column} {querydatatypes(dtype)} PRIMARY KEY,\n"
            else:
                query += f"  {column} {querydatatypes(dtype)},\n"
        
        # Remove the last comma and add closing parenthesis
        query = query.rstrip(',\n') + "\n);"
        print(query)

