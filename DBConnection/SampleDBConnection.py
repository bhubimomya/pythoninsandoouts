import configparser


class sampleDbConnection(object):
    """
     utility of this class is to raise an alert bar when snowflake query
     reach to the threshold level

    """

    @staticmethod
    def read_config(file_path):
        """

        :param file_path:
        :return:
        """
        cfg = configparser.ConfigParser()
        cfg.read(file_path)
        snowflake_credentials = dict(cfg.items('snowflake'))
        to_list = cfg.get("email", "to_list").split(',')
        admin_team = cfg.get("email", "Admin_Team")

        return snowflake_credentials, to_list, admin_team

    def __init__(self, file_path):
        """
        Init method to call the constructor
        :param file_path:
        """
        pass

    def __enter__(self):
        """
        Entry point of the context manager
        :return:
        """
        print("Establish the db connection")

        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Exit point of the context manager
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        print("Closing the snowflake connection")

    def query_run(self, conn):
        """
        Used to connect the sql database and run relevant query
        :param conn:
        :return:
        """
        print("Enter into query run ")

        pass

    def generate_html(self):
        pass

    def send_email(self):
        pass

    @classmethod
    def main(cls):
        """
        Mian function is a single entry function where it will orchestarte and run tthe following program
        It will take config_file_path as a parameter and invoke the class
        :return:
        """
        config_file_path = "C:\Users\Miku\Desktop\PythonProjects\pythoninsandoouts\DBConnection\Config\config.ini"

        with sampleDbConnection(config_file_path) as conn:
            sampleDbConnection.query_run(conn)

if __name__=="__main__":
    sampleDbConnection.main()
