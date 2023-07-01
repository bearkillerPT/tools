
gradesAndECTS = {
    "ALGORITMOS AVANÇADOS":	{
    "grade": 15,
    "ects": 6.0
},
"TEORIA ALGORÍTMICA DA INFORMAÇÃO":	{
    "grade": 12,
    "ects": 6.0
},
"RECUPERAÇÃO DE INFORMAÇÃO":	{
    "grade": 11,
    "ects": 6.0
},
"VISUALIZAÇÃO DE INFORMAÇÃO":	{
    "grade": 11,
    "ects": 6.0
},
"EXPLORAÇÃO DE DADOS":	{
    "grade": 12,
    "ects": 6.0
},
"COMPUTAÇÃO EM LARGA ESCALA":	{
    "grade": 12,
    "ects": 6.0
},
"ARQUITETURAS DE SOFTWARE":	{
    "grade": 11,
    "ects": 6.0
},
"SIMULAÇÃO E OTIMIZAÇÃO" : {
    "grade": 11,
    "ects": 6.0,
},
"SISTEMAS INTELIGENTES" : {
    "grade": 10,
    "ects": 6.0,
},
"SEGURANÇA E GESTÃO DE RISCO" : {
    "grade": 15,
    "ects": 6.0,
},
"PREPARAÇÃO DE DISSERTAÇÃO / ESTÁGIO" : {
    "grade": 14,
    "ects": 18.0,
},
"SISTEMAS OPERATIVOS E DE TEMPO-REAL" : {
    "grade": 13,
    "ects": 6.0,
},
"ARQUITETURAS DE ALTO DESEMPENHO" : {
    "grade": 11,
    "ects": 6.0,
}
}

# calculate the average grade
def calculateAvg(gradesAndECTS):
    sum = 0
    totalEcts = 0
    for key in gradesAndECTS:
        sum += gradesAndECTS[key]["grade"] * gradesAndECTS[key]["ects"]
        totalEcts += gradesAndECTS[key]["ects"]
    return sum / totalEcts

print("Average grade: ", calculateAvg(gradesAndECTS))