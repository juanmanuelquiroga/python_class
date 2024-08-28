import clips
import tkinter as tk
from tkinter import messagebox

# Configurar el sistema experto con CLIPS
sistemaExperto = clips.Environment()

# Definir las reglas en CLIPS para clasificar tipos de motos
reglas = [
    "(defrule moto_deportiva (cilindrada ?c&:(>= ?c 600)) (manejo deportivo) => (assert (tipo moto MT09)))",
    "(defrule moto_crucero (cilindrada ?c&:(>= ?c 500)) (manejo relajado) => (assert (tipo moto_crucero)))",
    "(defrule moto_naked (cilindrada ?c&:(<= ?c 650)) (manejo urbano) => (assert (tipo moto_naked)))",
    "(defrule moto_touring (cilindrada ?c&:(>= ?c 800)) (manejo viajes_largos) => (assert (tipo moto_touring)))",
    "(defrule moto_scooter (cilindrada ?c&:(<= ?c 400)) (manejo urbano) => (assert (tipo moto_scooter)))",
    "(defrule moto_enduro (cilindrada ?c&:(>= ?c 250)) (manejo todoterreno) => (assert (tipo moto_enduro)))"
]

for regla in reglas:
    sistemaExperto.build(regla)

# Función que evalúa las reglas y selecciona el tipo de moto
def clasificar_moto():
    # Limpiar las aserciones anteriores
    sistemaExperto.reset()

    # Insertar hechos en CLIPS según la selección del usuario
    sistemaExperto.assert_string(f"(cilindrada {cilindrada_var.get()})")
    sistemaExperto.assert_string(f"(manejo {manejo_var.get()})")

    # Ejecutar las reglas
    sistemaExperto.run()

    resultado = "No se encontró un tipo de moto para esta combinación."

    # Revisar cada hecho en el sistema experto
    for fact in sistemaExperto.facts():
        fact_str = str(fact)
        if "(tipo " in fact_str:
            tipo_moto = fact_str.split("(tipo ")[1].split(")")[0].strip()
            resultado = f"Tipo de Moto: {tipo_moto}"
            break

    # Mostrar el resultado
    messagebox.showinfo("Clasificación de Moto", resultado)


# Crear la ventana principal
root = tk.Tk()
root.title("Sistema Experto de Clasificación de Motos")

# Variables para almacenar las selecciones
cilindrada_var = tk.StringVar()
manejo_var = tk.StringVar(value="urbano")

# Etiquetas y menús desplegables para las opciones
tk.Label(root, text="Cilindrada (cc):").pack()
tk.Entry(root, textvariable=cilindrada_var).pack()

tk.Label(root, text="Tipo de Manejo:").pack()
tk.OptionMenu(root, manejo_var, "deportivo", "relajado", "urbano", "viajes_largos", "todoterreno").pack()

# Botón para ejecutar la clasificación
tk.Button(root, text="Clasificar Moto", command=clasificar_moto).pack()

# Iniciar la aplicación
root.mainloop()
