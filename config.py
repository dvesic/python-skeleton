import configparser
import argparse
import utils

cfg = configparser.ConfigParser()
cfg.optionxform = str

cfg.read('config.ini', encoding='utf-8')

# Logging section

enable_logging = cfg['Logs'].getboolean('enable_logging')

log_info = cfg['Logs'].get('info', '$date$-progress.txt').replace('$date$', utils.get_date_as_string())
log_error = cfg['Logs'].get('error', '$date$-error_file.txt').replace('$date$', utils.get_date_as_string())

if enable_logging:
    utils.check_if_dir_exists(log_info)
    utils.check_if_dir_exists(log_error)

# Params section

production = cfg['Params'].getboolean('production')
description = cfg['Params'].get('description')

excel_bom = cfg['Csv'].getboolean('excel_bom')

excel_columns = cfg['App'].get('excel_columns')

if excel_columns:
    excel_columns = excel_columns.split(",")
else:
    excel_columns = None


def read_cmd_parameters():
    # Parsing command line
    global description
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('-p', '--production', action='store_true', help='Production mode')

    args = parser.parse_args()
