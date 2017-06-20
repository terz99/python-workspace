#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

DELETE_MATCHES_QUERY = "delete from matches;"
DELETE_COMPETITORS_QUERY = "delete from competitors;"

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db_connection = connect()
    cursor = db_connection.cursor()

    cursor.execute(DELETE_MATCHES_QUERY)
    db_connection.commit()

    cursor.execute("update competitors set wins=0, matches=0;")
    db_connection.commit()

    db_connection.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db_connection = connect()
    cursor = db_connection.cursor()

    cursor.execute(DELETE_COMPETITORS_QUERY)
    db_connection.commit()

    db_connection.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db_connection = connect()
    cursor = db_connection.cursor()

    cursor.execute("select count(*) from competitors;")
    num_of_players = int(cursor.fetchall()[0][0])

    db_connection.close()
    return num_of_players


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db_connection = connect()
    cursor = db_connection.cursor()

    cursor.execute("insert into competitors (name) values (%s);", (name,))
    db_connection.commit()
    
    db_connection.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db_connection = connect()
    cursor = db_connection.cursor()

    cursor.execute("select * from competitors order by wins desc;")
    list_of_players = cursor.fetchall()
    
    db_connection.close()
    return list_of_players


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db_connection = connect()
    cursor = db_connection.cursor()

    cursor.execute("insert into matches (id1, id2) values ({}, {});".format(winner, loser))
    db_connection.commit()

    cursor.execute("select wins from competitors where id={};".format(winner))
    wins_winner = int(cursor.fetchall()[0][0])
    cursor.execute("select matches from competitors where id={};".format(winner))
    matches_winner = int(cursor.fetchall()[0][0])
    cursor.execute("select matches from competitors where id={};".format(loser))
    matches_loser = int(cursor.fetchall()[0][0])

    cursor.execute("update competitors set wins={}, matches={} where id={};".format(wins_winner+1, matches_winner+1, winner))
    db_connection.commit()
    cursor.execute("update competitors set matches={} where id={};".format(matches_loser+1, loser))
    db_connection.commit()


    db_connection.close()


 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db_connection = connect()
    cursor = db_connection.cursor()

    cursor.execute("select id, name, wins from competitors order by wins")
    list_of_players = cursor.fetchall()
    pairings = []
    for i in range(0, len(list_of_players)-1, 2):
        pairings.append((list_of_players[i][0], list_of_players[i][1], list_of_players[i+1][0], list_of_players[i+1][1]))

    return pairings

