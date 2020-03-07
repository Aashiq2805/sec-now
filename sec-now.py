from github import Github
import tweepy
import time


#github access token being defined here
ACCESS_TOKEN = '3c483466b20325641643dcada3aad4c6528ca24c'
#twitter consumer tokens being defined here
auth = tweepy.OAuthHandler("IUK4LzRRBjNZSPse0Yrh0ASzs", "R7wgP61StMDNKtSN71hWTj7ROjIa15m8643bfm9Cy8XsUG6BSR")
#twitter access tokens being defined here
auth.set_access_token("1226323598144458754-gAWJFxK7fzoioaPomxaUS7PemHhDIl", "MtMZOPHtFyTmAu14zwRRrgJNUZx8gDZUuItwXIz8VFMHv")
#twitter api call being set here
api = tweepy.API(auth)
#github api call being set here
g = Github(ACCESS_TOKEN)

#function to search github
def search_github(keywords):
    query = '+'.join(keywords) + '+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')

    for repo in result:
        #posting a tweet of security project over to twitter 
        api.update_status(repo.clone_url)

        #..........................................................................................................
        #below i have commented a line to print all repos gathered. used this when the 3 steps were separate code .
        #Now integerated it and the below line can be used for debugging                                          .
        #print(repo.clone_url)                                                                                    .                                                                                    
        #..........................................................................................................
        
        #sleeping for 6 hours before posting again
        #time.sleep(21600)

if __name__ == '__main__':
    keywords = str(input('Enter terms to search in quotes: '))
    keywords = [keyword.strip() for keyword in keywords.split(',')]
    search_github(keywords)
