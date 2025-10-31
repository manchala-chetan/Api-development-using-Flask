from flask import Flask,jsonify,request
import ipl
import ipl2

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello world'

# -- Define a route on how an user needs to redirect
@app.route('/api/teams')
def teams():
    teams = ipl.teamsAPI()
    return jsonify(teams)

@app.route('/api/teamvsteam')
def team_vs_team():
    team1 = request.args.get('team1')
    team2 = request.args.get('team2')
    response = ipl.team_vs_teamAPI(team1, team2)
    return jsonify(response)
    


@app.route('/api/team-record')
def team_record():
    team_name = request.args.get('team')
    response = ipl2.teamAPI(team_name)
    return response

@app.route('/api/batting-record')
def batting_record():
    batsman_name = request.args.get('batsman')
    response = ipl2.batsmanAPI(batsman_name)
    return response

@app.route('/api/bowling-record')
def bowling_record():
    bowler_name = request.args.get('bowler')
    response = ipl2.bowlerAPI(bowler_name)
    return response


app.run(debug=True)