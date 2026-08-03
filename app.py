import streamlit as st

st.set_page_config(page_title="Recomendador de Alimentación Infantil", page_icon="🍼")

st.title("🍼 Recomendador de Alimentación Infantil")
st.write("Ingresa los datos solicitados a continuación:")

meses = st.number_input("Edad (en meses)", min_value=0.0, step=1.0, format="%.0f")
peso = st.number_input("Peso (en kg, ej. 7.5)", min_value=0.0, step=0.1)
altura = st.number_input("Altura/Talla (en cm, ej. 68)", min_value=0.0, step=0.5)

if st.button("Ver recomendaciones"):
    st.markdown("---")
    st.subheader(
        f"Resultados (Edad: {meses:.0f}m | Peso: {peso}kg | Altura: {altura}cm)"
    )

    if meses < 0:
        st.error("❌ La edad en meses no puede ser negativa.")

    elif meses < 6:
        st.markdown("### 🍼 Lactancia Exclusiva (0 a 5 meses)")
        st.markdown("**Alimentos permitidos:** Leche materna o fórmula infantil.")
        st.markdown(
            "**Notas:** El sistema digestivo aún no está listo para sólidos ni agua pura."
        )

    elif 6 <= meses <= 8:
        st.markdown("### 🥣 Inicio de Alimentación Complementaria (6 a 8 meses)")
        st.markdown(
            "**Consistencia:** Purés suaves, papillas o grumos muy blandos (si usas BLW)."
        )
        st.markdown("**Alimentos recomendados:**")
        st.markdown(
            "- Verduras cocidas: Zanahoria, auyama/calabaza, chayote, calabacín.\n"
            "- Frutas: Guineo/banano, manzana, pera, aguacate.\n"
            "- Proteínas: Pollo, carne de res o pavo bien cocida y licuada/desmenuzada.\n"
            "- Cereales: Arroz, avena, maíz (sin azúcar ni sal)."
        )
        st.markdown("**Frecuencia:** 2 a 3 comidas al día + leche (materna o fórmula).")

    elif 9 <= meses <= 11:
        st.markdown("### 🍌 Transición a Texturas e Integración (9 a 11 meses)")
        st.markdown(
            "**Consistencia:** Alimentos picados finamente, aplastados con tenedor o en bastones suaves."
        )
        st.markdown("**Alimentos recomendados:**")
        st.markdown(
            "- Todo lo anterior, sumando legumbres (lentejas, garbanzos cocidos y aplastados).\n"
            "- Huevo entero bien cocido, pescado blanco.\n"
            "- Trocitos de fruta suave (guineo, melón, sandía)."
        )
        st.markdown("**Frecuencia:** 3 a 4 comidas al día + snacks saludables.")

    elif 12 <= meses <= 23:
        st.markdown("### 🍲 Alimentación Familiar Adaptada (12 a 23 meses)")
        st.markdown(
            "**Consistencia:** Comida de la mesa familiar (picada en trozos pequeños)."
        )
        st.markdown("**Alimentos recomendados:**")
        st.markdown(
            "- Dieta variada: Cereales integrales, carnes, pescados, verduras, frutas y legumbres.\n"
            "- Se pueden incorporar lácteos enteros (leche entera, queso pasteurizado, yogur natural sin azúcar)."
        )
        st.markdown(
            "**Restricciones:** Evitar frutos secos enteros (riesgo de asfixia), ultraprocesados y sal/azúcar en exceso."
        )

    else:
        st.markdown("### 🥗 Alimentación Completa de la Etapa Infantil (2+ años)")
        st.markdown("**Consistencia:** Dieta familiar regular equilibrada y variada.")
        st.markdown("**Alimentos recomendados:**")
        st.markdown(
            "- Proteínas de calidad, frutas frescas, verduras de todos los colores, "
            "granos enteros y grasas saludables (aguacate, aceite de oliva)."
        )
        st.markdown("**Consejo:** Limitar bebidas azucaradas y mecatos.")

    st.markdown("---")
    st.warning(
        "⚠️ **Evitar siempre en menores de 12 meses:**\n"
        "- Miel de abejas (riesgo de botulismo).\n"
        "- Sal y azúcares añadidos.\n"
        "- Leche entera de vaca directa."
    )
