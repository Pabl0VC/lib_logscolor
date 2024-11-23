from logscolor.logscl import info, error, trace, warning, infoL, errorL, traceL, warningL

# Usar las funciones sin la línea de código
info("1. Mensaje informativo sin línea")
trace("2. Mensaje de depuración sin línea")
warning("3. Mensaje de advertencia sin línea")
error("4. Mensaje de error sin línea")

# Usar las funciones con la línea de código
infoL("5. Mensaje informativo con línea")
traceL("6. Mensaje de depuración con línea")
warningL("7. Mensaje de advertencia con línea")
errorL("8. Mensaje de error con línea")

info({'nombre':'Peter'})
trace({'nombre':'Joe'})
error({'nombre':'Carl'})

infoL({'name':'Peter'})
traceL({'name':'Joe'})
errorL({'name':'Carl'})

info([0,3,2])
trace([0,3,2])
error([0,3,2])
info(type([0,3,2]))
traceL(type([0,3,2]))