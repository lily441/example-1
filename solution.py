import heapq
import sys
from constants import *
from environment import *
from state import State
"""
solution.py
# Some parts of this code were adapted from COMP3702 Tutorial 3
This file is a template you should use to implement your solution.

You should implement 

COMP3702 2022 Assignment 1 Support Code

Last updated by njc 01/08/22
"""


class StateNode:

    def __init__(self, env, state, parent, action_from_parent, path_steps, path_cost):
        """
        :param env: environment
        :param state: state belonging to this node
        :param parent: parent of this node
        :param action_from_parent: LEFT, RIGHT, UP, or DOWN
        """
        self.env = env
        self.state = state
        self.parent = parent
        self.action_from_parent = action_from_parent
        self.path_steps = path_steps
        self.path_cost = path_cost

    def get_path(self):
        """
        :return: A list of actions
        """
        path = []
        cur = self
        while cur.action_from_parent is not None:
            path.append(cur.action_from_parent)
            cur = cur.parent
        path.reverse()
        return path

    def get_successors(self):
        """
        :return: A list of successor StateNodes
        """
        successors = []
        for a in ROBOT_ACTIONS :
            success, cost, next_state = self.env.perform_action(self.state, a)
            if success:
                successors.append(
                    StateNode(self.env, next_state, self, a, self.path_steps + 1, self.path_cost + cost))
        return successors

    def __lt__(self, other):
        # compare nodes using path cost (for A*, this is overridden)
        return self.path_cost < other.path_cost

class Solver:

    def __init__(self, environment, loop_counter):
        self.environment = environment
        self.loop_counter = loop_counter
        #
        # TODO: Define any class instance variables you require here.
        #

    def solve_ucs(self):
        """
        Find a path which solves the environment using Uniform Cost Search (UCS).
        :return: path (list of actions, where each action is an element of ROBOT_ACTIONS)
        """
        container = [StateNode(self.environment, self.environment.get_init_state(), None, None, 0, 0)]
        heapq.heapify(container)
        # dict: state --> path_cost
        visited = {self.environment.get_init_state(): 0}
        n_expanded = 0
        while len(container) > 0:
            n_expanded += 1
            node = heapq.heappop(container)
            #self.loop_counter.inc()
            # check if this state is the goal
            if self.environment.is_solved(node.state):  # 若一致则完成以下操作，即完成搜索
                if 1:
                    print(f'Visited Nodes: {len(visited.keys())},\t\tExpanded Nodes: {n_expanded},\t\t'
                          f'Nodes in Container: {len(container)}')
                    print(f'Cost of Path (with Costly Moves): {node.path_cost}')
                return node.get_path()
                # add unvisited (or visited at higher path cost) successors to container
            successors = node.get_successors()
            for s in successors:
                if s.state not in visited.keys() or s.path_cost < visited[s.state]:  # 重要步骤：若s没被visited或s的cost低于到s的cost？
                    visited[s.state] = s.path_cost  # 将到达s的cost改为s。pathcost
                    heapq.heappush(container, s)  # container中为拜访过的结点 即父结点，将s加入
            self.loop_counter.inc()
            return None
        #
        # === Important ================================================================================================
        # To ensure your code works correctly with tester, you should include the following line of code in your main
        # search loop:
        #
        # self.loop_counter.inc()
        #
        # e.g.
        # while loop_condition():
        #   self.loop_counter.inc()
        #   ...
        #
        # ==============================================================================================================
        #
        #

        pass

    def solve_a_star(self):
        """
        Find a path which solves the environment using A* search.
        :return: path (list of actions, where each action is an element of ROBOT_ACTIONS)
        """

        #
        #
        # TODO: Implement your A* search code here
        #
        # === Important ================================================================================================
        # To ensure your code works correctly with tester, you should include the following line of code in your main
        # search loop:
        #
        # self.loop_counter.inc()
        #
        # e.g.
        # while loop_condition():
        #   self.loop_counter.inc()
        #   ...
        #
        # ==============================================================================================================
        #
        #

        pass

    #
    #
    # TODO: Add any additional methods here
    #
    #

