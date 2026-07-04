playlist=[]
print(playlist)
playlist.extend(['Blinding Lights', 'Levitating', 'Stay'])
print(playlist)
playlist.insert(2,'Peaches')
print(playlist)
playlist.insert(0,playlist.pop(-1))
print(playlist)
for i in range(0,2):
    if 'Blinding Lights' in playlist[i]:
        playlist.remove('Blinding Lights')
    else:
        print("This song title is not in the playlist") 
print(playlist)
for i in range(0,len(playlist)):
    print(i+1,'.',playlist[i],end=" ")
