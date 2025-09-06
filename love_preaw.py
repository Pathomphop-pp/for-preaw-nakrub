import streamlit as st
import datetime
import random

# ========================
# 🎀 ตั้งค่า
# ========================

# ชื่อ
her_name = "เปรียวเปรี้ยว 💖"

# วันแรกที่เจอกัน (เก็บแค่วันที่)
first_meet_date = datetime.date(2025, 3, 9)

# วันแรกที่คบกัน (เก็บวัน + เวลา)
first_girlfriend_date = datetime.datetime(2025, 9, 5, 23, 55, 0)

# วันนี้
today = datetime.datetime.now()

# จำนวนวัน
days_since = (today.date() - first_meet_date).days
# date_time_girlfriend = (today - first_girlfriend_date).days
date_time_girlfriend = (today - first_girlfriend_date)

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
        <iframe width="300" height="180" src="https://www.youtube.com/embed/M8Ao4NeNhFE?autoplay=1&loop=1&playlist=xkNAtS7_l9o"
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

st.markdown(
    f"<p style='text-align: center; font-size: 20px; color: hotpink;'>💘 เรารู้จักกันมาแล้ว <b>{days_since} วัน</b> 💘</p>",
    unsafe_allow_html=True
)

st.markdown(
    f"<p style='text-align: center; font-size: 20px; color: hotpink;'>💐 เราเป็นแฟนกันแล้ว <b>{date_time_girlfriend} วัน รู้มั้ยครับ</b> 💐</p>",
    unsafe_allow_html=True
)

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
