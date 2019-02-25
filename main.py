from pytrends import TrendRQ
import time as t

tim = 0

# connecting to Google
pytrends = TrendRQ(hl='en_us', tz=360)

# keywords of the video(s)
# add more video arrays if needed: videoX = [insert 3 keywords] then append to videos array
video1 = ["Hello", "Mac", "Apple"]
video2 = ["Samsung", "Galaxy", "Review"]
video3 = ["Windows", "Linux", "OS"]

videos = [video1, video2, video3]


# checks if any of thw keywords given by the user are trending on Google
def checkTrend():
    while True:
        trend = pytrends.trending_searches(pn='p1')
        tim = t.clock()
        for i in videos:
            for x in videos[i]:
                if(trend == x):
                    upload(videos[i])
        return(tim)


def upload(vid):
    def APIUpload(vid):
        # add code from google youtube API to upload a video
        
        return

    def seleniumUpload(vid):
        # or use selenium to interact with the browser and upload to youtube.
        import selenium.webdriver.firefox
        sel = selenium.webdriver.Firefox()
        sel.start_client()
        sel.get("www.youtube.com")
        return

    choice = int(input("If you have a Google Youtube API key click 1 to use it to upload your video, else click 2 /n to use selenium when you have signed in on chrome: "))
    if(choice == 1):
        APIUpload(vid)
    elif(choice == 2):
        seleniumUpload(vid)
    # print(vid)


# runs the code
while True:
    checkTrend()
    # checks if it has been 1 since the previous request
    ntim = t.clock()
    if(ntim >= (tim + 1)):
        checkTrend()

# __________________________________________________________________________________________________
