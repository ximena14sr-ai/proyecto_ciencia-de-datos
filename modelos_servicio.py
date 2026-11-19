"""Módulo de modelos de servicio para la gestión de turnos clínicos."""

TIEMPO_MAX_ESPERA_MIN = 25.0
UMBRAL_SATURACION_FILA = 8


class ModuloAtencion:
    """Representa un consultorio o módulo de atención médica."""

    def __init__(self, id_modulo: str, especialidad: str, operativo: bool = True):
        self._id_modulo = id_modulo
        self.especialidad = especialidad  # Usa el setter para validar
        self.operativo = operativo        # Usa el setter para validar
        self._tiempos_espera = []

    @property
    def especialidad(self) -> str:
        return self._especialidad

    @especialidad.setter
    def especialidad(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La especialidad no puede estar vacía.")
        self._especialidad = valor.strip()

    @property
    def operativo(self) -> bool:
        return self._operativo

    @operativo.setter
    def operativo(self, estado: bool) -> None:
        if not isinstance(estado, bool):
            raise TypeError("El estado operativo debe ser booleano (True/False).")
        self._operativo = estados