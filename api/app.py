#!/usr/bin/env python3

import connexion

app = connexion.App(__name__, specification_dir='./swagger/')
app.add_api('veracity-1.0.0-swagger.yaml', arguments={'title': 'Veracity API'})

# set the WSGI application callable to allow using uWSGI:
# uwsgi --http :8080 -w app
application = app.app

if __name__ == '__main__':
    # run our standalone gevent server
    app.run(port=8080)
