from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# قائمة المدن مع إحداثياتها الأصلية
cities = [
    {"name": "الخليل", "x": 249, "y": 428},
    {"name": "بئر السبع", "x": 198, "y": 490},
    {"name": "رفح", "x": 106, "y": 477},
    {"name": "غزه", "x": 142, "y": 424},
    {"name": "يافا", "x": 199, "y": 313},
    {"name": "اريحا", "x": 325, "y": 349},
    {"name": "القدس", "x": 282, "y": 368},
    {"name": "نابلس", "x": 293, "y": 259},
    {"name": "جنين", "x": 299, "y": 207},
    {"name": "طبريا", "x": 344, "y": 153},
    {"name": "الناصره", "x": 297, "y": 161},
    {"name": "صفد", "x": 339, "y": 98},
    {"name": "عكا", "x": 258, "y": 113},
    {"name": "حيفا", "x": 237, "y": 139}
]

# إعداد بيانات اللعبة
game_data = {"remaining_cities": [], "score": 0, "time_left": 60}

@app.route("/")
def index():
    game_data["remaining_cities"] = random.sample(cities, 10)  # اختيار 10 مدن عشوائياً
    game_data["score"] = 0
    game_data["time_left"] = 60
    return render_template("index.html", cities=cities)

@app.route("/next_question")
def next_question():
    if not game_data["remaining_cities"]:
        return jsonify({"city": None})  # انتهت الأسئلة
    next_city = game_data["remaining_cities"].pop(0)
    return jsonify({"city": next_city["name"]})

if __name__ == "__main__":
    app.run(debug=True)
