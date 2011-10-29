#!/usr/bin/env python

import ConfigParser

class SyncInfo:
  def __init__(self,syncmd=None,lpath=None,dpath=None,dhost=None,rec=True):
     self.syncmd = syncmd
     self.locpath = lpath
     self.destpath = dpath
     self.desthost = dhost
     self.recurse = rec 
  
  def set_syncmd(self,cmd):
    self.syncmd = cmd 

  def set_locpath(self,path):
    self.locpath = path

  def set_destpath(self,path):
    self.destpath = path

  def set_desthost(self,host):
    self.desthost = host

  def set_recurse(self,recurse):
    self.recurse = recurse

  def get_syncmd(self):
    return str(self.syncmd)

  def get_locpath(self):
    return str(self.locpath)

  def get_destpath(self):
    return str(self.destpath)

  def get_desthost(self):
    return str(self.desthost)

  def get_recurse(self):
    return bool(self.recurse)

class ParseCfg:
  
  def __init__(self,cfg_path):
    self.config = ConfigParser.ConfigParser()
    self.config.read(cfg_path)
    self.sections = {}
    self._set_sections()
  
  def print_all(self):
    for k,v in self.sections.iteritems():
      print k
      print v.get_syncmd()
      print v.get_locpath()
      print v.get_destpath()
      print v.get_desthost()
      print v.get_recurse()

  def _set_sections(self):
    for section in self.config.sections():
      info = SyncInfo()
      for option in self.config.options(section):
        try:
          info.set_recurse(self.config.getboolean(section,option))
        except ValueError:
          if option == "path":
            info.set_locpath(self.config.get(section,option))
          elif option == "syncmd":
            info.set_syncmd(self.config.get(section,option))
          elif option == "desthost":
            info.set_desthost(self.config.get(section,option))
          elif option == "destpath":
            info.set_destpath(self.config.get(section,option))
      self.sections[section] = info  
  
  def get_sections(self):
    return self.sections


if __name__ == "__main__":
  cfg_path = "example.ini"
  ParseCfg(cfg_path).print_all()
