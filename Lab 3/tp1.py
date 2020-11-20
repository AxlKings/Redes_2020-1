"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class Tp1 ( Topo ):
    "Simple topology example."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
        ha = self.addHost( 'ha', mac = '00:00:00:00:00:01' )
        hb = self.addHost( 'hb', mac = '00:00:00:00:00:02'  )
        hc = self.addHost( 'hc', mac = '00:00:00:00:00:03'  )
        hd = self.addHost( 'hd', mac = '00:00:00:00:00:04'  )
        he = self.addHost( 'he', mac = '00:00:00:00:00:05'  )
        hf = self.addHost( 'hf', mac = '00:00:00:00:00:06'  )
       
        sx = self.addSwitch( 's1' )
        sy = self.addSwitch( 's2' )
        sz = self.addSwitch( 's3' )
        # Add links
        self.addLink( ha, sx,1,2)#ha 1 => 2 sx
        self.addLink( hb, sx, 3,4)#hb 3 => 4 sx
        self.addLink( hc, sy,5,6 )#hc 5 => 6 sy
        self.addLink( hd, sy,7,8 )# hd 7 => 8 sy
        self.addLink( he, sz,9,10 )#he 9 => 10 sz
        self.addLink( hf, sz,11,12 )#hf 11 => 12 sz
        self.addLink( sx, sy,13,14 )#Sx 13 => 14 Sy
        self.addLink( sx, sz,15,16 )#Sx 15 => 16 Sz
        self.addLink( sy, sz,17,18 )#Sy 17 => 18 Sz



topos = { 'tp1': ( lambda: Tp1() ) }
