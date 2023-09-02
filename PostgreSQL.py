import psycopg2
import time
from datetime import datetime

sql_str_start = '''
  SELECT dbl_v
	FROM  public.ts_kv
	WHERE public.ts_kv.entity_id = '383e2180-3e91-11ee-8c07-bf0fc98b9140'
	AND   public.ts_kv.key = 100
	AND   public.ts_kv.ts > 1693501200000
	ORDER BY ts ASC
	LIMIT 1;
    '''

sql_str_end = '''
  SELECT dbl_v
	FROM  public.ts_kv
	WHERE public.ts_kv.entity_id = '383e2180-3e91-11ee-8c07-bf0fc98b9140'
	AND   public.ts_kv.key = 100
	AND   public.ts_kv.ts > 1693587599000
	ORDER BY ts DESC
	LIMIT 1;
    '''

def current_milli_time():
    return round(time.time() * 1000)



conn = psycopg2.connect(database="db_name",
                        host="xxx.xxx.x.x",
                        user="db_user",
                        password="db_pss",
                        port="5432")
cursor = conn.cursor()


cursor.execute(sql_str_start)
data_start = cursor.fetchone()

cursor.execute(sql_str_end)
data_end = cursor.fetchone()

kwh_data_start = None
kwh_data_end = None

print(data_start)

if(data_start):
    print('data_start[0] : ', data_start[0])   
    kwh_data_start = data_start[0] 
else:
    print("data_start is none")

print(data_end)

if(data_end):
    print('data_end[0] : ', data_end[0])
    kwh_data_end = data_end[0]
else:
    print("data_end is none")


if kwh_data_start and kwh_data_end:
    day_use =  kwh_data_end - kwh_data_start
    print('day_use : ', day_use)

# utc_time = datetime.strptime("2023-09-01T00:00:00.000Z", "%Y-%m-%dT%H:%M:%S.%fZ")
# milliseconds = (utc_time - datetime(1970, 1, 1)) # timedelta(milliseconds=1)
# print('utc_time : ', utc_time)
# print('milliseconds : ', milliseconds)




obj = time.gmtime(0)
epoch = time.asctime(obj)
print("The epoch is:",epoch)
curr_time = round(time.time()*1000)
print("Milliseconds since epoch:",curr_time)



print("Current date in string format:",datetime.utcnow())
date= datetime.utcnow() - datetime(1970, 1, 1)
print("Number of days since epoch:",date)
seconds =(date.total_seconds())
milliseconds = round(seconds*1000)
print("Milliseconds since epoch:",milliseconds)


dt = datetime(2023, 9, 1, 0, 0, 0)
milliseconds = int(round(dt.timestamp() * 1000))
print(milliseconds)

dt2 = datetime(2023, 9, 1, 23, 59, 59)
milliseconds2 = int(round(dt2.timestamp() * 1000))
print(milliseconds2)

    
#   SELECT entity_id, key, ts, dbl_v
# 	FROM  public.ts_kv
# 	WHERE public.ts_kv.entity_id = '383e2180-3e91-11ee-8c07-bf0fc98b9140'
# 	AND   public.ts_kv.key = 100
# 	AND   public.ts_kv.ts > 1693673999000
# 	ORDER BY ts ASC
# 	LIMIT 1;

# --  SELECT entity_id, key, ts, bool_v, str_v, long_v, dbl_v, json_v
# --	FROM public.ts_kv
# --	where entity_id = '383e2180-3e91-11ee-8c07-bf0fc98b9140' and key = 100 and ts >= 1693501200
# --	ORDER BY ts DESC LIMIT 10;

# -- 1693501200000  -- 20230901 00 00 00
# -- 1693587599000  -- 20230901 23 59 59
# 1693673999000


