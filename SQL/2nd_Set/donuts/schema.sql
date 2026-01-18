CREATE TABLE Ingredients
(
    "id" INTEGER NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "price_per_unit" NUMERIC
);



CREATE TABLE Donuts
(
    "id" INTEGER PRIMARY KEY,
    "name" TEXT NOT NULL,
    "gluten_free" TEXT NOT NULL CHECK("gluten_free" IN ('yes', 'no')),
    "price_per_unit" NUMERIC
);



CREATE TABLE Ingredients_in_each_donut
(
    "donut_id" INTEGER NOT NULL,
    "ingredient_id" INTEGER NOT NULL,
    "quantity" TEXT,
    PRIMARY KEY("donut_id", "ingredient_id", "quantity"),
    FOREIGN KEY("donut_id") REFERENCES Donuts("id"),
    FOREIGN KEY("ingredient_id") REFERENCES Ingredients("id")

);




CREATE TABLE Orders
(
    "id" INTEGER PRIMARY KEY,
    "customer" NOT NULL,
    FOREIGN KEY("customer") REFERENCES Customers("id")
);



CREATE TABLE Donuts_in_each_order
(
    "order_id" INTEGER NOT NULL,
    "donut_id" INTEGER NOT NULL,
    "quantity" INTEGER,
    FOREIGN KEY("donut_id") REFERENCES Donuts("id"),
    FOREIGN KEY("order_id") REFERENCES Orders("id"),
    PRIMARY KEY("order_id", "donut_id", "quantity")

);




CREATE TABLE Customers
(
    "id" INTEGER PRIMARY KEY,
    "first_name" TEXT,
    "last_name" TEXT
);



CREATE TABLE History_of_orders_per_costumer
(
    "customer_id" INTEGER NOT NULL,
    "order_id" INTEGER NOT NULL,
);

