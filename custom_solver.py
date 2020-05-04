from ortools.linear_solver import pywraplp

solver = pywraplp.Solver('LinearProgrammingExample', pywraplp.Solver.CBC_MIXED_INTEGER_PROGRAMMING)

variable_names = list(map(lambda x: x[:-1], open('variables.txt', 'r').readlines()))

# Non Negative Constraints
variables = [solver.IntVar(0, 1, variable_names[i]) for i in range(len(variable_names))]
# variables = [solver.BoolVar(variable_names[i]) for i in range(len(variable_names))]

# Constraints
with open('constraints.txt', 'r') as lines:
    for line in lines:
        left, right = line.split('=')
        is_less = left[-1] == '>'
        left, right = left[:-2].split('+'), float(right.strip())
        consts = list(map(lambda x: (float(x[1:x.index(')(')]), x[x.index(')(') + 2:-1]), left))
        if is_less:
            temp_constraint = solver.Constraint(-solver.infinity(), right)
        else:
            temp_constraint = solver.Constraint(right, solver.infinity())
        for cnt in consts:
            temp_constraint.SetCoefficient(variables[variable_names.index(cnt[1])], cnt[0])

# Objective Function
typ, obj_fn = open('objective.txt', 'r').readlines()
is_max = typ == 'Min\n'
obj_fn_vars = list(
    map(lambda x: (float(x[1:x.index(')(')]), x[x.index(')(') + 2:-1]), list(map(str, obj_fn[:-1].split('+')))))

objective = solver.Objective()
for cnt in obj_fn_vars:
    objective.SetCoefficient(variables[variable_names.index(cnt[1])], cnt[0])
if is_max:
    objective.SetMaximization()
else:
    objective.SetMinimization()
solver.Solve()

opt_solution = sum(list(map(lambda x: x[0] * variables[variable_names.index(x[1])].solution_value(), obj_fn_vars)))
# print('Optimum Value: ', opt_solution)
for i in range(len(variable_names)):
    print(variable_names[i] + ' : ', (variables[i].solution_value()))
