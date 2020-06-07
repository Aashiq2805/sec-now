from github import Github
import tweepy
import time
import csv


#github access token being defined here
ACCESS_TOKEN = "c475c65850b66ea764cf09d56e6b670962961c95"
#twitter consumer tokens being defined here
auth = tweepy.OAuthHandler("HPdeLBBAhcaGuCcN6MKd5fwk6", "BzQgSPProiCApnkeuB7dMsRMcOqFgE3xXsDNLnsl1qxsIBJk5s")
#twitter access tokens being defined here
auth.set_access_token("1262017120717533185-HpXoDfrrKSuCCiInVaXXdnI6hNm1Ia", "6vJSvudVE3kBqZvWr6FiKllWuJzWIGXSHpP6vZURC0ulE")
#twitter api call being set here
api = tweepy.API(auth)
          
#github api call being set here
#g = Github(ACCESS_TOKEN)         
g = Github("Aashiq-burn", "Amma@2805")

def get_keywords():
    keywords = str(input('Enter terms to search : '))
    keywords = [keyword.strip() for keyword in keywords.split(',')]
    return keywords

def search_github(keywords):
    query = '+'.join(keywords) + '+in:readme+in:description'
    result = g.search_repositories(query, 'stars', 'desc')
    print_data(result)
    return result
    
def post(url_list):
    for repo in url_list:
        a= check(repo.clone_url) 
        if(a==0):
          with open("tweeted.csv","a") as csv_file:
            writer=csv.writer(csv_file)
            writer.writerow([repo.clone_url])
          api.update_status("The trending repository for the day is: "+repo.name+"! With "+str(repo.stargazers_count)+" stars, check it out below!"+repo.clone_url)
          wait()
        else:
          continue
        
def check(url):
    
    with open('tweeted.csv', 'rt') as f:
     reader = csv.reader(f, delimiter=',') 
     for row in reader:
          for field in row:
              if field == url:
                  print(url, "is in file", field)
                  return 1
              else:
                  print(url, "not in file", field)
                  continue
    return 0            
def wait():
    time.sleep(86400)

def print_data(result):
    for repo in result:
        print(repo.clone_url, repo.stargazers_count)

def main():
    #keywords= get_keywords()
    keywords="hacking" # for sake of supervisord we are running hardcoded input, can run prompt if needed
    keywords = [keyword.strip() for keyword in keywords.split(',')]    
    result=search_github(keywords)
    #print(result)
    post(result)
    
if __name__ == '__main__':
    main()

    
#for reference
#print(repo.clone_url,repo.stargazers_count)
