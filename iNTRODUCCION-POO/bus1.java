public class Bus {
    private int totalAsientos;
    private int pasajeros;
    private double totalRecaudado;

    public Bus(int totalAsientos) {
        this.totalAsientos = totalAsientos;
        this.pasajeros = 0;
        this.totalRecaudado = 0.0;
    }
    public void subirPasajeros(int cantidad) {
        if (cantidad < 0) {
            System.out.println("No se puede subir una cantidad negativa de pasajeros.");
            return;
        }
        if (this.pasajeros + cantidad > this.totalAsientos) {
            System.out.println("No hay suficientes asientos disponibles.");
        } else {
            this.pasajeros += cantidad;
            System.out.println(cantidad + " pasajeros subieron al bus.");
        }
    }

    public void cobrarPasaje() {
        double costo = 1.50;
        if (this.pasajeros == 0) {
            System.out.println("No hay pasajeros para cobrar.");
            return;
        }
        this.totalRecaudado += this.pasajeros * costo;
        System.out.println("Se cobraron " + (this.pasajeros * costo) + " bs. por " + this.pasajeros + " pasajeros.");
    }

    public int asientosDisponibles() {
        int disponibles = this.totalAsientos - this.pasajeros;
        System.out.println("Asientos disponibles: " + disponibles);
        return disponibles;
    }
    public static void main(String[] args) {
        // Crear una instancia del bus
        Bus miBus = new Bus(50);

        miBus.subirPasajeros(10);
        miBus.cobrarPasaje();
        miBus.asientosDisponibles();

        miBus.subirPasajeros(40);
        miBus.cobrarPasaje();
        miBus.asientosDisponibles();
    }
}