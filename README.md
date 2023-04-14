## <center> Compositores: </center>
#### <center> Carlos Reynoso 2021-1188 </center>
#### <center> Neifi Medina 2021-0959 </center>
#### <center> Eddy Mena 2021-0942 </center>
___

# <center> El Problema De Los Filósofos </center>

Este es un problema clásico de sincronización que se utiliza para ilustrar los desafíos que pueden surgir cuando varios procesos compiten por un conjunto limitado de recursos.

En este problema, hay cinco filósofos sentados alrededor de una mesa redonda, y cada uno de ellos tiene un plato de espaguetis y un tenedor a su lado. Los filósofos pasan su tiempo alternando entre dos estados: pensando y comiendo. Para comer, un filósofo necesita dos tenedores, uno a su izquierda y otro a su derecha.

El problema surge cuando todos los filósofos deciden comer al mismo tiempo. Cada filósofo intentará recoger el tenedor a su lado izquierdo y el tenedor a su lado derecho simultáneamente. Si todos los filósofos lo hacen al mismo tiempo, es posible que se produzca un interbloqueo (deadlock), donde todos los filósofos están esperando a que se liberen los tenedores de sus vecinos antes de poder comer.

El problema de los filósofos ha sido utilizado en la informática para ilustrar problemas de sincronización y ha sido objeto de estudio en la teoría de la concurrencia y la programación concurrente.
___

# <center>Conceptos:</center>

1. **Concurrencia:** La concurrencia en informática se refiere a la capacidad de un sistema para realizar múltiples tareas simultáneamente. Estas tareas pueden ser procesos independientes o procesos que comparten recursos. La concurrencia es importante porque le permite hacer un mejor uso de los recursos del sistema y mejorar la eficiencia del procesamiento de datos.

2. **Paralelismo vs Concurrencia en informática:** El paralelismo y la concurrencia son dos conceptos relacionados pero diferentes. El paralelismo se refiere a la capacidad de un sistema para realizar múltiples tareas simultáneamente utilizando múltiples procesadores o núcleos de procesamiento. La concurrencia, por otro lado, se refiere a la capacidad de un sistema para realizar múltiples tareas simultáneamente, ya sea usando múltiples procesadores o compartiendo un solo procesador.

3. **Hilos implementación en Python:** En Python, los hilos se pueden implementar utilizando el módulo *'threading'* . Los hilos permiten que varias tareas se ejecuten simultáneamente dentro de un proceso. Los hilos son útiles para tareas que se pueden realizar de forma independiente y no bloquean el proceso principal. Los hilos en Python pueden compartir memoria y recursos, lo que hace que la programación concurrente sea más fácil y eficiente.

4. **Deadlock:** El deadlock es una situación en la que dos o más procesos están bloqueados esperando que otros procesos liberen los recursos que necesitan para seguir ejecutándose. El deadlock puede ocurrir en sistemas que utilizan la exclusión mutua, como los sistemas operativos, donde los procesos compiten por el acceso a los recursos del sistema.

5. **Exclusión mutual:** La exclusión mutua se refiere a la técnica utilizada para garantizar que solo un proceso pueda acceder a un recurso compartido a la vez. Esto se logra mediante el uso de semáforos, mutex o variables de condición. La exclusión mutua es importante para prevenir situaciones de interbloqueo y garantizar que los procesos accedan a los recursos de manera segura.

6. **Mantenga y espere:** El algoritmo de "mantener y esperar" es un algoritmo utilizado para prevenir el interbloqueo. El algoritmo establece que un proceso debe mantener todos los recursos que ha adquirido hasta que pueda adquirir todos los recursos que necesita para continuar su ejecución. Si un recurso que necesita está ocupado, el proceso debe esperar hasta que esté disponible.

7. **No preventivo:** Los sistemas operativos no preventivos son aquellos que no pueden evitar que un proceso bloquee a otro proceso. En estos sistemas, el interbloqueo puede ocurrir si los procesos no se diseñan adecuadamente para manejar la exclusión mutua.

8. **Espera circular:** La espera circular es una situación en la que dos o más procesos están esperando que otros procesos liberen los recursos que necesitan para continuar su ejecución. La espera circular es una causa común de interbloqueo en los sistemas que utilizan exclusión mutua.

9. **Como manejar el interbloqueo en sistemas operativos – Compara con el problema de los filósofos:** En términos de manejo de interbloqueo en sistemas operativos, el problema de los filósofos se puede abordar de diversas maneras. Una solución común es utilizar el algoritmo del banquero para asignar los recursos a los procesos solo si se puede cumplir con todas sus solicitudes. En este caso, los filósofos solo pueden tomar los tenedores si ambos están disponibles, lo que evita que ocurra el interbloqueo.
___

## <center> Diagrama De Los Filósofos: </center>
![Filosofo](./Diagrama/Problema%20De%20Los%20Filosofos.png)

## <center> Video De Explicación: </center>
[enlace del video de explicación](https://miucateciedu-my.sharepoint.com/personal/20211188_miucateci_edu_do/_layouts/15/stream.aspx?id=%2Fpersonal%2F20211188%5Fmiucateci%5Fedu%5Fdo%2FDocuments%2FGrabaciones%2FLlamada%20con%20Eddy%20y%201%20m%C3%A1s%2D20230413%5F232027%2DGrabaci%C3%B3n%20de%20la%20reuni%C3%B3n%2Emp4&ga=1)
