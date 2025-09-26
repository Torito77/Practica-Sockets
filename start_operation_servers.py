from OpServers.add_server import AddServer
from OpServers.sub_server import SubServer
from OpServers.prod_server import ProdServer
from OpServers.div_server import DivServer
from OpServers.mod_server import ModServer
from OpServers.pow_server import PowServer
from threading import Thread


def add_task():
    a = AddServer("localhost",7001, name="AddServer")
    a.server_start()

def sub_task():
    s = SubServer("localhost",7002, name="SubServer")
    s.server_start()

def prod_task():
    p = ProdServer("localhost",7003, name="ProductServer")
    p.server_start()

def div_task():
    d = DivServer("localhost",7004, name="DivServer")
    d.server_start()
    
def mod_task():
    m = ModServer("localhost",7005, name="ModServer")
    m.server_start()

def pow_task():
    pw = PowServer("localhost",7006, name="PowerServer")
    pw.server_start()

t1 = Thread(target=add_task)
t2 = Thread(target=sub_task)
t3 = Thread(target=prod_task)
t4 = Thread(target=div_task)
t5 = Thread(target=mod_task)
t6 = Thread(target=pow_task)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
