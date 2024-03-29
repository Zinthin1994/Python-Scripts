import praw,requests,re,time,sys,urllib.request,random,os

user_agent = ('redditmemebot by memeredditbot')


r = praw.Reddit(client_id = 'ZGNWR3s3yCdm5A', client_secret = 'IPzc0ClOPRd88rHgL0RwCKmTUFE', user_agent = user_agent)
subreddit = r.subreddit('meme')
submissions = subreddit.top("hour", limit = 1)

ext = ("JPEG", "jpg", "jpeg", "png", "PNG", "JPG")

for submission in submissions:
    print(submission.url)
    if (submission.url).endswith(ext):
         os.chdir("/var/www/zacharyalbright.com/Meme_Folder/")
         #urllib.request.urlretrieve(submission.url,str((random.randint(1,100000))))
         urllib.request.urlretrieve(submission.url,"a")
         
         print(submission.url)
#cache is not used, but maybe it can be used to store a counter value
sys.exit(0)