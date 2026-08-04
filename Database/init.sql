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

CREATE TABLE transactions (
	id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	item_id INTEGER NOT NULL REFERENCES products(id) ON DELETE RESTRICT,
	item_quantity_changed INTEGER NOT NULL,
	item_stock_before_transaction INTEGER NOT NULL,
	item_stock_after_transaction INTEGER NOT NULL,
	created_at TIMESTAMPTZ DEFAULT NOW(),
	by_user VARCHAR(20) NOT NULL,
	reason VARCHAR(50) NOT NULL
);

INSERT INTO suppliers (name, phone, address, description)
VALUES 
('Dell', '123-456-7890', '1234 Dell Street', 'One letter away from being feared'),
('HP', '098-765-4321', '2121 HP Street', 'Equal to one Horse in Power'),
('Lenovo', '111-222-3333', '500 ThinkPad Avenue', 'Business laptops and enterprise hardware'),
('Cisco', '222-333-4444', '170 West Tasman Drive', 'Networking equipment and infrastructure'),
('Logitech', '333-444-5555', '7700 Gateway Boulevard', 'Computer peripherals and accessories'),
('Samsung', '444-555-6666', '129 Samsung-ro', 'Displays, storage and mobile technology'),
('Kingston', '555-666-7777', '17600 Newhope Street', 'Memory and storage solutions'),
('ASUS', '666-777-8888', '15 ASUS Plaza', 'Consumer and gaming hardware');

INSERT INTO products (sku, name, stock, stock_critical, description, supplier_id)
VALUES 
('DELL-LAPTOP-32GB-BLK', 'Dell Laptop 32GB', 100, 15, 'Dell Laptop with 32 GB of RAM', (SELECT id FROM suppliers WHERE name = 'Dell')),

('HP-LAPTOP-16GB-BLK', 'HP Laptop 16GB', 50, 15, 'HP Laptop with 16 GB of RAM', (SELECT id FROM suppliers WHERE name = 'HP')),

('LEN-TP-T14-G5', 'Lenovo ThinkPad T14 Gen 5', 25, 5, 'Business laptop with Intel Core Ultra processor', (SELECT id FROM suppliers WHERE name = 'Lenovo')),
('LEN-DOCK-USB-C', 'Lenovo USB-C Dock', 8, 3, 'USB-C docking station for professional laptops', (SELECT id FROM suppliers WHERE name = 'Lenovo')),

('CISCO-SW-24P', 'Cisco 24 Port Switch', 12, 2, 'Managed network switch with PoE support', (SELECT id FROM suppliers WHERE name = 'Cisco')),
('CISCO-AP-WIFI6', 'Cisco WiFi 6 Access Point', 4, 2, 'Enterprise wireless access point', (SELECT id FROM suppliers WHERE name = 'Cisco')),

('LOG-MX-MASTER3S', 'Logitech MX Master 3S', 40, 10, 'Wireless ergonomic productivity mouse', (SELECT id FROM suppliers WHERE name = 'Logitech')),
('LOG-MX-KEYS', 'Logitech MX Keys Keyboard', 15, 5, 'Wireless office keyboard', (SELECT id FROM suppliers WHERE name = 'Logitech')),

('SAM-SSD-990PRO', 'Samsung 990 Pro 2TB SSD', 6, 3, 'High performance NVMe storage drive', (SELECT id FROM suppliers WHERE name = 'Samsung')),
('SAM-MON-27-4K', 'Samsung 27 inch 4K Monitor', 20, 5, 'Professional UHD monitor', (SELECT id FROM suppliers WHERE name = 'Samsung')),

('KING-RAM-32GB-DDR5', 'Kingston 32GB DDR5 RAM', 60, 15, 'DDR5 memory module', (SELECT id FROM suppliers WHERE name = 'Kingston')),
('KING-USB-128GB', 'Kingston 128GB USB Drive', 100, 20, 'USB storage device', (SELECT id FROM suppliers WHERE name = 'Kingston')),

('ASUS-ROG-LAPTOP', 'ASUS ROG Gaming Laptop', 3, 2, 'High performance gaming laptop', (SELECT id FROM suppliers WHERE name = 'ASUS')),
('ASUS-MB-B650', 'ASUS B650 Motherboard', 7, 2, 'AMD motherboard for desktop systems', (SELECT id FROM suppliers WHERE name = 'ASUS'));