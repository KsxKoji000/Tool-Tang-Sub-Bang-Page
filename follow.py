# +------------------------------------------------------------ -+
# | Tất Cả Được Share Tại Github Của Dươngg Phú Quốcc            |
# | Vui Lòng Không Sử Dụng Để Buôn Bán Dưới Bất Kì Hình Thức Nào |
# |                     -- Trân Trọng --                         |
# +--------------------------------------------------------------+

import requests,os,sys,time
from pystyle import Write, Colors,System
from datetime import datetime
try:
    os.remove('list_page.txt')
except:
    pass
file2 = open('list_page.txt','a+')
# <!--- Colors ---!>
_Black_ = '\033[1;30m'
_Red_ = '\033[1;31m'
_Green_ = '\033[1;32m'
_Yellow_ = '\033[1;33m'
_Blue_ = '\033[1;34m'
_Purple_ = '\033[1;35m'
_Cyan_ = '\033[1;36m'
_White_ = '\033[1;37m'
# <!--- Colors ---!>
def __gach__():
    Write.Print('────────────────────────────────────────────────────────\n', Colors.cyan_to_green, interval=0.00125)
def Banner():
    System.Clear()
    ban = f'''
{_Blue_}    ██╗  ██╗ ██████╗      ██╗██╗   ████████╗
{_White_}    ██║ ██╔╝██╔═══██╗     ██║██║   ╚══██╔══╝
{_Blue_}    █████╔╝ ██║   ██║     ██║██║█████╗██║   
{_White_}    ██╔═██╗ ██║   ██║██   ██║██║╚════╝██║   
{_Blue_}    ██║  ██╗╚██████╔╝╚█████╔╝██║      ██║   
{_White_}    ╚═╝  ╚═╝ ╚═════╝  ╚════╝ ╚═╝      ╚═╝   
{_Cyan_}    [{_Green_}Hello World {_Red_}- {_Green_}こんにちは世界 {_Blue_}- {_Green_}안녕 세계{_Cyan_}]
{_Purple_}─────────────────────────────────────────────────────
{_Cyan_}[ {_White_}🥱 {_Cyan_}] {_Yellow_}Author: {_Red_}Dươngg Phú Quốcc {_Red_}( {_Blue_}KsxKoji {_Red_})
{_Cyan_}[ {_White_}🥱 {_Cyan_}] {_White_}Phở Bò: {_Green_}https://facebook.com/100042415576964
{_Cyan_}[ {_White_}🥱 {_Cyan_}] {_Red_}Du Tu Be: {_Cyan_}https://www.youtube.com/@WuocsDev
{_Purple_}─────────────────────────────────────────────────────
'''
    for h in ban:
        sys.stdout.write(h)
        sys.stdout.flush()
        time.sleep(0.0025)

def loading(o):
    while o != 0:
        o = o - 1
        print(f'{_Cyan_}[{_Yellow_}/{_Cyan_}] {_Red_}Đang {_Green_}Loading{_Black_}, {_Yellow_}Còn {_Blue_}{o} {_Purple_}Giây {_Cyan_}Nữa      ', end='\r'); time.sleep(1/6)
        print(f'{_Cyan_}[{_Yellow_}-{_Cyan_}] {_Cyan_}Đang {_Red_}Loading{_Black_}, {_Green_}Còn {_Yellow_}{o} {_Blue_}Giây {_Purple_}Nữa      ', end='\r'); time.sleep(1/6)
        print(f'{_Cyan_}[{_Yellow_}\\{_Cyan_}] {_Purple_}Đang {_Cyan_}Loading{_Black_}, {_Red_}Còn {_Green_}{o} {_Yellow_}Giây {_Blue_}Nữa     ', end='\r'); time.sleep(1/6)
        print(f'{_Cyan_}[{_Yellow_}|{_Cyan_}] {_Blue_}Đang {_Purple_}Loading{_Black_}, {_Cyan_}Còn {_Red_}{o} {_Green_}Giây {_Yellow_}Nữa      ', end='\r'); time.sleep(1/6)
class KsxKoji():
    def __init__(self, ck) -> None:
        self.cookie = ck
        self.id_ck = ck.split('c_user=')[1].split(';')[0]
        self.author = 'Dươngg Phú Quốcc ( KsxKoji )'
        self.facebook = 'https://facebook.com/100042415576964'
        self.youtube = 'https://www.youtube.com/@WuocsDev'
    def __Get_ThongTin__(self):
        a = requests.get('https://mbasic.facebook.com/profile.php?='+self.id_ck, headers={'cookie': self.cookie}).text
        print(f'{_Yellow_} Đang Kiểm Tra Cookie !', end='\r')
        try:
            self.name = a.split('<title>')[1].split('</title>')[0]
            self.fb_dtsg = a.split('<input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
            self.jazoest = a.split('<input type="hidden" name="jazoest" value="')[1].split('"')[0]
            return True
        except:
            print(f'{_Cyan_}<ERROR:000> {_Red_}Cookie Die, Nhập Cookie Khác !!!')
            __gach__()
            return False
    def __Get_Page__(self):
        self.dem = 0
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'variables': '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
            'doc_id': '5300338636681652'
            }
        getidpro5 = requests.post('https://www.facebook.com/api/graphql/', headers = {'cookie':self.cookie}, data = data).json()['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
        for uidd in getidpro5:
            self.dem += 1
            uid_page = uidd['profile']['id']
            save = uid_page + ' | ' + self.fb_dtsg + ' | ' + self.jazoest + ' | ' +self.cookie + f'i_user={uid_page};'
            save_file = open('list_page.txt','a+', encoding='utf-8').write(save+'\n')
    
    def __Follow__(self, id, cookie, fb_dtsg, jazoest, taget):
        self.headers = {'accept': '*/*','accept-language': 'vi,vi-VN;q=0.9,en;q=0.8','cache-control': 'max-age=0','content-encoding': 'br','content-type': 'application/x-www-form-urlencoded','cookie': cookie,'origin': 'https://www.facebook.com','referer': 'https://www.facebook.com','sec-ch-prefers-color-scheme': 'light','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','sec-gpc': '1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}    
        data = {
            'av': id,
            '__user': id,
            'fb_dtsg': fb_dtsg,
            'jazoest': jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUserFollowMutation',
            'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,tap_search_bar,1713671419755,394049,190055527696468,,","is_tracking_encrypted":false,"subscribe_location":"PROFILE","subscribee_id":"'+taget+'","tracking":null,"actor_id":"'+id+'","client_mutation_id":"19"},"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '7393793397375006',
        }

        follow = requests.post('https://www.facebook.com/api/graphql/', headers=self.headers, data=data).text
        if 'IS_SUBSCRIBED' in follow:
            return True
        else:
            return False
#<!--- VÀO GIAO DIỆN ---!>
def __Main__():
    Banner(); dem_ck = 1
    while True:
        try:
            ck = input(f'{_Cyan_}[ {_Red_}+ {_Cyan_}] {_Yellow_}Nhập Cookie Account Chứa Pr5 {_Cyan_}[{_Purple_}{dem_ck}{_Cyan_}]{_Yellow_}: {_Green_}')
            if ck != '' and 'c_user=' in ck:
                f = KsxKoji(ck)
                fb = f.__Get_ThongTin__()
                if fb == True:
                    f.__Get_Page__()
                    __gach__()
                    print(f'{_Cyan_}(*) {_Green_}Name Profile: {_Yellow_}{f.name} {_Red_}| {_Green_}Có {_Yellow_}{f.dem} {_Green_}Page')
                    __gach__()
                    dem_ck += 1
            elif ck == '' and dem_ck > 1:
                break
            else:
                print(f'{_Red_} Bắt Buộc Nhập Ít Nhất 1 Cookie !!!')
                __gach__()
        except KeyboardInterrupt:
            quit()
    Banner()
    while True:
        taget = input(f'{_Cyan_}[ {_Red_}+ {_Cyan_}] {_Yellow_}Nhập UID Profile Muốn Tăng{_Yellow_}: {_Green_}')
        so_luong = int(input(f'{_Cyan_}[ {_Red_}+ {_Cyan_}] {_Yellow_}Nhập Số Lượng Muốn Tăng{_Yellow_}: {_Green_}'))
        delay = int(input(f'{_Cyan_}[ {_Red_}+ {_Cyan_}] {_Yellow_}Nhập Thời Gian Delay{_Cyan_}({_Purple_}defaul {_Yellow_}>= {_Red_}10{_Cyan_}){_Yellow_}: {_Green_}'))
        if delay < 10:
            print(f'{_Red_} Bắt Buộc Trên 10 Giây Mà 3:)')
            __gach__()
            delay = int(input(f'{_Cyan_}[ {_Red_}+ {_Cyan_}] {_Yellow_}Nhập Thời Gian Delay{_Cyan_}({_Purple_}defaul {_Yellow_}>= {_Red_}10{_Cyan_}){_Yellow_}: {_Green_}'))
        else:
            break
    Banner()
    x = 0; dem = 0
    open_file = open('list_page.txt','r').read().split('\n')
    while True:
        if x >= len(open_file):
            print(f'{_Cyan_} Đã Hết Page Để Follow, Tự Động Out ~')
            quit()
        elif x >= so_luong:
            print(f'{_Cyan_} Đã Xong, Out ~')
            quit()
        else:
            dem += 1
            id = open_file[x].split(' | ')[0]
            fb_dtsg = open_file[x].split(' | ')[1]
            jazoest = open_file[x].split(' | ')[2]
            cookie = open_file[x].split(' | ')[3]
            fl = f.__Follow__(id,cookie,fb_dtsg,jazoest,taget)
            if fl == True:
                print(f'{_Cyan_}[{_Red_}{dem}{_Cyan_}] {_Purple_}| {_Green_}KsxKoji~ {_Purple_}| {_Cyan_}[{_Yellow_}{id}{_Cyan_}] {_Red_}-> {_Cyan_}Follow {_Red_}-> {_Cyan_}[{_Yellow_}{taget}{_Cyan_}] {_Purple_}| {_Yellow_}Thành Công !')
            elif fl == False:
                print(f'{_Cyan_}[{_Red_}{dem}{_Cyan_}] {_Purple_}| {_Green_}KsxKoji~ {_Purple_}| {_Cyan_}[{_Yellow_}{id}{_Cyan_}] {_Red_}-> {_Cyan_}Follow {_Red_}-> {_Cyan_}[{_Yellow_}{taget}{_Cyan_}] {_Purple_}| {_Red_}Thất Bại !')
            x += 1
            loading(delay)
try:
    __Main__()
except KeyboardInterrupt:
    quit()