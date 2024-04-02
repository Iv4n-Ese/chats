from nltk.chat.util import Chat, reflections

mis_reflexiones = {
    "ir": "fui",
    "hola": "hey"
}
pares = [
    [
        r"Se ha caido el hosting",
        ["Sentimos por ese fallo",]
    ],
     [
        r"Cuando hay que pagar la factura",
        ["El dia 15 de cada mes",]
    ],
]

def chatear():
    print("Hola soy el chat de servicio") #Mensaje por defecto
    chat = Chat(pares, mis_reflexiones)
    chat.converse()

if __name__ == "__main__":
    chatear()

chatear()