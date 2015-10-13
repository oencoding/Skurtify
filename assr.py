#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib2 import urlopen
from json import load

def test_sr():
	'''testar sr:s api'''
	url = "http://api.sr.se/api/v2/playlists/rightnow?channelid=164&format=json"
	response = urlopen(url)
	json_obj = load(response)

	try:
		obj = json_obj['playlist']['song']['description']
		text = 'Just nu spelas'
		return (obj, text)
	except KeyError:
		try:
			obj = json_obj['playlist']['previoussong']['description']
			text = 'Previous song was'
			return (obj, text)
		except KeyError:
			obj = json_obj['playlist']['nextsong']['description']
			text = 'Next song is'
			return (obj, text)