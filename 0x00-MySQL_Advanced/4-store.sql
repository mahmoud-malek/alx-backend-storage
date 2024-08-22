-- a scirpt that creates trigger that deacrases the qauntity
-- of an item after adding a new order

DROP TRIGGER IF EXISTS update_quantity;
CREATE TRIGGER update_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET qauntity = qauntity - 1
	WHERE name = NEW.item_name;
END;

