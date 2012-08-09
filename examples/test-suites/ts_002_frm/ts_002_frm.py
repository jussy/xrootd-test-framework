from XrdTest.TestUtils import TestSuite, TestCase

def getTestSuite():
    ts = TestSuite()

    ts.name = "ts_002_frm"
    ts.clusters = ['cluster_002_frm']
    ts.machines = ['frm1', 'frm2', 'ds1', 'ds2', 'ds3', 'ds4', 'client1']
    ts.tests = ['simple_copy_to', 'simple_copy_from']
    
    ts.schedule = dict(second='30', minute='08', hour='*', day='*', month='*')

    ts.initialize = "file://suite_init.sh"
    ts.finalize = "file://suite_finalize.sh"

    return ts

def getTestCases():
    tcs = []

    tc1 = TestCase()
    tc1.name = "simple_copy_to"
    tc1.initialize = "file://tc/" + tc1.name + "/init.sh"
    tc1.run = "file://tc/" + tc1.name + "/run.sh"
    tc1.finalize = "file://tc/" + tc1.name + "/finalize.sh"
    tcs.append(tc1)
    
    tc2 = TestCase()
    tc2.name = "simple_copy_from"
    tc2.initialize = "file://tc/" + tc2.name + "/init.sh"
    tc2.run = "file://tc/" + tc2.name + "/run.sh"
    tc2.finalize = "file://tc/" + tc2.name + "/finalize.sh"
    tcs.append(tc2)

    return tcs
