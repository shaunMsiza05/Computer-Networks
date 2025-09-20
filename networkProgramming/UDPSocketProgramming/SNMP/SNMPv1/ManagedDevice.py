

MIB = {
    "OID": ,
    "Object Name": ,
    "data type": ,
    "Maximum access": ,
    "Description": ,
}

# so we have a single MIB which contains multiple mib objects

#to make this more interesting, let's assume this managed device is a switch, that way I can write more consistent mib object
# for demostration, write four objects, one which identifies the number of interfaces on the switch, one for a number of vlan (and maximum access should allow adding vlans and modifying vlan number)
# so the MIB structure will be stanardised in the nms, then local MIBs should be done here.


MIB = [{
    "OID": "1.3.6.1.2.2.1",
    "objectName": "vlanNumber",
    "Value": "Integer",
    "maximumAcess": "read-only",
    "Description": "Number of vlans configured on the switch"
}, {

}, {

}
]

def createMIBObject(oid, objectName, dataType, maximumAcess, description):

