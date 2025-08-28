import mysql.connector
import streamlit as st
from mysql.connector import Error

# Hàm tạo kết nối
def get_connection():
    try:
        conn = mysql.connector.connect(
            host=st.secrets["mysql"]["host"],
            port=int(st.secrets["mysql"]["port"]),
            database=st.secrets["mysql"]["database"],
            user=st.secrets["mysql"]["user"],
            password=st.secrets["mysql"]["password"]
        )
        if conn.is_connected():
            return conn
    except Error as e:
        st.error(f"❌ Lỗi khi kết nối MySQL Railway: {e}")
        return None

# Hàm đóng kết nối
def close_connection(conn):
    if conn and conn.is_connected():
        conn.close()

# ===================== LOG HOẠT ĐỘNG =====================
def add_log(user_id, action, details=""):
    try:
        conn = get_connection()
        if conn is None:
            return
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO activity_logs (user_id, action, details) 
            VALUES (%s, %s, %s)
            """,
            (user_id, action, details)
        )
        conn.commit()
        cursor.close()
        close_connection(conn)
        # ❌ Không in st.write ở đây
    except Error as e:
        st.error(f"❌ Lỗi khi ghi log: {e}")
