def createDomainFile(domainFileName, n):
    numbers = list(range(n))  # [0,...,n-1]
    pegs = ['a', 'b', 'c']
    domain_file = open(domainFileName, 'w')  # use domain_file.write(str) to write to domain_file
    "*** YOUR CODE HERE ***"

    domain_file.close()


# t - top. t16
# a\b\c - peg. b7
# o - on. 7o12
# g - ground. g6
# M - move. M-1-a2-b3: move disc 1 from resting on 2 in a to resting on 3 in b


def write_action(name, pre_props, del_props, add_props, problem_file):
    problem_file.write("Name: " + "-".join(name) + "\n")
    problem_file.write("pre: " + " ".join(pre_props) + "\n")
    problem_file.write("add: " + " ".join(add_props) + "\n")
    problem_file.write("delete: " + " ".join(del_props) + "\n")


def createProblemFile(problemFileName, n):
    numbers = list(range(n))
    pegs = ['a', 'b', 'c']
    problem_file = open(problemFileName, 'w')  # use problem_file.write(str) to write to problem_file

    for curr_peg in pegs:
        for next_peg in pegs:
            if curr_peg == next_peg:
                continue

            for curr_disc in numbers:
                for prev_supporting in numbers[curr_disc + 1:]:
                    for next_supporting in numbers[curr_disc + 1:]:
                        if prev_supporting == prev_supporting:
                            continue

                        # Move from resting on prev to resting on next
                        name = ['M', curr_disc, curr_peg + prev_supporting, next_peg + next_supporting]
                        pre_props = [curr_peg + curr_disc, 't' + curr_disc, curr_disc + 'o' + prev_supporting,
                                     't' + next_supporting, next_peg + next_supporting]
                        add_props = [next_peg + curr_disc, curr_disc + 'o' + next_supporting, 't' + prev_supporting]
                        del_props = [curr_peg + curr_disc, curr_disc + 'o' + prev_supporting, 't' + next_supporting]

                        write_action(name, pre_props, del_props, add_props, problem_file)

                        # Move from resting on ground to resting on next
                        name = ['M', curr_disc, curr_peg, next_peg + next_supporting]
                        pre_props = [curr_peg + curr_disc, 't' + curr_disc, 'g' + curr_disc,
                                     't' + next_supporting, next_peg + next_supporting]
                        add_props = [next_peg + curr_disc, curr_disc + 'o' + next_supporting, curr_peg + 'e']
                        del_props = [curr_peg + curr_disc, 'g' + curr_disc, 't' + next_supporting]

                        write_action(name, pre_props, del_props, add_props, problem_file)

                        # Move from resting on prev to resting on ground
                        name = ['M', curr_disc, curr_peg + prev_supporting, next_peg]
                        pre_props = [curr_peg + curr_disc, curr_peg + prev_supporting, 't' + curr_disc,
                                     curr_disc + 'o' + prev_supporting, next_peg + 'e']
                        add_props = [next_peg + curr_disc, 'g' + curr_disc, 't' + prev_supporting]
                        del_props = [curr_peg + curr_disc, curr_disc + 'o' + prev_supporting, next_peg + 'e']

                        write_action(name, pre_props, del_props, add_props, problem_file)

    problem_file.close()


import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: hanoi.py n')
        sys.exit(2)

    n = int(float(sys.argv[1]))  # number of disks
    domainFileName = 'hanoi' + str(n) + 'Domain.txt'
    problemFileName = 'hanoi' + str(n) + 'Problem.txt'

    createDomainFile(domainFileName, n)
    createProblemFile(problemFileName, n)