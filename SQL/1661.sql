SELECT machine_id, ROUND(AVG(processing_time),3) AS processing_time FROM( SELECT machine_id, process_id, start,end,
  (end - start) AS processing_time
FROM (
  SELECT machine_id, process_id,
    MAX(CASE WHEN activity_type = 'end' THEN timestamp END) AS end,
    MAX(CASE WHEN activity_type = 'start' THEN timestamp END) AS start
  FROM Activity
  GROUP BY machine_id, process_id
) AS subquery) A GROUP BY machine_id;