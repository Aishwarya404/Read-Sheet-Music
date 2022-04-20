# Contributors : Aishwarya Sivakumar, Roshan Babu, Nidhi Sunil Kumar, Yina Jian
# UNI : as6418, rbk2145, ns3566, yj2713

from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__, static_url_path='/static')


#DATA
learnInfo = {
    "1": {
            "id": "1",
            "content": "This is the first page content",
            "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8093ba7b5e84ed05/61d8a63ddea73a236fc56d12/Neon_KeyArt-Web.png"
    },
    "2": {
            "id": "2",
            "content": "This is the second page content",
            "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8093ba7b5e84ed05/61d8a63ddea73a236fc56d12/Neon_KeyArt-Web.png"
    },
    "3": {
            "id": "3",
            "content": "This is the third page content",
            "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8093ba7b5e84ed05/61d8a63ddea73a236fc56d12/Neon_KeyArt-Web.png"
    },
    "4": {
            "id": "4",
            "content": "This is the fourth page content",
            "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8093ba7b5e84ed05/61d8a63ddea73a236fc56d12/Neon_KeyArt-Web.png"
    },
    "5": {
            "id": "5",
            "content": "This is the fifth page content",
            "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8093ba7b5e84ed05/61d8a63ddea73a236fc56d12/Neon_KeyArt-Web.png"
    },
    "6": {
            "id": "6",
            "content": "This is the sixth page content",
            "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8093ba7b5e84ed05/61d8a63ddea73a236fc56d12/Neon_KeyArt-Web.png"
    },
    "7": {
            "id": "7",
            "content": "This is the seventh page content",
            "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8093ba7b5e84ed05/61d8a63ddea73a236fc56d12/Neon_KeyArt-Web.png"
    },
    "8": {
            "id": "8",
            "content": "This is the eighth page content",
            "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8093ba7b5e84ed05/61d8a63ddea73a236fc56d12/Neon_KeyArt-Web.png"
    },
    "9": {
            "id": "9",
            "content": "This is the ninth page content",
            "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8093ba7b5e84ed05/61d8a63ddea73a236fc56d12/Neon_KeyArt-Web.png"
    },
    "10": {
            "id": "10",
            "content": "This is the tenth page content",
            "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8093ba7b5e84ed05/61d8a63ddea73a236fc56d12/Neon_KeyArt-Web.png"
    },
    "11": {
            "id": "11",
            "content": "This is the eleventh page content",
            "image": "https://images.contentstack.io/v3/assets/bltb6530b271fddd0b1/blt8093ba7b5e84ed05/61d8a63ddea73a236fc56d12/Neon_KeyArt-Web.png"
    },
}

quiz_data = {
   "1": {
    	"id": 1,
		"question": "Question 1",
		"options": ["A", "B", "F", "G"],
		"correct_answer": "F",
		"media": "/static/media/F_note.png"
    },
   "2": {
		"id": 2,
		"question": "Question 2",
		"options": ["A", "B", "F", "G"],
		"correct_answer": "F",
		"media": "/static/media/F_note.png"
    },
   "3": {
		"id": 3,
		"question": "Question 3",
		"options": ["A", "B", "F", "G"],
		"correct_answer": "F",
		"media": "/static/media/F_note.png"
    },
   "4": {
		"id": 4,
		"question": "Question 4",
		"options": ["A", "B", "F", "G"],
		"correct_answer": "F",
		"media": "/static/media/F_note.png"
    },
   "5": {
		"id": 5,
		"question": "Question 5",
		"options": ["A", "B", "F", "G"],
		"correct_answer": "F",
		"media": "/static/media/F_note.png"
    }
}
user_score = 0

# ROUTES

@app.route('/')
def welcome():
	return render_template('welcome.html')


@app.route('/middle')
def middle():
	return render_template('middle.html')

@app.route('/result')
def result():
	return render_template('result.html', single_data = user_score)


@app.route('/quiz/<id>')
def quiz(id=None):
	global quiz_data
	return render_template('quiz.html', single_data = quiz_data[id])
	

@app.route('/calculate_score', methods=['GET', 'POST'])
def calculate_score():
	global quiz_data
	global user_score
	json_data = request.get_json()
	user_answer = json_data["answer"]
	id = json_data["id"]
	correct_answer = quiz_data[str(id)]["correct_answer"]
	if user_answer == correct_answer:
		user_score += 1
	return str(id+1)


@app.route('/learn/<id>')
def learn(id=None):
	global learnInfo;
	single_data = learnInfo[id]
	return render_template('learn.html', single_data=single_data)


@app.route('/edit_entry', methods=['GET', 'POST'])
def edit_entry():
	global learnTime
	json_data = request.get_json()
	id_rn = json_data["id_rn"]
	time = json_data["time"]

	new_name_entry =  {
		"id": id_rn,
		"time": time
	}
	learnTime[id_rn] = new_name_entry
	return


if __name__ == '__main__':
   app.run(debug = True)
