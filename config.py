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

# Params Section

production = cfg['Params'].getboolean('production')

# App Section

description = cfg['App'].get('description')


# CSV Section

excel_bom = cfg['Csv'].getboolean('excel_bom')

excel_columns = cfg['Csv'].get('excel_columns')

if excel_columns:
    excel_columns = excel_columns.split(",")
else:
    excel_columns = None


def read_cmd_parameters():
    # Parsing command line
    global description, production, enable_logging

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('-p', '--production', action='store_true', help='Production mode')
    parser.add_argument('-l', '--logging-off', action='store_true', help='Disable logging')

    args = parser.parse_args()

    if args.production:
        production = True

    if args.logging_off:
        enable_logging = False
