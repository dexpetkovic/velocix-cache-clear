'''
Created on 9 Oct 2014

@author: dpetkovic
'''
import sys
import clientHttpsTransport, wpObject, velocixCDN

if __name__ == '__main__':
    args = sys.argv
    cacheClearProperty = wpObject.wpObject(args[1], args[2])
    cdn = velocixCDN.velocixCDN(args[3], args[4])
    cdn.clearCache(cacheClearProperty)