import streamlit as st
import datetime
import random

# เป้าหมายของหัวใจ
her_name = "เปรียวเปรี้ยว 💖"

# รายชื่อข้อความรักที่ถูกสุ่มขึ้นมาทุกครั้ง
love_messages = [
    "อรุณสวัสดิ์ครับที่รัก ☀️ ขอให้วันนี้สดใสเหมือนรอยยิ้มของเธอเลยนะครับ 🌸",
    "ตื่นหรือยังครับคนน่ารัก 😘 วันนี้เราคิดถึงเธอตั้งแต่ลืมตาเลยนะ",
    "อย่าลืมกินข้าวนะครับ 💕 เพราะเรารักเธอมากจนอยากให้เธอแข็งแรงอยู่เสมอ",
    "รักเธอนะครับ มากกว่าดวงจันทร์ 🌙 และดวงดาวทุกดวงบนฟ้า ⭐️",
    "นอนได้แล้วนะครับ ฝันดี ฝันถึงเราด้วยนะ 💭💘",
    "อยากเจอเธอจังเลยครับ 😚 ถ้าเจอจะกอดแน่นๆเลย",
    "แค่ได้คิดถึงเธอก็ทำให้วันนี้สดใสขึ้นมาเลยครับ 💐",
    "เธอเป็นความสุขเล็กๆ ที่แสนยิ่งใหญ่ของเราเลยนะ 🥹",
    "จีบเธอทุกวันได้มั้ยครับ ถึงจะเป็นแฟนแล้วก็เถอะ 😘",
    "รักนะครับ คนเดียวในใจเราตอนนี้ก็คือเธอ 🫶"
]

# แสดงหน้าเว็บ
st.set_page_config(page_title="💘 Love Letter to Preaw", page_icon="💌")
st.markdown(
    f"<h1 style='text-align: center; color: pink;'>🌹 คิดถึงนะ {her_name} 🌹</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center;'>ทุกวันของเรามีความหมาย เพราะมีเธออยู่ในใจ 💞</h3>",
    unsafe_allow_html=True
)

# วันที่
today = datetime.date.today()
st.markdown(
    f"<p style='text-align: center; font-size: 18px;'>📅 วันนี้: <b>{today.strftime('%d %B %Y')}</b></p>",
    unsafe_allow_html=True
)

# ข้อความรักจากใจ
st.markdown("---")
st.markdown("### 💌 ข้อความรักจากใจของไตไต๋:")
st.success(random.choice(love_messages))

# ปุ่มวิเศษ
if st.button("💖 คลิกตรงนี้ถ้ารักเปรียวเปรี้ยว 💖"):
    st.balloons()
    st.markdown("### 🥰 เธอคือความมหัศจรรย์ที่เรารักทุกวันเลยนะครับ 💕")
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXU4dm12dG1mZGZpa2MxamR6bmNtc21yNzh2eWl5eHdscjdoZjY0YyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3ohhwmQJ2NR9sFLwNu/giphy.gif", width=300)

# ลายเซ็น
st.markdown("---")
st.caption("สร้างด้วย Python และความคลั่งรัก 💘 โดยไตไต๋ผู้หลงรักเปรียวเปรี้ยวทุกวัน 🌷")
