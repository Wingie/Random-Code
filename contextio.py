from contextIO.ContextIO import ContextIO
from collections import Counter
from youtube import *

import re
def striphtml(data):
    p = re.compile(r'<.*?>')#remove html
    data =  p.sub('', data)
    data.replace(u'\n','')
    return data# .replace("\r\n","") #and them pesky \r\n chars

def remove_tiny_words(text):
    return [i for i in text if len(i) > 4]

api_key = '8evz2620'
api_secret = '9ZjSzJbErY8LCdJG'
mailbox_to_query = 'wingston.sharon@gmail.com'


import argparse
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Python context.io wrapper")
    parser.add_argument('--email_ids', dest='email_ids', type=str, default=None, help='cmail ids seperate by comma ( , )')
    parser.add_argument('--limit', dest='limit', type=int, default=3, help='if case it takes too long a low number here will limit the numer of emails asked for.')
    args = parser.parse_args()
    api_client = ContextIO(api_key=api_key,
                                     api_secret=api_secret)
    email_ids = args.email_ids
    msg_ids = api_client.contactmessages(email_ids,account=mailbox_to_query,limit=args.limit).get_data() # add limit=10 iyw
    msgs =  [striphtml(api_client.messagetext(account=mailbox_to_query,message_id=msg[u'emailMessageId']).get_data()[0]['content']) for msg in msg_ids]
    print len(msgs)
    url_list = set()
    words = []
    for mail in msgs:
        for x in re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', mail):
            #v[0][v[0].find('.')+1:]
            if x.find('[') or x.find('>'):
                x=x.split('[')[0]
            url_list.add(x) 
    url_list = [ a for a in url_list if 'youtube' in a]

    print "*** List of URLS detected****"
    print url_list
    for url in url_list:
        print "--------start for " + url + "------------------------------"
        getmore(url.split('=')[1])
        print '***------------------***'


