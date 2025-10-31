# IPL Statistics API

A Flask-based REST API that provides various statistics about Indian Premier League (IPL) cricket matches.

## Features

- Get list of all IPL teams
- View head-to-head statistics between two teams
- Get detailed team records including matches played, wins, losses, and performance against other teams
- Access batting statistics for individual players
- Access bowling statistics for individual players

## API Endpoints

### 1. Get All Teams
```
GET /api/teams
```
Returns a list of all IPL teams that have participated in the tournament.

### 2. Team vs Team Statistics
```
GET /api/teamvsteam?team1={team1_name}&team2={team2_name}
```
Returns head-to-head statistics between two teams including:
- Total matches played
- Wins for each team
- Number of drawn matches

### 3. Team Record
```
GET /api/team-record?team={team_name}
```
Returns comprehensive statistics for a specific team including:
- Overall record (matches played, won, lost, no results, titles)
- Performance against each team

### 4. Batting Statistics
```
GET /api/batting-record?batsman={batsman_name}
```
Returns detailed batting statistics including:
- Total innings, runs, fours, sixes
- Average and strike rate
- Fifties and hundreds
- Highest score
- Performance against each team

### 5. Bowling Statistics
```
GET /api/bowling-record?bowler={bowler_name}
```
Returns detailed bowling statistics including:
- Innings bowled, wickets taken
- Economy rate, average, strike rate
- Best bowling figures
- Performance against each team

## Data Source
The API uses two primary data sources:
- IPL Matches dataset
- IPL Ball-by-ball dataset

Both datasets are accessed via Google Sheets CSV exports.

## Technical Details

### Dependencies
- Flask
- Pandas
- NumPy

### Files Structure
- `app.py`: Main Flask application with API routes
- `ipl.py`: Contains team-related statistics functions
- `ipl2.py`: Contains player-related statistics functions (batting and bowling)

## Running the Application

1. Install the required dependencies:
```bash
pip install flask pandas numpy
```

2. Run the Flask application:
```bash
python app.py
```

The API will be available at `http://localhost:5000` 
This will only runs in your Local System

## Error Handling
- Invalid team names will return an appropriate error message
- The API includes exception handling for data processing errors
