from datetime import datetime
from application.db.people import get_employess
from application.salary import calculate_salary



if __name__ == '__main__':
    print(datetime.now())
    calculate_salary()
    get_employess()
