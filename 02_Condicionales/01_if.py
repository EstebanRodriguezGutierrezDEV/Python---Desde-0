print("Programa de evaluación de alumnos")

note_alum = int(input("Intruduce la nota del alumno"))

def evaluate(note):
    value = "Aprobado"
    if note < 5:
        value = "Suspenso"

    return value

print(evaluate(note_alum))