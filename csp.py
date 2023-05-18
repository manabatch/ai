from constraint import Problem

def solve_csp(variables, domains, constraints):
    problem = Problem()
    
    for variable in variables:
        problem.addVariable(variable, domains[variable])
    
    for constraint in constraints:
        problem.addConstraint(constraint[1], constraint[0])
    
    return problem.getSolutions()

variables = ['A', 'B', 'C']
domains = {
    'A': [1, 2, 3],
    'B': [1, 2],
    'C': [1, 2, 3]
}
constraints = [
    (('A', 'B'), lambda a, b: a != b),
    (('B', 'C'), lambda b, c: b < c)
]

solutions = solve_csp(variables, domains, constraints)

if solutions:
    print("Solution found:")
    for solution in solutions:
        print(solution)
else:
    print("No solution found.")

