def gen_dict(vars, size):
    dict = {}
    k = 1
    for i in vars:
        for j in range(0, size):
            dict[(i, j)] = k
            k+=1
    return dict


dict = gen_dict(['x', 'y', 'z'], 4)
print(dict)

#write a function to generate a list of clauses for the SAT problem
def gen_clauses(vars, size):
    clauses = []
    for i in vars:
        for j in range(0, size):
            clause = []
            for k in range(0, size):
                if k != j:
                    clause.append(-dict[(i, k)])
            clause.append(dict[(i, j)])
            clauses.append(clause)
    return clauses