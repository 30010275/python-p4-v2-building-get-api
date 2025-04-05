from app import app
from models import db, Game

with app.app_context():
    games = Game.query.all()
    print("Games in database:", [game.title for game in games])
    
    if games:
        first_game = games[0].to_dict()
        print("First game data:", first_game)
    else:
        print("No games found in database")
