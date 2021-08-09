# T_2j_W1o6-vmrF7-OZsTkIPZ
# 352549064261-8osctpjbslo9i39frc3lk0hkk42rhl37.apps.googleusercontent.com


from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


api_key = 'AIzaSyDe0E6HjIBN5FM0Fs8hRclhSj9nTPsTJnQ'

youtube1 = build('youtube','v3', developerKey=api_key)

print(type(youtube1))


CLIENT_SECRET_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']


flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
credentials = flow.run_console()
youtube = build('youtube', 'v3', credentials=credentials)

# youtube.videos().rate(rating='like', id='bf75hYrWSCw').execute()

video_id =  'DJ33HAo7crk'
video_id2 = '-kMrpdMSrck'

channel_id = 'UCC3ld44jBPgWuyiE4PRdSTw'

comment_string1 = '  great  mann!!  USDT(BEP20)  Address :  0x48c255fe7194467a3c6145affd268c70652b1423 '
comment_string2 = ' bang on bro ..keep it up!! USDT(BEP20) Deposit Addresss :  0x48c255fe7194467a3c6145affd268c70652b1423 '
comment_string3 = 'we want more videos like thisss !! USDT(BEP20) Deposit Address :  0x48c255fe7194467a3c6145affd268c70652b1423 '
comment_string4 = ' great pajjiiiii !  USDT(BEP20)  Address :  0x48c255fe7194467a3c6145affd268c70652b1423 '
comment_string5 = ' doing really great !!  USDT(BEP20) Deposit Address :  0x48c255fe7194467a3c6145affd268c70652b1423 '



def insert_comment(youtube, channel_id, video_id, text):

    print('inside func')

    insert_result = youtube.commentThreads().insert(
        part="snippet",
        body=dict(
            snippet=dict(
                channelId=channel_id,
                videoId=video_id,
                topLevelComment=dict(
                    snippet=dict(
                        textOriginal=text)
                )
            )
        )
    ).execute()

    comment = insert_result["snippet"]["topLevelComment"]
    author = comment["snippet"]["authorDisplayName"]
    text = comment["snippet"]["textDisplay"]
    print("Inserted comment for %s: %s" % (author, text))


print('going in')

for i in range(10):
    insert_comment(youtube, channel_id, video_id , comment_string1)
    insert_comment(youtube, channel_id, video_id2 , comment_string1)


for i in range(10):
    insert_comment(youtube, channel_id, video_id , comment_string2)
    insert_comment(youtube, channel_id, video_id2 , comment_string2)


for i in range(10):
    insert_comment(youtube, channel_id, video_id , comment_string3)
    insert_comment(youtube, channel_id, video_id2 , comment_string3)


for i in range(10):
    insert_comment(youtube, channel_id, video_id , comment_string4)
    insert_comment(youtube, channel_id, video_id2 , comment_string4)


for i in range(10):
    insert_comment(youtube, channel_id, video_id , comment_string5)
    insert_comment(youtube, channel_id, video_id2 , comment_string5)





def list_comment(youtube, channel_id, video_id):

    print('inside list comment func')

    insert_result = youtube.commentThreads().list(
        part="snippet",
        videoId = video_id,
        textFormat="html"
        
    ).execute()


    # print(insert_result)
    print('done listing')
    return insert_result


print('going in list')
comments_results = list_comment(youtube, channel_id, video_id )


def Extractcomments(result):

    resultList=[]
    for ele in result['items']:

        var = dict(
            comment =  ele['snippet']['topLevelComment']['snippet']['textDisplay'],
            authorName = ele['snippet']['topLevelComment']['snippet']['authorDisplayName'],
            authorProfileImageUrl = ele['snippet']['topLevelComment']['snippet']['authorProfileImageUrl'],
            likeCount = ele['snippet']['topLevelComment']['snippet']['likeCount'],
            publishedAt = ele['snippet']['topLevelComment']['snippet']['publishedAt'],
            updatedAt = ele['snippet']['topLevelComment']['snippet']['updatedAt']
            )

        resultList.append(var)

    print(resultList)
    for ele in resultList:
        
        s="Comment : {} \t authorName : {} \t likeCounts : {} \t publishedAt : {} \t updatedAt : {} \t authorProfileImageUrl : {} "
        print(s.format(ele['comment'], ele['authorName'], ele['likeCount'], ele['publishedAt'],ele['updatedAt'], ele['authorProfileImageUrl'] ))
        print()

Extractcomments(comments_results)


