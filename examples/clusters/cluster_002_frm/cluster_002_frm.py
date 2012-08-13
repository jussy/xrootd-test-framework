from XrdTest.ClusterUtils import Cluster, Network, Host, Disk 

def getCluster():
    cluster = Cluster()
    #---------------------------------------------------------------------------
    # Global names
    #---------------------------------------------------------------------------
    cluster.name = 'cluster_002_frm' 
    network_name = 'net_frm'
    
    #---------------------------------------------------------------------------
    # Cluster defaults
    #---------------------------------------------------------------------------
    cluster.defaultHost.bootImage = '/var/lib/libvirt/images/slc6_testslave_ref.img'
    cluster.defaultHost.cacheBootImage = True
    cluster.defaultHost.arch = 'x86_64'
    cluster.defaultHost.ramSize = '1048576'
    cluster.defaultHost.net = network_name
    
    #---------------------------------------------------------------------------
    # Network definition
    #---------------------------------------------------------------------------
    net = Network()
    net.bridgeName = 'virbr_002_frm'
    net.name = network_name
    net.ip = '192.168.129.1'
    net.netmask = '255.255.255.0'
    net.DHCPRange = ('192.168.129.2', '192.168.129.254')

    #---------------------------------------------------------------------------
    # Host definitions
    #---------------------------------------------------------------------------
    frm1 = Host('frm1.xrd.test', '192.168.129.4', "52:54:00:65:44:73")
    frm2 = Host('frm2.xrd.test', '192.168.129.5', "52:54:00:65:44:74")
    ds1 = Host('ds1.xrd.test', '192.168.129.6', "52:54:00:65:44:75")
    ds2 = Host('ds2.xrd.test', '192.168.129.7', "52:54:00:65:44:76")
    ds3 = Host('ds3.xrd.test', '192.168.129.8', "52:54:00:65:44:77")
    ds4 = Host('ds4.xrd.test', '192.168.129.9', "52:54:00:65:44:78")
    client1 = Host('client1.xrd.test', '192.168.129.10', "52:54:00:65:44:79")
    
    #---------------------------------------------------------------------------
    # Additional host disk definitions
    #---------------------------------------------------------------------------
    frm1.disks =  [Disk('disk1', '59055800320', 'vdb')]
    frm2.disks =  [Disk('disk1', '59055800320', 'vdb')]
    ds1.disks =  [Disk('disk1', '59055800320', 'vdb')]
    ds2.disks =  [Disk('disk1', '59055800320', 'vdb')]
    ds3.disks =  [Disk('disk1', '59055800320', 'vdb')]
    ds4.disks =  [Disk('disk1', '59055800320', 'vdb')]
    client1.disks =  [Disk('disk1', '59055800320', 'vdb')]


    # Hosts to be included in the cluster
    hosts = [frm1, frm2, ds1, ds2, ds3, ds4, client1]

    net.addHosts(hosts)
    cluster.network = net
    cluster.addHosts(hosts)
    return cluster 
 