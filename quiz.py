import clips
import tkinter as tk
from tkinter import messagebox

# Configurar el sistema experto con CLIPS
sistemaExperto = clips.Environment()

# Definir las reglas en CLIPS para recomendar destinos y actividades con lugares específicos para cada combinación
reglas = [
    # Playa
    "(defrule destino_playa_bajo_descanso (preferencia playa) (presupuesto bajo) (necesidad descanso) => (assert (recomendacion 'santa marta')))",
    "(defrule destino_playa_bajo_lujo (preferencia playa) (presupuesto bajo) (necesidad lujo) => (assert (recomendacion 'Islas Baleares, España')))",
    "(defrule destino_playa_bajo_aventura (preferencia playa) (presupuesto bajo) (necesidad aventura) => (assert (recomendacion 'Surf en San Juan del Sur, Nicaragua')))",
    "(defrule destino_playa_medio_descanso (preferencia playa) (presupuesto medio) (necesidad descanso) => (assert (recomendacion 'Tenerife, España')))",
    "(defrule destino_playa_medio_lujo (preferencia playa) (presupuesto medio) (necesidad lujo) => (assert (recomendacion 'Bahamas')))",
    "(defrule destino_playa_medio_aventura (preferencia playa) (presupuesto medio) (necesidad aventura) => (assert (recomendacion 'Buceo en Roatán, Honduras')))",
    "(defrule destino_playa_alto_descanso (preferencia playa) (presupuesto alto) (necesidad descanso) => (assert (recomendacion 'Maldivas')))",
    "(defrule destino_playa_alto_lujo (preferencia playa) (presupuesto alto) (necesidad lujo) => (assert (recomendacion 'Bora Bora, Polinesia Francesa')))",
    "(defrule destino_playa_alto_aventura (preferencia playa) (presupuesto alto) (necesidad aventura) => (assert (recomendacion 'Kitesurf en Mauricio')))",

    # Montaña
    "(defrule destino_montaña_bajo_descanso (preferencia montaña) (presupuesto bajo) (necesidad descanso) => (assert (recomendacion 'Parque Nacional de los Picos de Europa, España')))",
    "(defrule destino_montaña_bajo_lujo (preferencia montaña) (presupuesto bajo) (necesidad lujo) => (assert (recomendacion 'Cabañas de lujo en los Pirineos, España')))",
    "(defrule destino_montaña_bajo_aventura (preferencia montaña) (presupuesto bajo) (necesidad aventura) => (assert (recomendacion 'Parque Nacional Torres del Paine, Chile')))",
    "(defrule destino_montaña_medio_descanso (preferencia montaña) (presupuesto medio) (necesidad descanso) => (assert (recomendacion 'Cabañas en los Alpes, Suiza')))",
    "(defrule destino_montaña_medio_lujo (preferencia montaña) (presupuesto medio) (necesidad lujo) => (assert (recomendacion 'Estancia en Aspen, EE. UU.')))",
    "(defrule destino_montaña_medio_aventura (preferencia montaña) (presupuesto medio) (necesidad aventura) => (assert (recomendacion 'Zermatt, Suiza')))",
    "(defrule destino_montaña_alto_descanso (preferencia montaña) (presupuesto alto) (necesidad descanso) => (assert (recomendacion 'Lodge de lujo en los Andes, Chile')))",
    "(defrule destino_montaña_alto_lujo (preferencia montaña) (presupuesto alto) (necesidad lujo) => (assert (recomendacion 'Resort en Whistler, Canadá')))",
    "(defrule destino_montaña_alto_aventura (preferencia montaña) (presupuesto alto) (necesidad aventura) => (assert (recomendacion 'Patagonia, Argentina')))",

    # Ciudad
    "(defrule destino_ciudad_bajo_descanso (preferencia ciudad) (presupuesto bajo) (necesidad descanso) => (assert (recomendacion 'Visita a Praga, República Checa')))",
    "(defrule destino_ciudad_bajo_lujo (preferencia ciudad) (presupuesto bajo) (necesidad lujo) => (assert (recomendacion 'Atenas, Grecia')))",
    "(defrule destino_ciudad_bajo_aventura (preferencia ciudad) (presupuesto bajo) (necesidad aventura) => (assert (recomendacion 'Exploración en Estambul, Turquía')))",
    "(defrule destino_ciudad_medio_descanso (preferencia ciudad) (presupuesto medio) (necesidad descanso) => (assert (recomendacion 'Florencia, Italia')))",
    "(defrule destino_ciudad_medio_lujo (preferencia ciudad) (presupuesto medio) (necesidad lujo) => (assert (recomendacion 'Dubái, EAU')))",
    "(defrule destino_ciudad_medio_aventura (preferencia ciudad) (presupuesto medio) (necesidad aventura) => (assert (recomendacion 'Nueva York, EE. UU.')))",
    "(defrule destino_ciudad_alto_descanso (preferencia ciudad) (presupuesto alto) (necesidad descanso) => (assert (recomendacion 'París, Francia')))",
    "(defrule destino_ciudad_alto_lujo (preferencia ciudad) (presupuesto alto) (necesidad lujo) => (assert (recomendacion 'Tokio, Japón')))",
    "(defrule destino_ciudad_alto_aventura (preferencia ciudad) (presupuesto alto) (necesidad aventura) => (assert (recomendacion 'Sídney, Australia')))",

    # Relajación
    "(defrule actividad_relajacion_bajo_descanso (preferencia relajacion) (presupuesto bajo) => (assert (recomendacion 'Retiros en Koh Phangan, Tailandia')))",
    "(defrule actividad_relajacion_medio_descanso (preferencia relajacion) (presupuesto medio) => (assert (recomendacion 'Retiro de spa en Bali, Indonesia')))",
    "(defrule actividad_relajacion_alto_descanso (preferencia relajacion) (presupuesto alto) => (assert (recomendacion 'Resorts en Maldivas')))",

    # Aventura
    "(defrule actividad_aventura_bajo_aventura (preferencia aventura) (presupuesto bajo) => (assert (recomendacion 'Senderismo en el Parque Nacional de los Picos de Europa, España')))",
    "(defrule actividad_aventura_medio_aventura (preferencia aventura) (presupuesto medio) => (assert (recomendacion 'Rafting en el Río Futaleufú, Chile')))",
    "(defrule actividad_aventura_alto_aventura (preferencia aventura) (presupuesto alto) => (assert (recomendacion 'Escalada en el Monte Everest, Nepal')))"
]

for regla in reglas:
    sistemaExperto.build(regla)

# Función que evalúa las reglas y selecciona el destino y la actividad recomendada
def recomendar_viaje():
    # Limpiar las aserciones anteriores
    sistemaExperto.reset()

    # Insertar hechos en CLIPS según la selección del cliente
    sistemaExperto.assert_string(f"(preferencia {preferencia_var.get()})")
    sistemaExperto.assert_string(f"(presupuesto {presupuesto_var.get()})")
    sistemaExperto.assert_string(f"(necesidad {necesidad_var.get()})")

    # Ejecutar las reglas
    sistemaExperto.run()

    resultado = "No se encontró una recomendación adecuada para esta combinación."

    # Revisar cada hecho en el sistema experto
    for fact in sistemaExperto.facts():
        fact_str = str(fact)
        if "(recomendacion " in fact_str:
            recomendacion = fact_str.split("(recomendacion ")[1].split(")")[0].strip().strip("'")
            resultado = f"Recomendación: Visita {recomendacion}"
            break

    # Mostrar el resultado
    messagebox.showinfo("Recomendación de Viaje", resultado)


# Crear la ventana principal
root = tk.Tk()
root.title("Sistema Experto de Recomendación de Viajes")

# Variables para almacenar las selecciones
preferencia_var = tk.StringVar(value="playa")
presupuesto_var = tk.StringVar(value="medio")
necesidad_var = tk.StringVar(value="descanso")

# Etiquetas y menús desplegables para las opciones
tk.Label(root, text="Preferencia de Viaje:").pack()
tk.OptionMenu(root, preferencia_var, "playa", "montaña", "ciudad", "relajacion", "aventura").pack()

tk.Label(root, text="Presupuesto:").pack()
tk.OptionMenu(root, presupuesto_var, "bajo", "medio", "alto").pack()

tk.Label(root, text="Necesidad del Cliente:").pack()
tk.OptionMenu(root, necesidad_var, "descanso", "lujo", "aventura", "cultura").pack()

# Botón para ejecutar la recomendación
tk.Button(root, text="Recomendar Viaje", command=recomendar_viaje).pack()

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
