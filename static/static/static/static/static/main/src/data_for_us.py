import datetime
from ..models import Date
def add_week(data):
    try:
        data = datetime.date(data.year, data.month, data.day + 7)
    except ValueError:
        try:
            datetime.date(data.year, data.month,31)
            try:
                data=datetime.date(data.year, data.month+1, 7-(31-data.day))
            except ValueError:
                data = datetime.date(data.year+1, 1, 7-(31-data.day))
        except ValueError:
            try:
                datetime.date(data.year,data.month,30)
                data = datetime.date(data.year, data.month + 1, 7 - (30 - data.day))
            except ValueError:
                try:
                    datetime.date(data.year,data.month,29)
                    data = datetime.date(data.year, data.month + 1, 7 - (29 - data.day))
                except ValueError:
                    data = datetime.date(data.year, data.month + 1, 7 - (28 - data.day))
    finally:
        return data
def get_date_for_user():
    now=datetime.date.today()
    year = Date.objects.order_by("data")
    arr=[]
    for el in year:
        if now<add_week(el.data):
            break
        if not (el.archive):
            arr.append((str(el.data),str(el.data)))
    return arr