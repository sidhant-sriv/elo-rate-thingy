from flask import Flask, jsonify
from elo_algorithm import calculate_elo_rating
import random
app = Flask(__name__)
# Dummy data
data = [{
    "name": "Sidhant",
    "rating": 1600,
    "description": "Googoogaagaa"
},
    {
    "name": "Tony Stark",
    "rating": 1500,
    "description": "Iron man"
},
{
    "name": "Dude101",
    "rating": 1300,
    "description": "Mera dimaag kharaab ho raha hai" # Checking if random matchmaking works, idk how to do rank based matchmaking yet
}]

# Get all the users
@app.route('/users')
def all_users():
    for i in data:
        print(i["rating"])
    return jsonify(data)


@app.route('/users/<id>')
def one_user(id):
    return jsonify(data[int(id)])


# Id1 is the index of the winner, Id2 is the index of the loser
@app.route('/match/<id1>/<id2>', methods=['POST'])
def match(id1, id2):
    id1, id2 = int(id1), int(id2)
    data[int(id1)]['rating'], data[id2]['rating'] = calculate_elo_rating(
        data[id1]['rating'], data[id2]['rating'])
    return jsonify(data)

@app.route('/matchmaking', methods=['GET','POST'])
def matchmaking():
    # Select random players
    player1 = random.choice(data)
    player2 = random.choice(data)

    # Ensure player1 and player2 are different
    while player1 == player2:
        player2 = random.choice(data)

    return jsonify({"player1": player1, "player2": player2})


if __name__ == '__main__':
    app.run()
