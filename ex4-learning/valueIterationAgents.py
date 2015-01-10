# valueIterationAgents.py
# -----------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import mdp, util

from learningAgents import ValueEstimationAgent


class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """

    def __init__(self, mdp, discount=0.9, iterations=100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter()  # A Counter is a dict with default 0
        self.policy = util.Counter()
        self.old_values = util.Counter()

        while self.iterations > 0:
            for state in self.mdp.getStates():
                state_actions = self.mdp.getPossibleActions(state)
                q_vals = util.Counter()
                for action in state_actions:
                    nextState_and_p = self.mdp.getTransitionStatesAndProbs(state, action)
                    for (nextState, probability) in nextState_and_p:
                        q_vals[action] += probability * (self.mdp.getReward(state, action, nextState) + self.discount*self.old_values[nextState])
                if len(q_vals.items()) is not 0:
                    max_arg = q_vals.argMax()
                    self.values[state] = q_vals[max_arg]
                    self.policy[state] = max_arg

            self.iterations -= 1
            self.old_values = self.values.copy()



    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]

    def getQValue(self, state, action):
        """
          The q-value of the state action pair
          (after the indicated number of value iteration
          passes).  Note that value iteration does not
          necessarily create this quantity and you may have
          to derive it on the fly.
        """
        nextState_and_probability = self.mdp.getTransitionStatesAndProbs(state, action)
        q_val = 0
        for (nextState, prob) in nextState_and_probability:
            q_val += prob * (self.mdp.getReward(state, action, nextState) + self.discount * self.values[nextState])
        return q_val

    def getPolicy(self, state):
        """
          The policy is the best action in the given state
          according to the values computed by value iteration.
          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        return self.policy[state]

    def getAction(self, state):
        "Returns the policy at the state (no exploration)."
        return self.getPolicy(state)
  
