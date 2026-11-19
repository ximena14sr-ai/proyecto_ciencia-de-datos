logs_quiosco = [
    "  MOD-01 | Medicina_General | 32.5min | Turno_A102  ",
    "mod-02 | Pediatria | 12.0min | Turno_B045",
    "MOD-01 | Medicina_General | 32.5min | Turno_A102",
    "  MOD-03 | Urgencias_Menores | ERROR_QUIOSCO | Turno_C011 ",
    " mod-04 | Cardiologia | 45.0min | turno_d009 ",
    "MOD-02 | Pediatria | -5.0min | Turno_B046",
    "  MOD-01 | Medicina_General | 28.0min | Turno_A103",
    "MOD-05 | Dermatologia | 5.5min | Turno_E020  ",
    "  mod-03 | Urgencias_Menores | 19.5min | Turno_C012 ",
    "MOD-04 | Cardiologia | ERROR_LECTURA | Turno_D010",
    "  MOD-06 | Nutricion | 15.0min | Turno_F001 ",
    "mod-01 | Medicina_General | 40.0min | Turno_A104  ",
]

registros_limpios = []

for registro in logs_quiosco:
    if "ERROR" in registro.upper():
        continue

    partes = registro.split("|")
    id_modulo = partes[0].strip().upper()
    especialidad = partes[1].strip().replace("_", " ").title()
    tiempo_texto = partes[2].strip().lower()
    turno = partes[3].strip().upper()

    if tiempo_texto.endswith("min"):
        tiempo_limpio = tiempo_texto[:-3].strip()
    else:
        tiempo_limpio = tiempo_texto

    registros_limpios.append({
        "id_modulo": id_modulo,
        "especialidad": especialidad,
        "tiempo_min": tiempo_limpio,
        "turno": turno,
    })

for item in registros_limpios:
    print(item)