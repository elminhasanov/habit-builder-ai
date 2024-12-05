from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Sample motivational quotes
quotes = {
    "default": ["Keep going!", "You're doing great!", "Every step counts!"],
    "exercise": ["Push harder today, rest tomorrow!", "Fitness is a journey, not a destination."],
    "reading": ["Books are a uniquely portable magic!", "A chapter a day keeps boredom away."]
}

# Store habits (for simplicity, using a dictionary)
habits = {}

@app.route('/add_habit', methods=['POST'])
def add_habit():
    data = request.json
    user = data['user']
    habit = data['habit']
    habits.setdefault(user, []).append({"habit": habit, "progress": []})
    return jsonify({"message": "Habit added successfully!"})

@app.route('/log_habit', methods=['POST'])
def log_habit():
    data = request.json
    user = data['user']
    habit = data['habit']
    habits[user] = [
        h if h["habit"] != habit else {**h, "progress": h["progress"] + [1]}
        for h in habits[user]
    ]
    return jsonify({"message": "Habit logged successfully!"})

@app.route('/motivation', methods=['GET'])
def get_motivation():
    habit = request.args.get('habit', 'default')
    return jsonify({"quote": random.choice(quotes.get(habit, quotes['default']))})

if __name__ == '__main__':
    app.run(debug=True)
