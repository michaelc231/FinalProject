import os
from flask import Flask, session, render_template, request, flash, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


# define database tables
class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    location = db.Column(db.String(64))
    players = db.relationship('Player', backref='team', cascade="delete")

class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    height = db.Column(db.String(64))
    weight = db.Column(db.Integer())
    pos = db.Column(db.String(64))
    team_id= db.Column(db.Integer, db.ForeignKey('teams.id'))


# app routes

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/team')
def show_all_teams():
    teams = Team.query.all()
    return render_template('team-all.html', teams=teams)

@app.route('/team/add', methods=['GET','POST'])
def add_group():
    if request.method == 'GET':
        return render_template('team-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        location = request.form['location']

        # insert the data into the database
        teams = Team(name=name, location=location)
        db.session.add(teams)
        db.session.commit()
        return redirect(url_for('show_all_teams'))

@app.route('/ajax/team/add', methods=['POST'])
def add_ajax_team():
    # get data from the form
    name = request.form['name']
    location = request.form['location']

    # insert the data into the database
    team = Team(name=name, location=location)
    db.session.add(team)
    db.session.commit()
    # flash message type: success, info, warning, and danger from bootstrap
    flash('Team Inserted', 'success')
    return jsonify({"id": str(team.id), "name": team.name})

@app.route('/team/edit/<int:id>', methods=['GET', 'POST'])
def edit_teams(id):
    teams = Team.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('team-edit.html', team=teams)
    if request.method == 'POST':
        # update data based on the form data
        teams.name = request.form['name']
        teams.location = request.form['location']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_teams'))


@app.route('/team/delete/<int:id>', methods=['GET', 'POST'])
def delete_team(id):
    teams = Team.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('team-delete.html', team=teams)
    if request.method == 'POST':
        # delete the groups by id

        db.session.delete(teams)
        db.session.commit()
        return redirect(url_for('show_all_teams'))


@app.route('/ajax/team/<int:id>', methods=['DELETE'])
def delete_ajax_team(id):
    teams = Team.query.get_or_404(id)
    db.session.delete(teams)
    db.session.commit()
    return jsonify({"id": str(team.id), "name": team.name})

@app.route('/player')
def show_all_players():
    player = Player.query.all()
    return render_template('player-all.html', player=player)

@app.route('/player/add', methods=['GET', 'POST'])
def add_players():
    if request.method == 'GET':
        player = Player.query.all()
        return render_template('player-add.html', player=player)
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        height = request.form['height']
        weight = request.form['weight']
        pos = request.form['pos']
        team_id = request.form['team_id']
        team = Team.query.filter_by(name=team_id).first()
        player = Player(name=name, height=height, weight=weight, pos=pos, team=team)

        # insert the data into the database
        db.session.add(player)
        db.session.commit()
        return redirect(url_for('show_all_players'))


@app.route('/player/edit/<int:id>', methods=['GET', 'POST'])
def edit_player(id):
    player = Player.query.filter_by(id=id).first()
    team = Team.query.all()
    if request.method == 'GET':
        return render_template('player-edit.html', player=player, team=team)
    if request.method == 'POST':
        # update data based on the form data
        player.name = request.form['name']
        player.height = request.form['height']
        player.weight = request.form['weight']
        player.pos = request.form['pos']
        team_name = request.form['team']
        team = Team.query.filter_by(name=team_name).first()
        team.name = teams
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_teams'))


@app.route('/player/delete/<int:id>', methods=['GET', 'POST'])
def delete_players(id):
    player = Player.query.filter_by(id=id).first()
    team = Team.query.all()
    if request.method == 'GET':
        return render_template('player-delete.html', players=player, teams=team)
    if request.method == 'POST':
        db.session.delete(player)
        db.session.commit()
        return redirect(url_for('show_all_players'))


@app.route('/ajax/player/<int:id>', methods=['DELETE'])
def delete_ajax_player(id):
    player = Player.query.get_or_404(id)
    db.session.delete(player)
    db.session.commit()
    return jsonify({"id": str(player.id), "name": player.name})



@app.route('/about')
def about():

    return render_template('about.html')





if __name__ == '__main__':
    app.run()
