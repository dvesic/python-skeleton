"""
Explanation what application does

Details are in README.md.
"""

__version__ = '0.1'
__author__ = 'Dejan Vesić, Dejan@Vesic.Org'

import config
import file_logging


if __name__ == "__main__":

    config.read_cmd_parameters()
    if not config.production:
        file_logging.log_info("APP Started")

    # Do something
