DELIMITER //

CREATE PROCEDURE obtener_calle(IN p_id_calle INT)
BEGIN
    SELECT * FROM calle WHERE id_calle = p_id_calle;
END //

DELIMITER ;
