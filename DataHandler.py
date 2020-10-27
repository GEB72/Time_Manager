from timeit import default_timer as timer
from datetime import date, timedelta, datetime
from WindowFinder import foreground_window
from Pickler import pickle_me, unpickle_me

time_dict = {}
presentable_time_dict = {}
dates = date.today()


def update_dict():
    # start timer and get current date
    start = timer()
    global dates

    # set dict key by concatenating date and exe, skip update if exe is empty from WMI error
    try:
        exe = foreground_window()
        key = str(dates) + " | " + exe
    except TypeError:
        return 0

    # check if key already present add add time accordingly
    if key in time_dict:
        time_dict[key] = time_dict[key] + timer() - start
    else:
        time_dict[key] = timer() - start


def send_to_pickler():
    # for precision/accuracy pickle corresponding time_dict values from presentable_time_dict
    temp_dict = {}

    for key, value in time_dict.items():
        if value > 60:
            temp_dict[key] = time_dict[key]
    pickle_me(temp_dict)


def get_from_pickler():
    # catch exception caused by empty pickle file
    temp_dict = unpickle_me()
    try:
        for key, value in temp_dict.items():
            time_dict[key] = value
    except AttributeError:
        pass


def get_from_pickler_ui():
    # due to multiprocessing not sharing memory, we need presentable_time_dict straight from pickle file
    temp_dict = unpickle_me()
    for key, value in temp_dict.items():
        value = int(value)
        presentable_time_dict[key] = "%s:%s" % ((value // 3600) % 60, (value // 60) % 60)
        time_dict[key] = value


def sum_values(values):
    summed_dict = {}

    # check if key present, if not create the key, if so add values
    for key, value in values:
        exe_substring = key[13:]

        if exe_substring in summed_dict:
            summed_dict[exe_substring] = summed_dict[exe_substring] + value
        else:
            summed_dict[exe_substring] = value

    return [[key, value] for key, value in summed_dict.items()]


def sort_data(start_date, end_date):
    get_from_pickler_ui()
    global dates

    if end_date == 0:
        # get all values from presentable_time_dict
        values = sorted([(key, value) for key, value in time_dict.items()], key=lambda val: -val[1])

    elif start_date != 0:
        # compile list of dates within the range
        start_date = datetime.strptime(start_date, "%Y-%m-%d")
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        date_range = (start_date - end_date).days

        date_list = [(start_date - timedelta(days=x)).strftime("%Y-%m-%d") for x in range(date_range)]

    elif end_date == "1 Day":
        # compile list of dates within the range
        date_list = [dates.strftime("%Y-%m-%d")]

    elif end_date == "3 Day" or end_date == "7 Day":
        # compile list of dates within the range
        date_list = [(dates - timedelta(days=x)).strftime("%Y-%m-%d") for x in range(int(end_date[0]))]

    elif end_date == "1 Month":
        # compile list of dates within the range
        date_list = [(dates - timedelta(days=x)).strftime("%Y-%m-%d") for x in range(int(end_date[0]) * 30)]

    elif end_date == "1 Year":
        # compile list of dates within the range
        date_list = [(dates - timedelta(days=x)).strftime("%Y-%m-%d") for x in range(int(end_date[0]) * 365)]

    try:
        # get values that match the date range, sum the values,then sort by time descending order
        values = [(key, time_dict[key]) for key, value in presentable_time_dict.items() if key[:10] in date_list]
        summed_values = sum_values(values)
        summed_values = sorted(list(summed_values), key=lambda val: -val[1])

        # ensure presentable format
        for i in range(0, len(summed_values)):
            value_tuple = summed_values[i]
            value = int(value_tuple[1])
            summed_values[i][1] = "%s:%s" % ((value // 3600) % 60, (value // 60) % 60)
        return summed_values

    except NameError:
        # values already present so just sum, sort and return
        summed_values = sum_values(values)
        summed_values = sorted(list(summed_values), key=lambda val: -val[1])

        # ensure presentable format
        for i in range(0, len(summed_values)):
            value_tuple = summed_values[i]
            value = int(value_tuple[1])
            summed_values[i][1] = "%s:%s" % ((value // 3600) % 60, (value // 60) % 60)
        return summed_values
