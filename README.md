# Quiz 2 2223-1
Un bodegón te ha contratado para que digitalices su almacén de bebidas, para ello deberás crear un programa que cumpla con los siguientes requerimientos:

* Estructurar los datos como se muestra en el diagrama a continuación:

![AyP Quiz 2 2223-1 Diagrama drawio (4)](https://user-images.githubusercontent.com/61355794/201145037-a34e6ed2-9323-444f-ba75-27801cb9ea5f.png)


* El método *mostrar* de la clase Bebida debe adaptarse, según sea necesario, a las otras clases, para mostrar todos los atributos que correspondan a las mismas.

* El bodegón requiere pasar su base de datos vieja a una nueva que contenga objetos, para ello tendrás que pasar todas las bebidas de la estructura de datos dada a objetos y agregarlos a tu nueva base de datos. **ESTO DEBE OCURRIR AL INICIAR EL PROGRAMA.**

* Menú:
  * Ver inventario: Se deberá mostrar de forma amigable para el usuario el inventario de bebidas.
  * Eliminar bebidas del inventario: Se deben mostrar todas las bebidas del almacén con un índice numérico que identifica a cada una, a partir de este índice el usuario podrá eliminar una bebida indicando el índice de la bebida correspondiente y mostrar qué bebida fue eliminada. **La eliminación de bebidas se hace marcando su atributo "disponible" como Falso.**
  * Volver al menú cada vez que se termine una operación.

* Deberá hacer uso correcto de objetos, clases y herencia. También deberá contar con las validaciones correspondientes, el uso adecuado de funciones y las convenciones de Python dadas en clase.

### ***BONO (3pts)***
El bodegón desea contar con un módulo de estadísticas (que debe agregarse como otra opción del menú principal), donde se muestre lo siguiente:
  * Bebida alcohólica con mayor grado alcohólico
  * Refresco con menor cantidad de gramos de azúcar
  * Marcas que tengan bebidas en las dos categorías
