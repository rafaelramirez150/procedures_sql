DELIMITER //

CREATE PROCEDURE actualizar_calle(IN p_id_calle INT, IN p_nueva_descripcion VARCHAR(255))
BEGIN
    UPDATE calle SET descripcion = p_nueva_descripcion WHERE id_calle = p_id_calle;
END //

DELIMITER ;
