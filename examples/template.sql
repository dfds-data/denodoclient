SELECT  *
FROM mytable
WHERE datetime BETWEEN '2020-01-01' AND NOW() 
AND mycolumn=123456
LIMIT 1000;