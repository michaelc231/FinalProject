# This is Michael Connelly's NFC East Application Markdown files

This application was designed to store the current players and teams in the National Football league.  This version currently stores data on all the teams in the National Football Conference in the Eastern Division.  

The fields in the Teams table will be: Team ID, Team Name and Team Location.

The fields in the Players table will be: Player ID, Player Name, Player Height, Player Weight, Player Position, and Player's Team from the team table.

The primary key in the Teams table is TeamID and the primary key in the Players table is PlayerID. Below are both tables and there contents.

## Teams Table:

Team ID |     Team Name   | Team Location
---------|------------------|-----------------------------------
1        | New York Giants | East Rutherford, NJ
2        | Dallas Cowboys | Dallas, TX
3        |  Philadelphia Eagles |Philadelphia, PA
4        |  Washington Redskins |Washington, D.C.



## Players Table  :

Player ID | Player Name | Height | Weight | Position | Team Name
------| -------------| --------|------|------------|---------|
1 | Eli Manning |  6-5 | 220 | QB | New York Giants
2 | Carson Wentz|  6-5 | 237 | QB | Philadelphia Eagles
3 | Dak Prescott|  6-2 | 229 | QB | Dallas Cowboys
4 | Alex Smith |  6-4 |216| QB | Washington Redskins
5 | Odell Beckham Jr. |  5-11 | 198 | WR | New York Giants
6 | Saquon Barkley |  5-11 | 234 | RB | New York Giants
7 | Ezekiel Elliott |  6-0 | 225 | RB | Dallas Cowboys


## To Run this DogBase Application
  *Make sure to use Python version 2.7.x.*

### Install necessary virtual environment file:

  *$ virtualenv venv*

### Activate the virtual environment:

  *$ source venv/bin/activate*

### Install necessary packages

  *$ pip install -r requirements.txt*

### Initialize the database

  *$ python manage.py deploy*

### Run the development server with the debugger on

  *$ python manage.py runserver -d*
