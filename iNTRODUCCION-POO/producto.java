public class Producto {
    private String nombre;
    private double precio;
    private int stock;

    public Producto(String nombre, double precio, int stock) {
        this.nombre = nombre;
        this.precio = precio;
        this.stock = stock;
    }

    public void vender(int cantidad) {
        if (cantidad <= 0) {
            System.out.println("La cantidad a vender debe ser mayor que cero.");
            return;
        }
        if (cantidad > stock) {
            System.out.println("No hay suficiente stock para vender esa cantidad.");
        } else {
            stock -= cantidad;
            System.out.println("Se vendieron " + cantidad + " unidades de " + nombre + ".");
        }
    }

    public void reabastecer(int cantidad) {
        if (cantidad <= 0) {
            System.out.println("La cantidad a reabastecer debe ser mayor que cero.");
            return;
        }
        stock += cantidad;
        System.out.println("Se reabastecieron " + cantidad + " unidades de " + nombre + ".");
    }

    public String getNombre() {
        return nombre;
    }

    public double getPrecio() {
        return precio;
    }

    public int getStock() {
        return stock;
    }
}