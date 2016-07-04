CREATE_FUNC = """CREATE OR REPLACE FUNCTION filter_ip_array(inet[])
RETURNS inet[]
AS
$$
DECLARE
        nt_curr cidr;
        networks cidr[];
        result inet[];
        i inet;
        l int := 0;
BEGIN
        FOREACH i IN ARRAY $1
        LOOP
              nt_curr = network(i);
              IF ARRAY[nt_curr] <@ networks THEN
                CONTINUE;
              ELSE
                SELECT array_append(networks, nt_curr) INTO networks;
              END IF;

              IF ARRAY[i] <@ result THEN
                CONTINUE;
              ELSE
                SELECT array_append(result, i) INTO result;
              END IF;
        END LOOP;
        SELECT array_length(networks, 1) INTO l;
        IF l > 1 THEN
                RETURN result;
        ELSE
                RETURN ARRAY[]::inet[];
        END IF;
END;
$$
LANGUAGE plpgsql"""

CREATE_VIEW = """CREATE MATERIALIZED VIEW user_ip AS
SELECT r.user1 , r.user2, filter_ip_array(r.ips) FROM
(SELECT t.user1, t.user2, array_agg(t.ip1) || array_agg(t.ip2) AS ips
FROM
(SELECT t1.user_id AS user1, t1.ip_address AS ip1, t2.user_id AS user2, t2.ip_address AS ip2
FROM
iptable t1 INNER JOIN iptable t2 ON t1.ip_address = t2.ip_address AND t1.user_id != t2.user_id) t
GROUP BY t.user1, t.user2) r
WHERE array_length(filter_ip_array(r.ips), 1) >= 2"""

CREATE_INDEX = """CREATE INDEX user_ip_users ON user_ip(user1, user2)"""

REFRESH_VIEW = """REFRESH MATERIALIZED VIEW user_ip"""
