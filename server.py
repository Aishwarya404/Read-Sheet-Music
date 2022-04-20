# Contributors : Aishwarya Sivakumar, Roshan Babu, Nidhi Sunil Kumar, Yina Jian
# UNI : as6418, rbk2145, ns3566, yj2713

from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__, static_url_path='/static')


#DATA
current_id = 0
learnTime = {

}
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



# ROUTES

@app.route('/')
def welcome():
   return render_template('welcome.html')

@app.route('/middle')
def middle():
   return render_template('middle.html')

@app.route('/quiz')
def quiz():
   return render_template('quiz.html')

@app.route('/learn/<id>')
def learn(id=None):
    global learnInfo;
    single_data = learnInfo[id]
    return render_template('learn.html', single_data=single_data)

@app.route('/edit_entry', methods=['GET', 'POST'])
def edit_entry():
    global learnTime
    global current_id


    json_data = request.get_json()
    id_rn = json_data["id_rn"]
    time = json_data["time"]

    current_id += 1
    new_id = str(current_id)
    new_name_entry =  {
        "id": id_rn,
        "time": time
    }

    learnTime[new_id]=new_name_entry
    return jsonify(learnTime=learnTime)

if __name__ == '__main__':
   app.run(debug = True)
