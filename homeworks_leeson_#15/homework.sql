-- Задание 1

CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
);

CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200),
    author_id INT REFERENCES authors(id),
    publication_year INT
);

CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    book_id INT REFERENCES books(id),
    quantity INT
);

INSERT INTO authors (first_name, last_name) VALUES
('Александр', 'Пушкин'),
('Лев', 'Толстой'),
('Федор', 'Достоевский'),
('Антон', 'Чехов');

INSERT INTO books (title, author_id, publication_year) VALUES
('Капитанская дочка', 1, 1836),
('Война и мир', 2, 1869),
('Преступление и наказание', 3, 1866),
('Идиот', 3, 1869),
('Книга без автора', NULL, 2024);

INSERT INTO sales (book_id, quantity) VALUES
(1, 5),
(1, 2),
(2, 3),
(3, 1);

SELECT * FROM authors;
SELECT * FROM books;
SELECT * FROM sales;

-- Задание 2

SELECT books.title, authors.first_name, authors.last_name
FROM books
INNER JOIN authors ON books.author_id = authors.id;

SELECT authors.first_name, authors.last_name, books.title
FROM authors
LEFT JOIN books ON authors.id = books.author_id;

SELECT books.title, authors.first_name, authors.last_name
FROM authors
RIGHT JOIN books ON authors.id = books.author_id;

-- Задание 3

SELECT authors.first_name, authors.last_name, books.title, sales.quantity
FROM authors
INNER JOIN books ON authors.id = books.author_id
INNER JOIN sales ON books.id = sales.book_id;

SELECT authors.first_name, authors.last_name, books.title, sales.quantity
FROM authors
LEFT JOIN books ON authors.id = books.author_id
LEFT JOIN sales ON books.id = sales.book_id;
