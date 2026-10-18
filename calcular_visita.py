def calcular_visita(zona, trabajo_mismo_dia, es_fin_de_semana):
    if trabajo_mismo_dia:
        return 0
    if zona == "centrica":
        return 8000
    if zona == "periferica":
        return 12000
    if zona == "fuera_ciudad":
        return 18000
