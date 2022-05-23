// Para practicar la encapsulación:

public class ob_ej8 { // (main)

    public static void main(String[] args) {

        // Crear un objeto persona en el main.
        Persona persona = new Persona();
        
        // Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono, por último muéstralas por consola.
        persona.setNombre("Guillermo");
        System.out.println("Mi nombre es " + persona.getNombre());
        persona.setEdad(44);
        System.out.println("Tengo " + persona.getEdad() + " años");
        persona.setTelefono(1150212981);
        System.out.println("Mi teléfono es " + persona.getTelefono());
    }
}

// Crear clase Persona.
class Persona {

    // Crear variables las privadas edad, nombre y telefono de la clase Persona.
    private int edad;
    private String nombre;
    private int telefono;

    // Crear gets y sets de cada propiedad.
    public int getEdad() {
        return edad;
    }
    
    public void setEdad(int edad){
        this.edad = edad;
    }
    
    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getTelefono() {
        return telefono;
    }

    public void setTelefono(int telefono){
        this.telefono = telefono;
    }
}