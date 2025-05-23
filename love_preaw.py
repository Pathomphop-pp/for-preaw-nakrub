import streamlit as st
import datetime
import random

# ชื่อสาวที่คุณอยากจีบ
her_name = "Preaw"

# ข้อความหวาน ๆ
love_messages = [
    "เธอรู้มั้ย? เธอคือเหตุผลที่เรายิ้มทุกวัน 😊",
    "อรุณสวัสดิ์ยามเช้างับผม 💻❤️",
    "ขอแค่ Preaw คืนดี เรายอมเธอทุกอย่างเลย ☺️",
    "คืนดีกันนะครับ 🤟",
    "แคร์คุณ Preaw นะครับ 🙂",
    "ฝันดีนะ 😪",
    "ชอบนะครับ",
    "คิดถึงนะครับคนน่ารัก",
    "ไปกินข้าวกันนะขอจอง 2 วันเลย"
]

# หน้าเว็บ
st.title("🌹 ถึงเธอนะ " + her_name)
st.write("วันนี้เป็นอีกวัน... ที่เราคิดถึงเธอออ 🥲")

# แสดงวันที่
today = datetime.date.today()
st.write(f"📅 วันที่: {today.strftime('%d %B %Y')}")

# ข้อความสุ่ม
st.markdown("### ข้อความจากใจ 💌")
st.success(random.choice(love_messages))

# ปุ่มเพิ่มความน่ารัก
if st.button("กดตรงนี้ 🪄"):
    st.balloons()
    st.write("กลับมาคุยกันได้มั้ยครับ 😊")

# ลายเซ็น
st.markdown("---")
st.caption("สร้างด้วยใจและ Python โดยคนที่ตกหลุมรักคุณทุกวัน 💻💘")
