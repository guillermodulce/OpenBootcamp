
//Open Bootcamp Ejercicios tema 3

/*Primera parte:
Crear una función con tres parámetros que sean números que se suman entre sí.
Llamar a la función en el main y darle valores.
*/

public class ob_ej3_parte1 {

    public static void main(String[] args) {
  
          int resultado = 0;
          resultado = suma(11, 22 , 33);
          System.out.println(resultado);
      }
  
      public static int suma (int a, int b, int c){
  
          return a + b + c;
      }
  }
