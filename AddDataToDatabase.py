import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-attendance-realtime-b2948-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "321654":
    {
        "name":"Karan Hansraj",
        "major": "Developer",
        "Starting_year": "2020",
        "total_attendance":5,
        "standing":"G",
        "year": 3,
        "last_attendance_time":"2023-08-26 22:40:54"
    },
    "852741":
    {
        "name":"Virat Kohli",
        "major": "Cricketer",
        "Starting_year": "2019",
        "total_attendance":32,
        "standing":"G",
        "year": 13,
        "last_attendance_time":"2023-08-26 22:40:54"
    },
    "963852":
    {
        "name":"Sachin",
        "major": "Alien",
        "Starting_year": "2020",
        "total_attendance":5,
        "standing":"G",
        "year": 4,
        "last_attendance_time":"2023-08-26 22:40:54"
    },
    
}

for key,value in data.items():
    ref.child(key).set(value)