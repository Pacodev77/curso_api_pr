/*using System;

namespace HolaMundoNet
{
    class Program{
        static void Main(string[] args){
            Console.WriteLine("\n¡Hola!, ¿Cómo te llamas?");
            string nombreUsuario = Console.ReadLine();
            Console.WriteLine($"¡Un gusto saludarte, {nombreUsuario}!");
            Console.WriteLine($"{nombreUsuario}, ¿Sabes la fecha del día de hoy y la hora?");
            Console.WriteLine("Bueno, sino lo sabes te lo digo.");
            DateTime ahora = DateTime.Now;
            Console.WriteLine($"{nombreUsuario}, Hoy es: {ahora}\n");
        }

    }
}*/

using System;
 
public class TiposDeDatos{
    public static void Main(string[] args){
        int edad = 30;
        double altura = 1.75;
        char letra = 'J';
        bool esMayorDeEdad = true;

        Console.WriteLine($"Edad: {edad}, Altura: {altura}, Inicial: {letra}, Mayor de edad: {esMayorDeEdad}");
        string nombre = "Juan Pérez";
        object objetoGenerico = nombre;
        Console.WriteLine($"Nombre: {nombre}, Objeto Genérico: {objetoGenerico}");

    }
}