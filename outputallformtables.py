# output generating as per userschoice
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


def op1NF(Primarykeys, df):
    Primarykey = list(df.keys())[0]
    table_name = "_".join(Primarykey) + "_table"
    df = df[Primarykey]
    query = f"CREATE TABLE {table_name} (\n"

    for column, dtype in zip(df.columns, df.dtypes):
        if column in Primarykeys:
            query += f"  {column} {querydatatypes(dtype)} PRIMARY KEY,\n"
        else:
            query += f"  {column} {querydatatypes(dtype)},\n"

    query = query.rstrip(',\n') + "\n);"

    print(query)


def op2_3_bcnf_4_5(relations):
    for relation_name, relation in relations.items():
        Primarykeys = relation_name
        Primarykeys = (Primarykeys,) if isinstance(
            Primarykeys, str) else Primarykeys
        table_name = "_".join(Primarykeys) + '_table'

        if table_name.count('_') >= 2:
            query = f"CREATE TABLE {table_name} (\n"

            for column, dtype in zip(relation.columns, relation.dtypes):
                if column in Primarykeys:
                    query += f" FOREIGN KEY ({column}) REFERENCES {column.replace('_fk','')}_table({column.replace('_fk','')}),\n"
                else:
                    query += f"  {column} {querydatatypes(dtype)},\n"

            query = query.rstrip(',\n') + "\n);"
        else:
            query = f"CREATE TABLE {table_name} (\n"

            for column, dtype in zip(relation.columns, relation.dtypes):
                if column in Primarykeys:
                    query += f"  {column} {querydatatypes(dtype)} PRIMARY KEY,\n"
                else:
                    query += f"  {column} {querydatatypes(dtype)},\n"

            query = query.rstrip(',\n') + "\n);"

        print(query)

