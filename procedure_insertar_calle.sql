DELIMITER //

CREATE PROCEDURE insertar_calle(IN p_id_calle INT, IN p_descripcion VARCHAR(255))
BEGIN
    INSERT INTO calle (id_calle, descripcion) VALUES (p_id_calle, p_descripcion);
END //

DELIMITER ;
