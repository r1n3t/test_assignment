SELECT promo_id, start_date, end_date, discount
FROM PROMO
WHERE '2022-12-01' BETWEEN start_date AND end_date
ORDER BY discount DESC
LIMIT 5;