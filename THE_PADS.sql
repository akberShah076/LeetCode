SELECT CONCAT(name, '(', SUBSTRING(Occupation, 1, 1) , ')')
FROM OCCUPATIONS
Order by Name;

SELECT CONCAT('There are a total of ', COUNT(*), ' ', LOWER(Occupation), 's.') AS occupation_count
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY occupation_count, Occupation ASC;
