---
name: session-close
description: Use when the user wants to close the session, says "cierra sesión", "cerrar sesión", "cierro la sesión", or asks to organize and commit the current session before stopping.
---

# Cierre de sesión controlado

Cuando el usuario pida cerrar la sesión, seguir este procedimiento:

1. Revisar el estado del repositorio con `git status`, `git diff` y los últimos commits relevantes.
2. Identificar únicamente los archivos que corresponden a la sesión actual.
3. No modificar, sobrescribir ni mezclar cambios que no pertenezcan a esa sesión.
4. Clasificar los cambios en las carpetas existentes del proyecto:
   - `comercial/contactos/` para interacciones con contactos
   - `comercial/pipeline.yaml` para el estado del pipeline
   - `estrategia/` para decisiones de negocio o posicionamiento
   - `contenido/` para publicaciones o material comercial
   - otras carpetas existentes cuando el cambio encaje mejor allí
5. Actualizar documentos existentes en lugar de crear archivos nuevos si la información pertenece a un documento ya creado.
6. No crear carpetas nuevas salvo que realmente no exista una ubicación adecuada.
7. Si falta contexto o el cambio es ambiguo, preguntar al usuario antes de inferir una decisión.
8. Ejecutar las comprobaciones disponibles del proyecto si existen.
9. Generar un resumen claro:
   - archivos modificados
   - qué se ha decidido o documentado
   - qué queda pendiente
   - propuesta de mensaje de commit
10. Pedir confirmación explícita antes de ejecutar `git add` y `git commit`.
11. Tras la confirmación, commitear solo los archivos seleccionados.
12. No ejecutar `git push`.

Si no hay cambios pendientes, informar de ello y cerrar sin crear un commit vacío.
