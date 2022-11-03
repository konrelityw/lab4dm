import numpy as np

matrix = [[1, 1, 1, 0, 0],
          [1, 0, 0, 0, 1],
          [1, 1, 1, 0, 0],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 0]]


def isReflective(matrix):
    reflective = True
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if (i == j):
                if (matrix[i][j] != 1):
                    reflective = False
                    return reflective

    return reflective


resultReflective = isReflective(matrix)


def isSymmetric(matrix):
    symmetric = True
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if ((matrix[i][j] != matrix[j][i]) & (i != j)):
                symmetric = False
                return symmetric

    return symmetric


resultSymmetric = isSymmetric(matrix)


def isTransitivity(matrix):
    transitivity = True
    for a in range(len(matrix)):
        for b in range(len(matrix)):
            for c in range(len(matrix)):
                if ((matrix[a][b] == 1) & (matrix[b][c] == 1)):
                    if (not (matrix[a][c] == 1)):
                        transitivity = False
                        return transitivity

    return transitivity


resultTransitivity = isTransitivity(matrix)


def isAntisymmetric(matrix):
    antisymmetric = True
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if ((matrix[i][j] == 1) & (matrix[j][i] != 0) & (i != j)):
                antisymmetric = False
                return antisymmetric

    return antisymmetric


resultAntisymmetric = isAntisymmetric(matrix)


def isAsymmetric(matrix):
    asymmetric = True
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if ((matrix[i][j] == 1) & (matrix[j][i] != 0)):
                asymmetric = False
                return asymmetric

    return asymmetric


resultAsymmetric = isAsymmetric(matrix)


def isEquivalence():
    if (resultReflective == True & resultTransitivity == True & resultSymmetric == True):
        print("Дане відношення є відношенням еквівалентності")
    else:
        print("Дане відношення НЕ є відношенням еквівалентності")


isEquivalence()


def isPartialOrder():
    if (resultReflective == True & resultAntisymmetric == True & resultTransitivity == True):
        print("Дане відношення є частковим порядком")
    else:
        print("Дане відношення НЕ є частковим порядком")


isPartialOrder()


def isStrictOrder():
    if (resultTransitivity == True & resultAntisymmetric == True & resultReflective == False):
        print("Дане відношення є строгим порядком")
    else:
        print("Дане відношення НЕ є строгим порядком")


isStrictOrder()


def reflectiveClosure(matrix):
    matrix1 = matrix
    for i in range(len(matrix1)):
        matrix1[i][i] = 1

    return matrix1


print("рефлективне замикання")
print(reflectiveClosure(matrix))


def symmetricalClosure(matrix):
    matrix1 = matrix
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            if not i == j:
                if matrix1[i][j] == 1:
                    matrix1[j][i] = 1

    return matrix1


print("симетричне замикання")
print(symmetricalClosure(matrix))


def transitiveClosure(matrix):
    matrix1 = matrix
    for a in range(len(matrix1)):
        for b in range(len(matrix1)):
            if not a == b:
                if matrix1[a][b] == 1:
                    for c in range(len(matrix1)):
                        matrix1[a][c] = matrix1[a][c] | matrix1[b][c]

    return matrix1


print("транзитивне замикання")
print(transitiveClosure(matrix))


def getComposition(matComp1, matComp2):
    length = len(matComp1)
    matComp = np.zeros((length, length))
    for c in range(length):
        for b in range(length):
            for a in range(length):
                if (matComp1[a][b] == 1) & (matComp2[b][c] == 1):
                    matComp[a][c] = 1
                    break

    return matComp


matComp1 = [[1, 1, 1, 0, 0],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0]]

matComp2 = getComposition(matComp1, matComp1)

matComp3 = getComposition(matComp2, matComp1)

print("другий степінь заданого відношення")
print(matComp2)
print("третій степінь заданого відношення")
print(matComp3)
