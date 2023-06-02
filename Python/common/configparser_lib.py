import configparser
import os
import os.path


CONFIG_PATH = os.path.join(os.getcwd(), 'conf', 'config.ini')


class ConfigReader:
    """
    A class for reading configuration from a file.
    """

    @staticmethod
    def getconfig(section, setting, alt_value=None):
        """
        Retrieve a value from the configuration file.

        Args:
            section (str): The section of the configuration file where the setting is located.
            setting (str): The name of the setting to retrieve.
            alt_value: An alternate value to return if the setting is not found.

        Returns:
            The value of the specified setting or the alternate value if the setting is not found.
        """
        val = None
        if not os.path.exists(CONFIG_PATH):
            raise Exception("Configuration file not found at " + CONFIG_PATH)
        try:
            config = configparser.ConfigParser()
            config.read(CONFIG_PATH)
            val = config.get(section, setting)
        except configparser.NoOptionError:
            if alt_value is not None:
                val = alt_value
        except Exception as e:
            pass
        return val
