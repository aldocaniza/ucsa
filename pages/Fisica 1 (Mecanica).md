- Prompt [[Fisica 1 (Mecanica)]]
- Actua como un profesor de fisica mecanica de grado universitario con orientacion didactica y utilizando tecnicas de nemotecnia con ejemplos practicos y entendibles para un estudiando de ingenieria en informatica con enfoque en la programacion, utilizas notaciones en español y siempre que inicias una leccion indicas la formula que utilizaras, con una explicacion breve de no mas de 2 lineas con una analogia de su uso en la vida real.
  Tu objetivo es que entiendas el tema del cual estamos hablando y lo expliques de forma facil de entender a mi que soy el estudiante y aclarar todas las dudas frecuentes que conoces que tienen los estudiantes igual a mi basado en tus anteriores interacciones, seleccionando las mejores que haz tenido.
  Debes entregarme la leccion en formato markdown, para que sea sencillo copiar en mis apuntes, tambien utilizas notacion LaTeX para las formulas, eso me ayudara a copiar la formula en mis apuntes.
  Como advertencia, debes tener en cuenta que la leccion tiene que ser facilmente entendible y puedes utilizar la tecnica de Feynman para que entienda, tambien tienes que tener en cuenta que quizas no te de la informacion completa, por lo que debes buscar en internet los datos que te falten, como son materiales conocidos, quizas encuentres esta informacion en fuentes de internet exactamente iguales a los datos que te paso, como por ejemplo ejercicios.
  Ahora, para esta Clase en particular, ten en cuenta todas nuestras interacciones anteriores referentes al tema actual y dame una leccion sobre lo siguiente:
  al finalizar Crea flashcard de esto con una referencia a la flascard con las opciones capciosas al estilo seleccion multiple con la respuesta correcta en ``{{cloze ...}}`` #card - guion indentacion titulo [[Fisica 1 (Mecanica)]] si hay latex conviertelo en texto plano para que no se vea afectado por la sintaxis ``{{cloze ..}}``
  Tambien ademas de las flashcard, dame las formulas de las lecciones en formato ``\[LATEX\]`` por separado de la leccion pero todas las formulas juntas con sus titulos para que pueda incluirlos en el formulario necesario para mi examen, incluye todas las formulas incluidas las implicitas por ejemplo ``\[ \sum \vec{F} = 0 \Rightarrow \vec{a} = 0 \]``, quiero que incluyas esta sintaxis de los dolares para copiarlos en Logseq, agrega tambien titulo a las formulas el codigo en latex ponlo con los titulos en el box de codigo, el estilo en Anki las flashcard tambien tienen que estar en box de codigo para poder copiarlos en Logseq, la respuesta de la flashcard tiene que estar al final con '{{cloze ...}}', y entre las opciones capciosas, pero no señaladas, como seria en un examen
  Ejemplo de FlashCard (es importante que la respuesta correcta este entre ``{{cloze ...}}``) no uses ``$$$$`` para latex
  Has tantas flashcard como temas haya en la leccion, no dejes fuera ningun tema
- Ley de Inercia: Si la fuerza neta es cero, un cuerpo estará en reposo o con movimiento rectilíneo uniforme.
	- ¿Cuál es la condición para que un cuerpo mantenga su estado de movimiento según la primera ley de Newton? #card
		- a) \( \sum F \neq 0 \)
		- b) \( \sum F = m a \)
		- c) \( \sum F = 0 \)
		- d) \( a \neq 0 \)
		- ``{{cloze Respuesta Correcta b) Sum(F) = m*a}}``
- Ejemplo de Formulario
	- % Ley de Newton - Segunda Ley
	  ```
	  \[
	  \sum \vec{F} = m \vec{a}
	  \]
	  ```
- Al final haz un resumen super conciso de lo principal de la leccion para poder estudiar, sin dar tantos detalles, solo lo principal para poder repasar rapidamente
- # Formulario
	- % Ley de Newton - Segunda Ley
	  \[
	  \sum \vec{F} = m \vec{a}
	  \]
	- % Primera Ley o Ley de Inercia
	  \[
	  \sum \vec{F} = 0 \Rightarrow \vec{a} = 0
	  \]
	- % Tercera Ley
	  \[
	  \vec{F}_{12} = -\vec{F}_{21}
	  \]
	- % Torque o Momento de fuerza
	  \[
	  M = r \cdot F \cdot \sin \theta
	  \]
	- % Torque máximo cuando fuerza es perpendicular
	  \[
	  M = F \cdot r
	  \]
	- % Condiciones de equilibrio para cuerpo extenso
	  \[
	  \sum \vec{F} = 0, \quad \sum \vec{M} = 0
	  \]
	- % Condiciones de equilibrio para partícula
	  \[
	  \sum \vec{F} = 0
	  \]
	- % Velocidad en MRUA
	  \[
	  v = v_0 + a t
	  \]
	- % Si la fuerza neta es cero
	  \[
	  \sum \vec{F} = 0 \Rightarrow \vec{a} = 0
	  \]
	- % Definición de aceleración (cambio de velocidad en tiempo)
	  \[
	  a = \frac{\Delta v}{\Delta t}
	  \]
	- % Velocidad promedio (caso general)
	  \[
	  v_{prom} = \frac{v_0 + v}{2}
	  \]
	- % Segunda Ley de Newton
	  \[
	  \vec{a} = \frac{\vec{F_r}}{m} \Rightarrow \vec{F_r} = m \times \vec{a}
	  \]
	- % Componentes en ejes cartesianos
	  \[
	  \vec{F_{r_x}} = m \times \vec{a_x} \\
	  \vec{F_{r_y}} = m \times \vec{a_y}
	  \]
	- % Tercera Ley de Newton
	  \[
	  \vec{F_{12}} = -\vec{F_{21}} \quad \text{o} \quad \vec{F_{12}} + \vec{F_{21}} = 0
	  \]
	- % Magnitudes iguales en acción y reacción
	  \[
	  \vec{F_{12}} = \vec{F_{21}}
	  \]
	- % Fuerza Peso
	  \[
	  \vec{P} = m \times \vec{g}
	  \]
	- % Fuerza de Rozamiento Estático
	  \[
	  F_{r_E} \leq \mu_e \times N
	  \]
	- % Fuerza de Rozamiento Dinámico
	  \[
	  F_{r_D} \leq \mu_d \times N
	  \]
	- % Equilibrio (Fuerza Neta Cero)
	  \[
	  \sum \vec{F} = 0 \Rightarrow \vec{a} = 0
	  \]
	- \begin{align}
	  0 \leq F_{r_E} \leq \mu_E \cdot N \quad &\text{(Estática)} \\
	  F_{r_D} \leq \mu_D \cdot N \quad &\text{(Dinámica)}
	  \end{align}
	- % Ley de Hooke Elasticidad
	  \[F = -k \cdot x
	  \]
	- %Conversion de Unidades
	  \[\frac{km}{h} \rightarrow \frac{m}{s} \quad \Rightarrow \quad \frac{km}{h} \cdot \frac{1000}{3600} = \frac{km}{h} \cdot \frac{5}{18}
	  \]
	- % Primera Ley de Newton - Ley de la Inercia
	  \[
	  \sum \vec{F} = 0 \Rightarrow \vec{a} = 0
	  \]
	- % Movimiento rectilíneo uniforme sin fuerzas
	  \[
	  \vec{v} = \text{constante}, \ \text{si} \ \sum \vec{F} = 0
	  \]
	- % Definición de fuerza peso (aunque es de otra lección, es base para entender fuerzas)
	  \[
	  \vec{P} = m \cdot \vec{g}
	  \]
	- % Condición general de equilibrio
	  \[
	  \sum \vec{F} = 0 \Rightarrow \text{Equilibrio Traslacional}
	  \]
	- Ley de Inercia:
	  \[
	  \sum \vec{F} = 0 \Rightarrow \vec{a} = 0
	  \]
	- MRU por ausencia de fuerza:
	  \[
	  \vec{v} = \text{constante}, \text{ si } \sum \vec{F} = 0
	  \]
	- Equilibrio:
	  \[
	  \sum \vec{F} = 0 \Rightarrow \text{Equilibrio Traslacional}
	  \]
- # Tarjetas
	- ## Leyes de Newton
		- Ley de Inercia: Si la fuerza neta es cero, un cuerpo estará en reposo o con movimiento rectilíneo uniforme.
			- ¿Cuál es la condición para que un cuerpo mantenga su estado de movimiento según la primera ley de Newton?#card
				- a) \( \sum F \neq 0 \)
				- b) \( \sum F = m a \)
				- c) \( \sum F = 0 \)
				- d) \( a \neq 0 \)
				- {{cloze Respuesta Correcta b) \( \sum F = m a \)}}
		- Torque o momento de fuerza es:
			- ¿Cuál es la fórmula correcta para el torque \(M\)?#card
			  card-last-interval:: 4
			  card-repeats:: 1
			  card-ease-factor:: 2.6
			  card-next-schedule:: 2025-07-10T03:51:23.980Z
			  card-last-reviewed:: 2025-07-06T03:51:23.981Z
			  card-last-score:: 5
				- a) \( M = F \cdot r \cdot \cos \theta \)
				- b) \( M = r \cdot F \cdot \sin \theta \)
				- c) \( M = F + r \)
				- d) \( M = F / r \)
				- {{cloze b) \( M = r \cdot F \cdot \sin \theta \)}}
		- Condición de equilibrio para un cuerpo extenso es:#card
		  card-last-interval:: 4
		  card-repeats:: 1
		  card-ease-factor:: 2.36
		  card-next-schedule:: 2025-07-10T01:39:47.775Z
		  card-last-reviewed:: 2025-07-06T01:39:47.776Z
		  card-last-score:: 3
			- a) \( \sum F = 0 \) y \( \sum M \neq 0 \)
			- b) \( \sum F \neq 0 \) y \( \sum M = 0 \)
			- c) \( \sum F = 0 \) y \( \sum M = 0 \)
			- d) \( \sum F \neq 0 \) y \( \sum M \neq 0 \)
			- {{cloze c) \( \sum F = 0 \) y \( \sum M = 0 \)}}
	- Segunda Ley de Newton:
		- ¿Cuál es la expresión correcta de la segunda ley de Newton?#card
		  card-last-interval:: 4
		  card-repeats:: 1
		  card-ease-factor:: 2.6
		  card-next-schedule:: 2025-07-10T16:55:56.394Z
		  card-last-reviewed:: 2025-07-06T16:55:56.396Z
		  card-last-score:: 5
			- a) a = m / F
			- b) ΣF = m a
			- c) F = m / a
			- d) ΣF = m + a
			- {{cloze Respuesta Correcta b) ΣF = m a}}
	- Aceleración y masa:
		- Si mantienes constante la fuerza, ¿qué sucede con la aceleración al aumentar la masa? #card
		  card-last-interval:: 4
		  card-repeats:: 1
		  card-ease-factor:: 2.6
		  card-next-schedule:: 2025-07-10T03:47:54.581Z
		  card-last-reviewed:: 2025-07-06T03:47:54.583Z
		  card-last-score:: 5
			- a) Aumenta
			- b) Disminuye
			- c) No cambia
			- d) Se vuelve negativa
			- {{cloze Respuesta Correcta b) Disminuye}}
	- Fuerza neta cero:
		- ¿Qué sucede con un objeto si la fuerza neta que actúa sobre él es cero? #card
		  card-last-interval:: 4
		  card-repeats:: 1
		  card-ease-factor:: 2.36
		  card-next-schedule:: 2025-07-10T03:50:38.046Z
		  card-last-reviewed:: 2025-07-06T03:50:38.047Z
		  card-last-score:: 3
			- a) Se acelera
			- b) Se desacelera
			- c) Mantiene su estado de movimiento
			- d) Cambia su masa
			- {{cloze Respuesta Correcta c) Mantiene su estado de movimiento}}
	- Fuerzas en diferentes direcciones:
		- ¿Cómo se obtiene la fuerza neta si hay varias fuerzas actuando en distintas direcciones? #card
			- a) Sumando solo las magnitudes
			- b) Restando todas las fuerzas
			- c) Sumando vectorialmente todas las fuerzas
			- d) Multiplicando las fuerzas
			- {{cloze Respuesta Correcta c) Sumando vectorialmente todas las fuerzas}}
	- Primera Ley de Newton #card #manual
	  card-last-interval:: 4
	  card-repeats:: 1
	  card-ease-factor:: 2.6
	  card-next-schedule:: 2025-07-10T03:49:14.820Z
	  card-last-reviewed:: 2025-07-06T03:49:14.822Z
	  card-last-score:: 5
		- {{cloze Establece que si sobre un punto material la fuerza resultante es nula, el mismo estará en reposo o con movimiento rectilineo uniforme **(MRU)**}}
	- Segunda Ley de Newton:
		- ¿Cuál es la relación correcta entre fuerza, masa y aceleración?#card
		  card-last-interval:: 4
		  card-repeats:: 1
		  card-ease-factor:: 2.36
		  card-next-schedule:: 2025-07-10T16:56:31.102Z
		  card-last-reviewed:: 2025-07-06T16:56:31.102Z
		  card-last-score:: 3
			- a) a = m / F
			- b) F = a / m
			- c) F = m × a
			- d) a = F × m
			- {{cloze Respuesta Correcta c) F = m × a}}
	- Componentes Cartesianas:
		- ¿Cómo se expresa la segunda ley de Newton en dirección horizontal?#card
		  card-last-interval:: 4
		  card-repeats:: 1
		  card-ease-factor:: 2.6
		  card-next-schedule:: 2025-07-10T16:56:08.075Z
		  card-last-reviewed:: 2025-07-06T16:56:08.075Z
		  card-last-score:: 5
			- a) F_r = m × a
			- b) F_r_y = m × a_y
			- c) F_r_x = m × a_x
			- d) a_x = F_r_y / m
			- {{cloze Respuesta Correcta c) F_r_x = m × a_x}}
	- Tercera Ley de Newton:
		- ¿Cuál de las siguientes afirmaciones representa mejor la 3ra ley de Newton?#card
			- a) F = m × a
			- b) F_12 = F_21
			- c) F_12 = -F_21
			- d) F_1 + F_2 = 0
			- {{cloze Respuesta Correcta c) F_12 = -F_21}}
	- Fuerza Peso:
		- ¿Qué fórmula representa la fuerza peso?#card
			- a) P = m / g
			- b) P = m × a
			- c) P = g / m
			- d) P = m × g
			- {{cloze Respuesta Correcta d) P = m × g}}
	- Rozamiento:
		- ¿Cuál es la fórmula del rozamiento dinámico?#card
			- a) F_r = N × μ_d
			- b) F_r = m × g
			- c) F_r ≤ μ_d × N
			- d) F_r ≥ μ_e × N
			- {{cloze Respuesta Correcta c) F_r ≤ μ_d × N}}
	- Fuerza Normal:
		- ¿De qué depende la fuerza normal?#card
		  card-last-interval:: 4
		  card-repeats:: 1
		  card-ease-factor:: 2.6
		  card-next-schedule:: 2025-07-10T03:51:12.573Z
		  card-last-reviewed:: 2025-07-06T03:51:12.573Z
		  card-last-score:: 5
			- a) Siempre es igual al peso
			- b) Depende de la masa
			- c) Depende de otras fuerzas del sistema
			- d) Es constante
			- {{cloze Respuesta Correcta: c)}}
	- Rozamiento:
		- ¿Cuál es el valor máximo que puede tomar la fuerza de rozamiento estática?#card
		  card-last-interval:: 4
		  card-repeats:: 1
		  card-ease-factor:: 2.6
		  card-next-schedule:: 2025-07-10T03:50:52.505Z
		  card-last-reviewed:: 2025-07-06T03:50:52.506Z
		  card-last-score:: 5
			- a) 0
			- b) μ_d × N
			- c) μ_e × N
			- d) m × g
			- {{cloze Respuesta Correcta: c)}}
	- Fuerza Elástica:
		- ¿Qué indica el signo negativo en la fórmula F = -k × x?#card
		  card-last-interval:: 4
		  card-repeats:: 1
		  card-ease-factor:: 2.6
		  card-next-schedule:: 2025-07-10T16:56:49.482Z
		  card-last-reviewed:: 2025-07-06T16:56:49.482Z
		  card-last-score:: 5
			- a) La fuerza disminuye con x
			- b) La fuerza está en sentido opuesto al desplazamiento
			- c) La fuerza es constante
			- d) El resorte se comprime
			- {{cloze Respuesta Correcta: b)}}
	- Conversión de Unidades:
		- ¿Cómo se convierte km/h a m/s?#card
		  card-last-interval:: 4
		  card-repeats:: 1
		  card-ease-factor:: 2.6
		  card-next-schedule:: 2025-07-10T03:49:35.181Z
		  card-last-reviewed:: 2025-07-06T03:49:35.182Z
		  card-last-score:: 5
			- a) × 3.6
			- b) × 1000
			- c) ÷ 3600
			- d) × 5/18
			- {{cloze Respuesta Correcta: d)}}
- Primera Ley de Newton [[Fisica 1 (Mecanica)]]
	- ¿Cuál es la condición para que un cuerpo mantenga su estado de movimiento según la primera ley de Newton? #card
	  card-last-interval:: 4
	  card-repeats:: 1
	  card-ease-factor:: 2.36
	  card-next-schedule:: 2025-07-10T03:48:12.040Z
	  card-last-reviewed:: 2025-07-06T03:48:12.040Z
	  card-last-score:: 3
		- a) sum F ≠ 0
		- b) sum F = m × a
		- c) sum F = 0
		- d) a ≠ 0
		- {{cloze Respuesta Correcta: c) sum F = 0}}
	- Definición de Inercia [[Fisica 1 (Mecanica)]]
		- ¿Qué es la inercia?#card
		  card-last-interval:: 4
		  card-repeats:: 1
		  card-ease-factor:: 2.6
		  card-next-schedule:: 2025-07-10T03:48:22.405Z
		  card-last-reviewed:: 2025-07-06T03:48:22.406Z
		  card-last-score:: 5
			- a) La tendencia a acelerar un cuerpo
			- b) La resistencia a cambiar de estado de movimiento
			- c) La fuerza que empuja un cuerpo
			- d) La velocidad constante de un cuerpo
			- {{cloze Respuesta Correcta: b) La resistencia a cambiar de estado de movimiento}}
	- Movimiento sin fuerzas [[Fisica 1 (Mecanica)]]
		- Si no hay fuerzas actuando sobre un objeto que ya se mueve, ¿qué le pasa al movimiento?#card
		  card-last-interval:: 4
		  card-repeats:: 1
		  card-ease-factor:: 2.36
		  card-next-schedule:: 2025-07-10T03:48:53.853Z
		  card-last-reviewed:: 2025-07-06T03:48:53.854Z
		  card-last-score:: 3
			- a) Se detiene lentamente
			- b) Se acelera
			- c) Cambia de dirección
			- d) Se mantiene constante en línea recta
			- {{cloze Respuesta Correcta: d) Se mantiene constante en línea recta}}
	- Sistema inercial [[Fisica 1 (Mecanica)]]
		- ¿Qué es un sistema de referencia inercial? #card
		  card-last-interval:: 4
		  card-repeats:: 1
		  card-ease-factor:: 2.6
		  card-next-schedule:: 2025-07-10T03:51:34.996Z
		  card-last-reviewed:: 2025-07-06T03:51:34.996Z
		  card-last-score:: 5
			- a) Donde siempre se detecta aceleración
			- b) Donde se aplica la ley de gravitación universal
			- c) Donde se cumple la primera ley de Newton
			- d) Un sistema que está acelerando
			- {{cloze Respuesta Correcta: c) Donde se cumple la primera ley de Newton}}
	- Efecto de fuerzas equilibradas [[Fisica 1 (Mecanica)]]
		- ¿Qué ocurre si la suma de las fuerzas sobre un objeto es cero? #card
		  card-last-interval:: 4
		  card-repeats:: 1
		  card-ease-factor:: 2.6
		  card-next-schedule:: 2025-07-10T03:51:46.674Z
		  card-last-reviewed:: 2025-07-06T03:51:46.674Z
		  card-last-score:: 5
			- a) Se acelera en línea recta
			- b) Se detiene
			- c) Mantiene su estado (reposo o MRU)
			- d) Cambia de dirección
			- {{cloze Respuesta Correcta: c) Mantiene su estado (reposo o MRU)}}
	-