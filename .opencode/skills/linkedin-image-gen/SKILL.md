SKILL: Generación de imágenes para publicaciones LinkedIn — estilo pizarra/tiza

Propósito
 - Plantilla reutilizable para generar imágenes minimalistas en estilo "tiza sobre pizarra" con tono irónico/infantil. Pensada para acompañar publicaciones sobre reporting, datos y consultoras en moda.

Cuándo usar
 - Cuando quieras una imagen limpia, con carga conceptual (ironía, comunicación rota) y aspecto hand-drawn.
 - Ideal para feeds LinkedIn: contraste alto, lectura rápida, composición simple.

Principios de la skill
 - Evitar personajes reales o marcas registradas. Usar siluetas y símbolos genéricos.
 - Composición izquierda/derecha para mostrar contraste (datos/consultoría vs usuario/BI).
 - Estética infantil: trazos sencillos, elementos tipo doodle, proporciones exageradas, pocas líneas.
 - Paleta: pizarra verde oscuro (#1d6b5b o similar), líneas blancas de tiza, 1 color de acento (amarillo o naranja suave).

Prompts (plantillas)

1) Prompt largo (español) — recomendado para modelos que admiten prompts extensos

"Ilustración minimalista estilo tiza sobre pizarra verde. Lado izquierdo: 'datos' y 'consultoría' representados con iconos sencillos dibujados a tiza blanca — una pila de papeles etiquetada como 'datos' (sin texto legible) y una figura-stick con clipboards representando a la consultora. Lado derecho: el usuario y un dashboard BI representados con una figura-stick frente a un portátil y un boceto simple de dashboard (barras + línea) en un color de acento suave. Entre ambos: un teléfono de lata con cuerda enredada y desgastada que simboliza comunicación rota. Composición equilibrada, tono irónico, estilo infantil/doodle, líneas de tiza hechas a mano, alto contraste blanco sobre verde, un único color de acento para los gráficos (amarillo). Sin logos, sin rostros realistas, sin texto adicional en la imagen. Formato horizontal 1200x627, alta resolución."

Negative prompt (qué evitar):
 - "no logos, no caracteres reales, no texto legible, no fotorealismo, no tipografías, no marcas registradas, no fondos complejos, no clutter"

2) Prompt corto (inglés) — variante para herramientas que funcionan mejor en inglés

"Chalkboard minimal illustration: left side data + consultancy (stack of papers, stick consultant with clipboard), right side user + BI dashboard (stick figure at laptop, simple bar+line chart), tin-can telephone with tangled frayed string between them symbolizing broken comms. White chalk lines on dark green chalkboard background, single accent color for charts, childlike doodle style, flat, ironic, landscape 1200x627. No logos, no real people."

Variantes útiles
 - Vertical / story: cambiar aspect ratio a 4:5 o 9:16; mantener composición top-bottom en lugar de left-right.
 - Miniatura / square: 1:1 centrando el teléfono en el medio con los elementos reducidos a ambos lados.
 - Monocromo extremo: blanco sobre negro si necesitas mayor contraste en algunas plataformas.

Parámetros sugeridos (Stable Diffusion / SD-like)
 - Sampler: Euler a / DPM++
 - Steps: 20–40
 - Guidance scale (CFG): 6.5–8
 - Seed: deja aleatorio para variaciones; fijar seed para reproducibilidad
 - Resolution: 1200x627 (landscape), 1080x1350 (vertical), 1080x1080 (square)

Post-procesado recomendado
 - Vectorizar trazos si vas a escalar la imagen (tracing en illustrator o herramienta vectorial)
 - Ajustar contraste de tiza y saturación del acento
 - Eliminar cualquier texto generado por la IA (si aparece) y reemplazar por leyenda separada en la publicación

Accesibilidad
 - Generar alt text breve y claro. Ejemplo: "Dibujo estilo tiza: a la izquierda datos y consultora, a la derecha usuario frente a un dashboard; entre ambos, teléfono de lata con cuerda enredada que simboliza comunicación rota." Inclúyelo en la publicación.

Notas legales y de uso
 - Evitar personajes icónicos (Mr. Bean, Marx Brothers, etc.) — usar personajes genéricos para no incurrir en derechos de imagen o copyright.
 - No incluir logotipos ni marcas de software (Power BI, Excel). Representarlos con iconos genéricos (gráficas, papeles).

Ejemplo de uso (workflow rápido)
 1. Copia el prompt largo al generador (p. ej. Stable Diffusion/InvokeAI/Midjourney)
 2. Añade el negative prompt
 3. Genera 4 variantes (nº de seeds distintos)
 4. Escoge la que mejor comunica la idea, vectoriza y ajusta color de acento
 5. Exporta en 1200x627 para LinkedIn

Plantillas de prompt (para pegar)

ES LARGO:
"Ilustración minimalista estilo tiza sobre pizarra verde. Lado izquierdo: 'datos' y 'consultoría' representados con iconos sencillos dibujados a tiza blanca — una pila de papeles etiquetada como 'datos' (sin texto legible) y una figura-stick con clipboards representando a la consultora. Lado derecho: el usuario y un dashboard BI representados con una figura-stick frente a un portátil y un boceto simple de dashboard (barras + línea) en un color de acento suave. Entre ambos: un teléfono de lata con cuerda enredada y desgastada que simboliza comunicación rota. Composición equilibrada, tono irónico, estilo infantil/doodle, líneas de tiza hechas a mano, alto contraste blanco sobre verde, un único color de acento para los gráficos (amarillo). Sin logos, sin rostros realistas, sin texto adicional en la imagen. Formato horizontal 1200x627, alta resolución."

EN CORTO (EN):
"Chalkboard minimal illustration: left side data + consultancy (stack of papers, stick consultant with clipboard), right side user + BI dashboard (stick figure at laptop, simple bar+line chart), tin-can telephone with tangled frayed string between them symbolizing broken comms. White chalk lines on dark green chalkboard background, single accent color for charts, childlike doodle style, flat, ironic, landscape 1200x627. No logos, no real people."

Fin del skill
