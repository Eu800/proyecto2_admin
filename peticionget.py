from pysnmp.hlapi import *

#Parametros para el envio de la peticion

#Valores que se pueden poner en authprotocolo
# usmNoAuthProtocol: Sin autenticación. (1, 3, 6, 1, 6, 3, 10, 1, 1, 1)
# usmHMACMD5AuthProtocol: HMAC-MD5-96. (1, 3, 6, 1, 6, 3, 10, 1, 1, 2)
# usmHMACSHAAuthProtocol: HMAC-SHA-96. (1, 3, 6, 1, 6, 3, 10, 1, 1, 3)

#Valores que se pueden poner en privprotocolo
# usmNoPrivProtocol: Sin encriptación. (1, 3, 6, 1, 6, 3, 10, 1, 2, 1)
# usmDESPrivProtocol: DES (Data Encryption Standard). (1, 3, 6, 1, 6, 3, 10, 1, 2, 2)
# usmAesCfb128Protocol: AES con una clave de 128 bits.  (1, 3, 6, 1, 6, 3, 10, 1, 2, 4)
# usmAesCfb192Protocol: AES con una clave de 192 bits. (1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 101)
# usmAesCfb256Protocol: AES con una clave de 256 bits. (1, 3, 6, 1, 4, 1, 9, 12, 6, 1, 102)

#------------------------------------------------------------------------------------------------

# username='estalinTI2'
# authkey='0123456789'
# privkey='9876543210'
# authprotocolo=(1, 3, 6, 1, 6, 3, 10, 1, 1, 3)
# privprotocolo=(1, 3, 6, 1, 6, 3, 10, 1, 2, 2)

# # Definir los parámetros de seguridad
# security_params = UsmUserData(username, authkey, privkey, authProtocol=authprotocolo, privProtocol=privprotocolo)

# # Definir la dirección IP de la máquina SNMP
# ip_address = '192.168.1.50'

# # Realizar la petición SNMP versión 3
# g = getCmd(SnmpEngine(),
#            security_params,
#            UdpTransportTarget((ip_address, 161)),
#            ContextData(),
#            ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

#---------------------------------------------------------------------------------------------------

# username='estalinTI4'
# authkey='0123456789'
# authprotocolo=(1, 3, 6, 1, 6, 3, 10, 1, 1, 3)

# # Definir los parámetros de seguridad
# security_params = UsmUserData(username, authkey, authProtocol=authprotocolo)

# # Definir la dirección IP de la máquina SNMP
# ip_address = '192.168.1.50'

# # Realizar la petición SNMP versión 3
# g = getCmd(SnmpEngine(),
#            security_params,
#            UdpTransportTarget((ip_address, 161)),
#            ContextData(),
#            ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

#-------------------------------------------------------------------------------------------------

username='estalinTI5'

# Definir los parámetros de seguridad
security_params = UsmUserData(username)

# Definir la dirección IP de la máquina SNMP
ip_address = '192.168.1.50'

# Realizar la petición SNMP versión 3
g = getCmd(SnmpEngine(),
           security_params,
           UdpTransportTarget((ip_address, 161)),
           ContextData(),
           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)))

# Iterar sobre los resultados de la petición
for (errorIndication, errorStatus, errorIndex, varBinds) in g:
    if errorIndication:
        print(errorIndication)
        break
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                             errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        break
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
