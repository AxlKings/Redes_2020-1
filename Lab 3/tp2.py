"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo

class Tp2 ( Topo ):
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
        hg = self.addHost( 'hg', mac = '00:00:00:00:00:07'  )
       
        
        sv = self.addSwitch( 's1' )
        sx = self.addSwitch( 's2' )
        sz = self.addSwitch( 's3' )
        sy = self.addSwitch( 's4' )
        sw = self.addSwitch( 's5' )
        su = self.addSwitch( 's6' )
        st = self.addSwitch( 's7' )

        # Add links
        self.addLink( ha, sv,1,2)#ha 1 => 2 sv
        self.addLink( hb, sv, 3,4)#hb 3 => 4 sv
        self.addLink( hc, sx,5,6 )#hc 5 => 6 sx
        self.addLink( hd, sx,7,8 )# hd 7 => 8 sx
        self.addLink( he, sz,9,10 )#he 9 => 10 sz
        self.addLink( hf, sz,11,12 )#hf 11 => 12 sz
        self.addLink( sv, su,13,14 )#Sv 13 => 14 Su
        self.addLink( sx, sw,15,16 )#Sx 15 => 16 Sw
        self.addLink( sz, sy,17,18 )#Sz 17 => 18 Sy
        self.addLink( sy, sw,19,20 )#Sy 19 => 20 Sw
        self.addLink( sw, su,21,22 )#Sw 21 => 22 Su
        self.addLink( su, st,23,24 )#Su 23 => 24 St
        self.addLink( st, sv,25,26 )#St 25 => 26 Sv
        self.addLink( hg, st,27,28 )#hg 27 => 28 st
        self.addLink( sv, sx,29,30 )#Sv 29 => 30 Sx
        self.addLink( sx, sz,31,32 )#Sx 31 => 32 Sz



topos = { 'tp2': ( lambda: Tp2() ) }
