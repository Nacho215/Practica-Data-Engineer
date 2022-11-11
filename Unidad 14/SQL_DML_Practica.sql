-- PRÁCTICA UNIDAD 14 - SQL DML

-- Listar los nombres de los proveedores cuya ciudad contenga la cadena de texto “Ramos”.
SELECT Nombre, Ciudad
FROM Proveedor
WHERE Ciudad LIKE '%Ramos%'

-- Listar los códigos de los materiales que provea el proveedor 4 y no los provea el proveedor 5. Se debe resolver de 3 formas.
-- (NOT IN)
SELECT CodMat
FROM Provisto_por
WHERE CodProv = 4 AND CodMat NOT IN (SELECT CodMat
FROM Provisto_por
WHERE CodProv = 5)
-- (NOT EXISTS)
SELECT CodMat
FROM Provisto_por pp
WHERE CodProv = 4 AND NOT EXISTS (SELECT 1
FROM Provisto_por pp2
WHERE CodProv = 5 and pp.CodMat=pp2.CodMat)
-- (EXCEPT)
SELECT CodMat
FROM Provisto_por pp
WHERE CodProv = 4
EXCEPT
SELECT CodMat
FROM Provisto_por pp
WHERE CodProv = 5

-- Listar los materiales, código y descripción, provistos por proveedores de la ciudad de Ramos Mejía.
SELECT m.CodMat, m.Descripcion
FROM Material m
INNER JOIN Provisto_Por pp
ON m.CodMat = pp.CodMat
INNER JOIN Proveedor p
ON pp.CodProv = p.CodProv
WHERE Ciudad = 'Ramos  Mejía'

/* Listar los proveedores y materiales que provee.
La lista resultante debe incluir a aquellos proveedores
que no proveen ningún material. */
SELECT p.CodProv, p.Nombre, m.CodMat, m.Descripcion
FROM Proveedor p
LEFT JOIN Provisto_Por pp
ON p.CodProv = pp.CodProv
LEFT JOIN Material m
ON pp.CodMat = m.CodMat

-- Listar los artículos que cuesten más de $30 o que estén compuestos por el material 2.
SELECT *
FROM Articulo
WHERE Precio > 30
OR CodArt IN (
	SELECT CodArt
	FROM Compuesto_Por
	WHERE CodMat = 2
)

-- Listar los artículos de Mayor precio.
SELECT TOP 1 *
FROM Articulo
ORDER BY Precio DESC

-- Listar los proveedores que proveen más de 3 materiales
SELECT p.Nombre, COUNT(pp.CodProv) as Cant_materiales
FROM Proveedor p
INNER JOIN Provisto_Por pp
ON p.CodProv = pp.CodProv
GROUP BY (p.Nombre)
HAVING COUNT(pp.CodProv) > 3

-- Crear una vista para el caso de los proveedores que proveen más de 4 materiales. Mostrar la forma de invocar esa vista.
CREATE VIEW v_proveedores_4_mat AS (
	SELECT p.Nombre, COUNT(pp.CodProv) as Cant_materiales
	FROM Proveedor p
	INNER JOIN Provisto_Por pp
	ON p.CodProv = pp.CodProv
	GROUP BY (p.Nombre)
	HAVING COUNT(pp.CodProv) > 4
)
SELECT *
FROM v_proveedores_4_mat