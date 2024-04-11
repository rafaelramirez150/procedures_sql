DELIMITER //

CREATE PROCEDURE eliminar_calle(IN p_id_calle INT)
BEGIN
    DELETE FROM calle WHERE id_calle = p_id_calle;
END //

DELIMITER ;