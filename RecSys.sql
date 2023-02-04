CREATE TABLE items
(
	item_id INT IDENTITY(1,1) not null,
	CONSTRAINT PK_item_id PRIMARY KEY (item_id),
	item_name VARCHAR (50) NOT NULL,

)

CREATE TABLE customers
(
	customer_id INT IDENTITY(1,1) not null,
	CONSTRAINT PK_customer_id PRIMARY KEY (customer_id),
	full_name VARCHAR (50) NOT NULL,
)

CREATE TABLE details 
(
	detail_id INT IDENTITY(1,1) NOT NULL,
	CONSTRAINT PK_detail_id PRIMARY KEY (detail_id),
	customer_id INT not null,
	CONSTRAINT FK_customer_id FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
	item_id INT NOT NULL,
    CONSTRAINT FK_item FOREIGN KEY (item_id) REFERENCES items(item_id),
	purchase_date DATE NOT NULL,
	price MONEY

)

