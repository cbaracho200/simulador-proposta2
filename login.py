import hmac
import streamlit as st



# Função para realizar login usando HMAC para verificar a senha
def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets["passwords"] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            st.session_state["authenticated_user"] = st.session_state["username"]  # Armazena o nome do usuário na sessão
            del st.session_state["password"]  # Não armazena a senha.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    with st.sidebar:
        login_form()
        if "password_correct" in st.session_state and not st.session_state["password_correct"]:
            st.error("😕 senha errada!")
        return False
