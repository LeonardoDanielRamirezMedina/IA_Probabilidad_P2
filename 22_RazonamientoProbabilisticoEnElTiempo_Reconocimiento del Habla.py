#------------ENFOQUE: PROBABILIDAD--------------#
#--LEONARDO DANIEL RAMÍREZ MEDINA-6E1-21310138--#
      
#Razonamiento Probabilístico en el tiempo
#Tema: Reconocimiento del Habla

# El reconocimiento del habla es una tecnología que permite a las computadoras identificar y comprender palabras habladas.

from google.cloud import speech_v1p1beta1 as speech # Importar la librería de reconocimiento de voz de Google Cloud
import io   # Importar la librería io para trabajar con archivos de audio

def transcribe_audio_file(file_path):   # Definir la función para transcribir un archivo de audio
    client = speech.SpeechClient()  # Crear un cliente de reconocimiento de voz

    with io.open(file_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)    # Crear un objeto de audio para el reconocimiento
    config = speech.RecognitionConfig(  # Crear un objeto de configuración para el reconocimiento
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,   # Especificar el formato de audio
        sample_rate_hertz=16000,    # Especificar la tasa de muestreo
        language_code="es-ES",  # Especificar el idioma del audio
    )

    response = client.recognize(config=config, audio=audio)   # Realizar el reconocimiento de voz

    for result in response.results:
        print("Transcript: {}".format(result.alternatives[0].transcript))   # Imprimir la transcripción del audio

# Llamar a la función con la ruta al archivo de audio
transcribe_audio_file("audio.wav")  