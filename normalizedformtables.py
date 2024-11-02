import pandas as pd
from itertools import combinations
import re

def list_or_set(item):
    return isinstance(item, (list, set))

def superkey(relation, determinant):
    grouped = relation.groupby(list(determinant)).size().reset_index(name='count')
    return not any(grouped['count'] > 1)

def closure(attributes, fds):
    closure_set = set(attributes)
    while True:
        before_closure = closure_set.copy()
        for det, dep in fds.items():
            if set(det).issubset(closure_set):
                closure_set.update(dep)
        if before_closure == closure_set:
            break
    return closure_set

def bcnf_decompose(relation, fds):
    decomposed = []
    for det, dep in fds.items():
        closure_set = closure(det, fds)
        if not closure_set.issuperset(relation.columns):
            cols = list(det) + dep
            if set(cols).issubset(relation.columns) and set(cols) != set(relation.columns):
                new_table = relation[list(det) + dep].drop_duplicates()
                decomposed.append(new_table)
                relation = relation.drop(columns=dep)
    return [relation] + decomposed if decomposed else [relation]

def is_one_nf(relation):
    for col in relation.columns:
        if relation[col].apply(lambda x: isinstance(x, (list, set, dict))).any():
            return False
    return True

def is_two_nf(primary_key, fds, relation):
    non_prime_attrs = [col for col in relation.columns if col not in primary_key]
    for det, dep in fds.items():
        if set(det).issubset(primary_key) and set(det) != set(primary_key):
            if any(attr in non_prime_attrs for attr in dep):
                return False
    return True

def is_three_nf(relations, fds):
    primary_keys = [key for key in fds]
    non_key_attrs = {item for sublist in fds.values() for item in sublist}
    for relation in relations.values():
        for det, dep in fds.items():
            if set(det).issubset(set(relation.columns)) and not set(det).issubset(primary_keys) and set(dep).issubset(non_key_attrs):
                return False
    return True

def is_bcnf(relations, primary_key, fds):
    for relation in relations.values():
        all_attrs = set(relation.columns)
        for det, dep in fds.items():
            if any(attr not in det for attr in dep):
                if all_attrs - closure(det, fds):
                    return False
    return True

def is_four_nf(relations, mvd_fds):
    for relation in relations.values():
        for det, dep in mvd_fds.items():
            for dependent in dep:
                det_cols = list(det) if isinstance(det, tuple) else [det]
                if all(col in relation.columns for col in det_cols + [dependent]):
                    grouped = relation.groupby(det_cols)[dependent].apply(set).reset_index()
                    if len(grouped) < len(relation):
                        return False
    return True

def fifth_nf_decomposition(relation_name, df, candidate_keys):
    def project(df, attrs):
        return df[list(attrs)].drop_duplicates()

    def is_lossless(df, df1, df2):
        common_columns = set(df1.columns) & set(df2.columns)
        if not common_columns:
            return False
        joined_df = pd.merge(df1, df2, on=list(common_columns), how='inner')
        return df.equals(joined_df)

    decomposed = [df]
    for key in candidate_keys:
        new_tables = []
        for table in decomposed:
            if set(key).issubset(set(table.columns)):
                table1 = project(table, key)
                remaining_columns = set(table.columns) - set(key)
                table2 = project(table, remaining_columns | set(key))
                if is_lossless(table, table1, table2):
                    new_tables.extend([table1, table2])
                else:
                    new_tables.append(table)
            else:
                new_tables.append(table)
        decomposed = new_tables
    return decomposed

def is_five_nf(relations):
    candidate_keys_dict = {}
    for relation_name, relation in relations.items():
        print(relation)
        user_input = input(f"Enter the candidate keys for {relation_name} (e.g., (A, B), (C, D)): ")
        tuples = re.findall(r'\((.*?)\)', user_input)
        candidate_keys = [tuple(map(str.strip, t.split(','))) for t in tuples]
        candidate_keys_dict[relation_name] = candidate_keys

    for relation_name, relation in relations.items():
        candidate_keys = candidate_keys_dict[relation_name]
        decomposed_relations = fifth_nf_decomposition(relation_name, relation, candidate_keys)
        if len(decomposed_relations) > 1:
            print(f"Decomposition for 5NF on {relation_name} yields:")
            for r in decomposed_relations:
                print(r)
            return False
    return True
