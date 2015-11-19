##Author: AE

#New research question: To what extent did main stream news media pick up on the recent Spooky Action at a Distance result?
#How many sentences, among the sources that mediacloud pulls from, include the three main terms together (spooky, action, distance)?
#Time frame given is all time (currently less than 1 month) past the publication date in Nature (Oct 21st 2015).

import mediacloud, datetime, logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('debug.log')
handler.setLevel(logging.DEBUG)

logger.addHandler(handler)


def call_media_cloud() :
	API_File = open('MC_ApiKey.txt','r')
	API_KEY = API_File.read()
	logger.debug('API key read')

	mc = mediacloud.api.MediaCloud(API_KEY)
	logger.debug('media cloud object created')

	res = mc.sentenceCount('(spooky AND action AND distance)', solr_filter=[mc.publish_date_query( datetime.date( 2015, 10, 20), datetime.date( 2015, 11, 18) ), 'media_sets_id:1' ])
	logger.debug('Got result: ',res)
	return res


res = call_media_cloud();
print "Count of (spooky AND action AND distance) occurences:", res['count'] #prints count of sentences that reference (spooky, action, distance)

    
#ran successfully. Count of (spooky AND action AND distance) occurences: 24

