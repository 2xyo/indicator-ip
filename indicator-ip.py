#!/usr/bin/env python
# -*- coding: utf-8 -*-

import appindicator
import gtk
import netifaces
import urllib2

URL_PUBLIC_IP = 'http://automation.whatismyip.coim/n09230945.asp'

def get_public_ip():
   opener = urllib2.build_opener()
   opener.addheaders = [('cache-control', 'no-cache')]
   
   return opener.open(URL_PUBLIC_IP).read()

def get_private_ip(i):
       return netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']


def create_menu(indi,a=None):
   
   menu = gtk.Menu()
   
   menu_item = gtk.MenuItem("Refresh")
   menu_item.connect("activate",create_menu,ind)
   menu.append(menu_item)
   menu_item.show()
  
   try:
     menu_item = gtk.MenuItem("Public : %s" % get_public_ip())
   except:
     menu_item = gtk.MenuItem("No public IP")

   menu.append(menu_item)
   menu_item.show()
   
   for i in netifaces.interfaces():
      if i != "lo":
         menu_item = gtk.MenuItem("%s : %s" % (i, get_private_ip(i)))
         menu.append(menu_item)
         menu_item.show()
   
   ind.set_menu(menu)


ind = appindicator.Indicator("indicator-network",
   "/usr/share/notify-osd/icons/gnome/scalable/status/notification-network-ethernet-connected.svg",
   appindicator.CATEGORY_COMMUNICATIONS)

ind.set_status (appindicator.STATUS_ACTIVE)


if __name__ == "__main__":
   create_menu(ind)
   gtk.main()

