from flask_script import Manager
from nfceast import app, db, Team, Player

manager = Manager(app)

# reset the database and create some initial data
@manager.command
def deploy():
    db.drop_all()
    db.create_all()

    Giants = Team(name='New York Giants', location='East Rutherford, NJ')
    Cowboys = Team(name='Dallas Cowboys', location='Dallas, TX')
    Eagles= Team(name='Philadelphia Eagles', location='Philadelphia, PA')
    Redskins = Team(name='Washington Redskins', location='Washington, D.C.')


    Manning = Player(name='Eli Manning',height='6-5', weight='220', pos='QB',  team=Giants)
    Wentz = Player(name='Carson Wentz', height='6-5', weight='237', pos='QB',  team=Eagles)
    Prescott = Player(name='Dak Prescott', height="6-2", weight='229', pos='QB',  team=Cowboys)
    Smith = Player(name='Alex Smith', height='6-4', weight='216', pos='QB',  team=Redskins)
    Beckham = Player(name='Odell Beckham Jr.', height='5-11', weight='198', pos='WR',  team=Giants)
    Barkley = Player(name='Saquon Barkley', height='5-11', weight='234', pos='RB', team=Giants)
    Elliott = Player(name='Ezekiel Elliott',height='6-0', weight='225', pos='RB',team=Cowboys)

    db.session.add(Giants)
    db.session.add(Cowboys)
    db.session.add(Eagles)
    db.session.add(Redskins)


    db.session.add(Manning)
    db.session.add(Wentz)
    db.session.add(Prescott)
    db.session.add(Smith)
    db.session.add(Beckham)
    db.session.add(Barkley)
    db.session.add(Elliott)

    db.session.commit()


if __name__ == '__main__':
    manager.run()
