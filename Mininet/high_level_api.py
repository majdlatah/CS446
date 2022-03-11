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
CLI(net)
net.stop()
