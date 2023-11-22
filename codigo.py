import re

# Definir un diccionario que asocie símbolos y palabras reservadas con números de estado
simbolos_y_palabras_reservadas = {
    '{': 200,
    '#': 201,
    '}': 202,
    '<': 1,
    '<=': 203,
    '<-': 2,
    '<-<': 3,
    '<-<-': 204,
    '>': 4,
    '>=': 205,
    ':': 5,
    '::': 206,
    ':=': 6,
    ':==': 207,
    '[': 7,
    '[[': 208,
    ']': 8,
    ']]': 209,
    '+': 210,
    '-': 211,
    ',': 212,
    '/,': 213,
    '*': 223,
    '=': 224,
    '(': 225,
    ')': 226,
    '.': 227,
    ' ': 228,
    'integer': 220,
    'decimal': 220,
    'string': 220,
    'logical': 220,
    'list': 220,
    'funcion': 220,
    'return': 220,
    'main': 220,
    'length': 220,
    'real': 220,
    'add': 220,
    'minimal': 220,
    'maximal': 220,
    'condition': 220,
    'in': 220,
    'true': 220,
    'while': 220,
    'for': 220,
    'repeat': 220,
    'doing': 220,
    'elif': 220,
    'else': 220,
    'range': 220,
    'and': 220,
    'or': 220,
    'input()': 220,
    'abs()': 220,
    'string()': 220,
    'power()': 220,
    'round()': 220,
}

# Agregamos las combinaciones especiales
combinaciones_especiales = {'::', '<-<-', '{{', '}}', '[[' , ']]', ':==', '>=', '<='}

# Creamos un regex que coincida con las combinaciones especiales
regex_combinaciones_especiales = re.compile('|'.join(f'({re.escape(c)})' for c in combinaciones_especiales))

identificador_regex = r'[a-zA-Z_][a-zA-Z0-9_]*'
entero_regex = r'\d+'
decimal_regex = r'\d+\.\d+'
notacion_cientifica_regex = r'\d+\.\d+[eE][-+]?\d+'


def analizar_archivo(archivo):
    with open(archivo, 'r') as f:
        contenido = f.read()

    pos = 0
    while pos < len(contenido):
        encontrado = False

        # Buscamos combinaciones especiales
        match_combinacion = regex_combinaciones_especiales.match(contenido, pos)
        if match_combinacion:
            combinacion = next((c for c in match_combinacion.groups() if c), None)
            print(f"Token encontrado: Estado {simbolos_y_palabras_reservadas[combinacion]} ({combinacion})")
            pos += len(combinacion)
            encontrado = True

        # Si no se encuentra una combinación especial, se verifica el resto de los símbolos y palabras reservadas
        if not encontrado:
            for simbolo, estado in simbolos_y_palabras_reservadas.items():
                if contenido.startswith(simbolo, pos):
                    print(f"Token encontrado: Estado {estado} ({simbolo})")
                    pos += len(simbolo)
                    encontrado = True
                    break

        # Si no se encuentra ninguna combinación especial ni símbolo, se continúa con las demás reglas
        if not encontrado:
            match = re.match(identificador_regex, contenido[pos:])
            if match:
                identificador = match.group(0)
                print(f"Identificador: Identificador ({identificador})")
                pos += len(identificador)
                encontrado = True

        if not encontrado:
            match = re.match(notacion_cientifica_regex, contenido[pos:])
            if match:
                numero = match.group(0)
                print(f"Número en notación científica: Numero notacion cientifica ({numero})")
                pos += len(numero)
                encontrado = True

        if not encontrado:
            match = re.match(decimal_regex, contenido[pos:])
            if match:
                numero = match.group(0)
                print(f"Número decimal: NumeroDecimal ({numero})")
                pos += len(numero)
                encontrado = True

        if not encontrado:
            match = re.match(entero_regex, contenido[pos:])
            if match:
                numero = match.group(0)
                print(f"Número entero: NumeroEntero ({numero})")
                pos += len(numero)
                encontrado = True

        if not encontrado:
            match = re.match(r'\s+', contenido[pos:])
            if match:
                espacio = match.group(0)
                print(f"Espacio: Espacio en blanco ({espacio})")
                pos += len(espacio)
                encontrado = True

        if not encontrado:
            match_input = re.match(r'input', contenido[pos:])
            if match_input:
                print(f"Palabra reservada: Estado 220 (input())")
                pos += len("input()")
                encontrado = True

        if not encontrado:
            # Analizador sintáctico básico
            if contenido.startswith("if", pos):
                print("Estructura encontrada: if")
                pos += 2
                encontrado = True
            elif contenido.startswith("else", pos):
                print("Estructura encontrada: else")
                pos += 4
                encontrado = True
            elif contenido.startswith("elif", pos):
                print("Estructura encontrada: elif")
                pos += 4
                encontrado = True
            elif contenido.startswith("for", pos):
                print("Estructura encontrada: for")
                pos += 3
                encontrado = True
            elif contenido.startswith("while", pos):
                print("Estructura encontrada: while")
                pos += 5
                encontrado = True
            elif contenido.startswith("funcion", pos):
                print("Estructura encontrada: funcion")
                pos += 7
                encontrado = True
            elif contenido.startswith("return", pos):
                print("Estructura encontrada: return")
                pos += 6
                encontrado = True

        if not encontrado:
            pos += 1

# Ejemplo de uso
analizar_archivo('ejemplo2.txt')
