# Apertura y almacenamiento del texto del txt

with open(r"C:\Users\NAZARENO\Documents\Codigo\Facultad\OrgContable\competenciaEncriptacion\text.txt", "r") as text:
    content = text.read()

print("Texto del txt: ", content)

alphabetGlobal = "abcdefghijklmnñopqrstwuvxyz"

# Contador de letras del txt para distinguir el total con el que se cuantificaran las instancias de las letras

def counterLettersFromFile(txtContent):
    alphabetLocal = "abcdefghijklmnñopqrstwuvxyz"
    counterAllLetters = 0
    for letter in txtContent:
        if letter == "":
            pass
        else:
            if letter.lower() in alphabetLocal:
                counterAllLetters+=1
    
    return counterAllLetters

print("Numero de letras del txt: ", counterLettersFromFile(content))

# Cuantificador de instancias de las letras

def lettersInTxt(txtContent):
    alphabetLocal = "abcdefghijklmnñopqrstwuvxyz"
    instanceLog = {letter: 0 for letter in alphabetLocal} # Para cada par de clave y valor letter, se inicializa en 0 por cada letter del alphabet

    # Se recorre el contenido del txt
    for letterTxt in txtContent:  
        letterTxt = letterTxt.lower()
        # Si existe una instancia de esa letra en el diccionario, se sobrescribe su valor en la clave correspondiente  
        if letterTxt in instanceLog:   
            instanceLog[letterTxt] += 1

    return instanceLog

test = lettersInTxt(content)

numberOfLetters = counterLettersFromFile(content)

instances = lettersInTxt(content)

def showLetterPercentage(numberOfLetters, instanceLog):
    print("Porcentaje de las intancias del txt: ")
    alphabetLocal = "abcdefghijklmnñopqrstwuvxyz"

    counter = 0
    for elem in instanceLog.values():
        letter = alphabetLocal[counter]
        counter+=1
        print(f"{letter}: ({(elem/numberOfLetters*100)} %)")

showLetterPercentage(numberOfLetters, instances)

# Codificacion de los parrafos

def encodeTxt(txt, displacement):

    alphabetLocal = "abcdefghijklmnñopqrstwuvxyz"
    alphabetLocalList = list(alphabetLocal)
    txtList = list(txt)

    for letter in range(len(txt)):
        if displacement > len(alphabetLocalList):
            txtList[letter] = alphabetLocalList[letter+displacement-(len(alphabetLocalList))]
        else:
            txtList[letter] = alphabetLocalList[letter+displacement]

    return "".join(txtList)

# Solo llega hasta 50 el desplazamiento, hacer uno que lo haga con numeros infinitos de desplazamientos

print(encodeTxt("hola", 51)) 


