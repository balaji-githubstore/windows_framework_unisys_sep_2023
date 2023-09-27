import pandas


def get_sheet_into_list(file_path,sheet_name):
    df = pandas.read_excel(io=file_path, sheet_name=sheet_name)
    return df.values.tolist()

