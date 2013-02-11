import gdata.youtube
import gdata.youtube.service
yt_service = gdata.youtube.service.YouTubeService()

def PrintVideoFeed(feed):
  for entry in feed.entry:
    PrintEntryDetails(entry)
def PrintEntryDetails(entry):
  print 'Video title: %s' % entry.media.title.text
  print 'Video published on: %s ' % entry.published.text
  print 'Video description: %s' % entry.media.description.text
  print 'Video category: %s' % entry.media.category[0].text
  print 'Video tags: %s' % entry.media.keywords.text
  print 'Video watch page: %s' % entry.media.player.url
  print 'Video flash player URL: %s' % entry.GetSwfUrl()
  print 'Video duration: %s' % entry.media.duration.seconds

def SearchAndPrintVideosByKeywords(list_of_search_terms):
  yt_service = gdata.youtube.service.YouTubeService()
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.orderby = 'viewCount'
  query.racy = 'include'
  for search_term in list_of_search_terms:
    new_term = search_term.lower()
    query.categories.append('/%s' % new_term)
  feed = yt_service.YouTubeQuery(query)
  PrintVideoFeed(feed)

def getmore(vid_id):
  entry = yt_service.GetYouTubeVideoEntry(video_id=vid_id)
  cat = [ x.text for x in entry.media.category]
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.orderby = 'viewCount'
  for search_term in cat:
    new_term = search_term.lower()
    query.categories.append('%s' % new_term)
    feed = yt_service.YouTubeQuery(query)

  for entry in feed.entry:
    print 'Video title: %s' % entry.media.title.text
    print 'Video flash player URL: %s' % entry.GetSwfUrl()

import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="youtube similar videos from url")
    parser.add_argument('--url', dest='url', type=str, default=None, help='cmail ids seperate by comma ( , )')
    args = parser.parse_args()
    vid_id = args.url.split('=')[1]

    entry = yt_service.GetYouTubeVideoEntry(video_id=vid_id)
    cat = [ x.text for x in entry.media.category]
    query = gdata.youtube.service.YouTubeVideoQuery()
    
    for search_term in cat:
        new_term = search_term.lower()
        query.categories.append('%s' % new_term)
    feed = yt_service.YouTubeQuery(query)

    for entry in feed.entry:
        print 'Video title: %s' % entry.media.title.text
        print 'Video flash player URL: %s' % entry.GetSwfUrl()