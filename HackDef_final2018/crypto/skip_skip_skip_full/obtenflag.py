from Crypto.Util.number import *
import gmpy
from Crypto.Util import number
from Crypto.PublicKey.RSA import construct
from Crypto.PublicKey import RSA
import sympy


modulo=open("Modulus","r")
N =bytes_to_long(modulo.read())
modulo.close()

exp=open("Exponent","r")
e=bytes_to_long(exp.read())
exp.close()

encrypted=open("Encrypted_wlmolbo_ednrau","r")
c =bytes_to_long(encrypted.read())
encrypted.close()

p = 0#probar
q = 0#obtener de N / p

#
def woodall_number(n):
	npow = pow(2,n)
	p1 = (n*npow)-1
	return p1
#	
#

for n in range(2, 1000000):
	p = woodall_number(n)
	
	if(N % p == 0 and isPrime(p)):
		q = N / p
		if(isPrime(q)):
			break

# ya tenemos p, q, N, e, mensaje_encriptado


#"print "mensaje_encriptado: " + str(mensaje_encriptado)

# calcular d, llave privada
d = long(gmpy.invert(e,(p-1)*(q-1)))


#mensaje_encriptado = pow(bytes_to_long("flag{esta es la chida}"), e, N)

mensaje_desencriptado = pow(c, d, N)
msj = long_to_bytes(mensaje_desencriptado)
print msj	

