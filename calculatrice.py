# Création d'une calculatrice en python3.11

# Import de la bibliothèque tkinter
import tkinter as tk

# Import de la bibliothèque Customtkinter
import customtkinter as cst


# Fonction pour supprimer toutes les valeurs dans entry_ope
def sup_entry_ope():
    vide = ""
    var_entry_ope.set(vide)
    var_entry_result.set(vide)


# Fonction pour supprimer le dernier caractère
def sup_last_entry_ope():
    val_tmp = var_entry_ope.get()
    if val_tmp != "":
        val = val_tmp[0:-1]
        var_entry_ope.set(val)
        eval_expression(var_entry_ope.get())


def format_result(result):
    sign_virg = result.find(".")
    if sign_virg > -1:
        nb1, nb2 = result.split(result[sign_virg])
        if len(nb2) > 6:
            nb2 = nb2[:6]

        result_tmp = nb1 + "." + nb2

        return result_tmp
    else:
        return result


def format_result_negatif(result):
    sign_moins = result.find("-")
    # si le signe est en premier
    if sign_moins == 0:
        return "- " + result[1:]
    else:
        return result


def find_int_or_float(nb1, nb2):
    # nb1 et nb2 sont des strings
    virg_nb1 = nb1.find(".")
    virg_nb2 = nb2.find(".")

    if virg_nb1 > -1:
        nb1 = float(nb1)
    else:
        nb1 = int(nb1)

    if virg_nb2 > -1:
        nb2 = float(nb2)
    else:
        nb2 = int(nb2)

    return nb1, nb2


# Fonction pour convertir une valeur en euros
def convert_en_dollar(expression):
    c = 0
    # Vérif si expression est vide
    if expression != "":
        # Vérif si signe dans expression:
        for i in expression:
            if i in key_sign:
                c += 1
        if c == 0:
            valeur = float(expression) * 1.1041
            valeur = "%.6f" % valeur
            var_entry_result.set(valeur)


# Fonction pour calculer un pourcentage
def calcul_pourcent(expression):
    # Vérif si expression est vide
    if expression != "":
        expression_tmp = ""
        # On enlève les espaces dans l'expression
        for i in expression:
            if i != " ":
                expression_tmp += i

        expression = expression_tmp

        # recherche signe 'x' pour savoir si c'est bien un pourcentage
        sign_multipli = expression.find("x")

        if sign_multipli > -1:
            nb1, nb2 = expression.split(expression[sign_multipli])
            if nb1 != "" and nb2 != "":
                nb_tmp1, nb_tmp2 = find_int_or_float(nb1, nb2)
                valeur = (nb_tmp1 * nb_tmp2) / 100
                val_tmp = str(valeur)
                if val_tmp[-1] == "0" and val_tmp[-2] == ".":
                    val_tmp = val_tmp[:-2]
                    var_entry_result.set(val_tmp)
                    var_entry_ope.set(val_tmp)
                else:
                    valeur = format_result(val_tmp)
                    var_entry_result.set(valeur)
                    var_entry_ope.set(valeur)


def calcul_expression(nb1, nb2, sign):
    if sign == "+":
        nb_tmp1, nb_tmp2 = find_int_or_float(nb1, nb2)
        valeur = nb_tmp1 + nb_tmp2
        val_tmp = str(valeur)
        valeur = format_result(val_tmp)
        return valeur

    elif sign == "-":
        nb_tmp1, nb_tmp2 = find_int_or_float(nb1, nb2)
        valeur = nb_tmp1 - nb_tmp2
        val_tmp = str(valeur)
        valeur = format_result(val_tmp)
        return valeur

    elif sign == "x":
        nb_tmp1, nb_tmp2 = find_int_or_float(nb1, nb2)
        valeur = nb_tmp1 * nb_tmp2
        val_tmp = str(valeur)
        valeur = format_result(val_tmp)
        return valeur

    elif sign == "/":
        if nb1 == "0":
            return "Div 0 Error"
        else:
            nb_tmp1, nb_tmp2 = find_int_or_float(nb1, nb2)
            valeur = nb_tmp1 / nb_tmp2
            val_tmp = str(valeur)
            if val_tmp[-1] == "0" and val_tmp[-2] == ".":
                val_tmp = val_tmp[:-2]
                return val_tmp
            else:
                valeur = format_result(val_tmp)
                return valeur


def eval_expression(expression):
    # Variable qui récupère la valeur dans 'entry_result'
    # entry_result_tmp = var_entry_result.get()

    expression_tmp = ""

    # Vérif si 'expression est vide'
    if expression != "":
        # On enlève les espaces dans l'expression
        for i in expression:
            if i != " ":
                expression_tmp += i

        expression = expression_tmp

        # L'expression ne commence pas par un '-'
        if expression[0] != "-":
            # Recherche des signes dans l'expression
            sign_plus = expression.find("+")
            sign_moins = expression.find("-")
            sign_multipli = expression.find("x")
            sign_divise = expression.find("/")

            if sign_plus > -1:
                nb1, nb2 = expression.split(expression[sign_plus])
                if nb1 != "" and nb2 != "":
                    result = calcul_expression(nb1, nb2, "+")
                    if result != "":
                        result = format_result_negatif(result)
                        var_entry_result.set(str(result))
                else:
                    var_entry_result.set("")

            elif sign_moins > -1:
                nb1, nb2 = expression.split(expression[sign_moins])
                if nb1 != "" and nb2 != "":
                    result = calcul_expression(nb1, nb2, "-")
                    if result != "":
                        result = format_result_negatif(result)
                        var_entry_result.set(str(result))
                else:
                    var_entry_result.set("")

            elif sign_multipli > -1:
                nb1, nb2 = expression.split(expression[sign_multipli])
                if nb1 != "" and nb2 != "":
                    result = calcul_expression(nb1, nb2, "x")
                    if result != "":
                        result = format_result_negatif(result)
                        var_entry_result.set(str(result))
                else:
                    var_entry_result.set("")

            elif sign_divise > -1:
                nb1, nb2 = expression.split(expression[sign_divise])
                if nb1 != "" and nb2 != "":
                    result = calcul_expression(nb1, nb2, "/")
                    if result != "":
                        result = format_result_negatif(result)
                        var_entry_result.set(str(result))
                else:
                    var_entry_result.set("")

        # Si l'expression commence par un '-' valeur négative
        else:
            val_tmp = expression[0]
            if val_tmp == "-":
                expression = expression[1:]

                # Recherche des signes dans l'expression
                sign_plus = expression.find("+")
                sign_moins = expression.find("-")
                sign_multipli = expression.find("x")
                sign_divise = expression.find("/")
                sign_pourcent = expression.find("%")

                if sign_plus > -1:
                    nb1, nb2 = expression.split(expression[sign_plus])
                    if nb1 != "" and nb2 != "":
                        nb1 = "-" + nb1
                        result = calcul_expression(nb1, nb2, "+")
                        if result != "":
                            result = format_result_negatif(result)
                            var_entry_result.set(str(result))
                    else:
                        var_entry_result.set("")

                elif sign_moins > -1:
                    nb1, nb2 = expression.split(expression[sign_moins])
                    if nb1 != "" and nb2 != "":
                        nb1 = "-" + nb1
                        result = calcul_expression(nb1, nb2, "-")
                        if result != "":
                            result = format_result_negatif(result)
                            var_entry_result.set(str(result))
                    else:
                        var_entry_result.set("")

                elif sign_multipli > -1:
                    nb1, nb2 = expression.split(expression[sign_multipli])
                    if nb1 != "" and nb2 != "":
                        nb1 = "-" + nb1
                        result = calcul_expression(nb1, nb2, "x")
                        if result != "":
                            result = format_result_negatif(result)
                            var_entry_result.set(str(result))
                    else:
                        var_entry_result.set("")

                elif sign_divise > -1:
                    nb1, nb2 = expression.split(expression[sign_divise])
                    if nb1 != "" and nb2 != "":
                        nb1 = "-" + nb1
                        result = calcul_expression(nb1, nb2, "/")
                        if result != "":
                            result = format_result_negatif(result)
                            var_entry_result.set(str(result))
                    else:
                        var_entry_result.set("")

    else:
        var_entry_result.set("")


# 1- Fonction qui récupère la touche enfoncé et l'affiche dans "entry_ope"
def press_key(val):
    # Variable qui récupère la valeur dans 'entry_ope'
    entry_ope_tmp = var_entry_ope.get()

    # Vérif de la valeur
    for x, row in enumerate(lst_keys):
        for y, el in enumerate(row):
            if val == el:
                if val == "AC":
                    sup_entry_ope()

                elif val == "<x":
                    sup_last_entry_ope()

                elif val == "$":
                    convert_en_dollar(entry_ope_tmp)

                elif val == "%":
                    calcul_pourcent(entry_ope_tmp)

                elif val == ".":
                    if entry_ope_tmp == "":
                        entry_ope_tmp += "0" + val
                        # Affichage de la valeur dans 'entry_ope'
                        var_entry_ope.set(entry_ope_tmp)
                    else:
                        entry_ope_tmp += val
                        # Affichage de la valeur dans 'entry_ope'
                        var_entry_ope.set(entry_ope_tmp)

                elif val in key_sign:
                    entry_result_tmp = var_entry_result.get()
                    if entry_result_tmp == "":
                        if entry_ope_tmp != "":
                            entry_ope_tmp += " " + val + " "
                            # Affichage de la valeur dans 'entry_ope'
                            var_entry_ope.set(entry_ope_tmp)

                    else:
                        entry_ope_tmp = entry_result_tmp
                        entry_ope_tmp += " " + val + " "
                        var_entry_ope.set(entry_ope_tmp)

                elif val == "=":
                    # Lancement fonction pour evaluer la valeur global
                    eval_expression(entry_ope_tmp)
                    var_entry_ope.set(var_entry_result.get())
                    var_entry_result.set("")

                else:
                    if val in lst_numbers:
                        entry_ope_tmp += val
                        # Affichage de la valeur dans 'entry_ope'
                        var_entry_ope.set(entry_ope_tmp)

                        # Lancement fonction pour evaluer la valeur global
                        eval_expression(entry_ope_tmp)


# On créer la fenêtre **********************************************
# Liste des signes
key_sign = ["+", "-", "x", "/"]
lst_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

cst.set_appearance_mode("dark")
cst.set_default_color_theme("blue")

fen = cst.CTk()

# fen = tk.Tk()
fen.title(" Calculatrice")
fen.geometry("350x408")
# fen.configure(bg='#264b59')

# Variable pour 'entry_ope'
var_entry_ope = tk.StringVar()
# Création du entry qui va recevoir les opérations
entry_ope = cst.CTkEntry(
    fen, textvariable=var_entry_ope, font=("arial", 28), justify="right"
)
entry_ope.pack(pady=15, fill="x", padx=5)

# var_entry_result = tk.StringVar()
var_entry_result = tk.StringVar()
# Création du entry qui reçoit les résultats
entry_result = cst.CTkEntry(
    fen, textvariable=var_entry_result, font=("arial", 18), justify="right", width=240
)

entry_result.pack(fill="x", pady=2, padx=5)

# Création d'un frame pour les boutons
# frame_button = tk.Frame(fen)
frame_button = cst.CTkFrame(fen, fg_color="transparent")
frame_button.pack(pady=10, padx=5)

# Création des bouttons pour les chiffres et autres
lst_keys = [
    ["AC", "$", "%", "/"],
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "<x", "="],
]


for pos_row, row in enumerate(lst_keys):
    for pos_col, col in enumerate(row):
        cst.CTkButton(
            frame_button,
            text=col,
            width=80,
            height=50,
            corner_radius=20,
            border_color="#1f1792",
            border_width=1,
            font=("arial", 16),
            command=lambda col_temp=col: press_key(col_temp),
        ).grid(column=pos_col, row=pos_row, padx=2, pady=3)


fen.mainloop()
