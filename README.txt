hey,

above is the python file to search for trending repositories through github based on the topic of your preference and post it to twitter

written in python3 it needs two packages to run successfully

these packages are:
1. tweepy
2. PyGithub

to install them :

pip install PyGithub
pip install tweepy

post this we can run the python application to see the output in Lucy's twitter page

As seen there are multiple files in this project:

post = the main file that posts trending repos from github to twitter

get_number_of_followers_of_followers = is a file that gets all the followers of those who follow you. Ex if a follows you and b and c follow a, this script prints b and c

get_follower_data= gets data of followers that follow you such as when was their account created, age range etc. Note:this is a work in progress and features to be added

follower_increrase = is a script that increases the number of followers you have by following all the followers of youe followers. Ex if a follows you and b and c follow a, now you will follow a, b and c increasing the chance they follow you back 

twitter_worldwide_trending_hashtags = is a file that processes worldwide trends for hashtags across twitter giving us a comprehensive view of what is trending on twitter live
