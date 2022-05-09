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
			"title": "Staff",
			"content": "Music notation is written on a staff. A staff is basically comprised of four spaces and five lines. This is what it looks like :",
			"image": ["http://bp3.blogger.com/_Tad4UOfdqXs/RZTwOqb7whI/AAAAAAAAAAc/A31QI-ZldAM/w1200-h630-p-k-no-nu/staff-2.png"]
	},
	"2": {
			"id": "2",
			"title": "Treble & Bass Clef",
			"content": "On every staff, there will be a symbol called a clef. There are two types of clefs: a treble clef and a bass clef. The treble clef is used for the higher sounding notes, usually played with the right hand. The bass clef, is used for the lower sounding notes, usually played with the left hand.",
			"image": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVYO1s_vM41xwwZKAeTn6rqBBHFIwc-Y0d3w&usqp=CAU"]
	},
	"3": {
			"id": "3",
			"title": "Overview",
			"content": "In this module, we will only learn notes on the treble clef. Here's an overview of what that will look like:",
			"image": ["http://www.piano-keyboard-guide.com/wp-content/uploads/2015/05/Treble-Clef-Notes.png"]
	},
	"4": {
			"id": "4",
			"title": "Space Notes",
			"content": "We'll only be learning one scale, that is, just 8 notes. Let's start with space notes. F,A,C,E. They spell the word Face!",
			"image": ["https://lessonsinyourhome.net/wp-content/uploads/FACE.jpg"]
	},
	"5": {
			"id": "5",
			"title": "Line Notes",
			"content": "Next, let's learn line notes. Try to memorize them! If you're finding this difficult, there's a hint on the next page",
			"image": ["http://www.piano-keyboard-guide.com/wp-content/uploads/2015/05/treble-clef-line-notes.png"]
	},
	"6": {
			"id": "6",
			"title": "Line Notes",
			"content": "The first letter of every word of the following sentence corresponds to this line: 'Every Good Boy Does Fine!'  You can use this to memorize line notes.",
			"image": ["https://www.dacapoalcoda.com/_dl/images/note-positions-tregle-clef-egbdf.png"]
	},
	"7": {
			"id": "7",
			"title": "Beats",
			"content": "We just finished learning a scale! Now, let's move on to beats. The following music notation denotes that you can hold a note down for a maximum of 4 beats in this melody",
			"image": ["https://press.rebus.community/app/uploads/sites/81/2017/07/4-4-time-signature_0001-e1552559771468.png"]
	},
	"8": {
			"id": "8",
			"title": "Whole",
			"content": "But how do we know exactly how many beats to hold a note for? If you see a note without any vertical lines on it, then you hold it down for exactly 4 beats. This is also called a whole note.",
			"image": ["https://study.com/cimages/multimages/16/773523164_whole_note.png"]
	},
	"9": {
			"id": "9",
			"title": "Half",
			"content": "If you see a note that is white on the inside and has a vertical line attached to it, then you hold it down for exactly 2 beats. This is also called a half note.",
			"image": ["https://media.istockphoto.com/vectors/black-music-half-note-on-staff-lines-vector-id1186530961?b=1&k=20&m=1186530961&s=170667a&w=0&h=3ly1SosFmcOheh8TtOPQmBqVmzbsyb4uol8XyFTT70w="]
	},
	"10": {
			"id": "10",
			"title": "Quarter",
			"content": "If you see a note that is coloured black and has a vertical line attached to it, then you hold it down for exactly 1 beat. This is also called a quarter note.",
			"image": ["https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRC_YLoC6DhohF5wQNJVCayTLL2ok9obgp3j9Iqrd0T4wi9GyiK"]
	},
	"11": {
			"id": "11",
			"title": "Eighth",
			"content": "And finally, if you see a note with a vertical line and a squiggly line on it, then you hold it down for exactly half a beat. This is also called an one eighth note.",
			"image": ["https://upload.wikimedia.org/wikipedia/commons/2/23/Eighth_Note_1_%28PSF%29.png"]
	},
	"12": {
			"id": "12",
			"title": "Beams",
			"content": "We saw how each flag halves the value of a note, so a single flag signifies 1/2 of a quarter note, a double flag halves that to 1/4 of a quarter note, et cetera. Beams do the same while allowing us to read the music more clearly and keep the notation less cluttered.",
			"image": ["/static/pictures/beam.jpeg"]
	},
	"13": {
			"id": "13",
			"title": "Dots & Ties",
			"content": "There are other ways to extend the length of a note. A dot after the note head, adds another half of that note’s duration to it. So, a half note with a dot would equal a half note and a quarter note. A tie may also be used to extend a note. Two notes tied together should be held as long as the value of both of those notes together.",
			"image": ["/static/pictures/ties.png"]
	},
	"14": {
			"id": "14",
			"title": "Rest",
			"content": "But what happens when there isn’t a note taking up each beat? It’s easy, we take a rest! A rest, just like a note, shows us how long it should be held based on its shape. A whole rest is taken for 4 beats, a half rest for 2 beats and so on." ,
			"image": ["/static/pictures/rest.png"]
	}
}

quiz_data  = {
	"1": {
		"id": 1,
		"question_image": True,
		"answer_image": False,
		"Question": "What is this note?",
		"Image": ["/static/pictures/F_note.png"],
		"Size": ['250px', '250px'],
		"Answers": {
			"A": "A",
			"B": "B",
			"C": "F",
			"D": "G"
		},
		"Correct_answer": "C"
	},
	"2": {
		"id": 2,
		"question_image": True,
		"answer_image": False,
		"Question": "How many beats does this hold note hold for?",
		"Image": ["/static/pictures/one_eighth_note.png"],
		"Size": ['250px', '250px'],
		"Answers":{
			"A": "1/2",
			"B": "1/4",
			"C": "1/8",
			"D": "1"
		},
		"Correct_answer": "A"
	},
	"3": {
		"id": 3,
		"question_image": False,
		"answer_image": True,
		"Question": "Click on the image corresponding to a B note",
		"Answers":{
			"A": "/static/pictures/F_note.png",
			"B": "/static/pictures/B_note.png",
			"C": "/static/pictures/C_note.png",
			"D": "/static/pictures/D_note.png"
		},
		"Correct_answer": "B"
	},
	"4": {
		"id": 4,
		"question_image": True,
		"answer_image": False,
		"Question": "Is the below statement True or False",
		"Image": ["/static/pictures/beams_q.png"],
		"Size": [],
		"Answers":{
			"A": "True",
			"B": "False"
		},
		"Correct_answer": "A"
	},
    "5": {
		"id": 5,
		"question_image": True,
		"answer_image": False,
		"Question": "Which letter note do both these images correspond to?",
		"Image": ["/static/pictures/F_note.png", "/static/pictures/F_note2.png"],
		"Size": ['250px', '250px'],
		"Answers":{
			"A": "A",
			"B": "E",
			"C": "F",
			"D": "G"
		},
		"Correct_answer": "C"
	},
	"6": {
		"id": 6,
		"question_image": False,
		"answer_image": True,
		"Question": "Which of the following represent a half note?",
		"Answers":{
			"A": "/static/pictures/full_note.png",
			"B": "/static/pictures/quarter_note.png",
			"C": "/static/pictures/half_note.png",
			"D": "/static/pictures/one_eighth_note.png"
		},
		"Correct_answer": "C"
	},
	"7": {
		"id": 7,
		"question_image": False,
		"answer_image": False,
		"Question": "How many lines does a staff have?",
		"Answers":{
			"A": "4",
			"B": "5",
			"C": "8",
			"D": "6"
		},
		"Correct_answer": "B"
	},
	"8": {
		"id": 8,
		"question_image": True,
		"answer_image": False,
		"Question": "How many beats does this rest hold for?",
		"Image":  ["/static/pictures/restdot.png"],
		"Size": [],
		"Answers":{
			"A": "3/8",
			"B": "3",
			"C": "3/4",
			"D": "3/2"
		},
		"Correct_answer": "D"
	},
	"9": {
		"id": 9,
		"question_image": True,
		"answer_image": False,
		"Question": "Which letter note do both these images correspond to?",
		"Image":  ["/static/pictures/E_note.png", "/static/pictures/E_note2.png"],
		"Size": ['250px', '250px'],
		"Answers":{
			"A": "A",
			"B": "E",
			"C": "F",
			"D": "G"
		},
		"Correct_answer": "B"
	},
	"10": {
		"id": 10,
		"question_image": True,
		"answer_image": False,
		"Question": "Count the total number of beats in the below sheet note.",
		"Image": ["/static/pictures/count.png"],
		"Size": [],
		"Answers":{
			"A": "12",
			"B": "10",
			"C": "14",
			"D": "11"
		},
		"Correct_answer": "D"
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
	global quiz_data

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
