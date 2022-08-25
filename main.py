from youtube_transcript_api import YouTubeTranscriptApi as yta


vid_id = '5k521GcBOYw'


data = yta.get_transcript(vid_id)



transcript = ''

for value in data:
    for key,val in value.items():
        if key == 'text':
            transcript += val

l = transcript.splitlines()
final_Trans = "  ".join(l)
data = final_Trans
file = open("file.txt","w+")
file.write(data)
file.close()