#!/usr/bin/python
import telnetlib
from time import sleep

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
    print "Hello"
    time.sleep(6)
    print "Hello6"
    ip_addr = '10.7.192.169'
    username = 'pete4027'
    password = 'Intel1000'

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)

    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output = remote_conn.read_until("ssword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    time.sleep(1)
    print output
    output = remote_conn.read_very_eager()
    print output
    remote_conn.close()

main()
