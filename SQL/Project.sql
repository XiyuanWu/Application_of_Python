SELECT
	t.get_date,
	count( DISTINCT CASE WHEN t.新老用户标识 = '新用户' THEN user_id ELSE NULL END ) AS 新用户数,
	count( DISTINCT CASE WHEN t.新老用户标识 = '老用户' THEN user_id ELSE NULL END ) AS 老用户数,
	count( DISTINCT CASE WHEN t.新老用户标识 = '未登录用户' THEN user_id ELSE NULL END ) AS 未登录用户数,
	sum( t.price )/ count( DISTINCT t.user_id ) AS 人均领取金额,
	count(*)/ count( DISTINCT t.user_id ) AS 人均领取次数 
FROM
	(
	SELECT
		g.get_date,
		g.user_id,
		g.price,
		( CASE WHEN u.whether_new = 1 THEN '新用户' WHEN u.whether_new = 0 THEN '老用户' ELSE '未登录用户' END ) AS 新老用户标识 
	FROM
		user_active AS u
		RIGHT JOIN get_redpacket AS g ON u.login_date = g.get_date 
		AND u.user_id = g.user_id 
	) AS t 
GROUP BY
	t.get_date;
