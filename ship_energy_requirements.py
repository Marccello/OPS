from datetime import datetime, timedelta
import datetime
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import zipfile
import math
from bisect import bisect_left
import colorama
colorama.init()


def compute_power(type, gt, oil_tk, chem_tk, gas_tk, blk, gcs, cont, roro, reefer, psgr, supp, fishing):
    power_required = 0

    # date_format_str = '%d/%m/%Y %H:%M'

    # start = pd.to_datetime(ata, format=date_format_str)
    # end = pd.to_datetime(atd, format=date_format_str)

    # Get interval between two timestamps as timedelta object
    # diff = end - start

    # Get interval between two timestamps in hours
    # diff_in_hours = diff.total_seconds() / 3600

    if type == oil_tk:
        if gt < 1000:
            power_required = 37
        elif gt < 5000:
            power_required = 161
        elif gt < 10000:
            power_required = 352
        elif gt < 25000:
            power_required = 476
        elif gt < 50000:
            power_required = 646
        elif gt < 100000:
            power_required = 834
        elif gt >= 100000:
            power_required = 1032

    elif type == chem_tk:
        if gt < 1000:
            power_required = 106
        elif gt < 5000:
            power_required = 289
        elif gt < 10000:
            power_required = 531
        elif gt < 25000:
            power_required = 723
        elif gt < 50000:
            power_required = 864
        elif gt < 100000:
            power_required = 1434
        elif gt >= 100000:
            power_required = 1536

    elif type == gas_tk:
        if gt < 1000:
            power_required = 111
        elif gt < 5000:
            power_required = 254
        elif gt < 10000:
            power_required = 667
        elif gt < 25000:
            power_required = 836
        elif gt < 50000:
            power_required = 1078
        elif gt < 100000:
            power_required = 2816
        elif gt >= 100000:
            power_required = 3556

    elif type == blk:
        if gt < 1000:
            power_required = 26
        elif gt < 5000:
            power_required = 80
        elif gt < 10000:
            power_required = 132
        elif gt < 25000:
            power_required = 197
        elif gt < 50000:
            power_required = 261
        elif gt < 100000:
            power_required = 350
        elif gt >= 100000:
            power_required = 438

    elif type == gcs:
        if gt < 1000:
            power_required = 12
        elif gt < 5000:
            power_required = 66
        elif gt < 10000:
            power_required = 149
        elif gt < 25000:
            power_required = 259
        elif gt < 50000:
            power_required = 416
        elif gt < 100000:
            power_required = 579
        elif gt >= 100000:
            power_required = 704

    elif type == cont:
        if gt < 1000:
            power_required = 31
        elif gt < 5000:
            power_required = 121
        elif gt < 10000:
            power_required = 332
        elif gt < 25000:
            power_required = 473
        elif gt < 50000:
            power_required = 864
        elif gt < 100000:
            power_required = 1535
        elif gt >= 100000:
            power_required = 2295

    elif type == roro:
        if gt < 1000:
            power_required = 28
        elif gt < 5000:
            power_required = 94
        elif gt < 10000:
            power_required = 213
        elif gt < 25000:
            power_required = 415
        elif gt < 50000:
            power_required = 529
        elif gt < 100000:
            power_required = 668
        elif gt >= 100000:
            power_required = 736

    elif type == reefer:
        if gt < 1000:
            power_required = 44
        elif gt < 5000:
            power_required = 153
        elif gt < 10000:
            power_required = 319
        elif gt < 25000:
            power_required = 542
        elif gt < 50000:
            power_required = 672
        elif gt < 100000:
            power_required = 800
        elif gt >= 100000:
            power_required = 960

    elif type == psgr:
        if gt < 1000:
            power_required = 20
        elif gt < 5000:
            power_required = 119
        elif gt < 10000:
            power_required = 272
        elif gt < 25000:
            power_required = 570
        elif gt < 50000:
            power_required = 1194
        elif gt < 100000:
            power_required = 2100
        elif gt >= 100000:
            power_required = 2912

    elif type == supp:
        if gt < 1000:
            power_required = 45
        elif gt < 5000:
            power_required = 144
        elif gt < 10000:
            power_required = 345
        elif gt < 25000:
            power_required = 553
        elif gt < 50000:
            power_required = 912
        elif gt < 100000:
            power_required = 1144
        elif gt >= 100000:
            power_required = 1248

    elif type == fishing:
        if gt < 1000:
            power_required = 43
        elif gt < 5000:
            power_required = 149
        elif gt < 10000:
            power_required = 284
        elif gt < 25000:
            power_required = 454
        elif gt < 50000:
            power_required = 454
        elif gt < 100000:
            power_required = 454
        elif gt >= 100000:
            power_required = 454

    else:
        power_required = 0

 #   elif type == "Embarcação à vela de treino":
 #       power_required = 0

 #   else:
 #       if gt < 1000:
 #           power_required = 28
 #       elif gt < 5000:
 #           power_required = 173
 #       elif gt < 10000:
 #           power_required = 344
 #       elif gt < 25000:
 #           power_required = 569
 #       elif gt < 50000:
 #           power_required = 988
 #       elif gt < 100000:
 #           power_required = 1282
 #       elif gt >= 100000:
 #           power_required = 1600

    # total_power = power_required * diff_in_hours

    return power_required
