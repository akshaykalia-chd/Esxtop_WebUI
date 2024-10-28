import logging
import os

import pandas as pd

from const import LOG_FILE
from ui_functions import *

logging.basicConfig(filename=LOG_FILE, encoding='utf-8', level=logging.INFO,
                    datefmt='%m/%d/%Y %I:%M:%S %p', format='%(asctime)s - %(levelname)s - %(message)s')


# --------------------------------------------------------------------------------
def prep_working_dir(dir_list, working_dir):
    for i in dir_list:
        if not (os.path.exists(os.path.join('./', working_dir, i))):
            os.makedirs(os.path.join('./', working_dir, i))
    return


# -------------------------------------------------------------------------
def read_csv_location():
    csv_location = get_file("Esxtop csv Data")
    return csv_location


# --------------------------------------------------------------------------
def load_csv(csv_location):
    if len(csv_location) == 0:
        error("No csv file selected")
    else:
        try:
            logging.info(f"Loading {csv_location} using Default encoding. This may take a while")
            tdf = pd.DataFrame(pd.read_csv(csv_location))
            logging.info("CSV file successfully loaded to Memory")
            return tdf
        except Exception as e:
            logging.error(f"file read error:{str(e)}")
        try:
            logging.info(f"Loading {csv_location} using ISO-8859–1 encoding. This may take a while")
            tdf = pd.DataFrame(pd.read_csv(csv_location, encoding='ISO-8859–1'))
            logging.info("CSV file successfully loaded to Memory")
            return tdf
        except Exception as e:
            errmsg = f"File Read Error:{str(e)}"
            logging.error(errmsg)
            if "Unable to allocate" in errmsg:
                error("File too big to load")
            else:
                error(errmsg)
                fix_file(csv_location)


def fix_file(csv_location):
    logging.info("Attempting to fix file structure")
    numberoflines = 0
    try:
        file = open(csv_location, "r")
        for line in file:
            if line:
                numberoflines = numberoflines + 1
        file.close()
        file = open(csv_location, "r")
        fixedfile = []
        i = 0
        numberoflines = numberoflines - 1
        for line in file:
            if i < numberoflines:
                fixedfile.append(line)
                i = i + 1
        file.close()
        file = open(csv_location, 'w')
        file.writelines(fixedfile)
        file.close()
        dialog("Fix success, please try to reload the file!")
    except Exception as e:
        logging.error(str(e))
        error("Fix failure, please send this file to akshay.kalia@broadcom.com for debugging")
