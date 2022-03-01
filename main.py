import sipfullproxy
import logging
import socket
import socketserver
import time

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s[%(levelname)s]%(message)s',filename='proxy_log.txt',level=logging.INFO,datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    
    hostname = socket.gethostname()
    logging.info("Hostname: %s" % hostname)
    
    ipaddress = socket.gethostbyname(hostname)
    logging.info("Host IP address: %s" % ipaddress)
    
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, sipfullproxy.PORT)
    
    server = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    server.serve_forever()