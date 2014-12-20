from action import Action
from actionLayer import ActionLayer
from util import Pair
from proposition import Proposition
from propositionLayer import PropositionLayer

class PlanGraphLevel(object):
  """
  A class for representing a level in the plan graph.
  For each level i, the PlanGraphLevel consists of the actionLayer and propositionLayer at this level in this order!
  """
  independentActions = []  # updated to the independentActions of the propblem GraphPlan.py line 31 
  actions = []             # updated to the actions of the problem GraphPlan.py line 32 and planningProblem.py line 25
  props = []               # updated to the propositions of the problem GraphPlan.py line 33 and planningProblem.py line 26
  
  @staticmethod
  def setIndependentActions(independentActions):
    PlanGraphLevel.independentActions = independentActions
  
  @staticmethod  
  def setActions(actions):
    PlanGraphLevel.actions = actions
  
  @staticmethod    
  def setProps(props):
    PlanGraphLevel.props = props   
  
  def __init__(self):
    """
    Constructor
    """
    self.actionLayer = ActionLayer()    		    # see actionLayer.py
    self.propositionLayer = PropositionLayer()	# see propositionLayer.py
  
  def getPropositionLayer(self):
  # returns the proposition layer
    return self.propositionLayer
  
  def setPropositionLayer(self, propLayer):
  # sets the proposition layer
    self.propositionLayer = propLayer  
  
  def getActionLayer(self):
  # returns the action layer
    return self.actionLayer
    
  def setActionLayer(self, actionLayer):
  # sets the action layer
    self.actionLayer = actionLayer

  def updateActionLayer(self, previousPropositionLayer):
    """ 
    Updates the action layer given the previous proposition layer (see propositionLayer.py)
    You should add an action to the layer if its preconditions are in the previous propositions layer,
    and the preconditions are not pairwise mutex. 
    allAction is the list of all the action (include noOp) in the domain
    You might want to use those functions:
    previousPropositionLayer.isMutex(prop1, prop2) returns true if prop1 and prop2 are mutex at the previous propositions layer
    previousPropositionLayer.allPrecondsInLayer(action) returns true if all the preconditions of action are in the previous propositions layer
    self.actionLayer.addAction(action) adds action to the current action layer
    """ 
    allActions = PlanGraphLevel.actions
    "*** YOUR CODE HERE ***"
    
  def updateMutexActions(self, previousLayerMutexProposition):
    """
    Updates the mutex list in self.actionLayer,
    given the mutex proposition from the previous layer.
    currentLayerActions are the actions in the current action layer
    You might want to use this function:
    self.actionLayer.addMutexActions(action1, action2)
    adds the pair (action1, action2) to the mutex list in the current action layer
    Note that action is *not* mutex with itself
    """
    currentLayerActions = self.actionLayer.getActions()
    "*** YOUR CODE HERE ***"
    
  def updatePropositionLayer(self):
    """
    Updates the propositions in the current proposition layer,
    given the current action layer.
    don't forget to update the producers list!
    Note that same proposition in different layers might have different producers lists,
    hence you should create two different instances.
    currentLayerActions is the list of all the actions in the current layer.
    You might want to use those functions:
    dict() creates a new dictionary that might help to keep track on the propositions that you've
           already added to the layer
    self.propositionLayer.addProposition(prop) adds the proposition prop to the current layer       
    
    """
    currentLayerActions = self.actionLayer.getActions()
    "*** YOUR CODE HERE ***"
    
  def updateMutexProposition(self):
    """
    updates the mutex propositions in the current proposition layer
    You might want to use those functions:
    mutexPropositions(prop1, prop2, currentLayerMutexActions) returns true if prop1 and prop2 are mutex in the current layer
    self.propositionLayer.addMutexProp(prop1, prop2) adds the pair (prop1, prop2) to the mutex list of the current layer
    """
    currentLayerPropositions = self.propositionLayer.getPropositions()
    currentLayerMutexActions =  self.actionLayer.getMutexActions()
    "*** YOUR CODE HERE ***"
    
  def expand(self, previousLayer):
    """
    Your algorithm should work as follows:
    First, given the propositions and the list of mutex propositions from the previous layer,
    set the actions in the action layer. 
    Then, set the mutex action in the action layer.
    Finally, given all the actions in the current layer,
    set the propositions and their mutex relations in the proposition layer.   
    """
    previousPropositionLayer = previousLayer.getPropositionLayer()
    previousLayerMutexProposition = previousPropositionLayer.getMutexProps()

    "*** YOUR CODE HERE ***"
            
  def expandWithoutMutex(self, previousLayer):
    """
    Questions 11 and 12
    You don't have to use this function
    """
    previousLayerProposition = previousLayer.getPropositionLayer()
    "*** YOUR CODE HERE ***"
		
def mutexActions(a1, a2, mutexProps):
  """
  This function returns true if a1 and a2 are mutex actions.
  We first check whether a1 and a2 are in PlanGraphLevel.independentActions,
  this is the list of all the independent pair of actions (according to your implementation in question 1).
  If not, we check whether a1 and a2 have competing needs
  """ 
  if Pair(a1,a2) not in PlanGraphLevel.independentActions:
    return True    
  return haveCompetingNeeds(a1, a2, mutexProps)

def haveCompetingNeeds(a1, a2, mutexProps):
  """
  Complete code for deciding whether actions a1 and a2 have competing needs,
  given the mutex proposition from previous level (list of pairs of propositions).
  Hint: for propositions p  and q, the command  "Pair(p, q) in mutexProps"
        returns true if p and q are mutex in the previous level
  """
  "*** YOUR CODE HERE ***" 
		
def mutexPropositions(prop1, prop2, mutexActions):
  """
  complete code for deciding whether two propositions are mutex,
  given the mutex action from the current level (list of pairs of actions).
  Your updateMutexProposition function should call this function
  You might want to use this function:
  prop1.getProducers() returns the list of all the possible actions in the layer that have prop1 on their add list
  """
  "*** YOUR CODE HERE ***"
