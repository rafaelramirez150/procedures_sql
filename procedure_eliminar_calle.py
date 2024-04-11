import mysql.connector

def eliminar_calle(id_calle):
    try:
        # Conectar a la base de datos
        cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
        cursor = cnx.cursor()

        # Llamar al procedimiento almacenado
        cursor.callproc('eliminar_calle', (id_calle,))

        # Confirmar los cambios
        cnx.commit()

        print("Calle eliminada con éxito.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Cerrar la conexión
        cursor.close()
        cnx.close()

# Llamar a la función eliminar_calle con el valor deseado
eliminar_calle(1)
