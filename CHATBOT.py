# Definir las respuestas del chatbot
respuestas = {
    "Hola": "¡Hola! Te saludamos de  Tactical Vencer o Morir IM JP, ventas de accesorios y artículos tácticos. ¿En qué podemos ayudarte?",
    "Identificate para agregarte y aproveches nuestras promociones": "Por favor, proporciona tu nombre y número de teléfono para agregarte a nuestras promociones.",
    "Ciudad de la que nos escribes": "¿De qué ciudad nos escribes?",
    "En que podemos ayudarte": "Estamos aquí para ayudarte. ¿Hay algo en particular en lo que necesites asistencia?",
    "Te dejamos el link de nuestro catálogo ": "Puedes encontrar nuestro catálogo en [https://vercatalogo.com/tactical_vencer_o_morir_im_jp/products/by-all/all].",
    "En que artículo estas interesado": "Por favor, dinos en qué artículo estás interesado para brindarte más información al respecto.",
    "Ubicación GPS de nuestro espacio físico": "Nuestra ubicación física es [https://maps.app.goo.gl/3HxffnRpFUy4sH2x8].",
    "Visita nuestras redes sociales": "Puedes visitar nuestras redes sociales en [https://www.tiktok.com/@venceromorir537?_t=8i7TUW2Ndvq&_r=1].",
    "Deja tu mensaje, en lo posible nos comunicaremos contigo": "Por favor, deja tu mensaje y nos comunicaremos contigo lo antes posible.",
    "Que tengas un buen día": "¡Gracias! Que tengas un excelente día también."
}

# Función para obtener la respuesta del chatbot
def obtener_respuesta(pregunta):
    return respuestas.get(pregunta, "Lo siento, no entendí esa pregunta.")

# Loop principal del chatbot
while True:
    pregunta = input("Tú: ")
    respuesta = obtener_respuesta(pregunta)
    print("Chatbot: " + respuesta)
