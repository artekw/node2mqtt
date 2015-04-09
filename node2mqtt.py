#!/usr/bin/python2
# -*- coding: utf-8 -*-

debug = True
version = '0.1-dev'
app_name = 'node2mtqq'

import os
#import logging
import simplejson as json
import multiprocessing # http://pymotw.com/2/multiprocessing

# tornado
import tornado.ioloop
import tornado.gen
from tornado.options import define, options

# sensnode
import sensnode.decoder, sensnode.connect
from sensnode.config import config

import paho.mqtt.publish as mqtt

ci = config(init=True)


define("broker_port",default=config().get("app", ['broker', 'port']),
		help="mosquitto hostname", type=int)
define("broker_hostname",default=config().get("app", ['broker', 'hostname']),
		help="mosquitto port")


def publish(jsondata):
	"""
	>> data = {'vrms': 220.39, 'timestamp': 1428338500, 'name': 'powernode', 'power': 246}
	>> publish(data, hostname="localhost" port="1883")
	/powernode/vrms 220.39
	/powernode/power 246
	/powernode/timestamp 1428338500
	"""
	name = jsondata['name']
	for k, v in jsondata.iteritems():
		mqtt.single("/%s/%s" % (name, k), v, hostname=options.broker_hostname, port=options.broker_port)
		

def main():
    print "%s %s was started" % (app_name, version)
    taskQ = multiprocessing.Queue()
    resultQ = multiprocessing.Queue()

    connect = sensnode.connect.Connect(taskQ, resultQ, debug=False)
    connect.daemon = True
    connect.start()

    decoder = sensnode.decoder.Decoder(debug=debug)
    tornado.options.parse_command_line()
    
    @tornado.gen.engine
    def checkResults():
        if not resultQ.empty():
            raw = resultQ.get()
            decoded = decoder.decode(raw)
            if debug:
                print "RAW: %s" % (raw)
                print "JSON %s" % (decoded)
            # publikowanie danych w MQTT do brokera
            # TODO: odbieranie
            publish(decoded)
            

    mainLoop = tornado.ioloop.IOLoop.instance()
    scheduler = tornado.ioloop.PeriodicCallback(
        checkResults, 500, io_loop=mainLoop)
    scheduler.start()
    mainLoop.start()

if __name__ == "__main__":
    main()
