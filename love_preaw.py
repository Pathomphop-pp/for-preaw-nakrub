import streamlit as st
import datetime
import random
from zoneinfo import ZoneInfo

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
        <iframe width="300" height="180" src="https://www.youtube.com/embed/M8Ao4NeNhFE?autoplay=1&loop=1&playlist=M8Ao4NeNhFE"
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
# ========================
# 🎀 Progress Bar ความรัก
# ========================
# ตั้ง milestone ครบรอบ (เช่น 100 วันถัดไป)
next_milestone = ((days_girlfriend // 100) + 1) * 100
progress = days_girlfriend / next_milestone

st.markdown("### 📊 Progress ความรักของเรา")
st.progress(progress)
st.markdown(
    f"<p style='text-align:center; font-size:16px;'>"
    f"อีก {next_milestone - days_girlfriend} วัน จะครบ {next_milestone} วัน 🎉"
    f"</p>",
    unsafe_allow_html=True
)

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
# 🎀 ข้อความรัก
# ========================
st.markdown("---")
st.markdown("### 💌 ข้อความจากใจของไตไต๋:")
st.success(random.choice(love_messages))

# ========================
# 🎀 ปุ่มพิเศษ
# ========================
if st.button("💖 คลิกตรงนี้นะครับเปรียวเปรี้ยว 💖"):
    st.balloons()
    st.markdown("### 💕 เราจะมีแค่เธอนะคนน่ารัก 💕")
    st.image("preaw_preaw2.gif", caption="คนนี้แฟนของผมครับ🧑🏻‍❤️‍💋‍👩🏻")

# ========================
# 🎀 ลายเซ็น
# ========================
st.markdown("---")
st.caption("💐")
st.caption("ด้วยรักจาก ไตไต๋ 💕")
