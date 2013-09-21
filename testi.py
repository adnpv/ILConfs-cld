import os

# SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

#dbsqlite= SITE_ROOT +'/ilconf.db'

# print SITE_ROOT +'/ilconf.db'
a = os.environ.get('DJANGO_DATABASE', 'main')
b = os.getenv('DJANGO_DATABASE')
if a == "local" :
	print 'esta'
	print a + ''
	print b
else:
	print 'no esta'
	print a + ''
	print b