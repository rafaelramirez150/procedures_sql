import mysql.connector

def insertar_calle(id_calle, descripcion):
    try:
        # Conectar a la base de datos
        cnx = mysql.connector.connect(user='root', password='root', database='direcciones')
        cursor = cnx.cursor()

        # Llamar al procedimiento almacenado
        cursor.callproc('insertar_calle', (id_calle, descripcion))

        # Confirmar los cambios
        cnx.commit()

        print("Datos de la calle insertados con éxito.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Cerrar la conexión
        cursor.close()
        cnx.close()

# Llamar a la función insertar_calle con los valores deseados
insertar_calle(6, 'Calle nueva')
