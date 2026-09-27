import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
from googletrans import Translator

duration = 5  # Kayıt süresi
sample_rate = 44100  # Örnekleme hızı
lang = input("Lütfen konuşmanızın dilini girin (örneğin: 'tr' Türkçe, 'en' İngilizce): ")
lang1 = input("Lütfen konuşmanızın çevirilecei dilin kodunu girin (örneğin: 'es' İspanyolca, 'en' İngilizce): ")

print("Şimdi konuşun...")
recording = sd.rec(
  int(duration * sample_rate), # kaydedilecek örnek sayısı
  samplerate=sample_rate,      # örnekleme hızı
  channels=1,                  # 1, mono kayıt anlamına gelir.
  dtype="int16")               # kayıtlı örnekler için veri türü
sd.wait()  # kayıt bitene kadar beklemek

wav.write("output.wav", sample_rate, recording)
print("Kayıt tamamlandı, şimdi tanıma işlemi devam ediyor...")

recognizer = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio, language=lang)
    print("Konuşmanızın ana hali:", text)
    translator = Translator()
    translated = translator.translate(text, dest=lang1)
    print(f"🌍 {lang1.upper()} diline çeviri:", translated.text)

except sr.UnknownValueError:             # - Google gürültü veya sessizlik nedeniyle konuşmayı anlayamadığında
    print("Konuşma tanınamadı.")
except sr.RequestError as e:             # - İnternet bağlantısı yoksa veya API kullanılamıyorsa
    print(f"Hizmet hatası: {e}")

