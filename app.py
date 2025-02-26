from flask import Flask, render_template, request, jsonify, redirect, url_for
import random

app = Flask(__name__)

# البيانات: المحافظات والمدن
provinces = {
    "شمال": [(257, 114, "عكا"), (238, 139, "حيفا"), (337, 100, "صفد"), (343, 152, "طبريا"), (338, 201, "بيسان"), (295, 161, "الناصرة"), (302, 206, "جنين")],
    "وسط": [(294, 261, "نابلس"), (282, 345, "رام الله"), (286, 370, "القدس"), (326, 349, "أريحا")],
    "جنوب": [(281, 385, "بيت لحم"), (248, 425, "الخليل"), (143, 422, "غزة"), (108, 479, "رفح"), (200, 489, "بئر السبع")]
}

all_cities = [city for region in provinces.values() for city in region]

# حالة اللعبة
current_phase = "provinces"
questions_answered = 0
score = 0
current_city = None

@app.route('/')
def index():
    global current_phase, questions_answered, score, current_city
    current_phase = "provinces"
    questions_answered = 0
    score = 0
    current_city = None
    return render_template('index.html', phase=current_phase, score=score)

@app.route('/next_question', methods=['POST'])
def next_question():
    global current_city, questions_answered, current_phase
    
    if current_phase == "provinces":
        choices = random.choice(list(provinces.values()))
    else:
        choices = all_cities
    
    current_city = random.choice(choices)
    return jsonify({"question": f"أين تقع {current_city[2]}؟"})

@app.route('/check_answer', methods=['POST'])
def check_answer():
    global questions_answered, score, current_phase
    
    data = request.get_json()
    x, y = data['x'], data['y']
    
    correct_x, correct_y, city_name = current_city
    
    distance = ((correct_x - x) ** 2 + (correct_y - y) ** 2) ** 0.5
    if distance < 20:
        score += 1
    
    questions_answered += 1
    
    if questions_answered == 10:
        if current_phase == "provinces":
            current_phase = "cities"
            questions_answered = 0
            return jsonify({"result": "next_phase"})
        else:
            return jsonify({"result": "game_over", "score": score})
    
    return jsonify({"result": "continue", "score": score})

if __name__ == '__main__':
    app.run(debug=True)
