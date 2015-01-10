# analysis.py
# -----------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

######################
# ANALYSIS QUESTIONS #
######################

# Change these default values to obtain the specified policies through
# value iteration.

def question2():
    #removing noise made it worth while to cross the bridge,once it was
    # relatively safe(less option for falling) the agent crossed
    answerDiscount = 0.9
    answerNoise = 0.01
    return answerDiscount, answerNoise


def question3a():
    #discount is bigger, living reward negative,noise reduced
    answerDiscount = 0.4
    answerNoise = 0.01
    answerLivingReward = -1.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3b():
    #discount is bigger, living reward negative
    answerDiscount = 0.4
    answerNoise = 0.2
    answerLivingReward = -1.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3c():
    #noise is lower
    answerDiscount = 0.9
    answerNoise = 0.01
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3d():
    #original values
    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = 0.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3e():
    #living reward is higher
    answerDiscount = 0.9
    answerNoise = 0.2
    answerLivingReward = 1.0
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question6():
    """
    answerEpsilon = None
    answerLearningRate = None
    return answerEpsilon, answerLearningRate
    """
    return 'NOT POSSIBLE'


if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis

    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('Question %s:\t%s' % (q, str(response)))
