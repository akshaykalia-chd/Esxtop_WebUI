import logging
import os
import time

import matplotlib.pyplot as plt
from PIL import Image

from const import LOG_FILE

log_file = LOG_FILE
logging.basicConfig(filename=LOG_FILE, encoding='utf-8', level=logging.INFO,
                    datefmt='%m/%d/%Y %I:%M:%S %p', format='%(asctime)s - %(levelname)s - %(message)s')


# -----------------------------------------------------------------------------------------
# Function to Plot a counter selection
def plotit(c_sel, filepath, c_filtred_data_frame, cg_sel):
    pname = c_sel.split("\\")
    pname = pname[3] + '-' + pname[4]
    pname = str('Plot-' + pname + '-' + str(int(time.time())) + '.png')
    pname = os.path.join(filepath, cg_sel, pname)
    plotdf = c_filtred_data_frame
    xdata = '(PDH-CSV 4.0) (UTC)(0)'
    ydata = c_sel
    fig_len = int(len(plotdf[xdata])) * 0.18
    fig_wid = fig_len * 0.5625
    if fig_wid > 5:
        fig_wid = 5
    if fig_len > 650:
        fig_len = 650
    plt.figure()
    plt.figure(figsize=(fig_len, fig_wid))
    plt.autoscale(enable=True, axis='both', tight=False)
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title(ydata)
    plt.xticks(rotation='vertical')
    plt.plot(plotdf[xdata], plotdf[ydata])
    try:
        plt.savefig(pname, bbox_inches="tight")
        plt.close()
        logging.info(f"Generated:{pname}")
        img = Image.open(pname)
        img.show()

    except OSError:
        fname = c_sel.split("\\")
        fname = fname[3].replace(":", "-") + "-" + fname[4]
        fname = fname.replace("?", " ")
        pname = str('Plot-' + fname + '-' + str(int(time.time())) + '.png')
        try:
            fname = os.path.join(filepath, cg_sel, pname)
            plt.savefig(fname, bbox_inches="tight")
            plt.close()
            logging.info(f"Generated:{fname}")
            img = Image.open(fname)
            img.show()
        except FileNotFoundError:
            pname = pname.replace("/", "-")
            fname = os.path.join(filepath, cg_sel, pname)
            plt.savefig(fname, bbox_inches="tight", dpi=100)
            plt.close()
            logging.info(f"Generated:{fname}")
            img = Image.open(fname)
            img.show()
    return
