# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 10:59:51 2015

@author: dheepan.ramanan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 16:42:41 2015

@author: dheepan.ramanan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 12:58:12 2015

@author: dheepan.ramanan
"""

from bs4 import BeautifulSoup as bsoup
import requests as rq
import re
import pandas as pd
import time

urls = ['/event/ev0000003/2015',
 u'/event/ev0000003/2014',
 u'/event/ev0000003/2013',
 u'/event/ev0000003/2012',
 u'/event/ev0000003/2011',
 u'/event/ev0000003/2010',
 u'/event/ev0000003/2009',
 u'/event/ev0000003/2008',
 u'/event/ev0000003/2007',
 u'/event/ev0000003/2006',
 u'/event/ev0000003/2005',
 u'/event/ev0000003/2004',
 u'/event/ev0000003/2003',
 u'/event/ev0000003/2002',
 u'/event/ev0000003/2001',
 u'/event/ev0000003/2000']
	
movies = [[u'Beasts of No Nation',
  u'http://www.imdb.com/title/tt1365050/',
  2016,
  'potential nominee'],
 ['Black Mass','http://www.imdb.com/title/tt1355683/',2016,'potential nominee'],
 [u'Bridge of Spies',
  u'http://www.imdb.com/title/tt3682448/',
  2016,
  'potential nominee'],
 [u'Brooklyn',
  u'http://www.imdb.com/title/tt2381111/',
  2016,
  'potential nominee'],
 [u'Carol',
  u'http://www.imdb.com/title/tt2402927/',
  2016,
  'potential nominee'],
 [u'Creed',
  u'http://www.imdb.com/title/tt3076658/',
  2016,
  'potential nominee'],
 ['Concussion','http://www.imdb.com/title/tt3322364/',2016,'potential nominee'],
 ['Far From The Madding Crowd','http://www.imdb.com/title/tt2935476/',2016,'potential nominee'],
 ['In The Heart Of The Sea','http://www.imdb.com/title/tt1390411/',2016,'potential nominee'],
 [u'Inside Out',
  u'http://www.imdb.com/title/tt2096673/',
  2016,
  'potential nominee'],
 ['Joy','http://www.imdb.com/title/tt2446980/',2016,'potenial nominee'],
 [u'Room', u'http://www.imdb.com/title/tt3170832/', 2016, 'potential nominee'],
 [u'Sicario',
  u'http://www.imdb.com/title/tt3397884/',
  2016,
  'potential nominee'],
 [u'The Big Short',
  u'http://www.imdb.com/title/tt1596363/',
  2016,
  'potential nominee'],
 [u'The Martian',
  u'http://www.imdb.com/title/tt3659388/',
  2016,
  'potential nominee'],
 ['Son of Saul','http://www.imdb.com/title/tt3808342/',2016,'potential nominee'],
 ['Star Wars: The Force Awakens','http://www.imdb.com/title/tt2488496/',2016,'potential nominees'],
 ['Spotlight','http://www.imdb.com/title/tt1895587/',2016,'potential nominee'],
 ['The Big Short','http://www.imdb.com/title/tt1596363/',2016,'potential nominee'],
 ['The Revenant','http://www.imdb.com/title/tt1663202/',2016,'potential nominee'],
 ['The Danish Girl','http://www.imdb.com/title/tt0810819/',2016,'potential nominee'],
 ['Trumbo','http://www.imdb.com/title/tt3203606/',2016,'potential nominee'],
 ['Truth','http://www.imdb.com/title/tt3859076/',2016,'potential nominee'],
 ['Suffragette','http://www.imdb.com/title/tt3077214/',2016,'potential nominee'],
 ['The Revenant','http://www.imdb.com/title/tt1663202/',2016,'potential nominee'],
 [u'Straight Outta Compton',
  u'http://www.imdb.com/title/tt1398426/',
  2016,
  'potential nominee'],
 [u'Mad Max: Fury Road',
  u'http://www.imdb.com/title/tt1392190/',
  2016,
  'potential nominee'],
 [u'Tangerine',
  u'http://www.imdb.com/title/tt3824458/',
  2016,
  'potential nominee']]	
 
def rottenT(movie):
    try:
       r =  rq.get('http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=bygj3ygu2cq4jtteu9zkmgwb&q='+str(movie)) #apicall to rotten tomatoes
       moviedata = r.json()
    except Exception:
        print "invalid title"
    try:       
       title = moviedata['movies'][0]['title']
       theaterdate = moviedata['movies'][0]['release_dates']['theater']
    except Exception:
        title = movie        
        theaterdate= ""
    try:
       dvddate = moviedata['movies'][0]['release_dates']['dvd']
    except Exception:
        dvddate = ""
    
    try:
       criticsscore = moviedata['movies'][0]['ratings']['critics_score']
       audiencescore= moviedata['movies'][0]['ratings']['audience_score']
      
    except Exception:
        criticsscore = ""
        audiencescore=""
        
    return title, criticsscore, audiencescore, theaterdate
        
def imdbscraper(url):
    data=[]
    r = rq.get('http://www.imdb.com/'+url)
    soup = bsoup(r.text, 'html.parser')
    year = int(url.split('/')[3]) #for some fancy math
    divtag = re.compile('al.*')
    movies = soup.findAll('blockquote')[1].findAll('div', attrs={'class': divtag})
    movielinks = [link.findAll('a')[1] for link in movies]
    movieinputs=[]
    for index, setlist in enumerate(movielinks):
        if index == 0:
            status = 'winner'
        else:
            status = 'nominee'
        movieurl = setlist['href']
        moviename = setlist.text
        movieinputs.append([movieurl, moviename, year,status])
    print movieinputs

    for movie in movieinputs:
            time.sleep(30)
            movielink = movie[0]
            movietitle = movie[1]
            oscaryear = movie[2]
            oscarstatus = movie[3]   
            print movietitle, movielink
            print rq.get('http://www.imdb.com'+movielink).url
            moviepage = bsoup(rq.get('http://www.imdb.com'+movielink).text, 'html.parser')
            reviewnumbers = int(moviepage.find('span', attrs={'itemprop':'reviewCount'}).text.replace(',','').replace('user',''))
            reviewagg = float(moviepage.find('div', attrs={'class':'imdbRating'}).span.text)
        
            try:
                genretext=[]
                genres = moviepage.find('div', attrs={'itemprop':'genre'}).findAll('a')
                for genre in genres:
                    genretext.append(genre.text)
                genretext=','.join(genretext)
            except Exception:
                genretext=''
            try:
                plotwordtext=[]
                plotwords= moviepage.find('div', attrs={'itemprop':'keywords'}).findAll('a')
                for plotword in plotwords[:-1]:
                    plotwordtext.append(plotword.text)
                plotwordtext= ','.join(plotwordtext)
            except Exception:
                plotwordtext=''

            try:
                boxoffice = float(moviepage.find('h4', text='Gross:').next.next.replace('$','').replace(',',''))
            except Exception:
                boxoffice=''
            moviestats = bsoup(rq.get('http://www.imdb.com'+movielink+'ratings').text, 'html.parser')
            total = re.search('\d*', moviestats.find('div', attrs={'id': 'tn15content'}).p.text)
            totalfloat = float(total.group(0))
            
            moviestatsdata = moviestats.find('div', attrs={'id': 'tn15content'}).findAll('tr')
            #stats ratings
            tens = float(moviestatsdata[1].td.next.next.text.replace('%',''))
            nines = float(moviestatsdata[2].td.next.next.text.replace('%',''))
            eights = float(moviestatsdata[3].td.next.next.text.replace('%',''))
            sevens = float(moviestatsdata[4].td.next.next.text.replace('%',''))
            sixes = float(moviestatsdata[5].td.next.next.text.replace('%',''))
            fives = float(moviestatsdata[6].td.next.next.text.replace('%',''))
            fours = float(moviestatsdata[7].td.next.next.text.replace('%',''))        
            threes = float(moviestatsdata[8].td.next.next.text.replace('%',''))                 
            twos = float(moviestatsdata[9].td.next.next.text.replace('%',''))
            ones = float(moviestatsdata[10].td.next.next.text.replace('%',''))        
            #gender stats
            maleper =  float(moviestatsdata[12].td.a.next.next.next.text)       
            femaleper = float(moviestatsdata[13].td.a.next.next.next.text)    
            #age stats
            under18 = float(moviestatsdata[14].td.a.next.next.next.text)
            thirty44 = float(moviestatsdata[17].td.a.next.next.next.text)
            over44 = float(moviestatsdata[20].td.a.next.next.next.text)
												
            RTdata = rottenT(movietitle)
            criticscore = RTdata[1]
            audiencescore = RTdata[2]
            releasedate = RTdata[3]
			
            try:
                director = moviepage.find('span', attrs={'itemprop':'director'})
                directorlink = director.a['href']
                directorname =  director.a.text
                directorpage = bsoup(rq.get('http://www.imdb.com'+directorlink).text, 'html.parser')
    												
            except Exception:
                director = moviepage.find('div', attrs={'itemprop':'director'})
                directorlink = director.a['href']
                directorname =  director.a.text
                directorpage = bsoup(rq.get('http://www.imdb.com'+directorlink).text, 'html.parser')

            try:
                directorage = year - int(directorpage.find('time').text.split(',')[1])
            except Exception:
                directorage = ''
                print 'BOOM! #1'

            directorsex = directorpage.find('div', attrs={'class':'inline'})
            if re.search(ur"he\s|He|his|His",directorsex.text):
                gender = 'male'
            elif re.search(ur"she|She|her|Her", directorsex.text):
                gender = 'female' 
            else:
                gender = ''
																				
            for i in range(0, reviewnumbers, 10):
                try:
                    movierequest = rq.get('http://www.imdb.com'+movielink+'reviews?start='+str(i))								
                    moviereviewspage = bsoup(movierequest.text, 'html.parser')
                    reviews = moviereviewspage.find('div', attrs={'id': 'tn15content'}).findAll('p')
                    print movietitle, i, 'success'
                    for review in reviews:
                        data.append([oscaryear,movietitle,releasedate,boxoffice,directorname,directorage,gender,oscarstatus, reviewagg,criticscore, audiencescore,totalfloat,maleper,femaleper,under18,thirty44,over44,ones,twos,threes,fours,fives,sixes,sevens,eights,nines,tens,review.text])
                except Exception:
                    time.sleep(60)
                    movierequest = rq.get('http://www.imdb.com'+movielink+'reviews?start='+str(i))
                    moviereviewspage = bsoup(movierequest.text, 'html.parser')
                    reviews = moviereviewspage.find('div', attrs={'id': 'tn15content'}).findAll('p')
                    print movietitle, i, 'paused-restart'
                    for review in reviews:
                        data.append([oscaryear,movietitle,releasedate,boxoffice,directorname,directorage,gender,oscarstatus, reviewagg,criticscore, audiencescore,totalfloat,maleper,femaleper,under18,thirty44,over44,ones,twos,threes,fours,fives,sixes,sevens,eights,nines,tens,review.text,plotwordtext,genretext])

                        
                                                                
    return pd.DataFrame(data,columns= ['year','movietitle','releasedate','boxoffice','director','directorage','directorgender','winner','reviewagg','criticscore','audiencescore','totalfloat','maleper','femaleper','under18','thirtyto44','over44','ones','twos','threes','fours','fives','sixes','sevens','eights','nines','tens','reviews','plotwordtext','genretext'])
				
def imdb2016(movies):
    data=[]
    for movie in movies:
            time.sleep(30)
            movielink = movie[1]
            movietitle = movie[0]
            oscaryear = movie[2]
            oscarstatus = movie[3]
									
            print movietitle, movielink
            print rq.get(movielink).url
            moviepage = bsoup(rq.get(movielink).text, 'html.parser')
            reviewnumbers = int(moviepage.find('span', attrs={'itemprop':'reviewCount'}).text.replace(',','').replace('user',''))
            reviewagg = float(moviepage.find('div', attrs={'class':'imdbRating'}).span.text)
            try:
                boxoffice = float(moviepage.find('h4', text='Gross:').next.next.replace('$','').replace(',',''))
                genres = moviepage.find('div', attrs={'itemprop':'genre'}).findAll('a')
                genrestext = [genre.text for genre in genres]
                genre1 = genrestext[0]
                genre2 = genrestext[1]
            except Exception:
                boxoffice=''
   
			
            moviestats = bsoup(rq.get(movielink+'ratings').text, 'html.parser')
            total = re.search('\d*', moviestats.find('div', attrs={'id': 'tn15content'}).p.text)
            totalfloat = float(total.group(0))
            
            moviestatsdata = moviestats.find('div', attrs={'id': 'tn15content'}).findAll('tr')
            #stats ratings
            tens = float(moviestatsdata[1].td.next.next.text.replace('%',''))
            nines = float(moviestatsdata[2].td.next.next.text.replace('%',''))
            eights = float(moviestatsdata[3].td.next.next.text.replace('%',''))
            sevens = float(moviestatsdata[4].td.next.next.text.replace('%',''))
            sixes = float(moviestatsdata[5].td.next.next.text.replace('%',''))
            fives = float(moviestatsdata[6].td.next.next.text.replace('%',''))
            fours = float(moviestatsdata[7].td.next.next.text.replace('%',''))        
            threes = float(moviestatsdata[8].td.next.next.text.replace('%',''))                 
            twos = float(moviestatsdata[9].td.next.next.text.replace('%',''))
            ones = float(moviestatsdata[10].td.next.next.text.replace('%',''))        
            #gender stats
            maleper =  float(moviestatsdata[12].td.a.next.next.next.text)       
            femaleper = float(moviestatsdata[13].td.a.next.next.next.text)    
            #age stats
            under18 = float(moviestatsdata[14].td.a.next.next.next.text)
            eighteen29 = float(moviestatsdata[17].td.a.next.next.next.text)
            thirty44 = float(moviestatsdata[20].td.a.next.next.next.text) 										
            over44 = float(moviestatsdata[23].td.a.next.next.next.text)
												
            RTdata = rottenT(movietitle)
            criticscore = RTdata[1]
            audiencescore = RTdata[2]
            releasedate = RTdata[3]
			
            try:
                director = moviepage.find('span', attrs={'itemprop':'director'})
                directorlink = director.a['href']
                directorname =  director.a.text
                directorpage = bsoup(rq.get('http://www.imdb.com'+directorlink).text, 'html.parser')
    												
            except Exception:
                director = moviepage.find('div', attrs={'itemprop':'director'})
                directorlink = director.a['href']
                directorname =  director.a.text
                directorpage = bsoup(rq.get('http://www.imdb.com'+directorlink).text, 'html.parser')

            try:
                directorage = oscaryear - int(directorpage.find('time').text.split(',')[1])
            except Exception:
                directorage = ''
                print 'BOOM! #1'

            directorsex = directorpage.find('div', attrs={'class':'inline'})
            if re.search(ur"he\s|He|his|His",directorsex.text):
                gender = 'male'
            elif re.search(ur"she|She|her|Her", directorsex.text):
                gender = 'female' 
            else:
                gender = ''
																				
            for i in range(0, reviewnumbers, 10):
                try:
                    movierequest = rq.get(movielink+'reviews?start='+str(i))								
                    moviereviewspage = bsoup(movierequest.text, 'html.parser')
                    reviews = moviereviewspage.find('div', attrs={'id': 'tn15content'}).findAll('p')
                    print movietitle, i, 'success'
                    for review in reviews:
                        data.append([oscaryear,movietitle,releasedate,boxoffice,directorname,directorage,gender,oscarstatus, reviewagg,criticscore, audiencescore,totalfloat,maleper,femaleper,under18,thirty44,over44,ones,twos,threes,fours,fives,sixes,sevens,eights,nines,tens,genre1, genre2,review.text])
                except Exception:
                    time.sleep(60)
                    movierequest = rq.get(movielink+'reviews?start='+str(i))
                    moviereviewspage = bsoup(movierequest.text, 'html.parser')
                    reviews = moviereviewspage.find('div', attrs={'id': 'tn15content'}).findAll('p')
                    print movietitle, i, 'paused-restart'
                    for review in reviews:
                        data.append([oscaryear,movietitle,releasedate,boxoffice,directorname,directorage,gender,oscarstatus, reviewagg,criticscore, audiencescore,totalfloat,maleper,femaleper,under18,eighteen29,thirty44,over44,ones,twos,threes,fours,fives,sixes,sevens,eights,nines,tens,genre1, genre2,review.text])

                        
                                                                
    return pd.DataFrame(data)
'''								
def main():
	newmovies = imdb2016(movies)
	return newmovies
		
if __name__ == '__main__':
	main()
	
'''    