#!/usr/bin/env python

'''
inpysync is a simple to use tool for Systems Administrators
to use to keep 1 or more nodes in sync with a master node.
inpysync runs on the master using inotify and rsync

Typical usage would be to have inpysync running on a master
webnode and have it sync changes to all slave nodes in the 
cluster. Thanks to the way rsync works you can have this
happen over an encrypted connection via ssh. If using the
rsync + ssh method make sure ssh keys are in place and that
the user running inpysync has permissions on the slave nodes
to write the changes to disk.

usage: 
inpysync --config=/path/to/config.ini


'''

__author__ = "Michael Rice"
__version__ = "0.1"
__license__ = "BSD"
__date__ = "2011-08-28"

import inpycfgparse 
import pyinotify
import os

#CFG_PATH = '/usr/local/etc/inpysync/config.ini'
CFG_PATH = 'example.ini'

class 

def setup_watch(sections):
  #loop through sections
  print len(sections)
  for k,v in sections.iteritems():
    syncmd = v.__dict__['syncmd']
    watchpath = v.__dict__['locpath']
    destpath = v.__dict__['destpath']
    desthost = v.__dict__['desthost']
    rec = v.__dict__['recurse']

    wm = pyinotify.WatchManager()
    notifier = pyinotify.Notifier(wm, default_proc_fun=

    #print k, "=>", v.__dict__
    #for opt,val in v.__dict__.iteritems():
      #print opt, val
  #for a thread for each one of the 
  #sections


if __name__ == "__main__":
  cfg = inpycfgparse.ParseCfg(CFG_PATH)
  sections = cfg.get_sections()
  setup_watch(sections)
