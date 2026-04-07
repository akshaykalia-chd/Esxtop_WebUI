import logging
import os
import re
import time

import numpy as np
import pandas as pd

from const import LOG_FILE, SYSTEM_OBJECT_PATTERNS
from ui_functions import *

logging.basicConfig(filename=LOG_FILE, encoding='utf-8', level=logging.INFO,
                    datefmt='%m/%d/%Y %I:%M:%S %p', format='%(asctime)s - %(levelname)s - %(message)s')


# --------------------------------------------------------------------------
# Function to implement object filtration
def filter_objects(working_dir, esxtop_data_frame):
    val_err = True
    while val_err:
        object_selection = get_list(
            "Do you know a name of object(VM name, Naa ID etc).Blank,In case you do not know the name of object.",
            "Object Filter")
        input_error = 0
        for i in object_selection:
            try:
                int(i)
                input_error = input_error + 1
            except ValueError:
                input_error = input_error
        if input_error > 0:
            error("Input Error String expected. Example Input: TestVM1,naa.123456789")
            val_err = True
        else:
            val_err = False
    # Processing data based on user input1
    out_df = esxtop_data_frame
    if len(object_selection) != 0:
        cols = esxtop_data_frame.columns.astype(str)
        escaped_items = [re.escape(obj) for obj in object_selection]
        combined_pattern = "|".join(escaped_items)
        matched_idx = cols.str.contains(combined_pattern, regex=True, na=False)
        matched_positions = np.where(matched_idx.to_numpy())[0].tolist()
        matched_positions.sort()
        selected_positions = [0] + matched_positions
        # Keep order stable but avoid duplicate timestamp column selection.
        selected_positions = list(dict.fromkeys(selected_positions))
        col_name = cols.take(selected_positions).tolist()
        out_df = esxtop_data_frame[col_name]

        # Validating data in Object filtered output
        if len(out_df.columns) <= 1:
            error("Unable to find the objects specified.Program will exit")
            return
        outfile = str(object_selection[0] + str(int(time.time())) + ".csv")
        outfile = os.path.join(working_dir, outfile)
        out_df.to_csv(outfile, index=False)
        logging.info(f" Generated: {outfile}")
    return out_df


# --------------------------------------------------------------------------------------
# Function to implement Counter Group filtration
def filer_counter_group(object_filtered_data_frame, cg_selection, working_dir):
    cols = object_filtered_data_frame.columns.astype(str)
    split_cols = cols.str.split("\\", expand=True)
    counter_groups = split_cols[3].str.split("\\(", expand=True)[0]
    column_list = [0] + np.where(counter_groups.eq(cg_selection).to_numpy())[0].tolist()
    column_list.sort()
    col_name = cols.take(column_list).tolist()
    out_df = object_filtered_data_frame[col_name]
    outfile = str(cg_selection + "-" + str(int(time.time())) + ".csv")
    outfile = os.path.join(working_dir, cg_selection, outfile)
    out_df.to_csv(outfile, index=False)
    logging.info(f"Generated: {outfile}")
    return out_df


# ------------------------------------------------------------------------------------------
# Function to implement Counter filtration
def filer_counter(cg_filtered_data_frame, c_selection, cg_selection, working_dir):
    out_df = cg_filtered_data_frame
    cols = cg_filtered_data_frame.columns.astype(str)
    time_se = str(cols[0])
    data_cols = cols[1:]
    split_cols = data_cols.str.split("\\", expand=True)
    try:
        column_list = np.where(split_cols[4].eq(c_selection).to_numpy())[0].tolist()
        column_list.sort()
        col_name = [time_se]
        col_name.extend(data_cols.take(column_list).tolist())
        out_df = out_df[col_name]
        outfile = str(cg_selection + "-" + c_selection + "-" + str(int(time.time())) + ".csv")
        outfile = os.path.join(working_dir, cg_selection, outfile)
        try:
            out_df.to_csv(outfile, index=False)
        except (FileNotFoundError, OSError):
            outfile = str(cg_selection + "-" + c_selection + "-" + str(int(time.time())) + ".csv")
            outfile = outfile.replace("/", "-")
            outfile = outfile.replace("?", " ")
            outfile = os.path.join(working_dir, cg_selection, outfile)
            out_df.to_csv(outfile, index=False)
        logging.info(f"Generated: {outfile}")
        return out_df
    except KeyError as e:
        logging.error(str(e))
        return


# ------------------------------------------------------------------------------------
# Function to prepare Counter group selection list
def prep_cg_selection(object_filtered_data_frame):
    cols = object_filtered_data_frame.columns.astype(str)
    split_cols = cols.str.split("\\", expand=True)
    counter_groups = split_cols[3].str.split("\\(", expand=True)[0]
    selection_list = counter_groups.replace('None', np.nan).dropna().unique().tolist()
    return selection_list


# ------------------------------------------------------------------------------------------
# Function to drop system objects
def drop_sys_obj(data):
    sel = question('Do you want to drop system objects like vpxa workers, hostd workers etc?')
    if sel == 2:
        cols = data.columns.astype(str)
        escaped_patterns = [re.escape(obj) for obj in SYSTEM_OBJECT_PATTERNS]
        combined_pattern = "|".join(escaped_patterns)
        c_name_list = cols[cols.str.contains(combined_pattern, regex=True, na=False)].tolist()
        out_df = data.drop(c_name_list, axis=1)
        logging.info('System objects dropped')
        return out_df
    else:
        return data


# ------------------------------------------------------------------------------------------
# Function to Prepare an Object Name
def find_obj(data, scope):
    obj_id = data.split("\\")
    if scope == 'sys':
        return str(obj_id[4])
    else:
        return str(obj_id[3])
