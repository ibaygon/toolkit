# Python para administradores de sistemas

## ¿Por qué Python además de Bash?

Bash es imprescindible para automatizar tareas del sistema operativo: mover archivos,
encadenar comandos, gestionar procesos. Sin embargo, tiene límites claros en cuanto
la complejidad crece.

Python complementa a Bash en los escenarios donde Bash se queda corto:

**Manipulación de datos estructurados.** Procesar un CSV de 1000 servidores, filtrar
por columnas y exportar a Excel es trivial con Pandas. En Bash requeriría awk, sed y
scripts frágiles difíciles de mantener.

**Integración con APIs externas.** Consultar ipinfo.io, parsear JSON y mostrar una
tabla formateada se hace en diez líneas con requests. En Bash necesitarías curl,
jq y lógica adicional propensa a errores.

**Orientación a objetos.** Modelar un inventario de red con clases Router y Server
que heredan de NetworkDevice permite escalar el código sin duplicar lógica.
Bash no tiene clases ni herencia.

**Pruebas unitarias.** pytest permite verificar que el parser de logs funciona
correctamente antes de desplegarlo en producción. Bash carece de un ecosistema
de testing equivalente.

**Conclusión.** Un administrador de sistemas moderno usa Bash para lo que es rápido
y directo, y Python cuando necesita lógica compleja, datos estructurados, APIs
o código mantenible a largo plazo. No son competidores, son complementarios.