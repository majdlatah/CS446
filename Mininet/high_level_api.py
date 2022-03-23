#!/usr/bin/python

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.cli import CLI
from mininet.node import RemoteController

class SingleSwitchTopo(Topo):
	def build(self,count):
		hosts = [ self.addHost('h%d'%i) for i in range(count) ]
		s1 = self.addSwitch('s1')
		for h in hosts:
			self.addLink(h,s1)

net = Mininet(topo=SingleSwitchTopo(5), controller=RemoteController)

net.start()

h1, h2 = net.getNodeByName('h0', 'h1')

h1_IpAddress = h1.IP()

print("Ping from "+h1.IP()+" to "+h2.IP())
print(h1.cmd("ping -c 3", h1_IpAddress))

net.iperf( ( h1, h2 ))

CLI(net)
net.stop()
