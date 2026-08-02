CREATE TABLE suppliers (
	id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name VARCHAR(30) UNIQUE NOT NULL,
	phone VARCHAR(12) DEFAULT 'NO PHONE PROVIDED',
	address TEXT DEFAULT 'NO ADDRESS PROVIDED',
	description TEXT DEFAULT 'NO DESCRIPTION PROVIDED'
);

CREATE TABLE products (
	id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	sku VARCHAR(100) UNIQUE NOT NULL,
	name VARCHAR(30) NOT NULL,
	stock INTEGER DEFAULT 0 CHECK (stock >= 0),
	stock_critical INTEGER DEFAULT 0 CHECK (stock_critical >= 0),
	description VARCHAR(100),
	supplier_id INTEGER NOT NULL REFERENCES suppliers(id) ON DELETE RESTRICT
);

INSERT INTO suppliers (name, phone, address, description)
VALUES 
('Dell', '123-456-7890', '1234 Dell Street', 'One letter away from being feared'),
('HP', '098-765-4321', '2121 HP Street', 'Equal to one Horse in Power');

INSERT INTO products (sku, name, stock, stock_critical, description, supplier_id)
VALUES 
('DELL-LAPTOP-32GB-BLK', 'Dell Laptop 32GB', 100, 15, 'Dell Laptop with 32 GB of RAM', (SELECT id FROM suppliers WHERE name = 'Dell')),
('HP-LAPTOP-16GB-BLK', 'HP Laptop 16GB', 50, 15, 'HP Laptop with 16 GB of RAM', (SELECT id FROM suppliers WHERE name = 'HP'));
