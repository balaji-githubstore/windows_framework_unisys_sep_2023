from utilities import read_utils
class DataSource:
    test_invalid_login = [
        ('john123@gmail.com', 'john123', 'Incorrect email or password'),
        ('pete123@gmail.com', 'pete123', 'Incorrect email or password')
    ]

    # test_invalid_login_excel=(read_utils.get_sheet_into_list
    #                           ('../test_data/zoom_data.xlsx','test_invalid_login'))
    # test_valid_login_excel = (read_utils.get_sheet_into_list
    #                           ('../test_data/zoom_data.xlsx', 'test_valid_login'))
    #
    # test_invalid_login_csv=read_utils.get_csv_into_list('../test_data/test_invalid_login.csv')