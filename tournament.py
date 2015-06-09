import psycopg2

#connect to the database and receive cursor.
tour = psycopg2.connect(dbname="tournament")
cursor = tour.cursor()

#Name        : registerPlayer
#Description : Add player in to the database by name. (database assigns ID)
#Parameters  : name
#Return      : none
def registerPlayer(name):
    cursor.execute("INSERT INTO players(name) VALUES (%s)", (name,))
    tour.commit()

#Name        : deletePlayers
#Description : Delete all the players from the database.
#Parameters  : none
#Return      : none	
def deletePlayers():
    cursor.execute("DELETE FROM players")
    tour.commit()

#Name        : playerStandings
#Description : Fetch all the players data ordered by most wins.
#Parameters  : none
#Return      : id, name, wins, total-matches	
def playerStandings():
    cursor.execute("SELECT id, name, wins, wins+losses FROM players ORDER BY wins")
    return cursor.fetchall()

#Name        : countPlayers
#Description : Return total numbers of players.
#Parameters  : none
#Return      : total
def countPlayers():
    cursor.execute("SELECT COUNT(id) FROM players")
    total = int((cursor.fetchall())[0][0])
    return total

#Name        : reportMatch
#Description : Insert winner and loser record in to the database.
#              Also increase players' wins and loses. 
#Parameters  : winner, loser
#Return      : none	
def reportMatch(winner, loser):
    cursor.execute("INSERT INTO matches(winner, loser) VALUES (%s, %s)", (winner, loser))
    tour.commit()

    cursor.execute("UPDATE players SET wins = wins + 1 WHERE id = (%s)", (winner,))
    tour.commit()

    cursor.execute("UPDATE players SET losses = losses + 1 WHERE id = (%s)", (loser,))
    tour.commit()

#Name        : deleteMatches
#Description : Delete all the matches from the database.
#Parameters  : none
#Return      : none	
def deleteMatches():
    cursor.execute("DELETE FROM matches")
    tour.commit()

#Name        : swissPairings
#Description : Given the existing set of registered players and the matches they have played,
#              generates and returns a list of pairings according to the Swiss system. 
#              Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of
#              the paired players. .
#Parameters  : none
#Return      : pairs	
def swissPairings():
    pairs = []
    cursor.execute("SELECT id, name FROM players ORDER BY wins")
    rows = cursor.fetchmany(2)
    while rows:
        pair = []
        for row in rows:
            pair += list(row)
        pairs.append(tuple(pair))
        rows = cursor.fetchmany(2)
    return pairs