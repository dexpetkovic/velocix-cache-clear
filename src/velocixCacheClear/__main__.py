'''
Created on 9 Oct 2014

@author: dpetkovic
'''
import sys
import clientHttpsTransport, wpObject, velocixCDN

if __name__ == '__main__':
    args = sys.argv
    cacheClearProperty = wpObject.wpObject(args[1], args[2])
    #cacheClearProperty = wpObject.wpObject('WP:XXXXXXXXXXXXXX', "/*")
    cdn = velocixCDN.velocixCDN()
    cdn.clearCache(cacheClearProperty)