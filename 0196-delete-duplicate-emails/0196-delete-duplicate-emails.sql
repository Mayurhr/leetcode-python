# Write your MySQL query statement below
DELETE p2 from person p1
JOIN person p2 on p1.email=p2.email
WHERE p1.id<p2.id