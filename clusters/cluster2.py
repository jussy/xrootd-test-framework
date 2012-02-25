from ClusterManager import Cluster, Network, Host
from copy import copy

def getCluster():
    cluster = Cluster()
    #---------------------------------------------------------------------------
    # Global names
    # Used commonly in network definition and hosts definition
    #---------------------------------------------------------------------------
    cluster.name = 'cluster2'
    cluster.diskImage = '/data/virtual/images/lt_slc5_refslave.img'

    network_name = 'net2.xrdtest'

    host1_mac = '52:54:00:65:44:69'
    host2_mac = '52:54:00:A3:F9:73'
    host3_mac = '52:54:00:E8:FD:17'
    #---------------------------------------------------------------------------
    # Network definition
    #---------------------------------------------------------------------------
    net = Network()
    net.bridgeName = 'virbr91'
    net.name = network_name
    net.ip = '192.168.131.1'
    net.netmask = '255.255.255.0'
    net.DHCPRange = ('192.168.131.2', '192.168.131.254')

    net.addHost((host1_mac, '192.168.131.2', 'm0.xrd.test'))
    net.addHost((host2_mac, '192.168.131.3', 'm1.xrd.test'))
    net.addHost((host3_mac, '192.168.131.4', 'm2.xrd.test'))

    cluster.network = net
    #---------------------------------------------------------------------------
    # Cluster machines definitions
    #---------------------------------------------------------------------------
    host1 = Host()
    host1.name = 'lt_pm1'
    host1.ramSize = '524288'
    host1.arch = 'x86_64'
    host1.uuid = '1fb103a6-8873-e114-a3d5-8bd89bcbac7f'
    
    host1.sourceNetwork = network_name
    host1.macAddress = host1_mac
    #---------------------------------------------------------------------------
    host2 = copy(host1)
    host2.name = 'lt_m12'
    host2.uuid = '1fb103a6-8873-e114-a3d5-8bd89bcbac80'
    host2.macAddress = host2_mac
    
    #---------------------------------------------------------------------------
    host3 = copy(host1)
    host3.name = 'lt_m22'
    host3.uuid = '1fb103a6-8873-e114-a3d5-8bd89bcbac82'
    host3.macAddress = host3_mac
    
    cluster.addHost(host1)
    cluster.addHost(host2)
    cluster.addHost(host3)

    return cluster

