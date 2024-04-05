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

    max_goals = -1

    for player, stats in players.items():
        if stats[0] > max_goals:
            max_goals = stats[0]
            goal_scorer = player

    tuple = (goal_scorer, max_goals)

    return tuple

def average(players):
    """This functions return a list of tuples with the name 
    and the average of the players based in goals, goals_avoided
    and assists"""
    average_list = []

    for player, stats in players.items():
        average = (stats[0] * 1.5) + (stats[1] * 1.25) + stats[2]
        average_list.append((player, average))

    return average_list

def mvp(players):
    """This function receives the list of tuples
    and returns the player who had the best performance 
    on the field"""
    average_list = average(players)
    max = -1

    for player in average_list:
        if player[1] > max:
            max = player[1]
            name = player[0]
    return name

def goals_average(goals):
    """This function receives the list of 
    goals of the entire team and returns 
    average of goals per match taking
    into account that 25 matches were played"""

    total = sum(goals)
    
    return total/25

def goal_scorer_average(players):
    """This function receives the goal_scorer and
    returns his/her goal average"""
    name = goal_scorer(players)

    goals = players[name][0]

    return goals/25 