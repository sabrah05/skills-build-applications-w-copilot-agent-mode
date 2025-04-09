use octofit_db;
printjson(db.getCollectionNames());
printjson(db.users.find().toArray());
printjson(db.teams.find().toArray());
printjson(db.activity.find().toArray());
printjson(db.leaderboard.find().toArray());
printjson(db.workouts.find().toArray());
