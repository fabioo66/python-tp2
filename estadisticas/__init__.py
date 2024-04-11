def constructor(names, goals, goals_avoided, assists):
    """ This function creates a dictionary of tuples.
    Each key contains the name, and the value is a tuple
    of three elements (pos[0] = goals; pos[1] = goals_avoided;
    pos[2] = assists)
    """

    players = {}

    names = names.split()
    for name, g, ga, a in zip(names, goals, goals_avoided, assists):
        players[name] = (g, ga, a)

    return players

def goal_scorer(players):
    """This function returns a tuple
    with the name of the scorer 
    of the team and the number of goals"""

    scorer, goals= max(players.items(), key = lambda x : x[1][0])

    return scorer, goals[0]

def average(players):
    """This functions return a list of tuples with the name 
    and the average of the players based in goals, goals_avoided
    and assists"""
    
    return [(player, (stats[0] * 1.5) + (stats[1] * 1.25) + stats[2]) for player, stats in players.items()]

def mvp(players):
    """This function receives the list of tuples
    and returns the player who had the best performance 
    on the field"""
    average_list = average(players)
    
    most_influential = max(average_list, key = lambda x : x[1])
    return most_influential[0]

def goals_average(goals):
    """This function receives the list of 
    goals of the entire team and returns 
    average of goals per match taking
    into account that 25 matches were played"""

    return sum(goals)/25

def goal_scorer_average(players):
    """This function receives a tuple that
    contains name and goals. Returns his/her goal average"""
    player = goal_scorer(players)
    
    return player[1]/25