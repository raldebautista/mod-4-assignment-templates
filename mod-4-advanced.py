'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if to_member in social_graph[from_member]['following'] and from_member in social_graph[to_member]['following']:
        answer = 'friends'
    elif to_member in social_graph[from_member]['following']:
        answer = 'follower'
    elif from_member in social_graph[to_member]['following']:
        answer = 'followed by'
    else:
        answer = 'no relationship'
    return answer


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    gameboard=list(board)
    row_sum=[]
    column_sum=[]
    cross=[]
    othercross=[]
    convertcross=[]
    total_sum=[]
    
    for y in range (len(gameboard)):
        for x in range (len(gameboard[y])):
            if gameboard[y][x] == 'O':
                gameboard[y][x]=7
            elif board[y][x] == 'X':
                gameboard[y][x]=1
            elif board[y][x] == '':
                gameboard[y][x]=0

    for x in range (len(gameboard)):
        row_sum.append(sum(gameboard[x]))           
    for x in range (len(gameboard)):
        column_sum.append(sum([item[x] for item in gameboard])) 
    for x in range (len(gameboard)):
        cross.append(gameboard[x][x])
    for x in range (len(gameboard)):
        othercross.append([item[len(gameboard)-1-x] for item in gameboard])
    for x in range (len(gameboard)):
        convertcross.append(othercross[x][x])
                
    total_sum = row_sum+column_sum
    total_sum.append(sum(cross))
    total_sum.append(sum(convertcross))
    
    if 7*len(gameboard) in total_sum:
            answer='O'
    elif 1*len(gameboard) in total_sum:
            answer='X'
    else:
            answer='NO WINNER'
            
    return answer


def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    new_keys=list(route_map.keys())
    first_keys=[item[0]for item in new_keys]
    second_keys=[item[1]for item in new_keys]

    newtime=list(route_map.values())
    answer=[]
    final=[]
    
    firstposition=first_keys.index(first_stop)
    secondposition=second_keys.index(second_stop)
        
    for x in range(len(newtime)):
            answer=answer+list(newtime[x].values())
    
    if first_stop == second_stop:
        return sum(answer)
    elif firstposition == secondposition:
        return answer[firstposition]
    elif firstposition<secondposition:
        final=answer[firstposition:secondposition+1]
        return sum(final)
    elif firstposition>secondposition:
        final=answer[firstposition:]+answer[:secondposition+1]
        return sum(final)
