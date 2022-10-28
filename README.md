# test-MillionAgents

Ответы на задачи по SQL

1)

```
SELECT user_id, SUM(reward)
FROM reports 
WHERE user_id IN (
  SELECT user_id FROM reports WHERE created_at > 1609448400 AND created_at < 1640984400 group by user_id
) AND NOT user_id IN (
  SELECT user_id FROM reports WHERE created_at < 1609448400 group by user_id
) AND created_at > 1640984400 AND created_at < 1672520400
GROUP BY user_id
```

2)

```
SELECT ARRAY_AGG((reports.barcode, reports.price)), pos.title
FROM reports JOIN pos
ON reports.pos_id = pos.id
GROUP BY pos.title
```