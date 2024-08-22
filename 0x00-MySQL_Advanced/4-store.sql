-- a scirpt that creates trigger that deacrases the qauntity
-- of an item after adding a new order

DROP TRIGGER IF EXISTS update_quantity;
CREATE TRIGGER update_quantity
AFTER INSERT ON orders
FOR EACH ROW
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;

