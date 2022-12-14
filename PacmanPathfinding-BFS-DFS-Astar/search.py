# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from asyncio.windows_events import NULL
from pathlib import Path
import this
from tkinter import E
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    # print("Start:", problem.getStartState())
    # print("STARTS SUCCESSORS: ", problem.getSuccessors(problem.getStartState()))

    # for child in problem.getSuccessors(problem.getStartState()):
    #     print("CHILD: ", child[0])
    #     print("GOAL???: ", problem.isGoalState(child[0]))
    #     print("CHILD SUCCESSORS: ", problem.getSuccessors(child[0]))
    
    stack = util.Stack()
    visited = set()

    start = problem.getStartState()
    parent = None
    direction = None
    stack.push((start, parent, direction))

    goal = NULL
    
    while not stack.isEmpty():
        current = stack.pop()

        if current[0] not in visited:
            visited.add(current[0])

        if problem.isGoalState(current[0]):
            # print("------------------GOAL REACHED------------------")
            goal = current
            break
        
        # print("CURRENT: ", current[0])

        for child in problem.getSuccessors(current[0]):
            if child[0] not in visited:
                # print("---CHILD: ", child[0])
                stack.push((child[0], current, child[1]))

    directionList = []

    while goal[1] != None:
        directionList.insert(0, goal[2])
        goal = goal[1]
    
    return directionList

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first.
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """

    queue = util.Queue()
    visited = set()

    start = problem.getStartState()
    parent = None
    direction = None
    queue.push((start, parent, direction))

    goal = NULL
    
    while not queue.isEmpty():
        current = queue.pop()

        if current[0] not in visited:
            visited.add(current[0])

        if problem.isGoalState(current[0]):
            # print("------------------GOAL REACHED------------------")
            goal = current
            break
        
        # print("CURRENT: ", current[0])

        for child in problem.getSuccessors(current[0]):
            if child[0] not in visited:
                # print("---CHILD: ", child[0])
                queue.push((child[0], current, child[1]))
                visited.add(child[0])

    directionList = []

    while goal[1] != None:
        directionList.insert(0, goal[2])
        goal = goal[1]
    
    return directionList

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""

    queue = util.PriorityQueue()
    visited = set()
    cost = 0

    start = problem.getStartState()
    parent = None
    direction = None
    queue.push((start, parent, direction, cost), cost)

    goal = NULL
    
    while not queue.isEmpty():
        current = queue.pop()

        if current[0] not in visited:
            visited.add(current[0])

        if problem.isGoalState(current[0]):
            # print("------------------GOAL REACHED------------------")
            goal = current
            break
        
        # print("CURRENT: ", current[0])

        for child in problem.getSuccessors(current[0]):
            if child[0] not in visited or problem.isGoalState(child[0]):
                # print("---CHILD: ", child[0])
                cost = child[2] + current[3]
                queue.update((child[0], current, child[1], cost), cost)
                visited.add(child[0])

    directionList = []

    while goal[1] != None:
        directionList.insert(0, goal[2])
        goal = goal[1]
    
    return directionList

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    
    queue = util.PriorityQueue()
    visited = set()
    cost = 0

    start = problem.getStartState()
    parent = None
    direction = None
    queue.push((start, parent, direction, cost), cost)

    goal = NULL
    
    while not queue.isEmpty():
        current = queue.pop()

        if current[0] not in visited:
            visited.add(current[0])

        if problem.isGoalState(current[0]):
            # print("------------------GOAL REACHED------------------")
            goal = current
            break
        
        # print("CURRENT: ", current[0])

        for child in problem.getSuccessors(current[0]):
            if child[0] not in visited or problem.isGoalState(child[0]):
                # print("---CHILD: ", child[0])
                cost = child[2] + current[3] - heuristic(current[0], problem) + heuristic(child[0], problem)
                queue.update((child[0], current, child[1], cost), cost)
                visited.add(child[0])

    directionList = []

    while goal[1] != None:
        directionList.insert(0, goal[2])
        goal = goal[1]
    
    return directionList

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
