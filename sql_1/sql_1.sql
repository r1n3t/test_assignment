SELECT warehouse_id,
       SUM(cost_sum) AS total_cost
FROM wh_costs AS wh
JOIN fp_desk AS fd ON wh.fp_code = fd.fp_code
WHERE fd.fp_code_label IN ('Ответственное хранение', 'Ремонт офисного и складского оборудования')
GROUP BY warehouse_id
HAVING SUM(cost_sum) >= 10000000
ORDER BY MIN(cost_date)
LIMIT 5;