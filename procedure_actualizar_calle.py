import mysql.connector

def actualizar_calle(id_calle, nueva_descripcion):
    try:
        # Conectar a la base de datos
        cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
        cursor = cnx.cursor()

        # Llamar al procedimiento almacenado
        cursor.callproc('actualizar_calle', (id_calle, nueva_descripcion))

        # Confirmar los cambios
        cnx.commit()

        print("Calle actualizada con éxito.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Cerrar la conexión
        cursor.close()
        cnx.close()

# Llamar a la función actualizar_calle con los valores deseados
actualizar_calle(1, 'Nueva Descripción de la Calle')
