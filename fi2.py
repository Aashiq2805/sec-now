from twitter import Twitter, OAuth, TwitterHTTPError


OAUTH_TOKEN = '1262017120717533185-HpXoDfrrKSuCCiInVaXXdnI6hNm1Ia'
OAUTH_SECRET = '6vJSvudVE3kBqZvWr6FiKllWuJzWIGXSHpP6vZURC0ulE'
CONSUMER_KEY = 'HPdeLBBAhcaGuCcN6MKd5fwk6'
CONSUMER_SECRET = 'BzQgSPProiCApnkeuB7dMsRMcOqFgE3xXsDNLnsl1qxsIBJk5s'

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET, CONSUMER_KEY, CONSUMER_SECRET))


def search_tweets(q, count=100, max_id=None):
    return t.search.tweets(q=q, result_type='recent', count=count, lang="en", max_id=max_id)


def favorites_create(tweet):
    try:
        result = t.favorites.create(_id=tweet['id'])
        print("Favorited: %s, %s" % (result['text'], result['id']))
        return result
    except TwitterHTTPError as e:
        print("Error: ", e)
        return None


def search_and_fav(q, count=100, max_id=None):
    result = search_tweets(q, count, max_id)
    first_id = result['statuses'][0]['id']
    last_id = result['statuses'][-1]['id']
    success = 0
    for t in result['statuses']:
        if favorites_create(t) is not None:
            success += 1
def main():
	search_and_fav("infosec", 1000)
    

if __name__ == '__main__':
    main()
