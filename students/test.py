from datetime import date
from models import Students
first_name="mohmmad"
last_name="kalid"
birth_date=date.today()
GPA = 3.5
newStudent= Students(first_name,last_name,birth_date,GPA)
print(newStudent)
