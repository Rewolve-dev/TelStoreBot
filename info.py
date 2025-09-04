import os
API_TOKEN =  os.environ.get("API_TOKEN") 
ADMINGROUP = (os.environ.get("ADMINGROUP"))

adminlist = {
        int(os.environ.get("OWNERID")) : {'acceptedorders': 0, 'phonenumber' : "+989029396145", 'order' : {'active_order' : False, 'order_for_userid' : None, 'orderid' : None}}
}


OWNERID = int(os.environ.get("OWNERID"))

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



CARDNUMBER = os.environ.get("CARDNUMBER")
CARDNUMBEROWNER = os.environ.get("CARDNUMBEROWNER")