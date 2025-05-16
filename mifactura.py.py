import streamlit as st

st.set_page_config(page_title="MiFactura", layout="centered")

st.title("🧾 MiFactura")

st.subheader("Generar nueva factura")

# --- Formulario para capturar datos ---
with st.form("factura_form"):
    nombre = st.text_input("Nombre completo")
    cedula = st.text_input("Cédula")
    correo = st.text_input("Correo electrónico")
    celular = st.text_input("Número de celular")
    establecimiento = st.text_input("Establecimiento")

    enviar_correo = st.checkbox("✅ Enviar copia al correo")
    guardar_copia = st.checkbox("✅ Guardar copia en la app", value=True)

    generar = st.form_submit_button("GENERAR FACTURA")

# --- Resultado si se genera la factura ---
if generar:
    st.success("✅ ¡Factura generada con éxito!")
    st.markdown(f"""
    *Nombre:* {nombre}  
    *Cédula:* {cedula}  
    *Correo:* {correo}  
    *Celular:* {celular}  
    *Establecimiento:* {establecimiento}  
    """)
