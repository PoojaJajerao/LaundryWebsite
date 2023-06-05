from common.constants import RESULTS, MESSAGE, ERROR_CODE
from common.mssql import MSSQL


def get():
    service_info = CLGetAllEmployeesData()
    return service_info.execute_call()


class CLGetAllEmployeesData:
    @staticmethod
    def execute_call():
        """
          executes the function call

        :return:
        """
        return_val = dict()
        cnx = None
        try:
            conn = MSSQL.connect()

            query = "SELECT first_name, last_name FROM employees"

            rows = MSSQL.execute_query_with_columns(conn, query)

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
