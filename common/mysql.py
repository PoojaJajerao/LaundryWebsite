import logging
import mysql.connector
import uuid
from common.constants import log_err_message
from common.configparser_lib import ConfigReader
from datetime import datetime
from dotenv import dotenv_values

env_values = dotenv_values(".env")


class MySQL:
    """
    A utility class for MySql database operations.
    """

    @staticmethod
    def connect():
        """
        Creates a connection to the given MySql server.

        Returns:
            MySql.Connection: The connection to the MySql server.
        """
        conn = None
        func_name = f"{__name__}.MySql.connect"
        try:
            username = env_values['USERNAME']
            passwd = env_values['PASSWORD']
            dbname = ConfigReader.getconfig('database', 'dbname')
            hostname = ConfigReader.getconfig('database', 'hostname')

            if username is None or passwd is None or dbname is None or hostname is None:
                raise Exception("Failed to fetch DB Creds")

            conn = mysql.connector.connect(user=username, password=passwd,
                                           host=hostname, database=dbname)

        except Exception as e:
            log_err_message(func_name, str(e))
            raise e
        return conn

    @staticmethod
    def execute_query_with_params(conn, query, **kwargs):
        """
        Executes a parameterized query on a MySql connection.

        Args:
            conn (MySql.Connection): The connection to the MySql server.
            query (str): The parameterized query to execute.
            **kwargs: The parameter values to substitute in the query.

        Returns:
            list: The results of the query as a list of dictionaries.
        """
        func_name = f"{__name__}.MySql.execute_query_with_params"
        cursor = None
        data = []
        sql = query
        try:
            cursor = conn.cursor()
            params = {k: v for k, v in kwargs.items()}
            cursor.execute(query, params)
            cols = [d[0].lower() for d in cursor.description]
            fetch_result = cursor.fetchall()
            for row in fetch_result:
                for i, j in enumerate(row):
                    try:
                        if isinstance(j, memoryview):
                            row[i] = str(uuid.UUID(bytes_le=str(j)))
                        elif type(j) == datetime:
                            row[i] = j.isoformat()
                        elif type(j) == bytearray:
                            row[i] = str(uuid.UUID(bytes_le=str(j)))
                    except Exception as e:
                        row[i] = None
            for rs in fetch_result:
                zip_data = dict(zip(cols, rs))
                data.append(zip_data)
        except Exception as e:
            log_err_message(func_name, str(e))
        finally:
            if cursor is not None:
                cursor.close()
        return data
