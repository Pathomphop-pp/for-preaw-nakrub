import streamlit as st
import datetime
import random

# ให้เธอคนเดียวเลย
her_name = "Preaw"

# ข้อความก็ให้เธอ
love_messages = [
    # "เธอรู้มั้ย? เธอคือเหตุผลที่เรายิ้มทุกวัน 😊",
    "อรุณสวัสดิ์ยามเช้างับผม 💻❤️",
    "วันนี้น่ารักอีกแล้วนะครับ",
    "คิดถึงว่าที่แฟนนะ😉",
    "ไปกินชาบูกับเรานะที่รัก",
    "อยากกอดเธอนะจะจุ๊บให้ด้วย🫣",
    "พักผ่อนเยอะๆครับเป็นห่วงนะ",
    "gxHocaodyo,yhp 😗",
    "คิดถึงคนขี้งอนนะ",
    "เธอคือคนเดียวและคนแรกที่เราอยากอยู่ด้วยตั้งแต่มากทม.☺️",
    # "ขอแค่ Preaw คืนดี เรายอมเธอทุกอย่างเลย ☺️",
    # "คืนดีกันนะครับ 🤟",
    # "แคร์คุณ Preaw นะครับ 🙂",
    # "ฝันดีนะ 😪",
    # "ชอบนะครับ",
    # "คิดถึงนะครับคนน่ารัก",
    # "ไปกินข้าวกันนะขอจอง 2 วันเลย",
    # "นอนหลับสบายมั้ยครับ😊",
    # "อยากเจอเธอแล้วเนี่ย",
    # "ที่รักครับ💕",
    # "แฟนเราตื่นยังนะ",
    # "ถ้าเธอให้เราไปหาอีกเราไปจริงนะครับ😏",
    # "เปรียวเปรี้ยวคนน่ารักของเรา 🌹",
    # "ให้ครับ 💐",
    # "คิดถึงนะคนน่ารักของเรา",
    # "วันนี้สู้ๆครับ",
    # "เราชอบเธอนะครับ",
    # "วันนี้คิดถึงเธออย่างเดียวเลยครับ",
    # "อยากจุ๊บเธออะครับ😂",
    "มาอยู่กับเรามั้ยครับ💐",
    # "จีบนะครับ ถ้าไม่เดี๋ยวเราจีบใหม่",
    # "สวัสดีครับแฟนในอนาคต"
]

# หน้าเว็บ
st.title("🌹 ถึงเธอนะ " + her_name)
st.write("วันนี้เธอเหนื่อยใช่มั้ย ส่งพลังใจและความคิดถึงไปให้นะครับ 🧑🏻‍❤️‍💋‍👩🏻")

# แสดงวันที่
today = datetime.date.today()
st.write(f"📅 วันที่: {today.strftime('%d %B %Y')}")

# ข้อความสุ่ม
st.markdown("### ข้อความจากใจ 💌")
st.success(random.choice(love_messages))

# ปุ่มเพิ่มความน่ารัก
if st.button("กดตรงนี้ 🪄"):
    st.balloons()
    # st.write("กลับมาคุยกันได้มั้ยครับ 😊")
    st.write("อยากให้เธอจุ๊บจังเลยครับ😍")

# ลายเซ็น
st.markdown("---")
st.caption("สร้างด้วยใจและ Python โดยคนที่ตกหลุมรักเปรียวเปรี้ยวทุกวัน 💻💘")
