import os

# SITE_ROOT = os.path.dirname(os.path.realpath(__file__))

#dbsqlite= SITE_ROOT +'/ilconf.db'

# print SITE_ROOT +'/ilconf.db'
a = os.environ.get('DJANGO_DATABASE', 'main')

if a == "local" :
	print 'esta'
	print a + ''
else:
	print 'no esta'
	print a + ''