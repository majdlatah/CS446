#!/usr/bin/python

from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import RemoteController

net = Mininet()
h1 = net.addHost( 'h1' )
h2 = net.addHost( 'h2' )
s1 = net.addSwitch( 's1' )
c0 = net.addController( 'c0', RemoteController)
net.addLink( h1, s1 )
net.addLink( h2, s1 )
net.start()
CLI( net )
net.stop()
