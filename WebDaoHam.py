import streamlit as st
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="SONthongphatthanhhuy - Math")
st.title("🚀 Hệ thống SONthongphatthanhhuy")
st.subheader("Trình giải Đạo hàm & Vẽ đồ thị lớp 12")

user_input = st.text_input("Nhập hàm số (Ví dụ: 3*x**2 + 5*x - 2):", "x**2")

if user_input:
    try:
        x = sp.symbols('x')
        f_expr = sp.sympify(user_input.replace('^', '**'))
        f_prime = sp.diff(f_expr, x)
        
        st.write("---")
        col1, col2 = st.columns(2)
        with col1:
            st.info("Hàm số gốc $f(x)$:")
            st.latex(sp.latex(f_expr))
        with col2:
            st.success("Đạo hàm $f'(x)$:")
            st.latex(sp.latex(f_prime))
            
        st.write("### Đồ thị minh họa")
        f_np = sp.lambdify(x, f_expr, 'numpy')
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f_np(x_vals)
        
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label=f"y = {user_input}", color='blue', lw=2)
        ax.axhline(0, color='black', lw=1)
        ax.axvline(0, color='black', lw=1)
        ax.grid(True, linestyle=':', alpha=0.6)
        st.pyplot(fig)
        
    except Exception as e:
        st.error(f"Sơn ơi kiểm tra lại cách nhập! Lỗi: {e}")

st.write("---")
st.caption("Dự án Nhóm 5 - SONthongphatthanhhuy - Ngày 09/04/2026")