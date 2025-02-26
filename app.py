from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# قائمة المحافظات مع إحداثياتها
governorates = [
    {"name": "القدس", "x": 286, "y": 370},
    {"name": "رام الله", "x": 282, "y": 345},
    {"name": "الخليل", "x": 248, "y": 425},
    {"name": "نابلس", "x": 294, "y": 261},
    {"name": "جنين", "x": 302, "y": 206},
    {"name": "طولكرم", "x": 280, "y": 220},
    {"name": "قلقيلية", "x": 270, "y": 230},
    {"name": "بيت لحم", "x": 281, "y": 385},
    {"name": "طوباس", "x": 310, "y": 240},
    {"name": "سلفيت", "x": 285, "y": 250}
]

# قائمة المدن مع إحداثياتها
cities = [
    {"name": "حيفا", "x": 238, "y": 139},
    {"name": "يافا", "x": 199, "y": 312},
    {"name": "غزة", "x": 143, "y": 422},
    {"name": "رفح", "x": 108, "y": 479},
    {"name": "بئر السبع", "x": 200, "y": 489},
    {"name": "صفد", "x": 337, "y": 100},
    {"name": "طبريا", "x": 343, "y": 152},
    {"name": "بيسان", "x": 338, "y": 201},
    {"name": "الناصرة", "x": 295, "y": 161},
    {"name": "عكا", "x": 257, "y": 114}
]

# إعداد بيانات اللعبة
game_data = {"remaining_items": [], "score": 0, "time_left": 60, "phase": "governorates"}

@app.route("/")
def index():
    game_data["phase"] = "governorates"
    game_data["remaining_items"] = random.sample(governorates, 10)
    game_data["score"] = 0
    game_data["time_left"] = 60
    return render_template("index.html")

@app.route("/next_question")
def next_question():
    if not game_data["remaining_items"]:
        if game_data["phase"] == "governorates":
            game_data["phase"] = "cities"
            game_data["remaining_items"] = random.sample(cities, 10)
            game_data["score"] = 0
            return jsonify({"message": "تهانينا! انتقلت إلى مرحلة المدن!"})
        else:
            return jsonify({"message": "مبروك! لقد أنهيت اللعبة."})
    next_item = game_data["remaining_items"].pop(0)
    return jsonify({"name": next_item["name"]})

if __name__ == "__main__":
    app.run(debug=True)
