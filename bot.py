import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import time
import random
import requests
import secrets
import os
import json
from bs4 import BeautifulSoup
import urllib.request
from uuid import uuid4
from datetime import datetime
from pydantic import BaseModel
import hmac
import hashlib
import urllib3
import urllib.parse
from urllib.parse import quote

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# MADE BY MARIOSKI <3
req = requests.session()
reportreq = requests.session()
uid = uuid4()
encoding = 'utf-8'
username = ''
password = ''
reportusername = ''
reportpassword = ''
name = ''

bottoken = "OTMzNzQzNTA5MjY0MDA3MjA5.Yel-aA.453gVZs6P6v_KAGY4K8xOcNAcXQ"

class UserInfo(BaseModel):
    username: str

class ReportUserInfo(BaseModel):
    reportusername: str


uwuuser = UserInfo
uwuusers = ReportUserInfo

logurl = 'https://i.instagram.com/api/v1/accounts/login/'
falogurl = 'https://i.instagram.com/api/v1/accounts/two_factor_login/'
edit_url = 'https://i.instagram.com/api/v1/accounts/edit_profile/'
nameurl = 'https://i.instagram.com/api/v1/accounts/set_phone_and_name/'

nonce = str(int(datetime.now().timestamp()))
uuid = str(uuid4())
uuid2 = str(uuid4())

DEVICE_SETS = {
    "app_version": "136.0.0.34.124",
    "android_version": "28",
    "android_release": "9.0",
    "dpi": "640dpi",
    "resolution": "1440x2560",
    "manufacturer": "samsung",
    "device": "SM-G965F",
    "model": "star2qltecs",
    "cpu": "samsungexynos9810",
    "version_code": "208061712",
}


USER_AGENT = 'Instagram {app_version} Android ({android_version}/{android_release}; {dpi}; {resolution}; ' \
             '{manufacturer}; {model}; armani; {cpu}; en_US)'.format(**DEVICE_SETS)

#deviceid = 'android-' + str({secrets.token_hex(8)})
deviceid = 'android-' + str(secrets.token_hex(8))

headers = {
    'Host': 'i.instagram.com',
    'X-Ig-App-Locale': 'en-US',
    'X-Ig-Device-Id': str(uuid2),
    'X-Ig-Family-Device-Id': str(uuid),
    'X-Ig-Android-Id': deviceid,
    'Priority': 'u=3',
    'User-Agent': USER_AGENT,
    'Accept-Language': 'en-US',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept-Encoding': 'gzip, deflate',
}


client = commands.Bot(command_prefix='!')

client.remove_command("help")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.ws.change_presence(activity = discord.Streaming(name = "by Marioski", url = "https://www.youtube.com/watch?v=nGkbsU9y1mk&ab_channel=TH1HOURCLIPS"))

@client.event
async def on_server_join(server):
    print("Joining {0}".format(server.name))


@client.command(pass_context=True)
async def help(ctx):
    member = ctx.message.author
    channel = ctx.message.channel

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Commands')
    embed.add_field(name='!login', value='Usedd !login to start (this acc will be used to copy) ', inline=False)
    embed.add_field(name='!t', value='Use !t "username" or !t username postcode ', inline=False)
    embed.add_field(name='!name', value='Use !name "name" to set a custom name ', inline=False)
    embed.add_field(name='!clean', value='Use !clean to remove everything on your profile ', inline=False)
    embed.add_field(name='!reportlogin', value='Use !reportlogin user pass to log into acc to report ', inline=False)
    embed.add_field(name='!report', value='Use !report "target" "verified" to report target for impersonating celeb verified ', inline=False)
    embed.add_field(name='Need more help?', value='Contact Marioski#0185', inline=False)
    await member.send(embed=embed)

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.add_field(name="Help command sent!", value="Check your DM <@" + str(member.id) + "> ...")

    await channel.send(embed=embed)

@client.command(pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await channel.trigger_typing()
    t2 = time.perf_counter()
    embed=discord.Embed(title=None, description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
    await channel.send(embed=embed)

@client.command(pass_context=True)
async def login(ctx, username, password):
    global log, loginJS
    global falog
    global coo
    global req
    global passwd
    
    uwuuser.username = username
    channel = ctx.message.channel

    print(username)
    print(password)

    def check(message):
        return message.author == message.author

    uwus = ctx.message.author

    nonce = str(int(datetime.now().timestamp()))
    uuid = str(uuid4())
    uuid2 = str(uuid4())

    DEVICE_SETS = {
        "app_version": "136.0.0.34.124",
        "android_version": "28",
        "android_release": "9.0",
        "dpi": "640dpi",
        "resolution": "1440x2560",
        "manufacturer": "samsung",
        "device": "SM-G965F",
        "model": "star2qltecs",
        "cpu": "samsungexynos9810",
        "version_code": "208061712",
    }
    
    IG_SIG_KEY = '4f8732eb9ba7d1c8e8897a75d6474d4eb3f5279137431b2aafb71fafe2abe178'
    SIG_KEY_VERSION = '4'

    USER_AGENT = 'Instagram {app_version} Android ({android_version}/{android_release}; {dpi}; {resolution}; ' \
                 '{manufacturer}; {model}; armani; {cpu}; en_US)'.format(**DEVICE_SETS)
    
    deviceid = 'android-' + str({secrets.token_hex(8)})

    headers = {
        'Host': 'i.instagram.com',
        'X-Ig-App-Locale': 'en-US',
        'X-Ig-Device-Id': str(uuid2),
        'X-Ig-Family-Device-Id': str(uuid),
        'X-Ig-Android-Id': deviceid,
        'Priority': 'u=3',
        'User-Agent': USER_AGENT,
        'Accept-Language': 'en-US',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
    }

    
    data = f'signed_body=SIGNATURE.%7B%22jazoest%22%3A%2222521%22%2C%22phone_id%22%3A%22{str(uuid)}%22%2C%22enc_password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{nonce}%3A{password}%22%2C%22username%22%3A%22{username}%22%2C%22guid%22%3A%22{uuid2}%22%2C%22device_id%22%3A%22{deviceid}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22login_attempt_count%22%3A%220%22%7D'
    log = req.post("https://i.instagram.com/api/v1/accounts/login/", headers=headers, data=data)
    loginJS = log.json()
    
    #print(loginJS)

    if 'logged_in_user' in log.text:
        coo = log.cookies
        embed=discord.Embed(title=None, description='Successfully Logged In! ✔ ', color=0x2ecc71)
        await channel.send(embed=embed)
        embed2=discord.Embed(title=None, description='Use command !t "username" to start!  ', color=0x2ecc71)
        await channel.send(embed=embed2)
    elif 'The password you entered is incorrect' in log.text:
        embed=discord.Embed(title="Error!", description='Password is incorrect! ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
    elif '"two_factor_required":true' in log.text:
        success = await login2FA(username, password, log.cookies['csrftoken'], loginJS['two_factor_info']['two_factor_identifier'], uuid, uuid2, deviceid, channel, uwus)
        if not success:
            embed=discord.Embed(title="Error!", description='2FA Detected, remove it an try again! ❌ ', color=0xe74c3c)
            await channel.send(embed=embed)
        else:
            embed=discord.Embed(title=None, description='Successfully Logged In! ✔ ', color=0x2ecc71)
            await channel.send(embed=embed)
            embed2=discord.Embed(title=None, description='Use command !t "username" to start!  ', color=0x2ecc71)
            await channel.send(embed=embed2)
    elif 'rate_limit_error' in log.text:
        print("Ratelimited! Please wait and try again! </3 ")
        embed=discord.Embed(title="Error!", description='Ratelimited! Please try again in a few minutes! ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
    elif 'challenge_required' in log.text:
        embed=discord.Embed(title="Error!", description='Challenge Required! ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
    else:
        print(log.text)
        embed=discord.Embed(title="Error!", description='Error Logging in! ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
        
    passwd = password
    
def generatesignature(data):
    parsed_data = urllib.parse.quote(data)

    return (
        'ig_sig_key_version=4' +
        '&signed_body=' + hmac.new(
            '012a54f51c49aa8c5c322416ab1410909add32c966bbaa0fe3dc58ac43fd7ede'.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest() +
        '.' + parsed_data)

async def login2FA(username, password, csrfToken, identifier, uuid, uuid2, deviceid, channel, uwus):
    global log, loginJS
    global coo
    global req

    embed=discord.Embed(title=None, description='Please input your 2fa code!:  ', color=0x2ecc71)
    await channel.send(embed=embed)
    
    two_factor_code = await client.wait_for('message', check=lambda message: message.author == uwus)
    
    print("2fa: " + str(two_factor_code.content))
    two_factor_code = two_factor_code.content
    
    data = f'signed_body=SIGNATURE.%7B%22verification_code%22%3A%22{two_factor_code}%22%2C%22phone_id%22%3A%22{str(uuid)}%22%2C%22two_factor_identifier%22%3A%22{identifier}%22%2C%22username%22%3A%22{username}%22%2C%22trust_this_device%22%3A%221%22%2C%22guid%22%3A%22{uuid2}%22%2C%22device_id%22%3A%22{deviceid}%22%2C%22verification_method%22%3A%223%22%7D'

    headers = {
        'Host': 'i.instagram.com',
        'X-Ig-App-Locale': 'en-US',
        'X-Ig-Device-Id': str(uuid2),
        'X-Ig-Family-Device-Id': str(uuid),
        'X-Ig-Android-Id': deviceid,
        'Priority': 'u=3',
        'User-Agent': USER_AGENT,
        'Accept-Language': 'en-US',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
    }

    log = requests.post(falogurl, headers=headers, data=data)

    if 'logged_in_user' in log.text:
        loginJS = log.json()
        print(loginJS)
        coo = log.cookies
        return True
    elif 'invalid' in log.text:
        embed=discord.Embed(title="Error!", description='Error! 2FA code incorrect ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
    elif 'rate_limit_error' in log.text:
        print("Ratelimited! Please wait and try again! </3 ")
        embed=discord.Embed(title="Error!", description='Ratelimited! Please try again in a few minutes! ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
    else:
        print(log.text)

    return False

@client.command(pass_context=True)
async def t(ctx, target, custompfp=None, multiple=None):
    global coo
    global uid
    global req
    global custompfplol
    global custompfplil
    global targetsID
    global deviceid

    channel = ctx.message.channel

    def check(message):
        return message.author == message.author
    
    headers2 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': USER_AGENT,
    }

    if custompfp:
        custompfpurl = "https://www.instagram.com/p/" + str(custompfp) + "/?__a=1"
        custompfplol = requests.get(custompfpurl, headers=headers2, cookies = coo)
        if custompfplol.status_code == 404:
            custompfp == False
            embed=discord.Embed(title="Error!", description='Error finding post! ❌ ', color=0xe74c3c)
            await channel.send(embed=embed)
            return
        if custompfplol.status_code == 200:
            countt = 0
            custompfp == True
            if 'edge_sidecar_to_children' in custompfplol.text:
                for i in custompfplol.json()['graphql']['shortcode_media']['edge_sidecar_to_children']['edges']:#['node']['display_url']:
                    countt += 1
                if not multiple:
                    
                    embed=discord.Embed(title="Select", description='Multiple images detected in post - Select 1/' + str(countt) + '✔', color=0xe74c3c)
                    await channel.send(embed=embed)
                    try:
                        multiple = await client.wait_for('message', check=check, timeout=60.0)
                        
                    except asyncio.TimeoutError:
                        embed=discord.Embed(title="Error!", description='Timeout! ❌ ', color=0xe74c3c)
                        return await channel.send(embed=embed)


                    multiple.content = int(multiple.content)
                    multiple.content -= 1
                    custompfplil2 = custompfplol.json()['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][multiple.content]
                    custompfplil = custompfplil2['node']['display_url']
                    
                if multiple:
                    multiple = int(multiple)
                    multiple -= 1
                    custompfplil2 = custompfplol.json()['graphql']['shortcode_media']['edge_sidecar_to_children']['edges'][multiple]
                    custompfplil = custompfplil2['node']['display_url']
                
            else:
                custompfplil = custompfplol.json()['graphql']['shortcode_media']['display_url']
        


    print("Target is: @ " + str(target))

    channel = ctx.message.channel
    try:
        csrftoken = coo["csrftoken"]
        dsuid = coo["ds_user_id"]
        #mid = coo["mid"]
        sessid = coo["sessionid"]
    except:
        embed=discord.Embed(title="Error!", description='Error! Please !login first ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
        print("> Error! User not logged in! -> do !login first ")
        return

    url2 = 'https://i.instagram.com/api/v1/accounts/current_user/?edit=true'


    response2 = requests.get(url2, headers=headers, cookies = coo)

    try:
        user_info = json.loads(response2.text)
    except json.decoder.JSONDecodeError:
        print("Error getting own info...")
        embed=discord.Embed(title="Error!", description='Error getting own info! ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
    
    my_name = str(user_info["user"]["full_name"])
    my_email = str(user_info["user"]["email"])
    my_username = str(user_info["user"]["username"])
    verifieduser = my_username
    targets = target
    my_phone_number = str(user_info["user"]["phone_number"])
    my_biography = str(user_info["user"]["biography"])
    my_website = str(user_info["user"]["external_url"])

    #GET OWN INFO DONE

    urlll = f'https://i.instagram.com/api/v1/fbsearch/topsearch_flat/?search_surface=top_search_page&timezone_offset=28800&count=15&query={target}&context=blended'
    response = requests.get(urlll, headers=headers, cookies = coo)
    
    if target not in response.text:
        embed=discord.Embed(title="Error!", description='Error Scraping user! ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
        print("Error scraping user")
        return
    
    for users in response.json()["list"]:
        try:
            if users["user"]["username"] == target:
                targetsID = users["user"]["pk"]
        except:
            pass

    urlsy = f"https://i.instagram.com/api/v1/users/{targetsID}/info/?entry_point=profile&from_module=blended_search"
    response = requests.get(urlsy, headers=headers, cookies = coo)
    csrftoken = response.cookies["csrftoken"]

    try:
        scraped = response.json()
    except json.decoder.JSONDecodeError:
        embed=discord.Embed(title="Error!", description='Error Scraping user! ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
        return

    if scraped == '':
        embed=discord.Embed(title="Error!", description='Error Scraping user! ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
        return

    bio = scraped["user"]["biography"]
    website = scraped["user"]["external_url"]
    
    if website is None:
       website = ""
       
    full_name = scraped["user"]["full_name"]
    full_name = full_name.encode().decode()
    profile_picture = scraped["user"]["hd_profile_pic_url_info"]["url"]
    try:
        if custompfp:
            with open("profilepic.jpg", 'wb') as f:
                resp = requests.get(str(custompfplil), verify=False)
                f.write(resp.content)
        else:
            with open("profilepic.jpg", 'wb') as f:
                resp = requests.get(str(profile_picture), verify=False)
                f.write(resp.content)
    except Exception as ff:
        print("Error: " + str(ff))

    namedata = {
        "first_name": str(full_name)
    }

    r2 = requests.post(nameurl, headers=headers, data=namedata, cookies=coo).status_code
    if r2 == 200:
        print(f"Name changed! ")
        await channel.send("Name Changed to: " + str(full_name))
    else:
        print(f"Error (Couldn't login to account input)")

    url_edit = "https://i.instagram.com/api/v1/accounts/edit_profile/"
    
    datas = 'SIGNATURE.{' + f'"primary_profile_link_type":"0","external_url":"{str(website)}","phone_number":"{str(my_phone_number)}","username":"{str(uwuuser.username)}","show_fb_link_on_profile":"false","first_name":"{str(full_name)}","device_id":"{str(deviceid)}","_uuid":"{str(uuid2)}","email":"{str(my_email)}"' + '}'
    datas = 'signed_body=' + urllib.parse.quote(datas)
    
    try:
        rf = req.post(url_edit, headers=headers, data=datas, cookies=coo, allow_redirects=False)
        if rf.status_code == 200:
            print("Website changed")
            await channel.send("Website Changed to: " + str(website))
        else:
            print(rf.text)
            embed=discord.Embed(title=None, description=f"Couldn't change website ❌ ", color=0xe74c3c)
            await channel.send(embed=embed)
            
    except Exception as e:
        print(e)
        embed=discord.Embed(title=None, description=f"Couldn't change website! ❌ ", color=0xe74c3c)
        await channel.send(embed=embed)

    
    try:
        bio_url = "https://i.instagram.com/api/v1/accounts/set_biography/"
        datas={'raw_text': bio}
        
        rf = req.post(bio_url, headers=headers, data=datas, cookies=coo, allow_redirects=False)
        if rf.status_code == 200:
            print("Bio Changed!")
            await channel.send("Bio Changed to: " + str(bio))
        elif "failed to mention" in rf.text:
            for i in rf.json()['non_mentionable_users']:
                bio = bio.replace(str(i['username']), " "+str(i['username']))
            
            datas={'raw_text': bio}
            
            rf = req.post(bio_url, headers=headers, data=datas, allow_redirects=False)
            if rf.status_code == 200:
                print("Bio Changed!")
                await channel.send("Bio Changed to: " + str(bio))
            else:
                print(rf.text)
                embed=discord.Embed(title=None, description=f"Couldn't change bio ❌ ", color=0xe74c3c)
                await channel.send(embed=embed)
        else:
            print(rf.text)
            embed=discord.Embed(title=None, description=f"Couldn't change bio ❌ ", color=0xe74c3c)
            await channel.send(embed=embed)
    except Exception as e:
        print(e)
        
    with open('profilepic.jpg', 'rb') as f: raw_data = f.read()
    
    uplod = f'{str(int(time.time()))}'
    nemz = f'{uplod}_0_-{str(random.randint(100000000, 999999999))}'
    imgurl = f'https://i.instagram.com/rupload_igphoto/{nemz}'
    
    header = {
        "Host": "i.instagram.com",
        "X-Entity-Length": str(len(raw_data)),
        "X-Entity-Name": nemz,
        "X-Instagram-Rupload-Params": r'''{"upload_id":"''' + uplod+ r'''","media_type":"1","image_compression":"{\"lib_name\":\"moz\",\"lib_version\":\"3.1.m\",\"quality\":\"70\"}"}''',
        "X-Entity-Type": "image/jpeg",
        "Offset": "0",
        "X-Ig-Connection-Type": "WIFI",
        "X-Ig-Capabilities": "3brTvwM=",
        "User-Agent": USER_AGENT,
        "Accept-Language": "en-US",
        "Content-Type": "application/octet-stream",
        "Content-Length": str(len(raw_data)),
        "Accept-Encoding": "gzip, deflate",
    }
    
    kek = req.post(imgurl, headers=header, data=raw_data, cookies = coo)
    
    kekz = req.post('https://i.instagram.com/api/v1/accounts/change_profile_picture/', headers={
        "X-Ig-Device-Id": str(uuid2),
        "X-Ig-Android-Id": deviceid,
        "X-Ig-Connection-Type": "WIFI",
        "X-Ig-Capabilities": "3brTvwM=",
        "User-Agent": USER_AGENT,
        "Accept-Language": "en-US",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        }, data=f'_csrftoken=missing&_uuid={uuid2}&use_fbuploader=true&upload_id={uplod}', cookies = coo)
    
    if kekz.status_code == 200:
        print("Profile picture changed!")
        if custompfp:
            await channel.send("Profile Picture Changed to: " + str(custompfplil))
        else:
            await channel.send("Profile Picture Changed to: " + str(profile_picture))
    else:
        print(kekz.text)
        embed=discord.Embed(title=None, description=f"Couldn't change pfp ❌ ", color=0xe74c3c)
        await channel.send(embed=embed)

    global reportcoo
    global reportreq
    global verifieduserID

    channel = ctx.message.channel
    
    try:
        checkReq = reportreq.get(f'https://instagram.com/{str(targets)}/?__a=1').json()
        targetsID = checkReq['logging_page_id'].split('_')[1]
        targetFbID = checkReq['graphql']['user']['fbid']
        print(f"{targets}'s UserID is {targetsID}")
        print(f"{targets}'s FBUserID is {targetFbID}")
    except Exception as e:
        print(e)
        embed=discord.Embed(title=None, description=f'Invalid Report Target @{targets} ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
        print(f'Invalid Report Target @{targets} </3 ')

    try:
        checkReq = reportreq.get(f'https://instagram.com/{str(verifieduser)}/?__a=1').json()
        verifieduserID = checkReq['logging_page_id'].split('_')[1]
        veriFbID = checkReq['graphql']['user']['fbid']
        print(f"{verifieduser}'s UserID is {verifieduserID}")
        print(f"{verifieduser}'s FBUserID is {veriFbID}")
    except Exception as e:
        print(e)
        embed=discord.Embed(title=None, description=f'Invalid Report Target @{verifieduser} ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
        print(f'Invalid Report Target @{verifieduser} </3 ')
    
    try:
        reportParams = f'%7B%22server_params%22%3A%7B%22is_bloks%22%3A1%2C%22profile_id%22%3A' + veriFbID + '%2C%22serialized_state%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22null%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_user_impersonation%5C%5C%5C%22%2C%5C%5C%5C%22ig_impersonation_celebrity%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22' + targetsID + '%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841442439280052%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A' + targetFbID + '%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_GB%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A0%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profile%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22195.0.0.31.123%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A567067343352427%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Afalse%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%2C%5C%5C%5C%22tag_source%5C%5C%5C%22%3A%5C%5C%5C%22tag_selection_screen%5C%5C%5C%22%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_profile_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profile%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22bloks%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22initial_screen_id%5C%5C%5C%5C%5C%5C%5C%22%3Anull%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22null%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D%7D'

        datas = f'params={reportParams}&_uuid={uid}&bk_client_context=%7B%22bloks_version%22%3A%22927f06374b80864ae6a0b04757048065714dc50ff15d2b8b3de8d0b6de961649%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=927f06374b80864ae6a0b04757048065714dc50ff15d2b8b3de8d0b6de961649'

        head = {
            "Host": "i.instagram.com",
            "User-Agent": USER_AGENT,
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Content-Length": f"{str(len(datas))}",
            "Accept-Encoding": "gzip, deflate",
        }
        
        reporturl = 'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_profile_selection_screen/'

        try:
            response = requests.post(reporturl, headers=head, data=datas, cookies = reportreq.cookies)
            print(response)
            if response.status_code == 200:
                print("Sent report")
                embed=discord.Embed(title=None, description=f'Successfully reported @{targets} ✔ ', color=0x2ecc71)
                await channel.send(embed=embed)
            else:
                print("Error")
        except Exception as e:
            print(e)
    except:
        embed=discord.Embed(title=None, description=f'No reporting acc... Please use command !reportlogin user pass ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)


@client.command(pass_context=True)
async def name(ctx, *, namep):
    global coo

    channel = ctx.message.channel

    
    namedata = {
        "first_name": str(namep)
    }

    r2 = requests.post(nameurl, headers=headers, data=namedata, cookies=coo).status_code
    if r2 == 200:
        print(f"Name changed! ")
        embed=discord.Embed(title=None, description='Name Changed to: ' + str(namep) + ' ✔ ', color=0x2ecc71)
        await channel.send(embed=embed)
    else:
        print(f"Error (Couldn't login to account input)")
        embed=discord.Embed(title=None, description=f'No account! Please do !login first <3 ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
        
@client.command(pass_context=True)
async def clean(ctx):
    global coo
    global uid
    global req

    try:
        csrftoken = coo["csrftoken"]
    except:
        embed=discord.Embed(title="Error!", description='Error! Please !login first ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
        print("> Error! User not logged in! -> do !login first ")
        return

    print("Cleaning profile...")

    channel = ctx.message.channel
    

    headers2 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0',
    }
    
    namedata = {
        "first_name": ""
    }

    r2 = requests.post(nameurl, headers=headers, data=namedata, cookies=coo).status_code
    if r2 == 200:
        print(f"Name cleared! ")
        embed=discord.Embed(title=None, description='Name cleared ✔ ', color=0x2ecc71)
        await channel.send(embed=embed)
    else:
        print(f"Error (Couldn't login to account input)")
        embed=discord.Embed(title=None, description=f'No account! Please do !login first <3 ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
        return

    url2 = 'https://i.instagram.com/api/v1/accounts/current_user/?edit=true'
    response2 = requests.get(url2, headers=headers, cookies = coo)
    try:
        user_info = json.loads(response2.text)
    except json.decoder.JSONDecodeError:
        print("Error getting own info...")
        embed=discord.Embed(title="Error!", description='Error getting own info! ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
    
    my_name = str(user_info["user"]["full_name"])
    my_email = str(user_info["user"]["email"])
    my_username = str(user_info["user"]["username"])
    my_phone_number = str(user_info["user"]["phone_number"])
    my_biography = str(user_info["user"]["biography"])
    my_website = str(user_info["user"]["external_url"])

    #GET OWN INFO DONE

    bio = ""
    website = ""
       
    full_name = my_name

    url_edit = "https://i.instagram.com/api/v1/accounts/edit_profile/"
    
    datas = 'SIGNATURE.{' + f'"primary_profile_link_type":"0","external_url":"{str(website)}","phone_number":"{str(my_phone_number)}","username":"{str(uwuuser.username)}","show_fb_link_on_profile":"false","first_name":"{str(full_name)}","device_id":"{str(deviceid)}","_uuid":"{str(uuid2)}","email":"{str(my_email)}"' + '}'
    datas = 'signed_body=' + urllib.parse.quote(datas)
    
    try:
        rf = req.post(url_edit, headers=headers, data=datas, cookies = coo, allow_redirects=False)
        if rf.status_code == 200:
            print(f"Website cleared! ")
            embed=discord.Embed(title=None, description='Website cleared ✔ ', color=0x2ecc71)
            await channel.send(embed=embed)
        else:
            print(rf.text)
            embed=discord.Embed(title=None, description=f"Couldn't change website ❌ ", color=0xe74c3c)
            await channel.send(embed=embed)
            
    except Exception as e:
        print(e)
        embed=discord.Embed(title=None, description=f"Couldn't change website! ❌ ", color=0xe74c3c)
        await channel.send(embed=embed)

    
    try:
        bio_url = "https://i.instagram.com/api/v1/accounts/set_biography/"
        datas={'raw_text': bio}
        
        rf = req.post(bio_url, headers=headers, data=datas, cookies = coo, allow_redirects=False)
        if rf.status_code == 200:
            print("Bio Cleared!")
            embed=discord.Embed(title=None, description='Bio cleared ✔ ', color=0x2ecc71)
            await channel.send(embed=embed)
    except Exception as e:
        print(e)


    await urllib.request.urlretrieve("https://i.imgur.com/F8GLylD.jpg", "profilepicc.jpg")
        
    with open('profilepicc.jpg', 'rb') as f: raw_data = f.read()
    
    uplod = f'{str(int(time.time()))}'
    nemz = f'{uplod}_0_-{str(random.randint(100000000, 999999999))}'
    imgurl = f'https://i.instagram.com/rupload_igphoto/{nemz}'
    
    header = {
        "Host": "i.instagram.com",
        "X-Entity-Length": str(len(raw_data)),
        "X-Entity-Name": nemz,
        "X-Instagram-Rupload-Params": r'''{"upload_id":"''' + uplod+ r'''","media_type":"1","image_compression":"{\"lib_name\":\"moz\",\"lib_version\":\"3.1.m\",\"quality\":\"70\"}"}''',
        "X-Entity-Type": "image/jpeg",
        "Offset": "0",
        "X-Ig-Connection-Type": "WIFI",
        "X-Ig-Capabilities": "3brTvwM=",
        "User-Agent": USER_AGENT,
        "Accept-Language": "en-US",
        "Content-Type": "application/octet-stream",
        "Content-Length": str(len(raw_data)),
        "Accept-Encoding": "gzip, deflate",
    }
    
    kek = req.post(imgurl, headers=header, data=raw_data)
    
    kekz = req.post('https://i.instagram.com/api/v1/accounts/change_profile_picture/', headers={
        "X-Ig-Device-Id": str(uuid2),
        "X-Ig-Android-Id": deviceid,
        "X-Ig-Connection-Type": "WIFI",
        "X-Ig-Capabilities": "3brTvwM=",
        "User-Agent": USER_AGENT,
        "Accept-Language": "en-US",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Accept-Encoding": "gzip, deflate",
        }, data=f'_csrftoken=missing&_uuid={uuid2}&use_fbuploader=true&upload_id={uplod}')
    
    if kekz.status_code == 200:
        print(f"Pfp cleared! ")
        embed=discord.Embed(title=None, description='Profile picture cleared ✔ ', color=0x2ecc71)
        await channel.send(embed=embed)

@client.command(pass_context=True)
async def reportlogin(ctx, reportusername, reportpassword):
    global log, loginJS
    global falog
    global reportcoo
    global reportreq
    global reportsessid

    uwuusers.username = reportusername
    two_factor_code = ''
    channel = ctx.message.channel

    nonce = str(int(datetime.now().timestamp()))
    uuid = str(uuid4())
    uuid2 = str(uuid4())

    DEVICE_SETS = {
        "app_version": "136.0.0.34.124",
        "android_version": "28",
        "android_release": "9.0",
        "dpi": "640dpi",
        "resolution": "1440x2560",
        "manufacturer": "samsung",
        "device": "SM-G965F",
        "model": "star2qltecs",
        "cpu": "samsungexynos9810",
        "version_code": "208061712",
    }
    

    USER_AGENT = 'Instagram {app_version} Android ({android_version}/{android_release}; {dpi}; {resolution}; ' \
                 '{manufacturer}; {model}; armani; {cpu}; en_US)'.format(**DEVICE_SETS)
    
    deviceid = 'android-' + str({secrets.token_hex(8)})

    headers = {
        'Host': 'i.instagram.com',
        'X-Ig-App-Locale': 'en-US',
        'X-Ig-Device-Id': str(uuid2),
        'X-Ig-Family-Device-Id': str(uuid),
        'X-Ig-Android-Id': deviceid,
        'Priority': 'u=3',
        'User-Agent': USER_AGENT,
        'Accept-Language': 'en-US',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Encoding': 'gzip, deflate',
    }

    
    data = f'signed_body=SIGNATURE.%7B%22jazoest%22%3A%2222521%22%2C%22phone_id%22%3A%22{str(uuid)}%22%2C%22enc_password%22%3A%22%23PWD_INSTAGRAM%3A0%3A{nonce}%3A{reportpassword}%22%2C%22username%22%3A%22{reportusername}%22%2C%22guid%22%3A%22{uuid2}%22%2C%22device_id%22%3A%22{deviceid}%22%2C%22google_tokens%22%3A%22%5B%5D%22%2C%22login_attempt_count%22%3A%220%22%7D'
    log = reportreq.post("https://i.instagram.com/api/v1/accounts/login/", headers=headers, data=data)
    
    loginJS = log.json()


    if 'logged_in_user' in log.text:
        reportcoo = log.cookies
        reportsessid = reportcoo['sessionid']
        embed=discord.Embed(title=None, description='Successfully Logged In to Report acc! ✔ ', color=0x2ecc71)
        await channel.send(embed=embed)
        embed2=discord.Embed(title=None, description='Use command !report "target" "verified" to start!  ', color=0x2ecc71)
        await channel.send(embed=embed2)
    elif 'The password you entered is incorrect' in log.text:
        embed=discord.Embed(title="Error!", description='Password is incorrect! ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
    elif '"two_factor_required":true' in log.text:
        embed=discord.Embed(title="Error!", description='2FA Detected, remove it an try again! ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
    elif 'rate_limit_error' in log.text:
        print("Ratelimited! Please wait and try again! </3 ")
        embed=discord.Embed(title="Error!", description='Ratelimited! Please try again in a few minutes! ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
    elif 'challenge_required' in log.text:
        embed=discord.Embed(title="Error!", description='Challenge Required! ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
    else:
        print(log.text)
        embed=discord.Embed(title="Error!", description='Error Logging in! ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)

@client.command(pass_context=True)
async def report(ctx, targets, verifieduser):
    global log, loginJS
    global falog
    global reportcoo
    global reportreq
    global targetsID
    global verifieduserID

    channel = ctx.message.channel
    
    try:
        checkReq = reportreq.get(f'https://instagram.com/{str(targets)}/?__a=1').json()
        targetsID = checkReq['logging_page_id'].split('_')[1]
        targetFbID = checkReq['graphql']['user']['fbid']
        print(f"{targets}'s UserID is {targetsID}")
        print(f"{targets}'s FBUserID is {targetFbID}")
    except Exception as e:
        print(e)
        embed=discord.Embed(title=None, description=f'Invalid Report Target @{targets} ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
        # MADE BY MARIOSKI <3
        print(f'Invalid Report Target @{targets} </3 ')

    try:
        checkReq = reportreq.get(f'https://instagram.com/{str(verifieduser)}/?__a=1').json()
        verifieduserID = checkReq['logging_page_id'].split('_')[1]
        veriFbID = checkReq['graphql']['user']['fbid']
        print(f"{verifieduser}'s UserID is {verifieduserID}")
        print(f"{verifieduser}'s FBUserID is {veriFbID}")
    except Exception as e:
        print(e)
        embed=discord.Embed(title=None, description=f'Invalid Report Target @{verifieduser} ❌ ', color=0xe74c3c)
        await channel.send(embed=embed)
        print(f'Invalid Report Target @{verifieduser} </3 ')
    
    
    reportParams = f'%7B%22server_params%22%3A%7B%22is_bloks%22%3A1%2C%22profile_id%22%3A' + veriFbID + '%2C%22serialized_state%22%3A%22%7B%5C%22schema%5C%22%3A%5C%22ig_frx%5C%22%2C%5C%22session%5C%22%3A%5C%22%7B%5C%5C%5C%22location%5C%5C%5C%22%3A%5C%5C%5C%22ig_profile%5C%5C%5C%22%2C%5C%5C%5C%22entry_point%5C%5C%5C%22%3A%5C%5C%5C%22chevron_button%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22null%5C%5C%5C%22%2C%5C%5C%5C%22tags%5C%5C%5C%22%3A%5B%5C%5C%5C%22ig_report_account%5C%5C%5C%22%2C%5C%5C%5C%22ig_user_impersonation%5C%5C%5C%22%2C%5C%5C%5C%22ig_impersonation_celebrity%5C%5C%5C%22%5D%2C%5C%5C%5C%22object%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22user_id%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22' + targetsID + '%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22reporter_id%5C%5C%5C%22%3A17841442439280052%2C%5C%5C%5C%22responsible_id%5C%5C%5C%22%3A' + targetFbID + '%2C%5C%5C%5C%22locale%5C%5C%5C%22%3A%5C%5C%5C%22en_GB%5C%5C%5C%22%2C%5C%5C%5C%22app_platform%5C%5C%5C%22%3A0%2C%5C%5C%5C%22extra_data%5C%5C%5C%22%3A%7B%5C%5C%5C%22container_module%5C%5C%5C%22%3A%5C%5C%5C%22profile%5C%5C%5C%22%2C%5C%5C%5C%22app_version%5C%5C%5C%22%3A%5C%5C%5C%22195.0.0.31.123%5C%5C%5C%22%2C%5C%5C%5C%22is_dark_mode%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22app_id%5C%5C%5C%22%3A567067343352427%2C%5C%5C%5C%22sentry_feature_map%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22shopping_session_id%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22logging_extra%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22is_in_holdout%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22preloading_enabled%5C%5C%5C%22%3Afalse%7D%2C%5C%5C%5C%22frx_feedback_submitted%5C%5C%5C%22%3Afalse%2C%5C%5C%5C%22additional_data%5C%5C%5C%22%3A%7B%7D%2C%5C%5C%5C%22tag_source%5C%5C%5C%22%3A%5C%5C%5C%22tag_selection_screen%5C%5C%5C%22%7D%5C%22%2C%5C%22screen%5C%22%3A%5C%22frx_profile_selection_screen%5C%22%2C%5C%22flow_info%5C%22%3A%5C%22%7B%5C%5C%5C%22nt%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22graphql%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22enrollment_info%5C%5C%5C%22%3Anull%2C%5C%5C%5C%22ig%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22ig_container_module%5C%5C%5C%5C%5C%5C%5C%22%3A%5C%5C%5C%5C%5C%5C%5C%22profile%5C%5C%5C%5C%5C%5C%5C%22%7D%5C%5C%5C%22%2C%5C%5C%5C%22bloks%5C%5C%5C%22%3A%5C%5C%5C%22%7B%5C%5C%5C%5C%5C%5C%5C%22initial_screen_id%5C%5C%5C%5C%5C%5C%5C%22%3Anull%7D%5C%5C%5C%22%2C%5C%5C%5C%22session_id%5C%5C%5C%22%3A%5C%5C%5C%22null%5C%5C%5C%22%7D%5C%22%2C%5C%22previous_state%5C%22%3Anull%7D%22%7D%7D'

    datas = f'params={reportParams}&_uuid={uid}&bk_client_context=%7B%22bloks_version%22%3A%22927f06374b80864ae6a0b04757048065714dc50ff15d2b8b3de8d0b6de961649%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=927f06374b80864ae6a0b04757048065714dc50ff15d2b8b3de8d0b6de961649'

    head = {
        "Host": "i.instagram.com",
        "User-Agent": "Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Content-Length": f"{str(len(datas))}",
        "Accept-Encoding": "gzip, deflate",
    }
    
    reporturl = 'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.instagram_bloks_bottom_sheet.ixt.screen.frx_profile_selection_screen/'

    try:
        response = requests.post(reporturl, headers=head, data=datas, cookies = reportreq.cookies)
        if response.status_code == 200:
            print("Sent report")
            embed=discord.Embed(title=None, description=f'Successfully reported @{targets} ✔ ', color=0x2ecc71)
            await channel.send(embed=embed)
        else:
            print("Error")
        time.sleep(3)
    except Exception as e:
        print(e)

@client.command(pass_context=True)
async def temp(ctx):
    global coo
    global password

    csrftoken = coo["csrftoken"]

    channel = ctx.message.channel
    
    headers = {
        'authority': 'www.instagram.com',
        'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR0oJRJQ-97uyyzutZe06Ng1ulaJbGnF0sTW7arDNDXvf3vl',
        'sec-ch-ua-mobile': '?0',
        'x-instagram-ajax': '6652cb6353b0',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'x-requested-with': 'XMLHttpRequest',
        'x-asbd-id': '198387',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'origin': 'https://www.instagram.com',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.instagram.com/accounts/remove/request/temporary/',
        'accept-language': 'en-EN,en;q=0.8',
        }

    nonce = str(int(datetime.now().timestamp()))
    
    data = {
      "enc_password": "#PWD_INSTAGRAM_BROWSER:0:" + str(nonce) + ":" + str(passwd),
      'deletion-reason': 'other'
    }
    
    headers6 = {
        'Host' : 'www.instagram.com',
        'User-Agent' : "Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:79.0) Gecko/20100101 Firefox/79.0",
        'Accept': "*/*",
        'Accept-Language': 'en-US,en;q=0.5',
        'X-CSRFToken': str(csrftoken),
        'X-Instagram-AJAX': '5898c63de2bf',
        'X-IG-App-ID': '936619743392459',
        'X-IG-WWW-Claim': 'hmac.AR1g8BS4Q0JFfT4AOYdvGc60uT9n1rrjpUv7XPlcARNwtGWI',
        'ContentType':'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.instagram.com',
        'DNT': '1',
        'KeepAlive': 'true',
        'Referer': "https://www.instagram.com/accounts/remove/request/temporary/",
        'TE': 'Trailers',
    }

    response = requests.post('https://www.instagram.com/accounts/remove/request/temporary/', headers=headers6, data=data, cookies=coo)

    if response.status_code == 200:
        embed=discord.Embed(title=None, description='Successfully Temped! ✔ ', color=0x2ecc71)
        await channel.send(embed=embed)
        
    elif response.status_code == 400:
        try:
            error = response.json['message']
            embed=discord.Embed(title=None, description=f"Can't temp... {error}❌ ", color=0xe74c3c)
            await channel.send(embed=embed)
        except:
            embed=discord.Embed(title=None, description=f"Can't temp... ❌ ", color=0xe74c3c)
            await channel.send(embed=embed)

@client.command(pass_context=True)
async def list(ctx, seconds=None):
    
    channel = ctx.message.channel
    
    if not seconds:
        seconds = 300
    
    try:
        targets = open("list.txt","r").read().splitlines()
        for target in targets:
                
            try:
                target = target.split()
                try:
                    custompfp = target[1]
                except:
                    custompfp = None
                    pass

                try:
                    multiple = target[2]
                except:
                    multiple = None
                    pass
                
                target = target[0]
                
                print(target)
                print(custompfp)
                print(multiple)
                await t(ctx, target, custompfp, multiple)
                await asyncio.sleep(int(seconds))
                
            except Exception as f:
                print(f)
                pass
            
    except Exception as e:
        print(e)

@client.command(pass_context=True)
async def stop(ctx,):
    list.cancel()
    embed=discord.Embed(title=None, description=f'Stopped running list command! ✔ ', color=0x2ecc71)
    await channel.send(embed=embed)

@client.command(pass_context=True)
async def watch(ctx, targetss, seconds=None):
    import time
    start_time = time.time()
    global reportsessid

    channel = ctx.message.channel

    if not seconds:
        seconds = 800
        embed=discord.Embed(title=None, description='Using default watch time: 800s ✔ ', color=0x2ecc71)
        await channel.send(embed=embed)

    seconds = int(seconds)

    if seconds <= 60:
        embed=discord.Embed(title=None, description=f"Seconds must be over 60! ❌ ", color=0xe74c3c)
        await channel.send(embed=embed)
        #MUST BE OVER 60 SECONDS!

    try:
        getid = reportreq.get(f'https://instagram.com/{str(targetss)}/?__a=1').json()
        targetssid = getid['logging_page_id'].split('_')[1]
    except:
        print(f"Error getting ID for {targetss}")
        embed=discord.Embed(title="Oops!", description=f"@{targetss} is already banned / doesn't exist ! ❌ ", color=0xffff00)
        await channel.send(embed=embed)

    url = f"https://i.instagram.com/api/v1/users/{targetssid}/info/?from_module=feed_timeline"
    

    headerslol = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Host':'i.instagram.com',
        'Cookie': f'sessionid={reportsessid}; csrftoken=3u8uOerK4kRwnhlQU8JuEzmhwkozvSuD;',
    }

    try:
        for i in range(seconds//60):
            ff = requests.get(url, headers=headerslol)
            print(ff.status_code)
            if ff.status_code == 404:
                embed=discord.Embed(title="Success!", description=f"Banned @{targetss} ! ❌ ", color=0x000000)
                await channel.send(embed=embed)
                elapsed = time.time() - start_time
                print(f"> Banned @{targetss} in {elapsed} seconds!")
                break
            print("not banned yet")
            await asyncio.sleep(60)
    except Exception as e:
        print(e)
        embed=discord.Embed(title=None, description=f"Error! Check Console for output! ❌ ", color=0xe74c3c)
        await channel.send(embed=embed)

client.run(str(bottoken))
# MADE BY MARIOSKI <3