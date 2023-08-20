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


def read_csv():
    # Ask user for the directory and file name
    directory = input("Enter the directory path where the CSV file is located: ")
    filename = input("Enter the name of the CSV file: ")
    try:
        # Read the CSV file using pandas
        df = pd.read_csv(f"{directory}/{filename}", sep=';')
    except FileNotFoundError:
        print('\033[91mFile not found!\033[m')
        return read_csv()

    return df, filename

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

def power_coupling(dataset, input_type, input_gt, input_ata, input_atd, input_terminal, date_format_str, term_name, oil_tk, chem_tk, gas_tk, blk, gcs, cont, roro, reefer, psgr, supp, fishing):
    try:
        type = dataset[input_type].tolist()
        gt = dataset[input_gt].tolist()
        ata = dataset[input_ata].tolist()
        atd = dataset[input_atd].tolist()
    except KeyError:
        print('\033[91mMismatching headers. Please insert the correct ones.\033[m')
        input_type, input_gt, input_ata, input_atd = define_headers()
        return power_coupling(dataset, input_type, input_gt, input_ata, input_atd, input_terminal, date_format_str, term_name, oil_tk, chem_tk, gas_tk, blk, gcs, cont, roro, reefer, psgr, supp, fishing)
    if input_terminal != 0:
        term = dataset[input_terminal].tolist()
    datetime_ata = pd.to_datetime(ata, format=date_format_str)
    datetime_atd = pd.to_datetime(atd, format=date_format_str)
    i = 0
    n = 0
    length = len(gt)
    power_required_kwh = [0] * length
    null_atd = 0
    while i < length:
        gt[i] = float(gt[i])
        #print(type[i], gt[i])
        if term_name == 'All':
            power_required_kwh[i] = compute_power(type[i], gt[i], oil_tk, chem_tk, gas_tk, blk, gcs, cont, roro, reefer, psgr, supp, fishing)
        else:
            if term[i] == term_name:
                power_required_kwh[i] = compute_power(type[i], gt[i], oil_tk, chem_tk, gas_tk, blk, gcs, cont, roro, reefer, psgr, supp, fishing)
        #print("The power needed is: ", power_required_kwh[i])
        #print("\n")
        if isinstance(atd[i], str) is False:
            null_atd = 1
            null_index = i
        i += 1

    #print(length, i, null_index)
    oldest = min(datetime_ata)

    if null_atd == 1:
        youngest = " "
    else:
        youngest = max(datetime_atd)

    #print("Oldest date: ", oldest)
    #print("Youngest date: ", youngest)

    youngest_list = round_dt(max(datetime_atd))
    oldest_list = round_dt(oldest)

    return youngest_list, oldest_list, type, gt, length, datetime_ata, datetime_atd, power_required_kwh

def boat_diagram(ata, atd, power_required_kwh, n):
    x = [str(ata), str(atd)]
    y = [power_required_kwh, power_required_kwh]

    plt.plot(x, y)

    plt.xlabel('ATA to ATD')
    plt.ylabel('Power Required (kW)')
    plt.title(f'Power required for vessel in row {n + 2}')

    plt.grid()

    plt.show()

def load_diagram(total_power_required, datetime_dts):

    plt.plot(datetime_dts[::10], total_power_required[::10])

    #plt.xlabel('Time')
    plt.ylabel('Power Required (kW)')
    plt.title(f'Load Diagram')

    plt.grid()

    plt.show()

def line(size=42):
    return '-' * size

def header(txt):
    print(line())
    print(txt.center(42))
    print(line())

def readInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERROR: please, enter a valid integer number.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\n\033[31mUser chose not to enter this number.\033[m')
            return 0
        else:
            return n

def menu(list):
    header('MAIN MENU')
    c = 1
    for item in list:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(line())
    opt = readInt('\033[32mOption: \033[m')
    return opt

def options_menu(list):
    header('OPTIONS')
    c = 1
    for item in list:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(line())
    print('\033[93mDon\'t forget to recalculate the program after changing dates\033[m')
    opt = readInt('\033[32mOption: \033[m')
    return opt

def setup_menu(list):
    header('SETUP MENU')
    c = 1
    for item in list:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(line())
    opt = readInt('\033[32mOption: \033[m')
    return opt

def define_headers():
    print('\033[93mMatch the header strings with the ones in your .csv file\033[m')
    input_type = input("Name for vessel type header: ")
    input_gt = input("Name for GT header: ")
    input_ata = input("Name for ATA header: ")
    input_atd = input("Name for ATD header: ")

    return input_type, input_gt, input_ata, input_atd

def define_types():
    print('\033[93mMatch the vessel type strings with the ones in your .csv file\033[m')
    oil_tk = input("Name for Oil tanker: ")
    chem_tk = input("Name for Chemical/Product tanker: ")
    gas_tk = input("Name for Gas tanker: ")
    blk = input("Name for Bulk carrier: ")
    gcs = input("Name for General cargo ship: ")
    cont = input("Name for Container ship: ")
    roro = input("Name for Ro-Ro ship: ")
    reefer = input("Name for Reefer ship: ")
    psgr = input("Name for Passenger/Cruise ship: ")
    supp = input("Name for Offshore supply ship: ")
    fishing = input("Name for Fishing vessel: ")

    return oil_tk, chem_tk, gas_tk, blk, gcs, cont, roro, reefer, psgr, supp, fishing

def menu_date(list, original_oldest_list, original_youngest_list, oldest_list, youngest_list):
    header('Date menu')
    c = 1
    for item in list:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(line())
    print('\033[4mFirst ATA in the database file:\033[m', original_oldest_list)
    print('\033[4mLast ATD in the database file:\033[m', original_youngest_list)
    print("Earliest date and time under analysis:", oldest_list)
    print("Latest date and time under analysis:", youngest_list)
    opt = readInt('\033[32mOption: \033[m')
    return opt

def menu_info(list):
    header('Detailed info menu')
    c = 1
    for item in list:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(line())
    opt = readInt('\033[32mOption: \033[m')
    return opt

def menu_cost(list, cost, cost_mt, co2_tax):
    header('Energy cost calculator')
    c = 1
    for item in list:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print(line())
    print("Current energy cost:", cost, " €/kWh")
    print("Current fuel cost:", cost_mt, " €/mt")
    print("Current CO2 emission tax:", co2_tax, " €/ton_CO2")
    opt = readInt('\033[32mOption: \033[m')
    return opt

def compute_csv_row():
    n = -1
    x = -1
    x = input("Check info of the vessel in the .csv row number: ")
    n = int(x) - 2
    return n

def datetime_range(start, end, delta):
    current = start
    while current < end:
        yield current
        current += delta

def round_dt(dt):
    dt = dt - datetime.timedelta(minutes=dt.minute % 15,
                                 seconds=dt.second,
                                 microseconds=dt.microsecond)
    return dt

# Python program to get average of a list
def Average(lst):
    return sum(lst) / len(lst)

def max_number(vessel_counter, datetime_dts):
    max_vessels = np.max(vessel_counter)
    max_index = np.argmax(vessel_counter)
    print("The maximum amount of simultaneously moored vessels is", round(max_vessels, 0), "in", datetime_dts[max_index])

def calculate_dts(oldest_list, youngest_list):
    delta = timedelta(minutes=15)

    dts = [dt.strftime('%Y-%m-%d %H:%M') for dt in
           datetime_range(oldest_list, youngest_list,
                          delta)]
    datetime_dts = pd.to_datetime(dts, format='%Y-%m-%d %H:%M')

    return datetime_dts


def power_array(datetime_dts, length, datetime_ata, datetime_atd, power_required_kwh, power_values, datetimes, proc_index):
    total_power_required = np.zeros(len(datetime_dts))
    vessel_counter = np.zeros(len(datetime_dts))

    for ata, atd, power in zip(datetime_ata, datetime_atd, power_required_kwh):
        mask = (ata <= datetime_dts) & (datetime_dts <= atd)
        total_power_required[mask] += power
        vessel_counter[mask] += (power != 0)

    if proc_index >= 0:
        power_index = 0
        for i, dt in enumerate(datetime_dts):
            if power_index < len(power_values) and dt in datetimes:
                total_power_required[i] += power_values[power_index]
                power_index += 1

    hourly_energy_list = []
    hourly_datetime_list = []

    for i in range(0, len(total_power_required), 4):
        hour_power = total_power_required[i:i + 4]
        hour_energy = np.mean(hour_power) * 0.25
        if i + 4 < len(total_power_required):
            hourly_energy_list.append(hour_energy)

    num_timestamps = len(hourly_energy_list)

    if len(datetime_dts) >= num_timestamps * 4:
        start_datetime = datetime_dts[0].replace(minute=0)
        end_datetime = datetime_dts[num_timestamps * 4 - 1]
        hourly_datetime_list = pd.date_range(start=start_datetime, end=end_datetime, freq='H').tolist()[:num_timestamps]

    return len(datetime_dts), total_power_required, vessel_counter, hourly_energy_list, hourly_datetime_list

def energy_calc(dts_len, total_power_required):
    i = 0
    j = 0
    hourly_energy_list = []
    while i < dts_len:
        j = i + 4
        hour_power = total_power_required[i:j]
        hour_energy = np.mean(hour_power) * 0.25  # calculate energy in kWh by taking average power over 1 hour
        hourly_energy_list.append(hour_energy)
        i += 4

    total_energy = sum(hourly_energy_list)

    return total_energy

def find_zero_power_periods(total_power_required, datetime_dts):
    zero_power_periods = []
    start_period = None
    end_period = None

    for i, power in enumerate(total_power_required):
        if power == 0:
            if start_period is None:
                start_period = datetime_dts[i]
            end_period = datetime_dts[i]
        else:
            if start_period is not None and end_period is not None:
                zero_power_periods.append((start_period, end_period))
                start_period = None
                end_period = None

    if start_period is not None and end_period is not None:
        zero_power_periods.append((start_period, end_period))

    return zero_power_periods

def calculate_zero_power_percentage(zero_power_periods, datetime_dts):
    total_duration = (datetime_dts[-1] - datetime_dts[0]).days + 1
    zero_power_duration = sum((end - start).days + 1 for start, end in zero_power_periods)

    zero_power_percentage = (zero_power_duration / total_duration) * 100
    return zero_power_percentage

def print_separator():
    separator = r'''******============================================******'''
    print(separator)


def opencsv():
    #dataset = pd.read_csv("historico_2019.csv", sep=';')
    print("\033[1mOnshore Power Supply Evaluator\033[0m")
    print("Program created by Marcelo Amaral")
    print_separator()

    dataset, filename = read_csv()

    input_type, input_gt, input_ata, input_atd = define_headers()

    input_terminal = 0

    oil_tk, chem_tk, gas_tk, blk, gcs, cont, roro, reefer, psgr, supp, fishing = define_types()

    date_format_str = '%d/%m/%Y %H:%M'

    term_name = "All"

    original_youngest_list, original_oldest_list, type, gt, length, datetime_ata, datetime_atd, power_required_kwh = power_coupling(dataset, input_type, input_gt, input_ata, input_atd, input_terminal, date_format_str, term_name, oil_tk, chem_tk, gas_tk, blk, gcs, cont, roro, reefer, psgr, supp, fishing)

    youngest_list = original_youngest_list
    oldest_list = original_oldest_list

    datetime_dts = calculate_dts(oldest_list, youngest_list)

#    print(oldest_list)
#    print(youngest_list)
#    print(datetime_dts)
#    print(power_required_kwh)
    # date_format_str_dts = '%Y/%m/%d %H:%M'
    # datetime_dts = pd.to_datetime(dts, format=date_format_str_dts)

    power_values = []
    datetimes = []
    proc_index = -1

    dts_len, total_power_required, vessel_counter, hourly_energy_list, hourly_datetime_list = power_array(datetime_dts, length, datetime_ata, datetime_atd, power_required_kwh, power_values, datetimes, proc_index)

#    print(total_power_required)
#    print(max(power_required_kwh))

    #total_energy = energy_calc(dts_len, total_power_required)
    total_energy = sum(hourly_energy_list)

    cost = 0.1533  # Cost of energy in €/kWh
    cons = 250  # g_fuel/kWh
    cost_mt = 650.7  # €/mt_fuel
    cost_kwh = cons * (cost_mt / 1000000)   # €/kWh
    co2_emission = 3.17  # g_CO2/g_fuel
    co2_tax = 100   # €/ton_CO2

    normal_cost = cost_kwh * total_energy
    fuel_cons = cons * total_energy  # g_fuel/kWh * kWh = g_fuel
    total_co2 = co2_emission * fuel_cons  # g_CO2/g_fuel * g_fuel = g_CO2
    tax_cost = co2_tax * (total_co2 / 1000000)  # €/ton_CO2 * ton_CO2 = €

    total_energy_price_omie = 0

    while True:
        option = menu(['Settings', 'Detailed info', 'Load diagram of the port', 'Max number of moored vessels', 'Peak power', 'Average power', 'Total energy', 'Energy cost', 'Exit'])
        if option == 1:
            while True:
                opt = menu_date(['Change first date', 'Change last date', 'Change load diagram of a vessel', 'Back'], original_oldest_list, original_youngest_list, oldest_list, youngest_list)
                if opt == 1:
                    new_oldest = str(input("First ATA (YYYY-MM_DD HH:MM): "))
                    try:
                        user_oldest_list = pd.to_datetime(new_oldest, format='%Y-%m-%d %H:%M')
                        if original_oldest_list <= user_oldest_list < original_youngest_list:
                            oldest_list = user_oldest_list
                            print("New date entered:", oldest_list)
                            datetime_dts = calculate_dts(oldest_list, youngest_list)
                            dts_len, total_power_required, vessel_counter, hourly_energy_list, hourly_datetime_list = power_array(datetime_dts, length, datetime_ata, datetime_atd, power_required_kwh, power_values, datetimes, proc_index)
                            total_energy = sum(hourly_energy_list)
                        else:
                            print('\033[91mThe entered datetime is out of bounds.\033[m')
                    except ValueError:
                        print('\033[31mInvalid date format! Please enter a date in the format YYYY-MM-DD.\033[m')
                elif opt == 2:
                    new_youngest = str(input("Last ATA (YYYY-MM-DD HH:MM): "))
                    try:
                        user_youngest_list = pd.to_datetime(new_youngest, format='%Y-%m-%d %H:%M')
                        if original_oldest_list < user_youngest_list <= original_youngest_list:
                            youngest_list = user_youngest_list
                            print("New date entered", youngest_list)
                            datetime_dts = calculate_dts(oldest_list, youngest_list)
                            dts_len, total_power_required, vessel_counter, hourly_energy_list, hourly_datetime_list = power_array(datetime_dts, length, datetime_ata, datetime_atd, power_required_kwh, power_values, datetimes, proc_index)
                            total_energy = sum(hourly_energy_list)
                        else:
                            print('\033[91mThe entered datetime is out of bounds.\033[m')
                    except ValueError:
                        print('\033[31mInvalid date format! Please enter a date in the format YYYY-MM-DD.\033[m')
                elif opt == 3:
                    power_values = []
                    datetimes = []
                    try:
                        ld_dataset, ld_filename = read_csv()
                        time_header = input("Enter the header for the time column: ")
                        power_header = input("Enter the header for the power column: ")
                        power = ld_dataset[power_header].tolist()
                        datetimes_list = ld_dataset[time_header].tolist()
                        datetime_values = pd.to_datetime(datetimes_list, format=date_format_str)

                        # Adjust the power values based on the datetime intervals
                        interval = timedelta(minutes=15)
                        for i, dt in enumerate(datetime_values):
                            power_values.extend([power[i]] * int(interval / (datetime_values[i] - datetime_values[i - 1])))

                        # Ensure datetimes have intervals of 15 minutes
                        start_datetime = datetime_values[0]
                        end_datetime = datetime_values[-1]
                        current_datetime = start_datetime

                        while current_datetime <= end_datetime:
                            datetimes.append(current_datetime)
                            current_datetime += interval

                        process_header = input("Enter the case number header in the .csv file of the port: ")
                        process_list = dataset[process_header].tolist()

                        case_number = input("Enter the case number of the vessel whose load chart is to be changed: ")

                        for i, process in enumerate(process_list):
                            if process == case_number:
                                power_required_kwh[i] = 0
                                proc_index = i
                                dts_len, total_power_required, vessel_counter, hourly_energy_list, hourly_datetime_list = power_array(datetime_dts, length, datetime_ata, datetime_atd, power_required_kwh, power_values, datetimes, proc_index)
                                total_energy = sum(hourly_energy_list)
                                break
                            else:
                                print("The provided case number doesn't exist!")
                                break

                    except FileNotFoundError:
                        print('\033[91mFile not found!\033[m')
                elif opt == 4:
                    break
                else:
                    print('\033[31mInsert a valid option!\033[m')
        elif option == 2:
            while True:
                opt = menu_info(['Single vessel info', 'Terminal info', 'Time periods with no consumption', 'Back'])
                if opt == 1:
                    n = compute_csv_row()
                    if n >= 0 and n < length:
                        #boat_diagram(datetime_ata[n], datetime_atd[n], power_required_kwh[n], n)
                        print("The vessel in the .csv row number", n + 2, "is a", type[n])
                        print("It arrived at the port on", datetime_ata[n], "and left on", datetime_atd[n])
                        print("This vessel requires a constant load of", power_required_kwh[n], "kW")
                    else:
                        print("Please enter a valid row number.")
                elif opt == 2:
                    if input_terminal == 0:
                        input_terminal = input("Terminal header name: ")
                    print('\033[93mTo analyze all port terminals type \"All\"\033[m')
                    term_name = input("Name of the terminal: ")
                    original_youngest_list, original_oldest_list, type, gt, length, datetime_ata, datetime_atd, power_required_kwh = power_coupling(dataset, input_type, input_gt, input_ata, input_atd, input_terminal, date_format_str, term_name, oil_tk, chem_tk, gas_tk, blk, gcs, cont, roro, reefer, psgr, supp, fishing)
                    youngest_list = original_youngest_list
                    oldest_list = original_oldest_list
                    datetime_dts = calculate_dts(oldest_list, youngest_list)
                    dts_len, total_power_required, vessel_counter, hourly_energy_list, hourly_datetime_list = power_array(datetime_dts, length, datetime_ata, datetime_atd, power_required_kwh, power_values, datetimes, proc_index)
                    #total_energy = energy_calc(dts_len, total_power_required)
                    total_energy = sum(hourly_energy_list)
                elif opt == 3:
                    zero_power_periods = find_zero_power_periods(total_power_required, datetime_dts)
                    print("The power supplied is null between: ")
                    for start_period, end_period in zero_power_periods:
                        print(f"> {start_period} - {end_period}")
                    zero_power_percentage = calculate_zero_power_percentage(zero_power_periods, datetime_dts)
                    print(f"The percentage of time where the power is 0: {zero_power_percentage:.2f}%")
                elif opt == 4:
                    break
                else:
                    print('\033[31mInsert a valid option!\033[m')
        elif option == 3:
            load_diagram(total_power_required, datetime_dts)
        elif option == 4:
            max_number(vessel_counter, datetime_dts)
        elif option == 5:
            print("The peak power is", max(total_power_required), "kW, reached in", datetime_dts[np.argmax(total_power_required)])
        elif option == 6:
            avg_power = Average(total_power_required)
            print("The average power is", round(avg_power, 2), "kW")
        elif option == 7:
            # Plot the hourly energy
            plt.plot(hourly_datetime_list, hourly_energy_list)
            plt.ylabel('Hourly Energy (kWh)')
            plt.title('Hourly Energy Consumption')
            plt.tight_layout()
            plt.grid()
            plt.show()
            print("The energy required is", round(total_energy / 1000, 2), "MWh")
          # total_energy_mwh = total_energy / 1000  # Convert kWh to MWh
          # print(f"Total energy consumed: {total_energy_mwh:.2f} MWh")
        elif option == 8:
            while True:
                opt = menu_cost(['Cost with OPS (constant tariff)', 'Cost with OPS (OMIE pricing)', 'Cost without OPS', 'Cost difference', 'Payback period', 'Change energy cost', 'Change fuel cost', 'Change CO2 tax', 'Back'], cost, cost_mt, co2_tax)
                if opt == 1:
                    print("The energy cost is", round(cost * total_energy, 0), "€")
                elif opt == 2:
                    zip_path = input("Please insert the .zip file path: ")
                    zip_name = input("Please insert the .zip file name: ")
                    # Define the full path to the zip file using pandas
                    zip_file_path = pd.Series([zip_path, zip_name]).str.cat(sep="/")
                    # Open the zip file
                    with zipfile.ZipFile(zip_file_path, "r") as zip_file:
                        # Loop through all the files in the zip file
                        datetime_list = []
                        price_list = []
                        for file_name in zip_file.namelist():
                            # Check if the file extension is .1, .2, .4, .8, etc.
                            if any(file_name.endswith(f".{i}") for i in range(1, 9)):
                                # Check if the file content ends with *
                                with zip_file.open(file_name) as f:
                                    file_content = f.read().decode("utf-8")

                                    # Process the file content
                                    lines = file_content.strip().split("\n")
                                    for line in lines[1:]:  # Skip the first row
                                        # Split the line using the semicolon separator
                                        data = line.strip().split(";")
                                        if len(data) >= 5:
                                            # Extract the datetime values
                                            year, month, day, hour = data[:4]
                                            hour = hour.zfill(2)  # Zero-padding the hour value
                                            if hour >= "25":
                                                continue
                                            if hour == "24":
                                                # Adjust hour to "00" of the next day
                                                hour = "00"
                                                next_day = pd.to_datetime(f"{year}-{month}-{day}") + pd.DateOffset(
                                                    days=1)
                                                year, month, day = next_day.year, next_day.month, next_day.day
                                            datetime_list.append(
                                                pd.to_datetime(f"{year}-{month}-{day} {hour}", format="%Y-%m-%d %H"))

                                            # Extract the price value
                                            price = data[4]
                                            price_list.append(float(price))

                    #print(len(hourly_datetime_list))

                    # Check if the maximum and minimum datetimes in datetime_dts are within the range of datetime_list
                    if min(hourly_datetime_list) >= min(datetime_list) and max(hourly_datetime_list) <= max(datetime_list):

                        min_datetime = min(hourly_datetime_list)  # Find the minimum datetime in datetime_dts
                        max_datetime = max(hourly_datetime_list)  # Find the maximum datetime in datetime_dts

                        min_position = None  # Variable to store the position where datetime_list equals min_datetime
                        # Iterate through datetime_list and find the position where datetime equals min_datetime
                        for i, dt in enumerate(datetime_list):
                            if dt == min_datetime:
                                min_position = i
                                break  # Exit the loop once a match is found

                        max_position = None  # Variable to store the position where datetime_list equals max_datetime
                        # Iterate through datetime_list and find the position where datetime equals min_datetime
                        for i, dt in enumerate(datetime_list):
                            if dt == max_datetime:
                                max_position = i
                                break  # Exit the loop once a match is found

                        # Convert price_list from EUR/MWh to EUR/kWh
                        price_list_kwh = [price / 1000 for price in price_list]

                        # Print the values for verification
                        #print("Min Position:", min_position)
                        #print("Max Position:", max_position)
                        #print("Min Datetime:", min_datetime)
                        #print("Max Datetime:", max_datetime)

                        #pos_diff = max_position - min_position
                        #print("Diff is:", pos_diff)


                        # Perform element-wise multiplication
                        energy_price_omie = [price * energy for price, energy in zip(price_list_kwh[min_position:], hourly_energy_list[:])]
                        #print(len(multiplied_list))
                        #print(len(hourly_datetime_list))

                        # Plot the multiplied_list_trimmed against hourly_datetime_list_trimmed
                        plt.plot(hourly_datetime_list, energy_price_omie)
                        plt.ylabel('Price (€/kWh)')
                        plt.title('Cost of Energy')
                        #plt.xticks(rotation=45)
                        plt.grid(True)
                        plt.show()

                        total_energy_price_omie = sum(energy_price_omie)
                        print("The total energy cost is", round(total_energy_price_omie, 0), "€")
                        print("The highest cost of energy under market prices was", max(energy_price_omie), "€/kWh, on", hourly_datetime_list[np.argmax(energy_price_omie)])
                        print("The lowest cost of energy under market prices was", min(energy_price_omie), "€/kWh, on", hourly_datetime_list[np.argmin(energy_price_omie)])
                    else:
                        print('\033[31mError: The datetime range of datetime_dts is not within the range of datetime_list.\033[m')

                elif opt == 3:
                    normal_cost = cost_kwh * total_energy
                    fuel_cons = cons * total_energy # g_fuel/kWh * kWh = g_fuel
                    total_co2 = co2_emission * fuel_cons    # g_CO2/g_fuel * g_fuel = g_CO2
                    tax_cost = co2_tax * (total_co2 / 1000000)  # €/ton_CO2 * ton_CO2 = €
                    cost_no_ops = normal_cost + tax_cost
                    print("The energy cost without OPS is", round(cost_no_ops, 0), "€:", round(normal_cost, 0), "€ (fuel cost) +", round(tax_cost, 0), "€ (CO2 emission cost)")
                elif opt == 4:
                    normal_cost = cost_kwh * total_energy
                    fuel_cons = cons * total_energy  # g_fuel/kWh * kWh = g_fuel
                    total_co2 = co2_emission * fuel_cons  # g_CO2/g_fuel * g_fuel = g_CO2
                    tax_cost = co2_tax * (total_co2 / 1000000)  # €/ton_CO2 * ton_CO2 = €
                    cost_no_ops = normal_cost + tax_cost
                    if total_energy_price_omie == 0:
                        cost_ops = cost * total_energy
                        print("If OPS is implemented, it saves", round(cost_no_ops - cost_ops, 0), "€ between", oldest_list, "and", youngest_list)
                    else:
                        print("If OPS is implemented, it saves", round(cost_no_ops - total_energy_price_omie, 0), "€ between", oldest_list, "and", youngest_list)
                elif opt == 5:
                    inv_cost = float(input("OPS investment cost (€): "))
                    if total_energy_price_omie == 0:
                        annual_profit = cost_no_ops - (cost * total_energy)
                    else:
                        annual_profit = cost_no_ops - total_energy_price_omie
                    payback_period = inv_cost / annual_profit
                    rounded_payback_period = math.ceil(payback_period)
                    print("The payback period is", rounded_payback_period, "years")
                elif opt == 6:
                    cost = float(input("New energy cost (€/kWh): "))
                elif opt == 7:
                    cost_mt = float(input("New fuel cost (€/mt): "))
                elif opt == 8:
                    co2_tax = float(input("New CO2 tax (€/ton_CO2): "))
                elif opt == 9:
                    break
                else:
                    print('\033[31mInsert a valid option!\033[m')
        elif option == 9:
            print("Exiting...")
            break
        else:
            print('\033[31mInsert a valid option!\033[m')


opencsv()