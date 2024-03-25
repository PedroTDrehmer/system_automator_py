import datetime


def first_day_past_month_year():
    now = datetime.datetime.now()
    past_month = now.month - 1 if now.month != 1 else 12
    year_of_past_month = now.year - 1 if past_month == 12 else now.year
    full_date = f"{year_of_past_month}{str(past_month).zfill(2)}01" + "000000"
    data = datetime.datetime.strptime(full_date, "%Y%m%d%H%M%S").strftime("%d/%m/%Y")
    return data


def last_day_past_month_year():
    now = datetime.datetime.now()
    first_day_of_month = now.replace(day=1)
    last_day_of_previous_month = first_day_of_month - datetime.timedelta(days=1)
    data = last_day_of_previous_month.strftime("%d/%m/%Y")
    return data


def past_month_year():
    now = datetime.datetime.now()
    past_month = now.month - 1 if now.month != 1 else 12
    year_of_past_month = now.year - 1 if past_month == 12 else now.year
    full_date = f"{year_of_past_month}{past_month:02d}"
    data = datetime.datetime.strptime(full_date, "%Y%m").strftime("%m.%Y")
    return data


def month_year():
    date = datetime.datetime.now().strftime("%m/%Y")
    return date
