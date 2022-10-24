
def get_tables_list_query():
    """
    --------------------
    Description
    --------------------
    -> get_tables_list_query (method): Function that returns the query used for extracting the list of tables from a Postgres table

    --------------------
    Parameters
    --------------------
    => To be filled by student
    -> name (type): description

    --------------------
    Pseudo-Code
    --------------------
    => To be filled by student
    -> pseudo-code

    --------------------
    Returns
    --------------------
    => To be filled by student
    -> (type): description
    """
    query = "SELECT table_schema, table_name FROM information_schema.tables;"
    return query

def get_table_data_query(schema_name, table_name):
    """
    --------------------
    Description
    --------------------
    -> get_table_data_query (method): Function that returns the query used for extracting the content of a Postgres table

    --------------------
    Parameters
    --------------------
    => To be filled by student
    -> name (type): description

    --------------------
    Pseudo-Code
    --------------------
    => To be filled by student
    -> pseudo-code

    --------------------
    Returns
    --------------------
    => To be filled by student
    -> (type): description
    """
	#=> To be filled by student
    query = f"SELECT * FROM {schema_name}.{table_name}"
    return query


def get_table_schema_query(schema_name, table_name):
    """
    --------------------
    Description
    --------------------
    -> get_table_schema_query (method): Function that returns the query used for extracting the list of columns from a Postgres table and their information

    --------------------
    Parameters
    --------------------
    => To be filled by student
    -> name (type): description

    --------------------
    Pseudo-Code
    --------------------
    => To be filled by student
    -> pseudo-code

    --------------------
    Returns
    --------------------
    => To be filled by student
    -> (type): description
    """
	#=> To be filled by student
    query = f"SELECT * FROM information_schema.columns WHERE table_schema = '{schema_name}' AND table_name = '{table_name}';"
    return query
