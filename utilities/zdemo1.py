# """will be deleted from project"""
# import pandas
#
# from utilities import read_utils
#
# df=pandas.read_excel(io='../test_data/zoom_data.xlsx',sheet_name='test_invalid_login')
#
# print(df)
#
# #this is enough
# print(df.values.tolist())
#
#
# print(df.loc[0])
# print(tuple(df.loc[0]))
#
# print(tuple(df.loc[1]))
# print("-"*40)
# list=[]
# for i in df.index:
#     print(tuple(df.loc[i]))
#     list.append(tuple(df.loc[i]))
#
# print(list)
#
#
#
# print("-"*40)
#
# test_invalid_login_excel=read_utils.get_sheet_into_list(
#     '../test_data/zoom_data.xlsx','test_invalid_login')
# print(test_invalid_login_excel)
#
# print("-"*40)
#
#
# df=pandas.read_csv(filepath_or_buffer='../test_data/test_invalid_login.csv',delimiter=';')
# print(df.values.tolist())