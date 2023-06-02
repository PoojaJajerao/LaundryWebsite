from Python.common.constants import RESULTS, MESSAGE, ERROR_CODE
from Python.common.mysql import MySQL


def get():
    service_info = CLGetAllEmployeesData()
    return service_info.execute_call()


class CLGetAllEmployeesData:
    def __init__(self):
        pass

    def execute_call(self):
        """
          executes the function call

        :return:
        """
        return_val = dict()
        cnx = None
        try:

            conn = MySQL.connect()
            query = "SELECT firstname, lastname FROM employees"

            rows = MySQL.execute_query_with_params(conn, query)

            if len(rows) > 0:
                return_val[RESULTS] = rows
            else:
                return_val[RESULTS] = None
        except Exception as ex:
            return_val[ERROR_CODE] = 400
            return_val[MESSAGE] = 'Something went wrong !!!'
        finally:
            if conn is not None:
                conn.close()
        return return_val
