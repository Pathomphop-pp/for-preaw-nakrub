import streamlit as st
import datetime
import random

# เป้าหมายของหัวใจ
her_name = "เปรียวเปรี้ยว 💖"

# รายชื่อข้อความรักที่ถูกสุ่มขึ้นมาทุกครั้ง
love_messages = [
    "อรุณสวัสดิ์ครับที่รัก ☀️ ขอให้วันนี้สดใสเหมือนรอยยิ้มของเธอเลยนะครับ 🌸",
    "ตื่นหรือยังครับคนน่ารัก 😘 วันนี้เราคิดถึงเธอตั้งแต่ลืมตาเลยนะ",
    "อย่าลืมกินข้าวนะครับ 💕 เพราะเรารักเธอมากจนอยากให้เธอแข็งแรงอยู่เสมองับ",
    # "รักเธอนะครับ มากกว่าดวงจันทร์ 🌙 และดวงดาวทุกดวงบนฟ้า ⭐️",
    # "นอนได้แล้วนะครับ ฝันดี ฝันถึงเราด้วยนะ 💭💘",
    "อยากเจอเธอจังเลยครับ 😚 ถ้าเจอจะกอดแน่นๆเลย",
    # "แค่ได้คิดถึงเธอก็ทำให้วันนี้สดใสขึ้นมาเลยครับ 💐",
    # "เธอเป็นความสุขเล็กๆ ที่แสนยิ่งใหญ่ของเราเลยนะ 🥹",
    "จีบเธอทุกวันได้มั้ยครับ😘",
    "รักนะครับ คนเดียวในใจเราตอนนี้ก็คือเธอ 💐",
    "วันนี้เราทำงานแต่ทักมาได้ตลอดนะงับ",
    "https://www.youtube.com/watch?v=tjKEo-DBuAI"
]

# แสดงหน้าเว็บ
st.set_page_config(page_title="💘 Love Letter to Preaw", page_icon="💌")
st.markdown(
    f"<h1 style='text-align: center; color: pink;'>🌹 คิดถึงนะ {her_name} 🌹</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<h3 style='text-align: center;'>ในใจของเราของไตไต๋ไม่ว่าง เพราะมีเธออยู่ในใจ 💞</h3>",
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
if st.button("💖 คลิกตรงนี้ถ้าเปรียวเปรี้ยวคิดถึง 💖"):
    st.balloons()
    st.markdown("### 💕 เธอคือที่รักของเราทุกวันเลยนะครับ 💕")
    st.image("preaw_preaw.gif", caption="คิดถึงเธอตลอดเวลาเลยนะ")
# ลายเซ็น
st.markdown("---")
st.caption("สร้างด้วยใจและความรัก 💘 โดยไตไต๋ผู้หลงรักเปรียวเปรี้ยวทุกวัน 🌷")
