"""
qa-student-tracker - Módulo principal
Sistema minimalista de validación de entregas académicas.
"""


def validar_entrega(nombre: str, nota: float, en_tiempo: bool) -> dict:
    """
    Valida si una entrega académica cumple los criterios mínimos.

    Args:
        nombre: Nombre de la entrega.
        nota: Nota obtenida (0-100).
        en_tiempo: Si fue entregada a tiempo.

    Returns:
        dict con estado y mensaje.
    """
    if not nombre or not isinstance(nombre, str):
        return {"estado": "error", "mensaje": "Nombre inválido"}
    if not (0 <= nota <= 100):
        return {"estado": "error", "mensaje": "Nota fuera de rango (0-100)"}

    aprobado = nota >= 61 and en_tiempo
    return {
        "estado": "aprobado" if aprobado else "reprobado",
        "nombre": nombre,
        "nota": nota,
        "en_tiempo": en_tiempo,
        "mensaje": "Entrega válida" if aprobado else "Entrega no cumple criterios",
    }


def calcular_promedio(notas: list) -> float:
    """
    Calcula el promedio de una lista de notas.

    Args:
        notas: Lista de valores numéricos.

    Returns:
        Promedio como float, o 0.0 si la lista está vacía.
    """
    if not notas:
        return 0.0
    return round(sum(notas) / len(notas), 2)


def estado_estudiante(promedio: float) -> str:
    """
    Determina el estado académico según el promedio.

    Args:
        promedio: Promedio del estudiante.

    Returns:
        Estado como string.
    """
    if promedio >= 90:
        return "Excelente"
    elif promedio >= 75:
        return "Satisfactorio"
    elif promedio >= 61:
        return "Aprobado"
    else:
        return "Reprobado"
