create_table = 'create table'


def is_create_table(sql_instruction: str):
    return (create_table in sql_instruction)
