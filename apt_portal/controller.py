#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#   (C) Copyright 2009, APT-Portal Developers
#    https://launchpad.net/~apt-portal-devs
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""
    controller related functions
"""
import cherrypy

def attach(controller, controller_path_name):    
    controller_path_name = controller_path_name.strip("/")
    setattr(cherrypy.root, controller_path_name, controller)

    
def publish(func=None, alias=None):   
    return cherrypy.expose(func, alias)

from apt_portal import pre_controller_tool