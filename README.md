# Language-Translator
# 🎙️ Voice Translator

A simple Python app that records your voice, converts it to text, and translates it into another language — all from the terminal.

Speak in Turkish, get it in Spanish. Speak in English, get it in German. Any language pair supported by Google Translate works.

## ✨ Features

- 🎤 Records audio from your microphone
- 📝 Converts speech to text with Google Speech Recognition
- 🌍 Translates the text into any supported language with `googletrans`
- ⚠️ Handles unclear speech and connection errors

## 🔧 How It Works

```
🎤 Microphone  →  💾 output.wav  →  📝 Speech-to-Text  →  🌍 Translation  →  🖥️ Output
```

1. You enter the language you will speak and the language to translate into.
2. The app records your voice for **5 seconds** and saves it as `output.wav`.
3. Google Speech Recognition turns the recording into text.
4. `googletrans` translates the text into the target language.
5. Both the original and the translated text are printed.

## 📦 Requirements

- Python 3.8+
- A working microphone
- An internet connection (both speech recognition and translation are online services)

## 🚀 Installation

Clone the repository and install the dependencies:

```bash
git clone https://github.com/<your-username>/<your-repo>.git
cd <your-repo>
pip install sounddevice numpy scipy SpeechRecognition googletrans==3.1.0a0
```

> **Note:** The code uses the synchronous `googletrans` API, so version `3.1.0a0` is required.
> Newer versions (4.x) are asynchronous and will raise
> `AttributeError: 'coroutine' object has no attribute 'text'`.

## ▶️ Usage

```bash
python main.py
```

Example session:

```
Lütfen konuşmanızın dilini girin (örneğin: 'tr' Türkçe, 'en' İngilizce): tr
Lütfen konuşmanızın çevirilecei dilin kodunu girin (örneğin: 'es' İspanyolca, 'en' İngilizce): en
Şimdi konuşun...
Kayıt tamamlandı, şimdi tanıma işlemi devam ediyor...
Konuşmanızın ana hali: merhaba bugün hava çok güzel
🌍 EN diline çeviri: hello the weather is very nice today
```

## 🌐 Common Language Codes

| Language | Code | Language | Code |
|---|---|---|---|
| Turkish | `tr` | Italian | `it` |
| English | `en` | Russian | `ru` |
| German | `de` | Arabic | `ar` |
| French | `fr` | Japanese | `ja` |
| Spanish | `es` | Chinese (Simplified) | `zh-cn` |

To see every supported language:

```python
from googletrans import LANGUAGES
print(LANGUAGES)
```

## ⚙️ Configuration

You can change these values at the top of the script:

| Variable | Default | Description |
|---|---|---|
| `duration` | `5` | Recording length in seconds |
| `sample_rate` | `44100` | Audio sample rate in Hz |

## 🛠️ Troubleshooting

| Message | Cause | Fix |
|---|---|---|
| `Konuşma tanınamadı.` | Speech was unclear, too quiet, or silent | Speak closer to the microphone and reduce background noise |
| `Hizmet hatası: ...` | No internet connection or the API is unavailable | Check your connection and try again |
| `'coroutine' object has no attribute 'text'` | `googletrans` 4.x is installed | `pip install googletrans==3.1.0a0` |
| `PortAudioError` | No microphone detected | Check that your microphone is connected and allowed in system settings |

## 🧰 Built With

- [sounddevice](https://python-sounddevice.readthedocs.io/) — audio recording
- [SciPy](https://scipy.org/) — saving the WAV file
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) — speech-to-text
- [googletrans](https://pypi.org/project/googletrans/) — translation

## 💡 Future Ideas

- Read the translation aloud with text-to-speech
- Keep a history of translations in a file
- Continuous mode for back-and-forth conversations
- A simple GUI with `tkinter`
