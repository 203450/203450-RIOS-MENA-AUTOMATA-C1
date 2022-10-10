from automata.fa.dfa import DFA
from encodings import utf_8
import pandas as pd
import xlrd
from pandas import ExcelWriter
import os


# import csv

dfa = DFA(
    states = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39','q40', 'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49', 'q50', 'q51', 'q52', 'q53', 'q54', 'q55', 'q56', 'q57', 'q58', 'q59', 'q60', 'q61', 'q62', 'q63', 'q64', 'q65', 'q66', 'q67', 'q68', 'q69', 'q70', 'q71', 'q72', 'q73', 'q74', 'q75', 'q76', 'q77'},
    input_symbols = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_', '.', '(', ')', ' '},
    transitions = {

        # Extracción de ASIGNATURA
        'q0':{'A':'q1', 'B':'q1', 'C':'q1', 'D':'q1', 'E':'q1', 'F':'q1', 'G':'q1', 'H':'q1', 'I':'q1', 'J':'q1', 'K':'q1', 'L':'q1', 'M':'q1', 'N':'q1', 'Ñ':'q1', 'O':'q1', 'P':'q1', 'Q':'q1', 'R':'q1', 'S':'q1', 'T':'q1', 'U':'q1', 'V':'q1', 'W':'q1', 'X':'q1', 'Y':'q1', 'Z':'q1', 'Á':'q1', 'É':'q1', '0':'q0'},
        'q1':{'a':'q1', 'b':'q1', 'c':'q1', 'd':'q1', 'e':'q1', 'f':'q1', 'g':'q1', 'h':'q1', 'i':'q1', 'j':'q1', 'k':'q1', 'l':'q1', 'm':'q1', 'n':'q1', 'ñ':'q1', 'o':'q1', 'p':'q1', 'q':'q1', 'r':'q1', 's':'q1', 't':'q1', 'u':'q1', 'v':'q1', 'w':'q1', 'x':'q1', 'y':'q1', 'z':'q1', 'á':'q2', 'é':'q2', 'í':'q2', 'ó':'q2', 'ú':'q2', ' ':'q3'},
        'q2':{'a':'q1', 'b':'q1', 'c':'q1', 'd':'q1', 'e':'q1', 'f':'q1', 'g':'q1', 'h':'q1', 'i':'q1', 'j':'q1', 'k':'q1', 'l':'q1', 'm':'q1', 'n':'q1', 'ñ':'q1', 'o':'q1', 'p':'q1', 'q':'q1', 'r':'q1', 's':'q1', 't':'q1', 'u':'q1', 'v':'q1', 'w':'q1', 'x':'q1', 'y':'q1', 'z':'q1'},
        'q3':{'a':'q4', 'b':'q4', 'c':'q4', 'd':'q4', 'e':'q4', 'f':'q4', 'g':'q4', 'h':'q4', 'i':'q4', 'j':'q4', 'k':'q4', 'l':'q4', 'm':'q4', 'n':'q4', 'ñ':'q4', 'o':'q4', 'p':'q4', 'q':'q4', 'r':'q4', 's':'q4', 't':'q4', 'u':'q4', 'v':'q4', 'w':'q4', 'x':'q4', 'y':'q4', 'z':'q4', 'A':'q7', 'B':'q7', 'C':'q7', 'D':'q7', 'E':'q7', 'F':'q7', 'G':'q7', 'H':'q7', 'I':'q7', 'J':'q7', 'K':'q7', 'L':'q7', 'M':'q7', 'N':'q7', 'Ñ':'q7', 'O':'q7', 'P':'q7', 'Q':'q7', 'R':'q7', 'S':'q7', 'T':'q7', 'U':'q7', 'V':'q7', 'W':'q7', 'X':'q7', 'Y':'q7', 'Z':'q7', '-':'q9'},
        'q4':{'a':'q4', 'b':'q4', 'c':'q4', 'd':'q4', 'e':'q4', 'f':'q4', 'g':'q4', 'h':'q4', 'i':'q4', 'j':'q4', 'k':'q4', 'l':'q4', 'm':'q4', 'n':'q4', 'ñ':'q4', 'o':'q4', 'p':'q4', 'q':'q4', 'r':'q4', 's':'q4', 't':'q4', 'u':'q4', 'v':'q4', 'w':'q4', 'x':'q4', 'y':'q4', 'z':'q4', 'á':'q6', 'é':'q6', 'í':'q6', 'ó':'q6', 'ú':'q6', ' ':'q5'},
        'q5':{'A':'q1', 'B':'q1', 'C':'q1', 'D':'q1', 'E':'q1', 'F':'q1', 'G':'q1', 'H':'q1', 'I':'q1', 'J':'q1', 'K':'q1', 'L':'q1', 'M':'q1', 'N':'q1', 'Ñ':'q1', 'O':'q1', 'P':'q1', 'Q':'q1', 'R':'q1', 'S':'q1', 'T':'q1', 'U':'q1', 'V':'q1', 'W':'q1', 'X':'q1', 'Y':'q1', 'Z':'q1', 'a':'q4', 'b':'q4', 'c':'q4', 'd':'q4', 'e':'q4', 'f':'q4', 'g':'q4', 'h':'q4', 'i':'q4', 'j':'q4', 'k':'q4', 'l':'q4', 'm':'q4', 'n':'q4', 'ñ':'q4', 'o':'q4', 'p':'q4', 'q':'q4', 'r':'q4', 's':'q4', 't':'q4', 'u':'q4', 'v':'q4', 'w':'q4', 'x':'q4', 'y':'q4', 'z':'q4', '-':'q9'},
        'q6':{'a':'q4', 'b':'q4', 'c':'q4', 'd':'q4', 'e':'q4', 'f':'q4', 'g':'q4', 'h':'q4', 'i':'q4', 'j':'q4', 'k':'q4', 'l':'q4', 'm':'q4', 'n':'q4', 'ñ':'q4', 'o':'q4', 'p':'q4', 'q':'q4', 'r':'q4', 's':'q4', 't':'q4', 'u':'q4', 'v':'q4', 'w':'q4', 'x':'q4', 'y':'q4', 'z':'q4'},
        'q7':{'a':'q1', 'b':'q1', 'c':'q1', 'd':'q1', 'e':'q1', 'f':'q1', 'g':'q1', 'h':'q1', 'i':'q1', 'j':'q1', 'k':'q1', 'l':'q1', 'm':'q1', 'n':'q1', 'ñ':'q1', 'o':'q1', 'p':'q1', 'q':'q1', 'r':'q1', 's':'q1', 't':'q1', 'u':'q1', 'v':'q1', 'w':'q1', 'x':'q1', 'y':'q1', 'z':'q1', 'A':'q7', 'B':'q7', 'C':'q7', 'D':'q7', 'E':'q7', 'F':'q7', 'G':'q7', 'H':'q7', 'I':'q7', 'J':'q7', 'K':'q7', 'L':'q7', 'M':'q7', 'N':'q7', 'Ñ':'q7', 'O':'q7', 'P':'q7', 'Q':'q7', 'R':'q7', 'S':'q7', 'T':'q7', 'U':'q7', 'V':'q7', 'W':'q7', 'X':'q7', 'Y':'q7', 'Z':'q7', 'á':'q7', 'é':'q7', 'í':'q7', 'ó':'q7', 'ú':'q7', ' ':'q8'},
        'q8':{'-':'q9'},
        'q9':{' ':'q10'},
        # Extracción de GRUPO
        'q10':{'M':'q11', 'I':'q24', 'E':'q34', '1':'q41', '2':'q45', '3':'q45', '4':'q45', '5':'q45', '6':'q45', '7':'q45', '8':'q45', '9':'q45', 'A':'q46', 'B':'q46', 'C':'q46', 'D':'q46'},
        'q11':{'I':'q12'},
        'q12':{'X':'q13'},
        'q13':{' ':'q14'},
        'q14':{'I':'q15'},
        'q15':{'d':'q16'},
        'q16':{'s':'q17'},
        'q17':{'_':'q18'},
        'q18':{'E':'q19'},
        'q19':{'n':'q20'},
        'q20':{'e':'q21'},
        'q21':{'-':'q22'},
        'q22':{'A':'q23', 'B':'q23', 'C':'q23', 'D':'q23'},
        'q23':{' ':'q40'},
        'q24':{'D':'q25', 'd':'q29',},
        'q25':{'S':'q26'},
        'q26':{'-':'q27'},
        'q27':{'A':'q28', 'B':'q28', 'C':'q28', 'D':'q28'},
        'q28':{' ':'q40'},
        'q29':{'s':'q30'},
        'q30':{'E':'q31'},
        'q31':{'n':'q33', 'A':'q32', 'B':'q32', 'C':'q32', 'D':'q32'},
        'q32':{' ':'q40'},
        'q33':{'A':'q32', 'B':'q32', 'C':'q32', 'D':'q32'},
        'q34':{'I':'q35', 'i':'q35'},
        'q35':{'d':'q36'},
        'q36':{'s':'q37'},
        'q37':{' ':'q38'},
        'q38':{'A':'q39', 'B':'q39', 'C':'q39', 'D':'q39', ' ':'q38'},
        'q39':{' ':'q40'},
        'q40':{'-':'q54'},
        'q41':{'0':'q42','A':'q43', 'B':'q43', 'C':'q43', 'D':'q43',' ':'q44'},
        'q42':{'A':'q43', 'B':'q43', 'C':'q43', 'D':'q43', ' ':'q44'},
        'q43':{' ':'q40'},
        'q44':{'A':'q43', 'B':'q43', 'C':'q43', 'D':'q43'},
        'q45':{'A':'q43', 'B':'q43', 'C':'q43', 'D':'q43', ' ':'q44'},
        'q46':{' ':'q47'},
        'q47':{'I':'q48', '-':'q54'},
        'q48':{'d':'q49'},
        'q49':{'s':'q50'},
        'q50':{'E':'q51'},
        'q51':{'n':'q52'},
        'q52':{' ':'q40', 'e':'q53'},
        'q53':{' ':'q40'},
        'q54':{' ':'q55'},
        # Extraccion de Nombres DOCENTE
        'q55':{'A':'q56', 'B':'q56', 'C':'q56', 'D':'q56', 'E':'q56', 'F':'q56', 'G':'q56', 'H':'q56', 'I':'q56', 'J':'q56', 'K':'q56', 'L':'q56', 'M':'q56', 'N':'q56', 'Ñ':'q56', 'O':'q56', 'P':'q56', 'Q':'q56', 'R':'q56', 'S':'q56', 'T':'q56', 'U':'q56', 'V':'q56', 'W':'q56', 'X':'q56', 'Y':'q56', 'Z':'q56'},
        'q56':{'A':'q56', 'B':'q56', 'C':'q56', 'D':'q56', 'E':'q56', 'F':'q56', 'G':'q56', 'H':'q56', 'I':'q56', 'J':'q56', 'K':'q56', 'L':'q56', 'M':'q56', 'N':'q56', 'Ñ':'q56', 'O':'q56', 'P':'q56', 'Q':'q56', 'R':'q56', 'S':'q56', 'T':'q56', 'U':'q56', 'V':'q56', 'W':'q56', 'X':'q56', 'Y':'q56', 'Z':'q56', 'Á':'q57', 'É':'q57', 'Í':'q57', 'Ó':'q57', 'Ú':'q57', ' ':'q58'},
        'q57':{'A':'q56', 'B':'q56', 'C':'q56', 'D':'q56', 'E':'q56', 'F':'q56', 'G':'q56', 'H':'q56', 'I':'q56', 'J':'q56', 'K':'q56', 'L':'q56', 'M':'q56', 'N':'q56', 'Ñ':'q56', 'O':'q56', 'P':'q56', 'Q':'q56', 'R':'q56', 'S':'q56', 'T':'q56', 'U':'q56', 'V':'q56', 'W':'q56', 'X':'q56', 'Y':'q56', 'Z':'q56', ' ':'q58'},
        'q58':{'A':'q56', 'B':'q56', 'C':'q56', 'D':'q56', 'E':'q56', 'F':'q56', 'G':'q56', 'H':'q56', 'I':'q56', 'J':'q56', 'K':'q56', 'L':'q56', 'M':'q56', 'N':'q56', 'Ñ':'q56', 'O':'q56', 'P':'q56', 'Q':'q56', 'R':'q56', 'S':'q56', 'T':'q56', 'U':'q56', 'V':'q56', 'W':'q56', 'X':'q56', 'Y':'q56', 'Z':'q56', '-':'q59'},
        'q59':{' ':'q60'},
        'q60':{'A':'q61', 'B':'q61', 'C':'q61', 'D':'q61', 'E':'q61', 'F':'q61', 'G':'q61', 'H':'q61', 'I':'q61', 'J':'q61', 'K':'q61', 'L':'q61', 'M':'q61', 'N':'q61', 'Ñ':'q61', 'O':'q61', 'P':'q61', 'Q':'q61', 'R':'q61', 'S':'q61', 'T':'q61', 'U':'q61', 'V':'q61', 'W':'q61', 'X':'q61', 'Y':'q61', 'Z':'q61'},
        # Extracción de PERIODO
        'q61':{'A':'q61', 'B':'q61', 'C':'q61', 'D':'q61', 'E':'q61', 'F':'q61', 'G':'q61', 'H':'q61', 'I':'q61', 'J':'q61', 'K':'q61', 'L':'q61', 'M':'q61', 'N':'q61', 'Ñ':'q61', 'O':'q61', 'P':'q61', 'Q':'q61', 'R':'q61', 'S':'q61', 'T':'q61', 'U':'q61', 'V':'q61', 'W':'q61', 'X':'q61', 'Y':'q61', 'Z':'q61', '-':'q62'},
        'q62':{'A':'q63', 'B':'q63', 'C':'q63', 'D':'q63', 'E':'q63', 'F':'q63', 'G':'q63', 'H':'q63', 'I':'q63', 'J':'q63', 'K':'q63', 'L':'q63', 'M':'q63', 'N':'q63', 'Ñ':'q63', 'O':'q63', 'P':'q63', 'Q':'q63', 'R':'q63', 'S':'q63', 'T':'q63', 'U':'q63', 'V':'q63', 'W':'q63', 'X':'q63', 'Y':'q63', 'Z':'q63'},
        'q63':{'A':'q63', 'B':'q63', 'C':'q63', 'D':'q63', 'E':'q63', 'F':'q63', 'G':'q63', 'H':'q63', 'I':'q63', 'J':'q63', 'K':'q63', 'L':'q63', 'M':'q63', 'N':'q63', 'Ñ':'q63', 'O':'q63', 'P':'q63', 'Q':'q63', 'R':'q63', 'S':'q63', 'T':'q63', 'U':'q63', 'V':'q63', 'W':'q63', 'X':'q63', 'Y':'q63', 'Z':'q63', ' ':'q64'},
        'q64':{'2':'q65'},
        'q65':{'0':'q66'},
        'q66':{'0':'q67', '1':'q67', '2':'q67', '3':'q67', '4':'q67', '5':'q67', '6':'q67','7':'q67', '8':'q67', '9':'q67'},
        'q67':{'0':'q68', '1':'q68', '2':'q68', '3':'q68', '4':'q68', '5':'q68', '6':'q68','8':'q68', '8':'q68', '9':'q68'},
        'q68':{' ':'q69', '.':'q73'},
        # Extracción de FORMATO
        'q69':{'(':'q70'},
        'q70':{'1':'q71', '2':'q71', '3':'q71', '4':'q71', '5':'q71', '6':'q71','7':'q71', '8':'q71', '9':'q71'},
        'q71':{')':'q72'},
        'q72':{' ':'q69', '.':'q73'},
        'q73':{'x':'q74'},
        'q74':{'l':'q75'},
        'q75':{'s':'q76'},
        'q76':{'x':'q77'},
        'q77':{},

    },

    allow_partial = True,
    initial_state = 'q0',
    final_states = {'q77'}
)

cadenas = []
#secciones
asignatura = []
grupo = []
docente = []
periodopar = []
periodo = []

def evaluar(datos):

    for x in datos:

        if dfa.accepts_input(x):
            print('accepted ->', x)

            aux = x.split(" - ")
            cadenas.append(aux)
            
        # else:
        #     print('rejected ->', x)
    print("-----------------------------------------")

    for y in cadenas:

        asignatura.append(y[0])
        grupo.append(y[1])
        docente.append(y[2])
        periodopar.append(y[3][0:-5])
        
    for j in periodopar:
        
        auxi = j.replace(" ", "$", 1)
        
        auxi = auxi.split(" ")
        
        periodo.append(auxi[0].replace("$", " "))
        
    print(periodo)

    # for g in periodo:
    #     periodo
    

def obtener_cadena(dir):

    with open(dir, "r", encoding = "utf-8") as archivo:
        CONTADOR = 1
        datos = []
        for line in archivo.readlines():

            if CONTADOR >= 8 :
                new=line[36:].rstrip()
                datos.append(new)

            CONTADOR += 1
        return datos

def main(dir):
    
    datos = obtener_cadena(dir)
    evaluar(datos)
    # reporte_excel()

def reporte_excel(directorio):

    ruta = directorio
    
    print("Ruta: ", ruta)

    df = pd.DataFrame({"Asignatura":asignatura, "Grupo":grupo, "Docente":docente, "Periodo":periodo})
    print('df ', df)
    
    if os.path.exists(ruta + "/Reporte.xlsx"):
        
        print("El archivo existe")
        
        aux = pd.read_excel(ruta + "/Reporte.xlsx", engine ='openpyxl')
        aux = aux.append(df)
        
        
        print('aux', aux)
        
        writer = ExcelWriter(ruta + '/Reporte.xlsx')
        aux.to_excel(writer, 'Hoja de datos', index=False)
    else:
        
        print("El archivo no existe")
        
        writer = ExcelWriter(ruta + '/Reporte.xlsx')
        df.to_excel(writer, 'Hoja de datos', index=False)

    writer.save()
    
    # archivos_reporte = []
    
    # archivos_reporte.append(pd.read_excel(ruta + "/Reporte.xlsx", engine ='openpyxl'))
    
    # for r in archivos_reporte:
    
    #     print(r)
    
    



    # data = pd.DataFrame({"Asignatura":asignatura, "Grupo":grupo, "Docente":docente, "Periodo":periodo})

    # escritor = pd.ExcelWriter("./reporte/Reporte.xlsx", engine = "xlsxwriter")

    # data.to_excel(escritor, sheet_name = "Hoja1", index = False)

    # escritor.save()

    # print("\ndatos guardados en excel exitosamente\n")

    # data.to_excel('Reporte.xlsx', sheet_name='Hoja1', index=False)

