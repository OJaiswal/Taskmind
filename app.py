import streamlit as st
from password_validator import is_valid_password

st.title("🔐 Password Validator")

password = st.text_input("Enter your password:", type="password")

if st.button("Validate"):
    if is_valid_password(password):
        st.success("✅ Password is valid!")
    else:
        st.error("❌ Password is invalid. Please follow the rules below:")
        st.markdown("""
        - Must be **7 to 20 characters** long  
        - Must include at least one **uppercase letter**  
        - Must include at least one **lowercase letter**  
        - Must include at least one **digit (0-9)**  
        - Must include at least one **special character**: `!@#$`  
        - Must **not contain spaces**
        """)

