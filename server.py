# Contributors : Aishwarya Sivakumar, Roshan Babu, Nidhi Sunil Kumar, Yina Jian
# UNI : as6418, rbk2145, ns3566, yj2713

from asyncio import format_helpers
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__, static_url_path='/static')

#DATA
learnTime = {
}

learnInfo = {
	"1": {
			"id": "1",
			"content": "Music notation is written on a staff. A staff is basically comprised of four spaces and five lines. This is what it looks like:",
			"image": "http://bp3.blogger.com/_Tad4UOfdqXs/RZTwOqb7whI/AAAAAAAAAAc/A31QI-ZldAM/w1200-h630-p-k-no-nu/staff-2.png"
	},
	"2": {
			"id": "2",
			"content": "On every staff, there will be a symbol called a clef. There are two types of clefs: a treble clef and a bass clef. The treble clef is used for the higher sounding notes, usually played with the right hand. The bass clef, is used for the lower sounding notes, usually played with the left hand.",
			"image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVYO1s_vM41xwwZKAeTn6rqBBHFIwc-Y0d3w&usqp=CAU"
	},
	"3": {
			"id": "3",
			"content": "In this module, we will only learn notes on the treble clef. Here’s an overview of that will look like:",
			"image": "http://www.piano-keyboard-guide.com/wp-content/uploads/2015/05/Treble-Clef-Notes.png"
	},
	"4": {
			"id": "4",
			"content": "We’ll only be learning one scale, that is, just 8 notes. Let’s start with space notes. F,A,C,E. They spell the word Face!",
			"image": "https://www.skoove.com/blog/wp-content/uploads/2021/07/image1.png"
	},
	"5": {
			"id": "5",
			"content": "Next, let’s learn line notes. Try to memorize them! If you’re finding this difficult, there’s a hint on the next page",
			"image": "http://www.piano-keyboard-guide.com/wp-content/uploads/2015/05/treble-clef-line-notes.png"
	},
	"6": {
			"id": "6",
			"content": "The first letter of every word of the following sentence corresponds to this line: 'Every Good Boy Does Fine' You can use this to memorize line notes.",
			"image": "https://www.dacapoalcoda.com/_dl/images/note-positions-tregle-clef-egbdf.png"
	},
	"7": {
			"id": "7",
			"content": "We just finished learning a scale! Now, let’s move on to beats. The following music notation denotes that you can hold a note down for a maximum of 4 beats in this melody",
			"image": "https://press.rebus.community/app/uploads/sites/81/2017/07/4-4-time-signature_0001-e1552559771468.png"
	},
	"8": {
			"id": "8",
			"content": "But how do we know exactly how many beats to hold a note for? If you see a note without any vertical lines on it, then you hold it down for exactly 4 beats. This is also called a whole note.",
			"image": "https://study.com/cimages/multimages/16/773523164_whole_note.png"
	},
	"9": {
			"id": "9",
			"content": "If you see a note that is white on the inside and has a vertical line attached to it, then you hold it down for exactly 2 beats. This is also called a half note.",
			"image": "https://media.istockphoto.com/vectors/black-music-half-note-on-staff-lines-vector-id1186530961?b=1&k=20&m=1186530961&s=170667a&w=0&h=3ly1SosFmcOheh8TtOPQmBqVmzbsyb4uol8XyFTT70w="
	},
	"10": {
			"id": "10",
			"content": "If you see a note that is coloured black and has a vertical line attached to it, then you hold it down for exactly 1 beat. This is also called a quarter note.",
			"image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRC_YLoC6DhohF5wQNJVCayTLL2ok9obgp3j9Iqrd0T4wi9GyiK"
	},
	"11": {
			"id": "11",
			"content": "And finally, if you see a note with a vertical line and a squiggly line on it, then you hold it down for exactly half a beat. This is also called an one eighth note.",
			"image": "https://upload.wikimedia.org/wikipedia/commons/2/23/Eighth_Note_1_%28PSF%29.png"
	},
}

quiz_data  ={
	"1": {
		"id": 1,
		"question_image": True,
		"Question": "What is this note?",
		"Image": ["/static/pictures/F_note.png"],
		"Answers": {
			"A": "A",
			"B": "B",
			"C": "F",
			"D": "G"},
		"Correct_answer": "C"
	},
	"2": {
		"id": 2,
		"question_image": False,
		"Question": "Click on the image corresponding to a B note",
		"Answers":{
			"A": "/static/pictures/F_note.png",
			"B": "/static/pictures/B_note.png",
			"C": "/static/pictures/C_note.png",
			"D": "/static/pictures/D_note.png"},
		"Correct_answer": "B"
	},
   "3": {
		"id": 3,
		"question_image": True,
		"Question": "Which letter note do both these images correspond to?",
		"Image": ["/static/pictures/F_note.png", "/static/pictures/F_note2.png"],
		"Answers":{
			"A": "A",
			"B": "E",
			"C": "F",
			"D": "G"},
		"Correct_answer": "C"
	},
	"4": {
		"id": 4,
		"question_image": True,
		"Question": "Which letter note do both these images correspond to?",
		"Image":  ["/static/pictures/E_note.png", "/static/pictures/E_note2.png"],
		"Answers":{
			"A": "A",
			"B": "E",
			"C": "F",
			"D": "G"},
		"Correct_answer": "B"
	},
	"5": {
		"id": 5,
		"question_image": False,
		"Question": "Which of the following represent a half note?",
		"Answers":{
			"A": "/static/pictures/full_note.png",
			"B": "/static/pictures/quarter_note.png",
			"C": "/static/pictures/half_note.png",
			"D": "/static/pictures/one_eighth_note.png"},
		"Correct_answer": "C"
	  }
   }

user_score = 0
right_ans = []


# ROUTES

@app.route('/')
def welcome():
	return render_template('welcome.html')


@app.route('/middle')
def middle():
	global user_score
	global right_ans
	user_score = 0
	right_ans = []
	return render_template('middle.html')


@app.route('/result')
def result():
	return render_template('result.html', single_data = user_score, right_ans = right_ans, question_data = quiz_data)


@app.route('/quiz/<id>')
def quiz(id=None):
	global quiz_data
	return render_template('quiz.html', question_data = quiz_data[id], id = int(id) - 1)


@app.route('/calculate_score', methods=['GET', 'POST'])
def calculate_score():
	global quiz_data
	global user_score
	global right_ans
	json_data = request.get_json()
	user_answer = json_data["answer"]

	id = json_data["id"]
	correct_answer = quiz_data[str(id)]["Correct_answer"]
	if user_answer == correct_answer:
		user_score += 1
		right_ans.append(True)
	else:
		right_ans.append(False)
	return str(id+1)



@app.route('/learn/<id>')
def learn(id=None):
	global learnInfo
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
	return jsonify(learnTime=learnTime)


if __name__ == '__main__':
    app.run(debug = True)
