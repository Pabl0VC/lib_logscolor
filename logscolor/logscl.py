import inspect
from colorama import Fore, Style, init
import logging

# Inicializar colorama para habilitar colores en la consola
init(autoreset=True)

# Configuración de colores para los niveles de log
LEVEL_COLORS = {
    "INFO": Fore.GREEN + Style.BRIGHT,     # Color verde brillante para mensajes informativos
    "WARNING": Fore.YELLOW + Style.BRIGHT,  # Color amarillo brillante para advertencias
    "ERROR": Fore.RED + Style.BRIGHT,     # Color rojo brillante para errores
    "TRACE": Fore.BLUE + Style.BRIGHT,    # Color azul brillante para trazas o mensajes debug
}
CONTENT_COLORS = {
    "INFO": Fore.GREEN,       # Color verde para el contenido de mensajes INFO
    "WARNING": Fore.YELLOW,   # Color amarillo para el contenido de advertencias
    "ERROR": Fore.RED,        # Color rojo para el contenido de errores
    "TRACE": Fore.BLUE,       # Color azul para el contenido de trazas/debug
}
# Colores adicionales
METADATA_COLOR = Fore.BLACK  # Color negro para metadatos (ej. línea de código)
DATE_COLOR = Fore.BLACK      # Color negro para la fecha
DASH_COLOR = Fore.BLACK      # Color negro para los guiones separadores

# Crear un logger específico llamado "logscl"
logger = logging.getLogger("logscl")
logger.setLevel(logging.DEBUG)  # Configurar el nivel de log (DEBUG captura todos los niveles)

# Clase personalizada para formatear los mensajes del log
class ColorFormatter(logging.Formatter):
    """
    Formateador de logs que añade colores a los mensajes, fechas y metadatos.
    """
    def format(self, record):
        # Cambiar DEBUG a TRACE para darle un nombre más descriptivo
        if record.levelname == "DEBUG":
            record.levelname = "TRACE"

        # Obtener colores configurados para el nivel actual del mensaje
        level_color = LEVEL_COLORS.get(record.levelname, Fore.WHITE)
        content_color = CONTENT_COLORS.get(record.levelname, Fore.WHITE)

        # Obtener información adicional de dónde se generó el log
        lineno = getattr(record, "custom_lineno", "")  # Línea del código
        filename = getattr(record, "custom_filename", "Desconocido")  # Nombre del archivo

        # Aplicar colores al nivel y mensaje
        record.levelname = f"{level_color}{record.levelname}{Style.RESET_ALL}"
        record.msg = f"{content_color}{record.msg}{Style.RESET_ALL}"

        # Formatear mensaje con metadatos si están disponibles
        formatted_message = f"{record.levelname} {DASH_COLOR}- {record.msg}"
        if lineno:
            formatted_message += f" {DASH_COLOR}- {METADATA_COLOR}L: {lineno}{Style.RESET_ALL}"

        # Formatear la fecha y aplicar color
        log_time = self.formatTime(record, "%Y-%m-%d %H:%M:%S")  # Fecha sin milisegundos
        log_time = f"{DATE_COLOR}{log_time} -{Style.RESET_ALL}"  # Añadir color a la fecha

        # Retornar el mensaje formateado
        return f"{log_time} {formatted_message}"

# Configuración del handler para mostrar los mensajes en consola
formatter = ColorFormatter('%(asctime)s - %(message)s')  # Definir formato base
handler = logging.StreamHandler()  # Crear un manejador de salida estándar
handler.setFormatter(formatter)  # Asignar el formateador de colores
logger.handlers = [handler]  # Añadir el handler al logger

# Función base para generar logs con metadatos personalizados
def _log_with_metadata(level, msg, with_line=False):
    """
    Registra un mensaje en el nivel especificado con metadatos opcionales.

    :param level: Nivel de log ('info', 'warning', 'error', 'trace')
    :param msg: Mensaje o datos a registrar
    :param with_line: Si True, incluye la línea de código donde se llamó al log
    """
    frame = inspect.stack()[2]  # Obtener información del marco de la llamada
    logger.log(
        getattr(logging, level.upper()),  # Obtener el nivel de log dinámicamente
        msg,  # Mensaje o datos a loguear
        extra={
            "custom_lineno": frame.lineno if with_line else "",  # Línea del código
            "custom_filename": frame.filename,  # Nombre del archivo
        },
        stacklevel=2,  # Asegurar que el contexto de la llamada se mantenga
    )

# Funciones para registrar mensajes de log sin incluir la línea de código
def info(msg):
    """Registra un mensaje de nivel INFO."""
    _log_with_metadata("info", msg, with_line=False)

def warning(msg):
    """Registra un mensaje de nivel WARNING."""
    _log_with_metadata("warning", msg, with_line=False)

def error(msg):
    """Registra un mensaje de nivel ERROR."""
    _log_with_metadata("error", msg, with_line=False)

def trace(msg):
    """Registra un mensaje de nivel TRACE."""
    _log_with_metadata("debug", msg, with_line=False)

# Funciones para registrar mensajes de log incluyendo la línea de código
def infoL(msg):
    """Registra un mensaje de nivel INFO con la línea de código."""
    _log_with_metadata("info", msg, with_line=True)

def warningL(msg):
    """Registra un mensaje de nivel WARNING con la línea de código."""
    _log_with_metadata("warning", msg, with_line=True)

def errorL(msg):
    """Registra un mensaje de nivel ERROR con la línea de código."""
    _log_with_metadata("error", msg, with_line=True)

def traceL(msg):
    """Registra un mensaje de nivel TRACE con la línea de código."""
    _log_with_metadata("debug", msg, with_line=True)

# Uso del logger
if __name__ == "__main__":
    # Ejemplos de uso con diferentes niveles
    info("Este es un mensaje de información.")
    trace("Este es un mensaje de traza.")
    warning("Este es un mensaje de advertencia.")
    error("Este es un mensaje de error.")
    infoL("Este mensaje incluye la línea de código.")
    traceL("Este mensaje incluye la línea de código.")
