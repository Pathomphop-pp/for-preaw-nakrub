import streamlit as st
import datetime
import random

# ========================
# 🎀 ตั้งค่า
# ========================

# ชื่อ
her_name = "เปรียวเปรี้ยว 💖"

# วันแรกที่เจอกัน
first_meet_date = datetime.date(2023, 7, 15)  # <<< ใส่วันจริงที่คุณเจอกันนะครับ
today = datetime.date.today()
days_since = (today - first_meet_date).days

# ข้อความรัก
love_messages = [
    "อย่าลืมสำลีก้านนะงับ",
    "สู้ๆนะคนน่ารักทำรีพอร์ทก็ไม่มีอะไรแล้วงับมีแค่สอนงาน",
    "อยากกินแซนด์วิชด้วยจังงับ",
    "มีอะไรให้เราช่วยก็บอกนะงับ😊",
    "https://www.youtube.com/watch?v=xkNAtS7_l9o&list=RDxkNAtS7_l9o&start_radio=1"
]

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
    f"<h1 style='text-align: center; color: deeppink;'>🌹 คิดถึงเรามั้ยครับ {her_name} AKA คนน่ารัก 🌹</h1>",
    unsafe_allow_html=True
)

st.markdown("<h3 style='text-align: center;'>💕💕💕</h3>", unsafe_allow_html=True)

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
    st.markdown("### 💕 ถึงยังไงเธอก็คือที่รักของเราทุกวันเลยนะครับ 💕")
    st.image("preaw_preaw.gif", caption="รักเธอนะครับคนน่ารักของเรา")

# ========================
# 🎀 ลายเซ็น
# ========================
st.markdown("---")
st.caption("🌹")
