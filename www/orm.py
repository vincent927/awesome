@asyncio.coroutine

def create_pool(loop,**kw):
	logging.info('create database connection pool...')
	global __pool
	__pool = yield from aiomysql.create_pool(
	host=kw.get('host', '192.168.1.83'),
	port=kw.get('port', 3306),
	user=kw['user'],
	password=kw['password'],
	db=kw['db'],
	charset=kw.get('charset', 'utf8'),
	autocommit=kw.get('autocommit', True),
	maxsize=kw.get('maxsize', 10),
	minsize=kw.get('minsize', 1),
	loop=loop
)