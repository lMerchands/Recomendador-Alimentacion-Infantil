import json

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Creciendo juntos by Michelle 🍊",
    page_icon="🍊",
    layout="centered",
)

# ------------------------------------------------------------------
# ESTILOS
# ------------------------------------------------------------------
st.markdown(
    """
    <style>
    .stApp { background-color: #FFFBEB; }
    .cj-header {
        background: linear-gradient(90deg, #059669, #22C55E, #059669);
        color: white;
        padding: 1.5rem 1.25rem;
        border-radius: 16px;
        margin-bottom: 1.25rem;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    .cj-header h1 { margin: 0; font-size: 1.8rem; }
    .cj-header p { margin: 0.15rem 0 0 0; opacity: 0.95; }
    .cj-card {
        background: white;
        border: 1px solid #A7F3D0;
        border-radius: 16px;
        padding: 1.25rem;
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }
    .cj-answer {
        background: #ECFDF5;
        border-left: 4px solid #10B981;
        border-radius: 0 12px 12px 0;
        padding: 1rem;
        margin-top: 0.75rem;
    }
    .cj-footer {
        text-align: center;
        color: #94A3B8;
        font-size: 0.75rem;
        margin-top: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def hablar(texto: str, key: str) -> None:
    """Botón que usa la síntesis de voz del navegador para leer un texto."""
    components.html(
        f"""
        <button
            onclick="
                window.speechSynthesis.cancel();
                var u = new SpeechSynthesisUtterance({json.dumps(texto)});
                u.lang = 'es-ES';
                u.rate = 0.9;
                u.pitch = 1.05;
                window.speechSynthesis.speak(u);
            "
            style="
                background:#059669;color:white;border:none;border-radius:8px;
                padding:6px 12px;font-size:12px;font-weight:bold;cursor:pointer;
            "
        >🔊 Escuchar a Michelle</button>
        """,
        height=40,
    )


# ------------------------------------------------------------------
# DATOS
# ------------------------------------------------------------------
FRASES_MOTIVACIONALES = [
    "Lo estás haciendo increíble, Mamá. Tu amor es el mejor regalo para tu bebé 🧡",
    "Tu dedicación diaria nutre la vida y la seguridad de tu bebé. Eres extraordinaria ✨",
    "Un día a la vez, Mamá. Estás construyendo un camino lleno de luz y felicidad 🍊",
    "Confía en tu instinto. Eres la persona más especial y capacitada para cuidar a tu bebé 💕",
    "Recuerda cuidarte y consentirte también. Tu bienestar es la base de todo 🍊",
]

FAQ = [
    {
        "pregunta": "¿Con qué frecuencia debe amamantar un recién nacido?",
        "respuesta": "durante las primeras semanas los recién nacidos deben alimentarse a demanda, generalmente cada 2 a 3 horas (de 8 a 12 veces al día).",
        "imagen": "https://images.unsplash.com/photo-1555252333-9f8e92e65df9?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Cuántas horas debe dormir un bebé según su edad?",
        "respuesta": "un recién nacido duerme entre 14 y 17 horas al día, mientras que a partir de los 6 meses duermen entre 12 y 15 horas, incluyendo siestas.",
        "imagen": "https://images.unsplash.com/photo-1519689680058-324335c77eba?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Cuándo se debe iniciar la alimentación complementaria?",
        "respuesta": "la OMS recomienda iniciar la alimentación complementaria a partir de los 6 meses de edad, manteniendo la lactancia materna.",
        "imagen": "https://images.unsplash.com/photo-1596461404969-9ae70f2830c1?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Es normal que el bebé pierda peso al nacer?",
        "respuesta": "es completamente normal que los bebés pierdan hasta un 10% de su peso en los primeros días de vida. Suelen recuperarlo en 10 a 14 días.",
        "imagen": "https://images.unsplash.com/photo-1516627145497-ae6968895b74?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Cómo sé si mi bebé está comiendo lo suficiente?",
        "respuesta": "la mejor señal es que el bebé moje al menos 5 o 6 pañales al día y gane peso de manera constante según sus controles médicos.",
        "imagen": "https://images.unsplash.com/photo-1544126592-807ade215a0b?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Qué debo hacer si el bebé tiene cólicos?",
        "respuesta": "puede realizar masajes suaves en la pancita en el sentido de las agujas del reloj o hacer el movimiento de 'bicicleta' con sus piernas.",
        "imagen": "https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Cuándo aparece el primer diente del bebé?",
        "respuesta": "el primer diente suele salir entre los 4 y 7 meses, aunque el rango es amplio. Generalmente los primeros son los incisivos inferiores.",
        "imagen": "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Cómo cuidar el muñón umbilical?",
        "respuesta": "se debe mantener limpio y seco. Se lava con agua y jabón neutro durante el baño, secándolo muy bien y dejándolo al aire libre.",
        "imagen": "https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Cuándo debe empezar a gatear un bebé?",
        "respuesta": "la mayoría de los bebés comienzan a gatear entre los 7 y 10 meses, aunque algunos bebés pasan directamente a ponerse de pie.",
        "imagen": "https://images.unsplash.com/photo-1476703993599-0035a21b17a9?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Qué vacunas necesita el bebé en sus primeros meses?",
        "respuesta": "el esquema varía según el país, pero generalmente al nacer reciben BCG y Hepatitis B, y a los 2, 4 y 6 meses la pentavalente/hexavalente.",
        "imagen": "https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Cuándo se considera que el bebé tiene fiebre?",
        "respuesta": "se considera fiebre cuando la temperatura corporal medida en la axila es de 38°C o más. En este caso debe consultar al pediatra.",
        "imagen": "https://images.unsplash.com/photo-1576765608535-5f04d1e3f289?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Qué es la crisis o brote de crecimiento?",
        "respuesta": "son etapas donde el bebé demanda más alimento porque necesita aumentar la producción de leche para su rápido desarrollo.",
        "imagen": "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Cómo prevenir la otitis en el bebé?",
        "respuesta": "se previene evitando acostar al bebé con el biberón y manteniendo al bebé alejado del humo del tabaco.",
        "imagen": "https://images.unsplash.com/photo-1516627145497-ae6968895b74?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Cómo cortar las uñas del bebé con seguridad?",
        "respuesta": "use cortaúñas o tijeras especiales de punta redonda para bebés, preferiblemente cuando el bebé esté dormido o muy tranquilo.",
        "imagen": "https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿A qué edad empiezan a hablar los bebés?",
        "respuesta": "las primeras palabras con significado ('mamá', 'papá') suelen aparecer entre los 10 y 14 meses, aunque el balbuceo inicia a los 6 meses.",
        "imagen": "https://images.unsplash.com/photo-1519689680058-324335c77eba?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Qué hacer si mi bebé tiene dermatitis del pañal?",
        "respuesta": "debe cambiar el pañal con frecuencia, aplicar cremas de barrera con óxido de zinc y dejar la zona al aire libre el mayor tiempo posible.",
        "imagen": "https://images.unsplash.com/photo-1544126592-807ade215a0b?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Cuándo puede tomar agua el bebé?",
        "respuesta": "antes de los 6 meses no necesitan agua si toman leche materna o de fórmula exclusiva. Se introduce con la alimentación complementaria.",
        "imagen": "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Es normal que el bebé regurgite después de comer?",
        "respuesta": "es cierto y muy común debido a la inmadurez de su esfínter esofágico. Si el bebé no muestra dolor y gana peso, no es de preocupación.",
        "imagen": "https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Cómo ayudar al bebé a conciliar el sueño?",
        "respuesta": "es recomendable establecer rutinas constantes antes de dormir (baño, masaje, cuento) y mantener la habitación a temperatura agradable.",
        "imagen": "https://images.unsplash.com/photo-1519689680058-324335c77eba?auto=format&fit=crop&w=800&q=80",
    },
    {
        "pregunta": "¿Cuándo llevar al bebé a urgencias?",
        "respuesta": "acuda de inmediato si presenta fiebre mayor a 38°C (especialmente en menores de 3 meses), dificultad para respirar, letargo o vómitos.",
        "imagen": "https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?auto=format&fit=crop&w=800&q=80",
    },
]

RUTINAS_ESTIMULACION = [
    (3, "0 a 3 meses", "Tummy Time boca abajo.", "Masajes suaves tras el baño.", "Seguimiento visual con objetos de colores.",
     "https://images.unsplash.com/photo-1555252333-9f8e92e65df9?auto=format&fit=crop&w=800&q=80"),
    (6, "4 a 6 meses", "Ejercicio de bicicleta con las piernas.", "Estimular el giro con juguetes a los lados.", "Sonajeros con distintas texturas.",
     "https://images.unsplash.com/photo-1515488042361-ee00e0ddd4e4?auto=format&fit=crop&w=800&q=80"),
    (9, "7 a 9 meses", "Incentivo al gateo con objetos a corta distancia.", "Equilibrio sentado con cojines.", "Juego de tapar el rostro (cucú-tras).",
     "https://images.unsplash.com/photo-1476703993599-0035a21b17a9?auto=format&fit=crop&w=800&q=80"),
    (12, "10 a 12 meses", "Ponerse de pie con apoyo de muebles.", "Ejercitar la pinza fina con comida.", "Lectura de cuentos ilustrados.",
     "https://images.unsplash.com/photo-1522771739844-6a9f6d5f14af?auto=format&fit=crop&w=800&q=80"),
    (18, "13 a 18 meses", "Caminata asistida.", "Juegos de apilar vasos o bloques.", "Cantar canciones e imitar sonidos.",
     "https://images.unsplash.com/photo-1519689680058-324335c77eba?auto=format&fit=crop&w=800&q=80"),
    (24, "19 a 24 meses", "Subir peldaños con ayuda.", "Patear pelotas y clasificar juguetes por color.", "Ampliar vocabulario nombrando objetos.",
     "https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?auto=format&fit=crop&w=800&q=80"),
]
RUTINA_MAYOR_2_ANIOS = (
    "Más de 2 años", "Juego libre al aire libre.", "Dibujar con crayones gruesos.", "Juegos de imaginación y rol.",
    "https://images.unsplash.com/photo-1516627145497-ae6968895b74?auto=format&fit=crop&w=800&q=80",
)


def calcular_rango_peso(meses: int) -> tuple[float, float]:
    if meses <= 5:
        return 3.2 + meses * 0.7, 5.5 + meses * 0.9
    if meses <= 11:
        return 6.5 + (meses - 6) * 0.35, 9.5 + (meses - 6) * 0.45
    return 8.5 + (meses - 12) * 0.25, 12.5 + (meses - 12) * 0.35


# ------------------------------------------------------------------
# ESTADO
# ------------------------------------------------------------------
if "registrada" not in st.session_state:
    st.session_state.registrada = False
if "nombre" not in st.session_state:
    st.session_state.nombre = "Mamá"
if "tratamiento" not in st.session_state:
    st.session_state.tratamiento = "Mamá"

st.markdown(
    """
    <div class="cj-header">
        <h1>🍊 Creciendo juntos</h1>
        <p>by Michelle 🍊 & Neuro Green 🌿 — Un espacio dulce y acogedor para tu maternidad</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------
# PASO 1: REGISTRO
# ------------------------------------------------------------------
if not st.session_state.registrada:
    st.markdown('<div class="cj-card">', unsafe_allow_html=True)
    st.subheader("¡Bienvenida a Creciendo juntos! 🍊")
    st.caption("by Michelle 🍊 & Neuro Green")
    st.write("¿Cómo prefieres que Michelle se dirija a ti?")

    if st.button("🍊 Llama solo \"Mamá\"", use_container_width=True):
        st.session_state.nombre = "Mamá"
        st.session_state.tratamiento = "Mamá"
        st.session_state.registrada = True
        st.rerun()

    st.markdown("**— o ingresa tu nombre —**")
    with st.form("form_registro"):
        nombre = st.text_input("Escribe tu nombre aquí...")
        enviado = st.form_submit_button("Ingresar con mi nombre", use_container_width=True)
        if enviado:
            if nombre.strip():
                st.session_state.nombre = nombre.strip()
                st.session_state.tratamiento = f"señora {nombre.strip()}"
            else:
                st.session_state.nombre = "Mamá"
                st.session_state.tratamiento = "Mamá"
            st.session_state.registrada = True
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------------------------------
# PASO 2: PANEL PRINCIPAL
# ------------------------------------------------------------------
else:
    tratamiento = st.session_state.tratamiento
    st.success(f"Bienvenida, **{st.session_state.nombre}** 🍊")

    tab_faq, tab_nutricion, tab_estimulacion = st.tabs(
        ["❓ Preguntas Frecuentes", "⚖️ Peso y Alimentación", "🧸 Estimulación"]
    )

    # --- SECCIÓN A: FAQ ---
    with tab_faq:
        st.markdown('<div class="cj-card">', unsafe_allow_html=True)
        st.markdown("### 🍊 Preguntas Frecuentes de Maternidad")
        st.caption("Elige una de las 20 opciones de la lista:")

        opciones = [f"{i + 1}. {item['pregunta']}" for i, item in enumerate(FAQ)]
        idx = st.selectbox("Pregunta", opciones, label_visibility="collapsed")
        seleccion = FAQ[opciones.index(idx)]

        st.markdown('<div class="cj-answer">', unsafe_allow_html=True)
        st.image(seleccion["imagen"], use_container_width=True)
        texto_respuesta = f"Sí, {tratamiento}, {seleccion['respuesta']}"
        st.markdown(f"**🍊 Respuesta Personalizada:**\n\n{texto_respuesta}")
        hablar(texto_respuesta, key="faq")
        st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- SECCIÓN B: NUTRICIÓN ---
    with tab_nutricion:
        st.markdown('<div class="cj-card">', unsafe_allow_html=True)
        st.markdown("### ⚖️ Evaluación Nutricional (1 a 24 meses)")
        st.caption("Ingresa los meses (1-24), peso y altura de tu bebé:")

        with st.form("form_nutricion"):
            c1, c2, c3 = st.columns(3)
            meses_nut = c1.number_input("Meses (1 a 24)", min_value=1, max_value=24, value=6, step=1)
            peso = c2.number_input("Peso (kg)", min_value=0.0, value=7.5, step=0.1)
            altura = c3.number_input("Altura (cm)", min_value=0.0, value=67.0, step=0.5)
            calcular = st.form_submit_button("Calcular Evaluación Nutricional", use_container_width=True)

        if calcular:
            st.markdown('<div class="cj-answer">', unsafe_allow_html=True)
            peso_min, peso_max = calcular_rango_peso(meses_nut)
            if peso < peso_min:
                estado_peso = "ligeramente por debajo del promedio"
            elif peso > peso_max:
                estado_peso = "por encima del promedio sugerido"
            else:
                estado_peso = "dentro de un rango saludable y adecuado"

            if meses_nut <= 5:
                imagen = "https://images.unsplash.com/photo-1555252333-9f8e92e65df9?auto=format&fit=crop&w=800&q=80"
                explicacion = (
                    f"Sí, {tratamiento}, tu bebé tiene {meses_nut} meses y su peso de {peso} kilos está "
                    f"{estado_peso}. De 0 a 5 meses la prioridad absoluta es la lactancia materna exclusiva "
                    "o fórmula infantil adaptada a demanda. No requiere agua ni jugos aún."
                )
                pautas = [
                    "**Lactancia materna exclusiva** o fórmula infantil de inicio a demanda.",
                    "No ofrecer agua, té, jugos ni otros alimentos sólidos antes de los 6 meses.",
                    "Asegurar agarre correcto para evitar molestias y asegurar nutrición.",
                    "Mantener controles periódicos con el pediatra.",
                ]
                titulo_pautas = "Pautas de alimentación (0 a 5 meses):"
            elif meses_nut <= 11:
                imagen = "https://images.unsplash.com/photo-1596461404969-9ae70f2830c1?auto=format&fit=crop&w=800&q=80"
                explicacion = (
                    f"Sí, {tratamiento}, a los {meses_nut} meses el peso de {peso} kilos está {estado_peso}. "
                    "Etapa de alimentación complementaria: ofrecer purés, papillas o cortes seguros junto a la "
                    "leche. Iniciar pequeñas cantidades de agua potable."
                )
                pautas = [
                    "Inicio de **alimentación complementaria** manteniendo la leche materna o de fórmula.",
                    "Ofrecer verduras, frutas, cereales sin azúcar y carnes/proteínas bien cocidas.",
                    "Probar un alimento nuevo a la vez para descartar alergias.",
                    "Ofrecer pequeñas cantidades de agua potable en vaso entrenador.",
                ]
                titulo_pautas = "Pautas de alimentación (6 a 11 meses):"
            else:
                imagen = "https://images.unsplash.com/photo-1544126592-807ade215a0b?auto=format&fit=crop&w=800&q=80"
                explicacion = (
                    f"Sí, {tratamiento}, con {meses_nut} meses el peso de {peso} kilos está {estado_peso}. "
                    "De 12 a 24 meses el bebé se integra a la dieta familiar con 3 comidas principales y 2 "
                    "colaciones saludables. Evitar azúcares añadidos y procesados."
                )
                pautas = [
                    "Integrar al bebé a la **comida familiar equilibrada** (3 comidas + 2 colaciones).",
                    "Proteínas variadas (huevo, pollo, pescado, legumbres) y grasas saludables (aguacate, aceite de oliva).",
                    "Evitar ultraprocesados, sal en exceso, bebidas azucaradas y fritos.",
                    "Fomentar que coman solos para desarrollar autonomía.",
                ]
                titulo_pautas = "Pautas de alimentación (12 a 24 meses):"

            st.image(imagen, use_container_width=True)
            st.markdown(
                f"**Evaluación para su bebé de {meses_nut} meses ({peso} kg, {altura} cm): Peso {estado_peso}.**"
            )
            st.markdown(f"**{titulo_pautas}**")
            for p in pautas:
                st.markdown(f"- {p}")
            hablar(explicacion, key="nutricion")
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    # --- SECCIÓN C: ESTIMULACIÓN ---
    with tab_estimulacion:
        st.markdown('<div class="cj-card">', unsafe_allow_html=True)
        st.markdown("### 🧸 Ejercicios y Estimulación Temprana")
        st.caption("Ingresa la edad en meses del bebé:")

        c1, c2 = st.columns([3, 1])
        meses_est = c1.number_input(
            "Meses del bebé", min_value=1, max_value=36, value=6, step=1, label_visibility="collapsed"
        )
        obtener = c2.button("Obtener Rutina", use_container_width=True)

        if obtener:
            st.markdown('<div class="cj-answer">', unsafe_allow_html=True)
            rutina = next((r for r in RUTINAS_ESTIMULACION if meses_est <= r[0]), None)
            if rutina:
                _, etiqueta, e1, e2, e3, imagen = rutina
                conector = "Sí"
            else:
                etiqueta, e1, e2, e3, imagen = RUTINA_MAYOR_2_ANIOS
                conector = "Sí"

            explicacion = f"{conector}, {tratamiento}, para la etapa de {etiqueta}: {e1} {e2} {e3}"

            st.image(imagen, use_container_width=True)
            st.markdown(f"**{conector}, {tratamiento}, para la etapa de {etiqueta}:**")
            st.markdown(f"- {e1}\n- {e2}\n- {e3}")
            hablar(explicacion, key="estimulacion")
            st.markdown("</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown(
    """
    <div class="cj-footer">
        Creciendo juntos by Michelle 🍊<br>
        © Todos los derechos reservados a <b>Michelle</b> y al grupo <b>Neuro Green</b> 🌿🍊
    </div>
    """,
    unsafe_allow_html=True,
)
