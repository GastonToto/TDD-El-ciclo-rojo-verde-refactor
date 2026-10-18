def calcular_visita(zona, trabajo_mismo_dia, es_fin_de_semana):
    if trabajo_mismo_dia:
        return 0
    if zona == "centrica":
        visita = 8000
        if es_fin_de_semana:
            visita = 12000
        return visita
    if zona == "periferica":
        return 12000
    if zona == "fuera_ciudad":
        return 18000
    if zona not in ("centrica", "periferica", "fuera_ciudad"):
        raise ValueError("Zona inexistente")