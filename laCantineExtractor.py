import urllib2
import re
import sys

#Modes Url
mode_url = "http://lacantine.ubicast.eu/videos/modes/"

headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1535.0 Safari/537.36' }

#Regexp
media_id_regexp = re.compile('media_id: "(.*)",')
youtube_url_regexp = re.compile('{"file": "(.*)"}}, "name":')

"""
Return the first match of regexp past in param on the url given
Param :
	-url : a website url
	-regexp : a compiled regexp
"""
def get_regexp_in_html(url,regexp):
	req = urllib2.Request(url, None, headers)
	html = urllib2.urlopen(req).read()
	result = regexp.findall(html)
	#Yes I know
	return result[0]


if __name__ == '__main__':
	if len(sys.argv) == 2 :
		url = sys.argv[1]
	else:
		print 'Usage : python2.7 ' + sys.argv[0] +' http://lacantine.ubicast.eu/videos/xxxxxx'
		exit()


	#Getting the media_id
	media_id = get_regexp_in_html(url,media_id_regexp)
	#Building the url
	url = mode_url  + media_id
	#Getting the youtube url
	youtube_url = get_regexp_in_html(url,youtube_url_regexp)

	print youtube_url
