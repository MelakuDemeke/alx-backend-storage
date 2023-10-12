-- Retrieve and rank the countries of origin for metal bands based on
--their total number of fans.
SELECT origin, SUM(fans) AS nb_fans
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;
