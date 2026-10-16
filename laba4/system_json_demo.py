import os
import json

def show_system_json(): print("Поточна папка:", os.getcwd())
student = {
    "name": "Dina",
    "course": 2,
    "specialty": "IST"
}

print(json.dumps(student, ensure_ascii=False, indent=4))