import os
API_TOKEN =  os.environ.get("API_TOKEN") 

ADMINGROUP = (os.environ.get("ADMINGROUP")) 

adminlist = {
        int(os.environ.get("OWNERID")) : {'acceptedorders': 0, 'phonenumber' : "+989000000000", 'order' : {'active_order' : False, 'order_for_userid' : None, 'orderid' : None}}
}


OWNERID = int(os.environ.get("OWNERID")) 

CARDNUMBER = os.environ.get("CARDNUMBER") 

CARDNUMBEROWNER = os.environ.get("CARDNUMBEROWNER") 