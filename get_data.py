import pandas


def get_data_from_excel(col_name):
    excel_data = pandas.read_excel('task_support.xlsx', sheet_name='Tasks', usecols=[col_name])
    return excel_data[col_name].tolist()[1:]
