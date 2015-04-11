#!/usr/bin/python
# -*- coding: utf-8 -*-


import urllib2
import urllib
import re



def search(song,singer):
    
    searchurl = "http://www.xiami.com/ajax/search-index?key="+urllib.quote(song.encode('utf-8'))

    request = urllib2.Request(searchurl)
    
    request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36')


    response = urllib2.urlopen(request)
    html = response.read().decode('utf-8')
#     print html


    
    

    res = '歌曲'.decode('utf-8')
    
    detailre = re.findall('<h3 class="song">'+res+'</h3>(.*)<a href="(.*?)" title="(.*?)" class=(.*?)<span>'+singer+'</strong></a>' ,html,re.S)
    
    print detailre
    
    if(detailre == []):
        print detailre
        
        return {"status":"-1","message":"song not found"}
    
    else:
        searchtagurl = detailre[0][1]
        tagrequest = urllib2.Request(searchtagurl)
        tagrequest.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36')
        tagresponse = urllib2.urlopen(tagrequest)
        taghtml = tagresponse.read()
#         print html
        tagdetailre = re.findall(r'title="标签为(\S*?)的歌曲">' ,taghtml,re.S)
        
        if(tagdetailre == []):
            return {"status":"-2","message":"no tags"}
        else:
            return {"status":"1","message":"ok","tags":tagdetailre}
            


if __name__ == '__main__':
#     search(u'好久不见',u'陈奕迅')    
    search(u'People Need Love',u'ABBA')
    
    