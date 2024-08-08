import datetime
from statistics import median

def solution(expenses):
    all_expenses = []
    
    for year_month, days in expenses.items():
        year, month = map(int, year_month.split('-'))
        
        first_day = datetime.date(year, month, 1)
        first_sunday = first_day
        while first_sunday.weekday() != 6:
            first_sunday += datetime.timedelta(days=1)
        
        for day in range(1, first_sunday.day + 1):
            day_str = f"{day:02d}"
            if day_str in days:
                all_expenses.extend(sum(days[day_str].values(), []))
    
    if not all_expenses:
        return None
    
    return median(all_expenses)

expenses = {
    "2023-01": {
        "01": {
            "food": [22.11, 43, 11.72, 2.2, 36.29, 2.5, 19],
            "fuel": [210.22]
        },
        "09": {
            "food": [11.9],
            "fuel": [190.22]
        }
    },
    "2023-03": {
        "07": {
            "food": [20, 11.9, 30.20, 11.9]
        },
        "04": {
            "food": [10.20, 11.50, 2.5],
            "fuel": []
        }
    },
    "2023-04": {}
}

print(solution(expenses))