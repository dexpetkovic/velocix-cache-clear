'''
Created on 3 Oct 2014

@author: dpetkovic
'''
import re

class wpObject:
    '''
    classdocs
    '''
           
    def __init__(self, wpProtohash, urls):
        '''
        Constructor
        '''
        self.wpProtohash = wpProtohash
        self.urls = urls if urls is not None else None

    def getWpObject(self):
        return self
    
    def getStructWpObject(self):
        wpObjectStruct = {'protohash': self.wpProtohash, 'urls': self.urls}
        return wpObjectStruct
         
    def __str__(self):
            stringOutput = "{protohash:" + self.wpProtohash + ",urls:" + self.urls + "}"
            return stringOutput
        