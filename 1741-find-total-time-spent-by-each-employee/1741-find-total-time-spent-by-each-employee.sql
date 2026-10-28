# Write your MySQL query statement below
SELECT
event_day AS day,
emp_id,
SUM(out_time - in_time) AS total_time
FROM
Employees
GROUP BY
event_day,
emp_id

-- Synced seamlessly with LeetHub Pro
-- Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
-- Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna