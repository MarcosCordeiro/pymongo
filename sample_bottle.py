import bottle
import pymongo

@bottle.route('/nome/<name2:re:[a-z]+>')
def index(name2):
	connection = pymongo.MongoClient('localhost', 27017)
	db = connection.test

	names = db.nomes
	item = names.find_one()

	return '<b>Hello %s da cidade de %s!</b> E benvindo %s' % (item['nome1'],item['cidade'],name2)

@bottle.route('/<nome3>')
def nome(nome3):
	return '<b> Nome outra rota %s</b>' % nome3

bottle.run(host='localhost', port=8082)