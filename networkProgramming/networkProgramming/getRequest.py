from pysnmp.hlapi import getCmd, SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity

# Define SNMP parameters
snmp_engine = SnmpEngine()
community_data = CommunityData('public', mpModel=0)  # SNMPv1
udp_transport_target = UdpTransportTarget(('192.168.1.1', 161))  # IP address and port of the device
context_data = ContextData()

# Define OID
oid = ObjectIdentity('.1.3.6.1.2.1.1.1.0')  # sysDescr

# Create an SNMP GET request
result = getCmd(snmp_engine, community_data, udp_transport_target, context_data, ObjectType(oid))

# Process the response
for response in result:
    error_indication, error_status, error_index, var_binds = response
    if error_indication:
        print(f"SNMP error: {error_indication}")
    elif error_status:
        print(f"SNMP error: {error_status.prettyPrint()} at {error_index and var_binds[int(error_index) - 1][0] or '?'}")
    else:
        for oid, value in var_binds:
            print(f"System Description: {value.prettyPrint()}")