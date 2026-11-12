import sqlite3,json
from .common import unique_ids
def run(data):
 rows=data['rows']
 if not isinstance(rows,list)or len(rows)>1000:raise ValueError('rows')
 unique_ids(rows)
 with sqlite3.connect(':memory:')as db:
  db.execute('create table payload(id text,doc text)')
  db.executemany('insert into payload values (?,?)',[(r['id'],json.dumps(r['doc'],allow_nan=False))for r in rows])
  result=[dict(id=i,json_type=t,sql_value=v,sql_type=s)for i,t,v,s in db.execute("select id,json_type(doc,'$.x'),json_extract(doc,'$.x'),typeof(json_extract(doc,'$.x'))from payload order by rowid")]
 return {'rows':result,'sqlite_version':sqlite3.sqlite_version}
