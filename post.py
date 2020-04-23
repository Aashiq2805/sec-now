from github import Github
import tweepy
import time
import csv


#github access token being defined here
ACCESS_TOKEN = "bb0a9604734003c2d96515a40f4428958c29c814"
#twitter consumer tokens being defined here
auth = tweepy.OAuthHandler("IUK4LzRRBjNZSPse0Yrh0ASzs", "R7wgP61StMDNKtSN71hWTj7ROjIa15m8643bfm9Cy8XsUG6BSR")
#twitter access tokens being defined here
auth.set_access_token("1226323598144458754-gAWJFxK7fzoioaPomxaUS7PemHhDIl", "MtMZOPHtFyTmAu14zwRRrgJNUZx8gDZUuItwXIz8VFMHv")
#twitter api call being set here
api = tweepy.API(auth)
          
#github api call being set here
          
g = Github("LucyAnnaTwitter", "Lucy@github123")

def get_keywords():
    keywords = str(input('Enter terms to search : '))
    keywords = [keyword.strip() for keyword in keywords.split(',')]
    return keywords

def search_github(keywords):
    query = '+'.join(keywords) + '+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')
    #print_data(result)
    return result
    
def post(url_list):
    for repo in url_list:
        a= check(repo.clone_url) 
        a=0
        if(a==0):
          with open("tweeted.csv","w") as csv_file:
            writer=csv.writer(csv_file)
            writer.writerow([repo.clone_url])
          api.update_status(repo.clone_url)
          wait()
        else:
          continue
        
def check(url):
    with open("tweeted.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        for lines in csv_reader:
            if url in lines:
                #csv_reader.close()
                return 1
              
            else:
                #csv_reader.close()
                return 0
                        
def wait():
    time.sleep(86400)

def print_data(result):
    for repo in result:
        print(repo.clone_url, repo.stargazers_count)

def main():
    keywords= get_keywords()
    result=search_github(keywords)
    #print(result)
    post(result)
    
if __name__ == '__main__':
    main()

    
#for reference
#print(repo.clone_url,repo.stargazers_count)
