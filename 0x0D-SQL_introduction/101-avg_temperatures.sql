-- a script that displays the average temperature (Fahrenheit) by city ordered
SELECT city, AVG(value) AS avg_tempp
FROM temperatures
GROUP BY city
ORDER BY avg_tempp DESC;
