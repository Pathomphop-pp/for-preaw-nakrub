import streamlit as st
import datetime
import random
from zoneinfo import ZoneInfo

import gspread
from google.oauth2.service_account import Credentials
import json

# ========================
# 🎀 ตั้งค่า
# ========================

# ชื่อ
her_name = "เปรียวเปรี้ยว 💖"

# วันแรกที่เจอกัน (เก็บแค่วันที่)
first_meet_date = datetime.date(2025, 3, 9)

# วันแรกที่คบกัน (เก็บวัน + เวลา)
first_girlfriend_date = datetime.datetime(2025, 9, 5, 23, 55, 0, tzinfo=ZoneInfo("Asia/Bangkok"))

# วันนี้
today = datetime.datetime.now(ZoneInfo("Asia/Bangkok"))

# จำนวนวัน
days_since = (today.date() - first_meet_date).days
diff = today - first_girlfriend_date
days_girlfriend = diff.days
hours_girlfriend, remainder = divmod(diff.seconds, 3600)
minutes_girlfriend, seconds_girlfriend = divmod(remainder, 60)

# ========================
# 📖 โหลดข้อความจากไฟล์
# ========================
def load_messages(file_path="love_messages.txt"):
    with open(file_path, "r", encoding="utf-8") as f:
        messages = [line.strip() for line in f if line.strip()]
    return messages

love_messages = load_messages()

####################################################################################################
# กำหนดวันเกิดเปรียวเปรี้ยว
birthday_month = 6
birthday_day = 19

# วันเกิดปีนี้
this_year_birthday = datetime.date(today.year, birthday_month, birthday_day)

# ถ้าวันเกิดปีนี้ผ่านไปแล้ว → ใช้ปีหน้าแทน
if this_year_birthday < today.date():
    next_birthday = datetime.date(today.year + 1, birthday_month, birthday_day)
else:
    next_birthday = this_year_birthday

# คำนวณเวลาที่เหลือ
countdown = datetime.datetime.combine(next_birthday, datetime.time(0, 0), tzinfo=ZoneInfo("Asia/Bangkok")) - today

days_left_birthday = countdown.days
hours_left_birthday, remainder_birthday = divmod(countdown.seconds, 3600)
minutes_left_birthday, seconds_left_birthday = divmod(remainder_birthday, 60)
####################################################################################################
# ========================
# 🎀 ตกแต่งหน้าเว็บ
# ========================
st.set_page_config(page_title="💘 Love Letter to Preaw", page_icon="💌")

page_bg = """
<style>
.stApp {
    background: linear-gradient(135deg, #ffe6f0, #fff0f5, #e6f0ff);
    background-attachment: fixed;
}
h1, h2, h3, p {
    font-family: "Tahoma", "sans-serif";
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.markdown(
    f"<h1 style='text-align: center; color: deeppink;'>🌹 รักเธอนะครับคุณแฟน☺️ AKA คนน่ารัก 🌹</h1>",
    unsafe_allow_html=True
)

st.markdown("<h3 style='text-align: center;'>💕💕💕</h3>", unsafe_allow_html=True)
# ========================
# 🎶 เพลงเปิดอัตโนมัติ
# ========================
st.markdown(
    """
    <div style="text-align: center;">
        <iframe width="320" height="180" src="https://www.youtube.com/embed/5YKBgBMynbI?autoplay=1&loop=1&playlist=5YKBgBMynbI"
        frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
    </div>
    """,
    unsafe_allow_html=True
)
# ========================
# 🎀 วันที่ และนับวัน
# ========================
st.markdown(
    f"<p style='text-align: center; font-size: 18px;'>📅 วันนี้: <b>{today.strftime('%d %B %Y')}</b></p>",
    unsafe_allow_html=True
)

# วันแรกที่คบกัน
st.markdown(
    f"<p style='text-align: center; font-size: 18px; color: deeppink; '>💞 วันแรกที่เราเป็นแฟนกันคือ <b>{first_girlfriend_date.strftime('%d %B %Y %H:%M')}</b></p>",
    unsafe_allow_html=True
)

st.markdown(
    f"<p style='text-align: center; font-size: 20px; color: hotpink;'>💘 เรารู้จักกันมาแล้ว <b>{days_since} วัน</b> 💘</p>",
    unsafe_allow_html=True
)

st.markdown(
    f"<p style='text-align: center; font-size: 18px; color: deeppink;'>💐 เราเป็นแฟนกันแล้วนะ {days_girlfriend} วัน {hours_girlfriend} ชั่วโมง {minutes_girlfriend} นาที</p>",
    unsafe_allow_html=True
)
# # ========================
# # 🎀 Progress Bar ความรัก
# # ========================
# # ตั้ง milestone ครบรอบ (เช่น 100 วันถัดไป)
# next_milestone = ((days_girlfriend // 100) + 1) * 100
# progress = days_girlfriend / next_milestone

# st.markdown("### 📊 Progress ความรักของเรา")
# st.progress(progress)
# st.markdown(
#     f"<p style='text-align:center; font-size:16px;'>"
#     f"อีก {next_milestone - days_girlfriend} วัน จะครบ {next_milestone} วัน 🎉"
#     f"</p>",
#     unsafe_allow_html=True
# )

# ========================
# 🎀 ปฏิทิน Anniversary
# ========================
st.markdown("### 📅 ปฏิทิน Anniversary")

anniversaries = {
    "ครบ 100 วัน": first_girlfriend_date.date() + datetime.timedelta(days=100),
    "ครบ 1 ปี": first_girlfriend_date.date() + datetime.timedelta(days=365),
}

for title, date in anniversaries.items():
    days_left = (date - today.date()).days
    if days_left > 0:
        st.markdown(f"💖 {title}: {date.strftime('%d %B %Y')} (อีก {days_left} วัน)")
    else:
        st.markdown(f"💖 {title}: {date.strftime('%d %B %Y')} (ผ่านมาแล้ว {abs(days_left)} วัน)")
        
# ========================
# 🎂 นับถอยหลังวันเกิดแฟน
# ========================
st.markdown("### 🎂 อันนี้นับถอยหลังวันเกิดแฟนนะ💕")

st.markdown(
    f"<p style='font-size:18px; text-align:center; color:purple;'>"
    f"เหลืออีก <b>{days_left_birthday} วัน {hours_left_birthday} ชั่วโมง {minutes_left_birthday} นาที</b> "
    f"ก็จะถึงวันเกิดของ {her_name} 🎉🎂</p>",
    unsafe_allow_html=True
)
st.progress((365 - days_left) / 365)  # bar ความใกล้วันเกิด
####################################################################################################
# ========================
# 🔑 ตั้งค่า Google Sheets
# ========================
scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

# โหลด JSON จาก st.secrets
creds_dict = json.loads(st.secrets["google"]["service_account"])

# สร้าง Credentials และ authorize
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
client = gspread.authorize(creds)

# เปิด Google Sheet
spreadSheet = client.open_by_key("1LG2wqUEfMdeonWDUfS7ADLXYMBiF2C1wYXKA0gEaFXw")
sheet_wedding_day = spreadSheet.sheet1
# ========================
# 💍 โหลดวันแต่งงานจาก Sheet
# ========================
def load_wedding_date():
    try:
        date_str = sheet_wedding_day.acell("A1").value  # อ่าน cell A1
        if date_str:
            return datetime.date.fromisoformat(date_str)
    except:
        return None

# ========================
# 💍 บันทึกวันแต่งงานลง Sheet
# ========================
def save_wedding_date(date):
    sheet_wedding_day.update("A1", [[date.isoformat()]])

# ========================
# 💖 Streamlit UI
# ========================

saved_wedding_date = load_wedding_date()
default_wedding_date = saved_wedding_date if saved_wedding_date else today

st.markdown("### 💍 อันนี้เป็นวันแต่งงานของเราทั้งคู่นะ💕")

wedding_date = st.date_input(
    "เลือกวันแต่งงานของเราตามใจคนน่ารักเลยนะ 💖",
    value=default_wedding_date,
    min_value=today
)

if wedding_date != saved_wedding_date:
    save_wedding_date(wedding_date)

# แสดงผล
if wedding_date > today.date():
    days_to_wedding = (wedding_date - today.date()).days
    st.markdown(
        f"<p style='font-size:18px; text-align:center; color:green;'>"
        f"อีก <b>{days_to_wedding} วัน</b> จะถึงวันแต่งงานของเรา 💍✨</p>",
        unsafe_allow_html=True
    )
    progress_value = max(0.0, min(1.0, 1 - (days_to_wedding / 365)))
    st.progress(progress_value)
elif wedding_date == today.date():
    st.markdown(
        "<p style='font-size:20px; text-align:center; color:red;'>"
        "💖 วันนี้คือวันแต่งงานของเราแล้วนะ 🎉💍</p>",
        unsafe_allow_html=True
    )
    st.balloons()
else:
    days_since_wedding = (today.date() - wedding_date).days
    st.markdown(
        f"<p style='font-size:18px; text-align:center; color:blue;'>"
        f"เราแต่งงานกันแล้วนะ <b>{days_since_wedding} วันงับผม</b> 🥰</p>",
        unsafe_allow_html=True
    )
####################################################################################################

# ========================
# 🎀 ลายเซ็น
# ========================
st.markdown("---")
answer = st.radio("❓ วันเกิดแฟนเปรี้ยววันไหนเอ่ย?", ["7 มีนาคม", "25 พฤศจิกายน", "24 พฤศจิกายน"])
if answer == "25 พฤศจิกายน":
    st.success("รักนะงับที่จำกันได้ เอ๊ะ? หรือกดหลายรอบกันนะ🥰")
    st.balloons()
else:
    st.error("ผิดน้าา งอนๆๆๆ 💕")

# ========================
# 🎀 ปุ่มพิเศษ
# ========================
if st.button("💖 คลิกตรงนี้นะครับเปรียวเปรี้ยว 💖"):
    st.balloons()
    st.markdown("### 💕 เราจะมีแค่เธอนะคนน่ารัก 💕")
    st.image("preaw_preaw2.gif", caption="คนนี้แฟนของผมครับ🧑🏻‍❤️‍💋‍👩🏻")

st.markdown("""
<div class="hearts">
  <span>💖</span>
  <span>💞</span>
  <span>💕</span>
  <span>💘</span>
  <span>💓</span>
  <span>❤️</span>
  <span>💗</span>
  <span>💝</span>
</div>

<style>
.hearts {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  overflow: hidden;
  z-index: 9999;
}

.hearts span {
  position: absolute;
  top: -10%;
  font-size: 24px;
  animation: fall 8s linear infinite;
  opacity: 0.8;
}

/* สุ่มตำแหน่งและเวลาการร่วง */
.hearts span:nth-child(1) { left: 10%; animation-delay: 0s; }
.hearts span:nth-child(2) { left: 25%; animation-delay: 2s; font-size:28px; }
.hearts span:nth-child(3) { left: 40%; animation-delay: 4s; font-size:20px; }
.hearts span:nth-child(4) { left: 55%; animation-delay: 1s; }
.hearts span:nth-child(5) { left: 70%; animation-delay: 3s; font-size:30px; }
.hearts span:nth-child(6) { left: 85%; animation-delay: 5s; }
.hearts span:nth-child(7) { left: 50%; animation-delay: 6s; font-size:22px; }
.hearts span:nth-child(8) { left: 15%; animation-delay: 7s; font-size:26px; }

@keyframes fall {
  0% { transform: translateY(-10%); opacity: 1; }
  100% { transform: translateY(110vh); opacity: 0; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("### 📝 บอร์ดข้อความของเราทั้งคู่นะ")

sheet_chat = spreadSheet.worksheet("sheet2")
message = st.text_area("มีอะไรในใจก็เขียนได้นะงับ 💕", "")
# ตั้งชื่อฝั่งเรา
MY_NAME = "เปรี้ยว"
PARTNER_NAME = "ไตไต๋"

# เลือกผู้ส่ง (ปกติหน้าเว็บเราเป็นเรา)
sender = st.selectbox("คุณกำลังส่งข้อความเป็นใคร?", [MY_NAME, PARTNER_NAME])

if st.button("ส่งข้อความ 💌"):
    if message.strip():
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sheet_chat.append_row([timestamp, sender, message])
        st.success(f"ส่งข้อความเรียบร้อยแล้ว 💖 (โดย {sender})")
    else:
        st.error("กรุณาใส่ข้อความก่อนนะครับ 🥹")

# แสดงข้อความแบบ Chat
rows = sheet_chat.get_all_values()
st.markdown("---")
for row in rows:
    timestamp = row[0] if len(row) > 0 else ""
    sender_name = row[1] if len(row) > 1 else "ไม่ทราบชื่อ"
    text = row[2] if len(row) > 2 else ""

    if sender_name == MY_NAME:
        # ข้อความเรา สีชมพู ขวา
        st.markdown(
            f"<p style='text-align:right; color:deeppink;'>"
            f"🕒 <b>{timestamp}</b> — <b>{sender_name}</b><br>"
            f"{text}</p>", 
            unsafe_allow_html=True
        )   
    else:
        # ข้อความแฟน สีม่วง ซ้าย
        st.markdown(
            f"<p style='text-align:left; color:purple;'>"
            f"🕒 <b>{timestamp}</b> — <b>{sender_name}</b><br>"
            f"{text}</p>", 
            unsafe_allow_html=True
        )

st.caption("ด้วยรักจาก ไตไต๋ 💕")