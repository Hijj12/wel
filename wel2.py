import amino
import requests
import time
try:
    import colorama
except ModuleNotFoundError:
    os.system("pip install colorama")
    import colorama
try:
    import pyfiglet
except ModuleNotFoundError:
    os.system("pip install pyfiglet")
    import pyfiglet

colorama.init()
print(colorama.Fore.GREEN)
print(colorama.Style.BRIGHT)
f = pyfiglet.Figlet(font='slant')
print (f.renderText('TECH'))
f = pyfiglet.Figlet(font='slant')
print (f.renderText('VISION'))
f = pyfiglet.Figlet(font='digital')
print (f.renderText('Welcome Bot'))
dec = '━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━' 
print("""
Youtube:
https://youtube.com/channel/UCPuZzOqlfpx_QTaC2yix7Pg

Discord Server:
https://discord.gg/YMfvAxm6zF
""")
print(dec)
email=input("Enter Email: ")
password=input("Enter Password: ")
client=amino.Client()
client.login(email=email,password=password)
print("logged in")
n=input("Community/chat link : ")
fok=client.get_from_code(n)
id=client.get_from_code(n).objectId
cid=fok.path[1:fok.path.index("/")]

msg="""Follow GC rules
1.Do not spam
2.Respect Leaders, curators, Host and Cohosts
3.Don't spread hate
4.Be polite in chatrooms"""

subclient=amino.SubClient(comId=cid,profile=client.profile)
chts=subclient.get_public_chat_threads(type="recommended", start=0, size=100).chatId
for chats in chts:
	try:
		subclient.join_chat(chatId=chats)
	except Exception:
		pass
print(dec)
print("\nJoined all Chatrooms")
@client.event("on_group_member_join")
def on_group_member_join(data):
	i=data.message.author.icon
	response=requests.get(f"{i}")
	file=open("profile.png","wb")
	file.write(response.content)
	file.close()
	img=open("profile.png","rb")
	subclient.send_message(chatId=data.message.chatId,message=f"""
[C]━━━━━━━━━━━━━━━
[c]Welcome <${data.message.author.nickname}$>
[C]━━━━━━━━━━━━━━━
{msg}
[C]━━━━━━━━━━━━━━━
""",embedId=data.message.author.userId,embedTitle=data.message.author.nickname,embedLink=f"ndc://x{cid}/user-profile/{data.message.author.userId}",embedImage=img,mentionUserIds=[data.message.author.userId])
print(dec)
print("\nWelcome Bot ready")
def socketRoot():
	j=0
	while True:
		if j>=300:
			print("Updating socket.......")
			client.close()
			client.start()
			print("Socket updated")
			j=0
		j=j+1
		time.sleep(1)
socketRoot()