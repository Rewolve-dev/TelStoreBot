
import telebot
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from telebot.util import antiflood

import datetime
import os
import time
import logging

from info import *



Texts = {
    "StartText"                     :   "شروع کار ربات",
    "HelpMenuText"                  :   "راهنما",
    "Send_welcome"                  :   "به فروشگاه بازی های ما خوش آمدید کاربر عزیز!",
    "MyAccountInfoText"             :   "اطلاعات اکانت شما",
    "ContactAdminText"              :   "ارتباط با ادمین / پشتیبانی",
    "GamesSectionText"              :   "رفتن به بخش خدمات بازی ها",
    "MLBBText"                      :   "MLBB ورود سریع به دسته ی بازی ",
    "CallOfDutyMobileText"          :   "Call of Duty Mobile ورود سریع به دسته ی بازی ",
    "ClashOfClansText"              :   "Clash Of Clans ورود سریع به دسته ی بازی",
    "ClashRoyaleText"               :   "Clash Royale ورود سریع به دسته ی بازی",
    "GameMessage1"                  :   "لطفا نوع خدمت خودتون رو انتخاب کنید",

}


logging.getLogger('telebot').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)
logging.basicConfig(filename = "StoreTelBot.log", level = logging.DEBUG, format = '%(asctime)s  |||||||  %(message)s')

bot = telebot.TeleBot(API_TOKEN)

hideboard = ReplyKeyboardRemove()

userdata = dict()
usersteps = dict()
orders = dict()
active_chats = dict()
usertempdata = dict()





#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


MLBBPrices = {

            "50 Diamonds"   :   "30 هزارتومان",
            "150 Diamonds"  :   "60 هزارتومان",
            "250 Diamonds"  :   "90 هزارتومان",
            "500 Diamonds"  :   "120 هزارتومان",
            "1000 Diamonds" :   "150 هزارتومان",
            "1500 Diamonds" :   "180 هزارتومان",
            "2000 Diamonds" :   "210 هزارتومان",
            "2500 Diamonds" :   "240 هزارتومان",
            "4000 Diamonds" :   "270 هزارتومان",
            "5000 Diamonds" :   "300 هزارتومان"
            
            }


CODMPrices = {

            "80 CP"     :    "80 هزارتومان",
            "420 CP"    :    "200 هزارتومان",
            "880 CP"    :    "400 هزارتومان",
            "2400 CP"   :    "900 هزارتومان",
            "5000 CP"   :    "1.500 هزارتومان",
            "10800 CP"  :    "2.600 هزارتومان",
            "Pack Price":    "400 هزارتومان"

            }


COCPrices = {

        "80 COC Gems"   :   "90 هزارتومان",
        "500 COC Gems"  :   "430 هزارتومان",
        "1200 COC Gems" :   "860 هزارتومان",
        "6500 COC Gems" :   "4.100 هزارتومان",
        "14000 COC Gems":   "8.200 هزارتومان",
        "2500 COC Gems" :   "1.680 هزارتومان",
        "Golden pass"   :   "700 هزارتومان"
}



CRPrices = {

    "80 CR Gems"    :   "100 هزارتومان",
    "500 CR Gems"   :   "473 هزارتومان",
    "1200 CR Gems"  :   "910 هزارتومان",
    "6500 CR Gems"  :   "4.400 هزارتومان",
    "14000 CR Gems" :   "8.300 هزارتومان",
    "2500 CR Gems"  :   "1.800 هزارتومان",
    "Diamond Pass"  :   "1.090 هزارتومان"
}



#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------



commands = {
    "start"                    :       Texts['StartText'],
    "help"                     :       Texts['HelpMenuText'],
    "my_account_info"          :       Texts['MyAccountInfoText'],
    "contact_admin"            :       Texts['ContactAdminText'],
    "games"                    :       Texts['GamesSectionText'],
    "game_MLBB"                :       Texts['MLBBText'],
    "game_CallOfDutyMobile"    :       Texts['CallOfDutyMobileText'],
    "game_ClashOfClans"        :       Texts['ClashOfClansText'],
    "game_ClashRoyale"         :       Texts['ClashRoyaleText'],


}

admincommands = {

    'startchatwith'            :    "پیام از طریق ربات به یک کاربر با استفاده از آیدی عددی اون کاربر",

}


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------              LISTENER


def listener(messages):
    for m in messages:
        print(f"@{m.chat.username}, Name: {m.chat.first_name} ||| {datetime.datetime.today() : '%c'}, type:{m.content_type}, Message:\n{m.text}\n")
        os.makedirs(os.path.join('Data', str(m.chat.id)), exist_ok=True)


bot.set_update_listener(listener)



#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


def send_message(*args, **kwargs):
    try:
        return antiflood(bot.send_message, *args, **kwargs)
    except Exception as e:
        logging.exception(f'error in send message, error: {e}')

def copy_message(*args, **kwargs):
    try:
        return antiflood(bot.copy_message, *args, **kwargs)
    except Exception as e:
        logging.exception(f'error in copy message, error: {e}')

def delete_message(*args, **kwargs):
    try:
        return antiflood(bot.delete_message, *args, **kwargs)
    except Exception as e:
        logging.exception(f'error in delete message, error: {e}')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


def clean_text(text):
    return str(text).replace('.', '\.',).replace('_', "\_")
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------


@bot.callback_query_handler(func= lambda call: True)
def callback_handler(call):
    cid = call.message.chat.id
    mid = call.message.message_id
    call_id = call.id
    data = call.data

    if data.split("_")[0] == "return":
        section = data.split("_")[1]

        if section == "canceled":
            canceledOrder = data.split("_")[-1]
            bot.send_message(cid, "سفارش شما لغو شد.")
            delete_message(cid, mid)
            userid = call.from_user.id
            orders.get(userid)[-1].pop(canceledOrder)
            mainpage(call.message)
        

        elif section == "mainpage":
            try:
                delete_message(cid, mid)
            except Exception:
                bot.answer_callback_query(call_id, "عملیات معتبر نمیباشد!")
            mainpage(call.message)


        elif section == "contactadmin":
            command_contact_admin_handler(call.message)
    
    elif data.split("_")[0] == "confirmed":

        if data.split("_")[1] == "order":
            orderid = int(data.split("_")[-2])
            userid = int(data.split("_")[-1])
            
    # keyboard.add(InlineKeyboardButton("قبول کردن سفارش", callback_data= f"confirmed_order_{cid}"))
    # keyboard.add(InlineKeyboardButton("رد کردن سفارش", callback_data= f"rejected_order_{cid}"))
# orders.setdefault(cid,{orderid : {'admin' : None, 'userdata' : {'email' : None, 'password' : None},'cost' : None, 'service' : None}})
            adminID = call.from_user.id

            if adminID in adminlist:

                orders.get(userid)[-1][orderid]['admin'] = adminID
                adminlist[adminID]['order']['active_order'] = True
                adminlist[adminID]['order']['order_for_userid'] = userid
                adminlist[adminID]['order']['orderid'] = orderid
                send_message(userid, clean_text(f"سفارش شما توسط ادمین `{adminID}` قبول شد. لطفا با اکانت ثبت شده وارد بازی نشید و تلفن همراهتون در دسترس باشه.\nپس از اتمام سفارش به شما از طریق ربات اطلاع خواهیم داد."),parse_mode = "MarkdownV2")
                keyboard = InlineKeyboardMarkup()
                keyboard.add(InlineKeyboardButton(f"تایید شده توسط ادمین {call.from_user.username}✅", callback_data= "nothing"))
                keyboard.add(InlineKeyboardButton(f"تکمیل سفارش با موفقیت انجام شد", callback_data= f"finishedorder_{orderid}"))
                bot.edit_message_reply_markup(cid,mid, reply_markup= keyboard)
            else:
                bot.answer_callback_query(call_id, "شما ادمین ربات نیستید!")
            
        
        elif data.split("_")[1] == "game": #userstep continue_on_ordering_service
            #    keyboard.add(InlineKeyboardButton("تایید و ادامه", callback_data= f"confirmed_game_COD_{service}"),
            bot.edit_message_reply_markup(cid,mid, reply_markup= None)
            game = data.split("_")[2]
            orderid = int(cid) + int(time.time())
            keyboard = InlineKeyboardMarkup()
            keyboard.add(InlineKeyboardButton("بازگشت به صفحه اصلی", callback_data= f"return_mainpage_canceled_order_{orderid}"))
            send_message(cid, "لطفا ایمیل اکانت مورد نظر رو وارد کنید", reply_markup= keyboard)
            if orders.get(cid):
                new_order = {orderid: {'admin': None,'userdata': {'email': None, 'password': None},'cost': None,'service': None}}
                orders[cid].append(new_order)
            else:
                orders.setdefault(cid,[{orderid : {'admin' : None, 'userdata' : {'email' : None, 'password' : None},'cost' : None, 'service' : None}}])
            
            service = data.split("_")[-1]
            orders.get(cid)[-1][orderid]['service'] = service
            if game == "MLBB":
                orders[cid][-1][orderid]['cost'] = MLBBPrices[f'{service}']#contains service/product info
            elif game == "COD":
                orders[cid][-1][orderid]['cost'] = CODMPrices[f'{service}']#contains service/product info
            
            elif game == "COC":
                orders[cid][-1][orderid]['cost'] = COCPrices[f'{service}']#contains service/product info
            
            elif game == "CR":
                orders[cid][-1][orderid]['cost'] = CRPrices[f'{service}']#contains service/product info
           
            if usertempdata.get(cid):
                usertempdata.pop(cid)
                usertempdata[cid] = orderid
            else:
                usertempdata[cid] = orderid
    
            usersteps[cid] = "continue_on_ordering_service"
    
    elif data.split("_")[0] == "change":
        if data.split("_")[1] == "acc":
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            keyboard.add("تغییر شماره تلفن", "تغییر ایمیل")
            send_message(cid, "کدوم یکی رو میخواید تغییر بدید؟", reply_markup= keyboard)
            
    elif data.split("_")[0] == "finishedorder":
        adminID = call.from_user.id
        userid = adminlist[adminID]['order']['order_for_userid']
        orderid = int(data.split("_")[-1])
        for order in orders.get(userid, []):
            if orderid in order:
                theorder = order[orderid]
                break
        if theorder:
            if orderid == adminlist[adminID]['order']['orderid']:
                send_message(userid, f"سفارش شماره {orderid} شما تکمیل شد. با تشکر از خرید شما❤")
                keyboard = InlineKeyboardMarkup()
                keyboard.add(InlineKeyboardButton(f"توسط ادمین {call.from_user.username} با موفقیت به اتمام رسید✅", callback_data= "nothing"))
                bot.edit_message_reply_markup(cid,mid, reply_markup= keyboard)
                adminlist[adminID]['acceptedorders'] += 1
                adminlist[adminID]['order']['active_order'] = False
                adminlist[adminID]['order']['order_for_userid'] = None
                adminlist[adminID]['order']['orderid'] = None
                orders.pop(userid)
                userdata[userid]['orderscount'] += 1
            else:
                bot.answer_callback_query(call_id, "شما این سفارش رو قبول نکردید.")
        else:
            bot.answer_callback_query(call_id, "معتبر نمیباشد, مشکلی پیش اومده.")

    elif data.split("_")[0] == "rejected":
        if data.split("_")[1] == "order":
            userid = data.split("_")[-1]
            orderid = data.split("_")[-2]
            adminID = call.from_user.id
            # rejected_order_wrongsentamount_
            # rejected_order_faketrphoto_
            # rejected_order_wronginfo_
            keyboard = InlineKeyboardMarkup()
            reason = data.split("_")[2]
            if adminID in adminlist:

                if reason == "wrongsentamount":
                    keyboard.add(InlineKeyboardButton(f"رد شده توسط ادمین {call.from_user.username}❌", callback_data= "nothing"))
                    keyboard.add(InlineKeyboardButton(f"دلیل: مقدار واریزی اشتباه", callback_data= "nothing"))
                    bot.edit_message_reply_markup(cid,mid, reply_markup= keyboard)
                    send_message(userid, clean_text(f"سفارش شماره `{orderid}` شما رد شد.\nدلیل رد سفارش شما مقدار واریز شده ی اشتباه بوده. اگر فکر میکنید مقدار واریزی درست بوده با پشتیبانی تماس بگیرید: /contact_admin"), parse_mode= "MarkdownV2")

                elif reason == "faketrphoto":
                    keyboard.add(InlineKeyboardButton(f"رد شده توسط ادمین {call.from_user.username}❌", callback_data= "nothing"))
                    keyboard.add(InlineKeyboardButton(f"دلیل: رسید واریزی فیک", callback_data= "nothing"))
                    bot.edit_message_reply_markup(cid,mid, reply_markup= keyboard)
                    send_message(userid, clean_text(f"سفارش شماره `{orderid}` شما رد شد.\nرسید ارسالی شما مورد تایید ادمین ها نبود. اگر فکر میکنید اشتباهی پیش اومده با پشتیبانی تماس بگیرید: /contact_admin"), parse_mode= "MarkdownV2")

                elif reason == "wronginfo":
                    keyboard.add(InlineKeyboardButton(f"رد شده توسط ادمین {call.from_user.username}❌", callback_data= "nothing"))
                    keyboard.add(InlineKeyboardButton(f"دلیل: اطلاعات اکانت اشتباه هست", callback_data= "nothing"))
                    bot.edit_message_reply_markup(cid,mid, reply_markup= keyboard)
                    send_message(userid, clean_text(f"سفارش شماره `{orderid}` شما رد شد.\nاطلاعات وارد شده برای اکانت اشتباه هستند. اگر فکر میکنید اطلاعات درست ثبت شدن با پشتیبانی تماس بگیرید: /contact_admin"), parse_mode= "MarkdownV2")
            else:
                bot.answer_callback_query(call_id, "شما ادمین ربات نیستید!")
    
    
    # keyboard.add(InlineKeyboardButton("پاسخ به ادمین", callback_data= f"reply_admin_to_user_{cid}"))
    # keyboard.add(InlineKeyboardButton("علامت زدن به عنوان خوانده شده", callback_data= f"user_seen_message_admin_{mid}_{cid}"))


    elif data.split("_")[0] == "reply":
        adminID = call.from_user.id
        userid = int(data.split("_")[-1])
        if usertempdata.get(adminID):
            usertempdata.pop(adminID)
            usertempdata.setdefault(adminID, {})
        else:
            usertempdata.setdefault(adminID, {})
        usertempdata[adminID]['userid'] = userid
        usertempdata[adminID]['usermessageid'] = usertempdata[userid]['messageid']
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton(f"درحال پاسخ توسط ادمین @{call.from_user.username}", callback_data= "nothing"))
        bot.edit_message_reply_markup(cid,mid, reply_markup= keyboard)
        send_message(adminID, "لطفا پیام ارسالی خودتون به کاربر رو ارسال کنید.")
        usersteps[adminID] = "send admin message to user"




#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------



@bot.message_handler(commands= ['start'])#NOT DONE-----***********************************************************************************************
def mainpage(message):
    cid = message.chat.id
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(Texts['GamesSectionText'])
    keyboard.add(Texts['ContactAdminText'])
    keyboard.add(Texts['MyAccountInfoText'])
    
    if message.text == "/start":
        send_message(cid, Texts['Send_welcome'], reply_markup= keyboard)

    elif message.text.split()[-2] == "startchatwith" and cid in adminlist:
        userid = message.text.split()[-1]
        #connect_user_withAdmin(message, userid)
    

@bot.message_handler(commands= ['help'])#DONE-----
def help_menu(message):

    cid = message.chat.id
    text = ""
    for command,desc in commands.items():
        text += f"/{command} : {desc}\n"
    if cid in adminlist:
        text+= "*************************\nدستورات ادمین:"
        for acommand, adesc in admincommands.items():
            text += f"/{acommand} : {adesc}\n"    
    send_message(cid, text)

@bot.message_handler(commands= ['my_account_info'])#DONE-----entering_account_info_process
def command_my_account_info_handler(message):
    cid = message.chat.id
    if cid not in userdata:
        userdata[cid] = {'email': None, 'phonenumber': None, "user_name": message.chat.first_name, 'orderscount' : 0}

    if userdata[cid]['email'] is None:
        send_message(cid, "لطفا ایمیل خودتون رو برای تکمیل اطلاعات حساب کاربری وارد کنید:", reply_markup = hideboard)
        usersteps[cid] = "entering_account_info_process"


    else:
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton("بازگشت به صفحه اصلی", callback_data= "return_mainpage"),
                     InlineKeyboardButton("تغییر اطلاعات حساب کاربری", callback_data= 'change_acc_info'))
        text = f"""
اطلاعات حساب کاربری شما:
نام کاربری: {userdata[cid]['user_name']}
شماره تماس: {userdata[cid]['phonenumber']}
ایمیل: {userdata[cid]['email']}
تعداد سفارشات شما: {userdata[cid]['orderscount']}
        """

        send_message(cid, text, reply_markup= keyboard)



@bot.message_handler(commands= ['contact_admin'])#DONE-----
def command_contact_admin_handler(message):
    cid = message.chat.id
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("بازگشت به صفحه اصلی", callback_data= "return_mainpage"))
    send_message(cid, "لطفا پیام خود را ارسال کنید.", reply_markup = keyboard)
    usersteps[cid] = "send user message from support to admin group"

@bot.message_handler(commands= ['games'])#DONE-----
def command_games_handler(message):
    cid = message.chat.id
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Mobile Legends","Call of Duty Mobile")
    keyboard.add("Clash Of Clans", "Clash Royale")
    send_message(cid, "لطفا بازی مورد نظر خودتون رو انتخاب کنید", reply_markup= keyboard)


@bot.message_handler(commands= ['game_MLBB'])#DONE-----
def command_game_MLBB_handler(message):
    game_MLBB_section(message)

@bot.message_handler(commands= ['game_CallOfDutyMobile'])#DONE-----
def command_game_CallOfDutyMobile_handler(message):
    game_CallOfDutyMobile_section(message)
    
@bot.message_handler(commands= ['game_ClashOfClans'])#DONE-----
def command_game_ClashOfClans_handler(message):
    game_ClashOfClans_section(message)

@bot.message_handler(commands= ['game_ClashRoyale'])#DONE-----
def command_game_ClashRoyale_handler(message):
    game_ClashRoyale_section(message)


#-------------------------------------------------------------------------------    ADMIN COMMANDS

@bot.message_handler(commands= ['startchatwith'])
def command_startchatwith_handler(message):
    cid = message.chat.id
    if cid in adminlist:
        send_message(cid, "لطفا آیدی کاربر مورد نظر رو وارد کنید:")
        usersteps[cid] = "Get admin message in startchatwith"
    else:
        default_handler(message)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

#return_buttons_handler----DONE
@bot.message_handler(func = lambda message: message.text.split()[0] == "بازگشت")
def button_return_handler(message):
    cid = message.chat.id
    section = message.text.split()[-1]
    if section == "اصلی": #return to mainpage- button text: بازگشت به صفحه اصلی
        mainpage(message)


#mainpage_buttons-----DONE
@bot.message_handler(func= lambda message: message.text == Texts['MyAccountInfoText'])
def button_my_account_info_handler(message):
    command_my_account_info_handler(message)

@bot.message_handler(func= lambda message: message.text == Texts['ContactAdminText'])
def button_contact_admin_handler(message):
    command_contact_admin_handler(message)

@bot.message_handler(func= lambda message: message.text == Texts['GamesSectionText'])
def button_games_handler(message):
    command_games_handler(message)


#change_acc_info----DONE
@bot.message_handler(func= lambda message: message.text.split()[0] ==  "تغییر")#userstep_B_C
def button_change_my_acccount_information(message):
    cid = message.chat.id
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text.split()[1] == "ایمیل":
        send_message(cid, "لطفا ایمیل جدیدتون رو وارد کنید")
        usersteps[cid] = "change_accinfo_email"
    elif message.text.split()[2] == "تلفن":
        keyboard.add(KeyboardButton("ثبت شماره تلفن", request_contact= True))
        send_message(cid, "لطفا شماره تماس جدید خودتون رو از طریق دکمه ی زیر ثبت کنید", reply_markup= keyboard)
        usersteps[cid] = "change_accinfo_phonenumber"
    else:
        command_my_account_info_handler(message)


#GAMES---------DONE
@bot.message_handler(func= lambda message: message.text == ("Mobile Legends"))#"MLBB_selectproduct_process"
def game_MLBB_section(message):
    cid = message.chat.id
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("50 Diamonds", "150 Diamonds", "250 Diamonds", "500 Diamonds")
    keyboard.add("1000 Diamonds", "1500 Diamonds", "2000 Diamonds")
    keyboard.add("2500 Diamonds", "4000 Diamonds", "5000 Diamonds")
    keyboard.add("بازگشت به صفحه اصلی")

    send_message(cid, Texts['GameMessage1'], reply_markup= keyboard)
    usersteps[cid] = "MLBB_selectproduct_process"

@bot.message_handler(func= lambda message: message.text.startswith("Call of Duty Mobile"))#CODM_selectproduct_process
def game_CallOfDutyMobile_section(message):
    cid = message.chat.id
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("80 CP", "420 CP", "880 CP", "2400 CP")
    keyboard.add("5000 CP", "10800 CP", "Pack Price", "بازگشت به صفحه اصلی")
    send_message(cid, Texts['GameMessage1'], reply_markup= keyboard)
    usersteps[cid] = "CODM_selectproduct_process"


@bot.message_handler(func= lambda message: message.text.startswith("Clash Of Clans"))#COC_selectproduct_process
def game_ClashOfClans_section(message):
    cid = message.chat.id
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("80 COC Gems", "500 COC Gems", "1200 COC Gems")
    keyboard.add("6500 COC Gems", "14000 COC Gems", "2500 COC Gems")
    keyboard.add("Golden pass", "بازگشت به صفحه اصلی")
    send_message(cid, Texts['GameMessage1'], reply_markup= keyboard)
    usersteps[cid] = "COC_selectproduct_process"


@bot.message_handler(func= lambda message: message.text.startswith("Clash Royale"))#CR_selectproduct_process
def game_ClashRoyale_section(message):
    cid = message.chat.id
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("80 CR Gems", "500 CR Gems", "1200 CR Gems")
    keyboard.add("6500 CR Gems", "14000 CR Gems", "2500 CR Gems")
    keyboard.add("Other offers", "بازگشت به صفحه اصلی")
    send_message(cid, Texts['GameMessage1'], reply_markup= keyboard)
    usersteps[cid] = "CR_selectproduct_process"
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

@bot.message_handler(func= lambda message: usersteps.get(message.chat.id) == "send user message from support to admin group")
def send_user_message_to_admin_group(message):
    cid = message.chat.id
    mid = message.message_id
    senttext = f"""پیام ارسال شده از: @{message.chat.username}\n*{message.text}*"""
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(f"پاسخ به کاربر @{message.chat.username}", callback_data= f"reply_admin_to_user_{cid}"))
    send_message(ADMINGROUP, clean_text(senttext), reply_markup = keyboard, parse_mode = "MarkdownV2")
    send_message(cid, "پیام شما با موفقیت ارسال شد. تا پاسخ ادمین ها به پیامتون صبور باشید.", reply_to_message_id = mid)
    if usertempdata.get(cid):
        usertempdata.pop(cid)
        usertempdata.setdefault(cid, {})    
    else:
        usertempdata.setdefault(cid, {})
    usertempdata[cid]['messageid'] = mid





@bot.message_handler(func = lambda message: usersteps.get(message.chat.id) == "entering_account_info_process")
def step_entering_account_info_process_handler(message):
    cid = message.chat.id
    userdata[cid]['email'] = message.text
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("به اشتراک گذاری شماره تلفن", request_contact= True))
    keyboard.add("بازگشت به صفحه اصلی")
    send_message(cid, "لطفا شماره تماس خودتون رو با استفاده از دکمه ی زیر ارسال کنید", reply_markup= keyboard)


@bot.message_handler(func= lambda message: usersteps.get(message.chat.id) == "change_accinfo_email")
def step_change_accinfo_email_handler(message):
    cid = message.chat.id
    userdata[cid]['email'] = message.text
    send_message(cid, "ایمیل شما ثبت شد.")
    command_my_account_info_handler(message)


@bot.message_handler(func= lambda message: usersteps.get(message.chat.id) == "change_accinfo_phonenumber")
def step_change_accinfo_phonenumber_handler(message):
    cid = message.chat.id
    send_message(cid, "شماره تلفن شما با موفقیت تغییر کرد.")
    command_my_account_info_handler(message)

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

@bot.message_handler(func= lambda message: usersteps.get(message.chat.id) == "MLBB_selectproduct_process")
def step_MLBB_selectproduct_process_handler(message):
    cid = message.chat.id
    service = message.text
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("تایید و ادامه", callback_data= f"confirmed_game_MLBB_{service}"),
                  InlineKeyboardButton("انصراف و بازگشت", callback_data= "return_MLBB_section"))
    if service.split()[1] == "Diamonds":
        send_message(cid, f'''نام محصول: Diamonds"
    {service.split()[0]}:تعداد الماس 
    هزینه:{MLBBPrices[f'{service}']}
        تایید میکنید؟''', reply_markup= keyboard)

    else:
        text = f'''نام محصول: {service}"
    هزینه:{MLBBPrices[f'{service}']}
        تایید میکنید؟'''
        send_message(cid, text, reply_markup = keyboard)

@bot.message_handler(func= lambda message: usersteps.get(message.chat.id) == "CODM_selectproduct_process")
def step_F_handler(message):
    cid = message.chat.id
    service = message.text
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("تایید و ادامه", callback_data= f"confirmed_game_COD_{service}"),
                  InlineKeyboardButton("انصراف و بازگشت", callback_data= "return_CallOfDutyMobile_section"))
    if service.split()[1] == "CP":

        send_message(cid, f'''نام محصول: CP
تعداد: {service.split()[0]} CP
هزینه: {CODMPrices[f'{service}']}
تایید میکنید؟''', reply_markup= keyboard)
    
    else:
        text = f'''نام محصول: {service}
هزینه: {CODMPrices[f'{service}']}
تایید میکنید؟'''
        send_message(cid, text, reply_markup = keyboard)


@bot.message_handler(func= lambda message: usersteps.get(message.chat.id) == "COC_selectproduct_process")
def step_G_handler(message):
    cid = message.chat.id
    service = message.text
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("تایید و ادامه", callback_data= f"confirmed_game_COC_{service}"),
                  InlineKeyboardButton("انصراف و بازگشت", callback_data= "return_ClashOfClans_section"))
    if service.split()[-1] == "Gems":
        send_message(cid, f'''
        نام محصول: Gem"
        {service.split()[0]}:تعداد Gem 
        هزینه:{COCPrices[f'{service}']}
            تایید میکنید؟''', reply_markup= keyboard)
    else:
        text = f'''
        نام محصول: Gem"
        {service.split()[0]}:تعداد Gem 
        هزینه:{COCPrices[f'{service}']}
            تایید میکنید؟'''
        send_message(cid, text, reply_markup = keyboard)


@bot.message_handler(func= lambda message: usersteps.get(message.chat.id) == "CR_selectproduct_process")
def step_H_handler(message):
    cid = message.chat.id
    service = message.text
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("تایید و ادامه", callback_data= f"confirmed_game_CR_{service}"),
                  InlineKeyboardButton("انصراف و بازگشت", callback_data= "return_ClashRoyale_section"))
    if service.split()[-1] == "Gems":
        send_message(cid, f'''
        نام محصول: Gem"
        {service.split()[0]}:تعداد Gem 
        هزینه:{CRPrices[f'{service}']}
            تایید میکنید؟''', reply_markup= keyboard)

    else:
        text = f'''
        نام محصول: Gem"
        {service.split()[0]}:تعداد Gem 
        هزینه:{CRPrices[f'{service}']}
            تایید میکنید؟'''
        
        send_message(cid, text, reply_markup = keyboard)


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

@bot.message_handler(func= lambda message: usersteps.get(message.chat.id) == "continue_on_ordering_service")
def step_continue_on_ordering_service_handler(message):
    cid = message.chat.id
    orderid = usertempdata[cid]
    orders[cid][-1][orderid]['userdata']['email'] = message.text
    send_message(cid, "لطفا رمز ورود به اکانت رو ارسال کنید.")
    usersteps[cid] = "continue_on_ordering_serviceB"


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------



@bot.message_handler(func= lambda message: usersteps.get(message.chat.id) == "continue_on_ordering_serviceB")
def step_continue_on_ordering_serviceB_handler(message):
    cid = message.chat.id
    orderid = usertempdata[cid]
    orders[cid][-1][orderid]['userdata']['password'] = message.text
    text = f"""
اطلاعات سفارش شما:
ایمیل ثبت شده: {orders[cid][-1][orderid]['userdata']['email']}
شماره تلفن ثبت شده جهت تماس توسط ادمین (بعد از ثبت سفارش حتما در دسترس باشید): +{userdata[cid]['phonenumber']}
شماره سفارش: {orderid}
پسورد ثبت شده: {orders[cid][-1][orderid]['userdata']['password']}
محصول: {orders[cid][-1][orderid]['service']}
هزینه: {orders[cid][-1][orderid]['cost']}"""

    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("لغو پرداخت و بازگشت به صفحه اصلی", callback_data= "return_canceled"))
    send_message(cid, text)
    send_message(cid, clean_text(f" لطفا در صورت تایید اطلاعات  مبلغ {orders[cid][-1][orderid]['cost']} رو به شماره کارت `{CARDNUMBER}` به نام *{CARDNUMBEROWNER}* واریز کنید و رسید واریز رو ارسال کنید تا سفارش شما برای ادمین ها ارسال بشه و پردازش بشه. در صورت لغو شدن سفارش به هر دلیلی مبلغ واریز شده به همان حساب عودت میگردد."), reply_markup= keyboard, parse_mode= "MarkdownV2")

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------






@bot.message_handler(func= lambda message: usersteps.get(message.chat.id) == "transaction_screenshot")
def step_transaction_screenshot_handler(message):
    cid = message.chat.id
    orderid = usertempdata[cid]['orderid']
    text = f"""
اطلاعات سفارش کاربر \n@{message.chat.username} / {message.chat.first_name}:
آیدی عددی کاربر: `{cid}`
تعداد سفارشات ثبت شده توسط این کاربر: {userdata[cid]['orderscount']}
ایمیل ثبت شده: `{orders[cid][-1][orderid]['userdata']['email']}`
شماره تلفن ثبت شده جهت تماس توسط ادمین: `+{userdata[cid]['phonenumber']}`
پسورد ثبت شده: `{orders[cid][-1][orderid]['userdata']['password']}`
محصول: {orders[cid][-1][orderid]['service']}
هزینه: {clean_text(orders[cid][-1][orderid]['cost'])}"""     
    

    clean_text(text)
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton("✅قبول کردن سفارش", callback_data= f"confirmed_order_{orderid}_{cid}"))
    keyboard.add(InlineKeyboardButton("رد کردن سفارش \ اطلاعات اشتباه", callback_data= f"rejected_order_wronginfo_{orderid}_{cid}"))
    keyboard.add(InlineKeyboardButton("رد کردن سفارش \ رسید واریزی فیک", callback_data= f"rejected_order_faketrphoto_{orderid}_{cid}"))
    keyboard.add(InlineKeyboardButton("رد کردن سفارش \ مبلغ واریزی نادرست", callback_data= f"rejected_order_wrongsentamount_{orderid}_{cid}"))
    with open(f"{os.path.join('Data', str(cid), str(userdata.get(cid)['orderscount']))}.{usertempdata.get(cid)[orderid]}", 'rb') as f:
        bot.send_photo(ADMINGROUP, f, caption= text , reply_markup= keyboard, parse_mode= "MarkdownV2")
    send_message(cid, "لطفا تا تایید سفارشتون توسط ادمین ها صبور باشید. پس از تایید سفارش به هیچ وجه داخل اکانتتون نرید!", reply_markup = hideboard)







#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------



@bot.message_handler(func= lambda message: usersteps.get(message.chat.id) == "Get admin message in startchatwith")
def step_Get_admin_message_in_startchatwith_handler(message):
    cid = message.chat.id
    userid = message.text
    if userid.isdigit():    
        if usertempdata.get(cid):
            usertempdata.pop(cid)
            usertempdata.setdefault(cid, {})
        else:
            usertempdata.setdefault(cid, {})
        usertempdata[cid]['userid'] = userid
        send_message(cid, "لطفا پیامتون رو ارسال کنید")
        usersteps[cid] = "Get admin message in startchatwith2"
    else:
        send_message(cid, "لطفا فقط آیدی عددی کاربر رو ارسال کنید")
        command_startchatwith_handler(message)


@bot.message_handler(func= lambda message: usersteps.get(message.chat.id) == "Get admin message in startchatwith2")
def step_Get_admin_message_in_startchatwith2_handler(message):
    cid = message.chat.id
    userid = usertempdata[cid]['userid']
    adminid = cid + userid

    adminmessage = clean_text(f"""
    شما پیامی از ادمین ها دارید:
                              
    *{clean_text(message.text)}*

    برای پاسخ به پشتیبانی پیام بدید.
""")
    
    send_message(userid, adminmessage, parse_mode = "MarkdownV2")
    send_message(cid, "پیام شما در صورت درست بودن اطلاعات ارسال خواهد شد.")
    send_message(ADMINGROUP, f"ادمین @{message.chat.username} پیامی به کاربر ارسال کرد. محتوای پیام:\n{adminmessage}")

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

@bot.message_handler(func= lambda message: usersteps.get(message.chat.id) == "send admin message to user")
def step_send_admin_message_to_user_handler(message):
    cid = message.chat.id
    text = message.text
    adminmessage = f"""
    شما پیام جدیدی از ادمین دارید:

*{text}*

"""
    
    mid = usertempdata[cid]['usermessageid']
    userid = usertempdata[cid]['userid']
    send_message(userid, adminmessage, reply_to_message_id = mid, parse_mode = "MarkdownV2")
    send_message(cid, "پیام شما با موفقیت ارسال شد.")


#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------



@bot.message_handler(content_types=['contact'])
def content_contact_handler(message):
    cid = message.chat.id
    userdata[cid]['phonenumber'] = message.contact.phone_number
    if message.contact.user_id == cid:
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton("تایید و بازگشت", callback_data= "return_mainpage"),
                    InlineKeyboardButton("تغییر اطلاعات", callback_data= "change_acc_info"))
        if usersteps[cid] == "change_accinfo_phonenumber":
            step_change_accinfo_phonenumber_handler(message)
            
        else:
            send_message(cid, f"اطلاعات شما با موفقیت ثبت شد. در صورتی که میخواستید اطلاعات ثبت شده رو تغییر بدید روی دکمه ی زیر کلیک کنید.\nاطلاعات:\nشماره تلفن: {userdata[cid]['phonenumber']}\nجیمیل: {userdata[cid]['email']}", reply_markup= keyboard)
    else:
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton("بازگشت به صفحه اصلی", callback_data= "return_mainpage"))
        send_message(cid, "لطفا شماره ی همین اکانت تلگرامتون رو به اشتراک بزارید", reply_markup = keyboard)



@bot.message_handler(content_types=['photo'])
def content_photo_handler(message):
    cid = message.chat.id
    if usersteps.get(cid) == "continue_on_ordering_serviceB":
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        content = bot.download_file(file_info.file_path)
        orderid = usertempdata[cid]
        usertempdata.pop(cid)
        usertempdata.setdefault(cid, {})
        usertempdata[cid]['orderid'] = orderid
        usertempdata[cid][orderid]= file_info.file_path.split('.')[-1]   #usertempdata[cid][orderid]
        os.makedirs(os.path.join('Data', str(cid)), exist_ok=True)
     
        with open(f"{os.path.join('Data', str(cid), str(userdata.get(cid)['orderscount']))}.{usertempdata.get(cid)[orderid]}", 'wb') as f:
            f.write(content)

        usersteps[cid] = "transaction_screenshot"
        step_transaction_screenshot_handler(message)

    elif usersteps.get(cid) == "send user message from support to admin group":
        mid = message.message_id
        usermessage = message.caption
        keyboard = InlineKeyboardMarkup()
        keyboard.add(InlineKeyboardButton(f"پاسخ به کاربر @{message.chat.username}", callback_data= f"reply_admin_to_user_{cid}_{mid}"))
        bot.copy_message(ADMINGROUP, cid, mid, clean_text(f"پیام ارسال شده از: @{message.chat.username}\n*{usermessage}*"), parse_mode= "MarkdownV2", reply_markup= keyboard)
        send_message(cid, "پیام شما با موفقیت ارسال شد. تا پاسخ ادمین ها به پیامتون صبور باشید.", reply_to_message_id = mid)
        if usertempdata.get(cid):
            usertempdata.pop(cid)
            usertempdata.setdefault(cid, {})    
        else:
            usertempdata.setdefault(cid, {})
        usertempdata[cid]['messageid'] = mid


    elif usersteps.get(cid) == "send admin message to user":
        text = message.caption
        adminmessage = f"""
شما پیام جدیدی از ادمین دارید:

*{text}*

    """
        
        mid = usertempdata[cid]['usermessageid']
        userid = usertempdata[cid]['userid']
        bot.copy_message(userid, cid, message.message_id, clean_text(adminmessage), "MarkdownV2", reply_to_message_id= mid)
        send_message(cid, "پیام شما با موفقیت ارسال شد.")
        usersteps.pop(cid)


        
    else:
        default_handler(message)
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
#----------------------------------------------------------------------------







@bot.message_handler(func=lambda message: True, content_types=['text'])
def default_handler(message):
    send_message(message.chat.id, "متوجه نشدم منظورتون چیه, شاید دنبال دستوری باشید که میتونید از طریق /help بهش دست پیدا کنید." )




    
bot.infinity_polling()