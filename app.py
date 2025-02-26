from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# بيانات المحافظات
provinces = [
    {"name": "الخليل", "x": 248, "y": 425},
    {"name": "رام الله", "x": 282, "y": 345},
    {"name": "القدس", "x": 286, "y": 370},
    {"name": "نابلس", "x": 294, "y": 261},
    {"name": "جنين", "x": 302, "y": 206},
    {"name": "طولكرم", "x": 270, "y": 230},
    {"name": "قلقيلية", "x": 260, "y": 250},
    {"name": "سلفيت", "x": 275, "y": 270},
    {"name": "طوباس", "x": 310, "y": 220},
    {"name": "أريحا", "x": 326, "y": 349},
]

# بيانات المدن (المرحلة الثانية)
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
    {"name": "عكا", "x": 257, "y": 114},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_question/<int:level>')
def get_question(level):
    if level == 1:
        question_data = random.choice(provinces)
    else:
        question_data = random.choice(cities)
    return jsonify(question_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
