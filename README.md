
# StoreTelBot - ربات فروشگاه تلگرام 🤖

یک ربات فروشگاه تلگرام پیشرفته و ماژولار برای فروش آیتم‌های درون‌بازی (In-Game Items) و ارزهای مجازی بازی‌های محبوب موبایل.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Telegram Bot](https://img.shields.io/badge/Telegram-Bot_API-green)
![MySQL](https://img.shields.io/badge/Database-MySQL-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue)

## ✨ ویژگی‌های کلیدی

*   **پشتیبانی از چندین بازی:** Mobile Legends, Call of Duty Mobile, Clash of Clans, Clash Royale
*   **سیستم مدیریت محصول:** اضافه، حذف و مدیریت آیتم‌های فروشگاهی
*   **پنل مدیریت کامل:** پیگیری سفارشات، مدیریت کاربران و پاسخگویی به پیام‌ها
*   **پرداخت امن:** تایید تراکنش‌ها توسط ادمین‌ها
*   **سیستم حساب کاربری:** اطلاعات کاربری، تاریخچه سفارشات
*   **لاگ‌گیری جامع:** ثبت تمامی فعالیت‌ها و خطاها
*   **پایگاه داده MySQL:** ذخیره‌سازی مطمئن اطلاعات و دسترسی راحت

## 🚀 شروع سریع

### پیش‌نیازها

*   Python 3.8 یا بالاتر
*   کتابخانه `pyTelegramBotAPI`
*   یک توکن ربات تلگرام از [BotFather](https://t.me/BotFather)

### نصب و راه‌اندازی

1.  مخزن را کلون کنید:
    ```bash
    git clone https://github.com/your-username/StoreTelBot.git
    cd StoreTelBot
    ```

2.  وابستگی‌های لازم را نصب کنید:
    ```bash
    pip install pyTelegramBotAPI
    ```
    ```bash
    pip install -r requirements.txt
    ```
    ```bash
    pip install mysql-connector-python
    ```


3.  فایل پیکربندی را ایجاد و تنظیم کنید (`info.py`):
    ```python
    API_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
    ADMINGROUP = YOUR_ADMIN_GROUP_CHAT_ID
    OWNERID = YOUR_TELEGRAM_USER_ID

    adminlist = {
        ADMIN_TELEGRAM_ACCOUNT_ID: {'phonenumber': 'YOUR_PHONE_NUMBER', 'acceptedorders': 0}
    }

    ```

4.  ربات را اجرا کنید:
    ```bash
    python main.py
    ```

## 📖 ساختار پروژه

```
StoreTelBot
├── main.py                # فایل اصلی ربات
├── info.py                # تنظیمات و توکن‌ها
├── DML.py                 # عملیات نوشتن در دیتابیس (Insert/Update/Delete)
├── DQL.py                 # عملیات خواندن از دیتابیس (Query)
├── Data/                  # پوشه ذخیره‌سازی داده‌های کاربران
├── StoreTelBot.log        # فایل لاگ (پس از اجرا ایجاد می‌شود)
└── README.md              # این فایل
```

## 🎮 بازی‌های پشتیبانی شده

| بازی | آیتم‌های فروشی |
|------|----------------|
| **Mobile Legends: Bang Bang** | الماس (۵۰ تا ۵۰۰۰) |
| **Call of Duty: Mobile** | CP (۸۰ تا ۱۰۸۰۰) و Pack |
| **Clash of Clans** | Gem (۸۰ تا ۱۴۰۰۰) و Golden Pass |
| **Clash Royale** | Gem (۸۰ تا ۱۴۰۰۰) و Diamond Pass |

## 👨‍💼 مدیریت ربات

### دستورات ادمین

*   `/startchatwith` - شروع چت با کاربر خاص
*   `/addproduct` - اضافه کردن محصول جدید
*   `/removeproduct` - حذف محصول
s

### دستورات کاربران

*   `/start` - شروع کار با ربات
*   `/games` - نمایش دسته‌بندی بازی‌ها
*   `/my_account_info` - اطلاعات حساب کاربری
*   `/contact_admin` - تماس با پشتیبانی
*   `/help` - راهنمای دستورات

### دستورات مالک

*   `/add_admin` - اضافه کردن ادمین جدید از طریق آیدی تلگرام
*   `/remove_admin` - حذف کردن کردن ادمین از طریق آیدی تلگرام
*   `/send_message_to_all` - ارسال پیام برای تمامی کاربران ربات
*   `/delete_last_message` - حذف آخرین پیام ارسال شده برای تمامی کاربران




## 🔧 توسعه و سفارشی‌سازی

### اضافه کردن بازی جدید

1. یک بخش جدید در `main.py` اضافه کنید:
```python
insert_GAMESECTION_data(5, "Game Name", "Publisher")
game_prices = {
    "Item 1": "Price 1",
    "Item 2": "Price 2"
}
for prod, price in game_prices.items():
    insert_PRODUCT_data(5, prod, price)
```

2. دستورات مربوطه را در بخش `commands` اضافه کنید.

## 📝 لاگ‌گیری

ربات به طور کامل تمام فعالیت‌ها را در فایل `StoreTelBot.log` ثبت می‌کند که برای عیب‌یابی و پیگیری مشکلات مفید است.


## 📄 لایسنس

این پروژه تحت لایسنس MIT منتشر شده است.

## 📞 پشتیبانی

برای پشتیبانی و راهنمایی می‌توانید از طریق بخش Issues گیت‌هاب یا از طریق تلگرام با آیدی [@Rewolve](https://t.me/Rewolve) تماس بگیرید.

