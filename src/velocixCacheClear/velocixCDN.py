
import xmlrpc.client
import sys
import clientHttpsTransport, wpObject

class velocixCDN:

	def __init__(self):
		self.account = "Account-Name";
		self.host = "https://console.cdn.yourCDNhost.com/xmlrpc"
		
		# This keyfile is an OpenSSL file containing both public and private
		# key in PEM blocks. You need to generate certificate for each
		# account in Velocix console and make it available to this script
		if self.account == "account1":
			keyfile = "user-account1-certificate.pem";
		elif self.account == "account2":
			keyfile = "user-account2-certificate.pem"
		elif self.account == "account3":
			keyfile = "user-account3-certificate.pem";
			
		self.server = xmlrpc.client.ServerProxy( self.host, clientHttpsTransport.ClientHttpsTransport(keyfile, keyfile), verbose=False )
	
	def clearCache(self, obj):
		try:
			# getStructWpObject returns WP object parameters in the struct form. If this is string then the WP object does not get created.
			clearCacheResponse = self.server.xmlrpc.flushURLs(obj.getStructWpObject())
			return clearCacheResponse
		except Exception as e: print(e)
	
	def queryObject(self, obj):
		try:
			response = self.server.xmlrpc.queryObject(obj.getStructWpObject())
			print(response);
		except Exception as e: print(e)