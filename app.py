from flask import Flask, jsonify
from elo_algorithm import calculate_elo_rating
app = Flask(__name__)
#Dummy data
data = [{
    "name": "Sidhant",
    "rating": 1600,
    "description": "Googoogaagaa"
},
    {
    "name": "Tony Stark",
    "rating": 1500,
    "description": "Iron man"
}]

#Get all the users
@app.route('/')
def main():
    for i in data:
        print(i["rating"])
    return jsonify(data)

#Id1 is the index of the winner, Id2 is the index of the loser
@app.route('/match/<id1>/<id2>', methods=['POST'])
def match(id1, id2):
    id1, id2 = int(id1),int(id2)
    data[int(id1)]['rating'], data[id2]['rating'] = calculate_elo_rating(
        data[id1]['rating'], data[id2]['rating'])
    return jsonify(data)


if __name__ == '__main__':
    app.run()
