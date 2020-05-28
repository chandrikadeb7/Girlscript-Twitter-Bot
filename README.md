<h1 align="center">GirlScript Twitter Bot</h1>

<div align= "center">
  <h4>A Twitter Bot that automatically retweets, favourites the tweets with hashtag <code>#girlscript</code></h4>
</div>


## Follow on Twitter - Click [Girlscript Bot](https://twitter.com/girlscript_bot)

### :star: Star us on GitHub — it helps!


<p align="center"><img src="https://github.com/chandrikadeb7/Girlscript-Twitter-Bot/blob/master/Readme%20images/Screen%20Shot%202020-05-28%20at%2011.05.52%20AM.png"></p>

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/chandrikadeb7/Girlscript-Twitter-Bot/issues)
[![Forks](https://img.shields.io/github/forks/chandrikadeb7/Girlscript-Twitter-Bot.svg?logo=github)](https://github.com/chandrikadeb7/Girlscript-Twitter-Bot/network/members)
[![Stargazers](https://img.shields.io/github/stars/chandrikadeb7/Girlscript-Twitter-Bot.svg?logo=github)](https://github.com/chandrikadeb7/Girlscript-Twitter-Bot/stargazers)
[![Issues](https://img.shields.io/github/issues/chandrikadeb7/Girlscript-Twitter-Bot.svg?logo=github)](https://github.com/chandrikadeb7/Girlscript-Twitter-Bot/issues)
[![MIT License](https://img.shields.io/github/license/chandrikadeb7/Girlscript-Twitter-Bot.svg?style=flat-square)](https://github.com/chandrikadeb7/Girlscript-Twitter-Bot/blob/master/LICENSE)
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555)](https://www.linkedin.com/in/chandrika-deb/)

## 🚀&nbsp; Installation

#### Clone the repo
```
$ git clone https://github.com/chandrikadeb7/Girlscript-Twitter-Bot.git
```

#### Install tweepy Python module
```
$ pip install tweepy
```
## :bulb: Working

### Sign up for a Twitter Developer Account
* Create a separate Twitter account for your bot.
* Sign up for Twitter Developer Account from this site - [Apply for a Twitter Developer Account](https://developer.twitter.com/en/apply-for-access)
* Enter the necessary fields and await for email confirmation.
* Click on [Create an app](https://developer.twitter.com/en/apps)
* Enter the details and keep safe the access tokens generated.


#### Enter your generated access tokens and consumer keys in the file <code>credentials.py</code>

```
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
```
#### Edit the retweet and other details in the file <code>config.py</code>

```
# This is hastag which Twitter bot will search and retweet. You can edit this with any hastag .For example : '#javascript'
QUERY = '#anything'

# Twitter bot setting for liking Tweets
LIKE = True 

# Twitter bot setting for following user who tweeted
FOLLOW = True

# Twitter bot sleep time settings in seconds. For example SLEEP_TIME = 300 means 5 minutes.
# you can decrease it or increase it as you like.Please,use large delay if you are running bot all the time  so that your account does not get banned.

SLEEP_TIME = 300
```

## :key: Deployment

* Sign up for a free account in [Heroku](heroku.com)
* Click on New -> Create new app
* Enter the app-name in lower case and select your nearest region.
* Choose Heroku CLI for deployment. Follow the steps given in Deploy tab.
* Once the build is successful enable the Free Dynos option from Overview tab.

## :clap: And it's done!
Feel free to **file a new issue** with a respective title and description on the the [Girlscript-Twitter-Bot](https://github.com/chandrikadeb7/Girlscript-Twitter-Bot/issues) repository. If you already found a solution to your problem, **I would love to review your pull request**! 


## 📘&nbsp; License
The Girlscript Twitter Bot is released under the under terms of the [MIT License](LICENSE).

## :heart: Contributor
Made by [Chandrika Deb](https://github.com/chandrikadeb7)
