---
url: https://docs.cloud.google.com/text-to-speech/docs/gemini-3.1-flash-tts-voice-replication-eap
title: Gemini-TTS 3.1 Flash voice replication \u00a0|\u00a0 Cloud Text-to-Speech \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:39.578732+00:00
---

# Gemini-TTS 3.1 Flash voice replication  |  Cloud Text-to-Speech  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/docs/gemini-3.1-flash-tts-voice-replication-eap

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)



Send feedback 

#  Gemini-TTS 3.1 Flash voice replication Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms#1) and the [Generative AI Service Specific Terms](https://cloud.google.com/terms/service-terms#20), as well as the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). 

Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** To request access, fill out this form: [Gemini-TTS Voice Replication Allowlist](https://docs.google.com/forms/d/1jzHeYXKM8rvoTHyvY_PFl76d6RNYJOGcZH3ctVP5XXk).

Voice replication enables the Gemini-TTS model to mimic the voice, tone, cadence, and timbre of a custom voice sample, offering unique voice experiences beyond the standard [prebuilt voices](https://ai.google.dev/gemini-api/docs/speech-generation).

Use the Voices API to perform this replication in a stateless two-step process:

  1. **Generate a voice replication key** : Provide a reference audio sample (`source_audio`) of the target speaker along with a recorded statement of consent (`consent_audio`). The service verifies ownership and produces an encrypted, signed voice replication key.
  2. **Synthesize speech** : Pass the generated voice replication key in subsequent generation requests to synthesize speech in the replicated voice. This workflow secures the voice profile and prevents the need to re-upload large audio files with every request.



**Note:** Voice replication keys are valid for seven days. The key must be regenerated in order to continue using a replicated voice. 

## Audio sample requirements

Before generating a voice key, verify that your audio files meet the following criteria:

  * **Format** : Both the reference audio (`source_audio`) and the consent audio (`consent_audio`) must be little-endian, LINEAR16, mono (single-channel) WAV files, with a 24kHz sample rate.
  * **Optimal length** : The `source_audio` reference sample should be between 10 and 30 seconds long. Longer samples generally achieve higher output replication quality.
  * **Required consent script** : The `consent_audio` statement must contain the target speaker reading the required phrase word-for-word. Refer to the table under Supported languages and consent scripts for the exact script mapped to each language. Any deviation from the script will result in a validation failure.
  * **Audio quality:** The quality of the generated speech heavily depends on the quality of the `source_audio`. Use recordings with little to no background noise.



## How to use voice replication

To replicate a voice and generate content:

  1. **Request a voice replication key** :

     * Request a key using the `voices` REST endpoint and the `gemini-3.1-flash-tts-preview` model.
     * Set `store` to `false` (indicating a stateless, client-managed key).
     * Package the reference audio and consent audio within the `voice.replicated` payload.
     * Extract the returned token from the `key` field of the response. **Note that the key is valid for seven days and should be regenerated before it expires to avoid disruptions.** The `expire_time` field of the response contains the Unix timestamp indicating when the key will expire.
  2. **Synthesize speech** :

     * Call `GenerateContent` or `StreamGenerateContent` using the `gemini-3.1-flash-tts-preview` model.
     * Set the `response_modalities` parameter to `["AUDIO"]` in the generation config.
     * Provide the generated replication key in the `voice` field under `speech_config.voice_config`.
     * Set the `language_code` parameter inside `speech_config` to specify the synthesis language (for example, `en-US`).
     * Supply the input text to synthesize inside the `contents` field.



## Code examples

The following examples demonstrate how to load local WAV files, request a stateless voice replication key, and then use the key to synthesize text into speech.

### Python (Unary)
    
    
    import base64
    import wave
    
    import google.auth
    from google.auth.transport.requests import Request
    import requests
    
    PROJECT_ID = "YOUR_PROJECT_ID"
    SOURCE_AUDIO_PATH = "SOURCE_AUDIO_PATH.wav"
    CONSENT_AUDIO_PATH = "CONSENT_AUDIO_PATH.wav"
    OUTPUT_FILE_PATH = "OUTPUT_FILE_PATH.wav"
    
    # Set up the wave file to save the output:
    def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
      with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)
    
    # Read voice and consent samples
    with open(SOURCE_AUDIO_PATH, "rb") as f:
      source_audio_bytes = f.read()
    
    with open(CONSENT_AUDIO_PATH, "rb") as f:
      consent_audio_bytes = f.read()
    
    # Get credentials token
    credentials, _ = google.auth.default()
    if not credentials.valid:
      credentials.refresh(Request())
    
    # Step 1: Create a voice replication key using the REST endpoint
    url = f"https://aiplatform.googleapis.com/v1beta1/projects/{PROJECT_ID}/locations/global/voices"
    headers = {
        "Authorization": f"Bearer {credentials.token}",
        "x-goog-user-project": PROJECT_ID,
        "Content-Type": "application/json",
    }
    
    body = {
        "voice": {
            "model": "models/gemini-3.1-flash-tts-preview",
            "type": "REPLICATED",
            "replicated": {
                "source_audio": {
                    "mime_type": "audio/wav",
                    "data": base64.b64encode(source_audio_bytes).decode("utf-8"),
                },
                "consent_audio": {
                    "mime_type": "audio/wav",
                    "data": base64.b64encode(consent_audio_bytes).decode("utf-8"),
                },
            },
        },
        "store": False,
    }
    
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    voice_key = response.json()["key"]
    
    # Step 2: Synthesize speech using the replication key.
    synthesis_url = f"https://aiplatform.googleapis.com/v1beta1/projects/{PROJECT_ID}/locations/global/publishers/google/models/gemini-3.1-flash-tts-preview:generateContent"
    synthesis_body = {
        "contents": {
            "role": "user",
            "parts": [{"text": "Say the following: This is a replicated voice."}],
        },
        "generation_config": {
            "response_modalities": ["AUDIO"],
            "speech_config": {
                "voice_config": {
                    "voice": voice_key,
                },
                "language_code": "en-US",
            },
        },
    }
    
    synthesis_response = requests.post(synthesis_url, headers=headers, json=synthesis_body)
    synthesis_response.raise_for_status()
    
    data = synthesis_response.json()["candidates"][0]["content"]["parts"][0]["inlineData"]["data"]
    audio_bytes = base64.b64decode(data)
    
    wave_file(OUTPUT_FILE_PATH, audio_bytes)  # Saves the file to current directory
    

### Python (Streaming)
    
    
    import base64
    import json
    import wave
    
    import google.auth
    from google.auth.transport.requests import Request
    import requests
    
    PROJECT_ID = "YOUR_PROJECT_ID"
    SOURCE_AUDIO_PATH = "SOURCE_AUDIO_PATH.wav"
    CONSENT_AUDIO_PATH = "CONSENT_AUDIO_PATH.wav"
    OUTPUT_FILE_PATH = "OUTPUT_FILE_PATH.wav"
    
    # Set up the wave file to save the output:
    def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
      with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)
    
    # Read voice and consent samples
    with open(SOURCE_AUDIO_PATH, "rb") as f:
      source_audio_bytes = f.read()
    
    with open(CONSENT_AUDIO_PATH, "rb") as f:
      consent_audio_bytes = f.read()
    
    # Get credentials token
    credentials, _ = google.auth.default()
    if not credentials.valid:
      credentials.refresh(Request())
    
    # Step 1: Create a voice replication key using the REST endpoint
    url = f"https://aiplatform.googleapis.com/v1beta1/projects/{PROJECT_ID}/locations/global/voices"
    headers = {
        "Authorization": f"Bearer {credentials.token}",
        "x-goog-user-project": PROJECT_ID,
        "Content-Type": "application/json",
    }
    
    body = {
        "voice": {
            "model": "models/gemini-3.1-flash-tts-preview",
            "type": "REPLICATED",
            "replicated": {
                "source_audio": {
                    "mime_type": "audio/wav",
                    "data": base64.b64encode(source_audio_bytes).decode("utf-8"),
                },
                "consent_audio": {
                    "mime_type": "audio/wav",
                    "data": base64.b64encode(consent_audio_bytes).decode("utf-8"),
                },
            },
        },
        "store": False,
    }
    
    response = requests.post(url, headers=headers, json=body)
    response.raise_for_status()
    voice_key = response.json()["key"]
    
    # Step 2: Synthesize speech stream using the replication key.
    synthesis_url = f"https://aiplatform.googleapis.com/v1beta1/projects/{PROJECT_ID}/locations/global/publishers/google/models/gemini-3.1-flash-tts-preview:streamGenerateContent?alt=sse"
    synthesis_body = {
        "contents": {
            "role": "user",
            "parts": [{"text": "Say the following: This is a replicated voice."}],
        },
        "generation_config": {
            "response_modalities": ["AUDIO"],
            "speech_config": {
                "voice_config": {
                    "voice": voice_key,
                },
                "language_code": "en-US",
            },
        },
    }
    
    synthesis_response = requests.post(synthesis_url, headers=headers, json=synthesis_body, stream=True)
    synthesis_response.raise_for_status()
    
    full_data = b""
    for line in synthesis_response.iter_lines():
      if line:
        decoded_line = line.decode("utf-8").strip()
        # SSE events start with "data: "
        if decoded_line.startswith("data:"):
          # Remove "data: " prefix and load JSON
          event_json = json.loads(decoded_line[5:].strip())
          if "candidates" in event_json:
            for candidate in event_json["candidates"]:
              if "content" in candidate and "parts" in candidate["content"]:
                for part in candidate["content"]["parts"]:
                  if "inlineData" in part:
                    data_base64 = part["inlineData"].get("data")
                    if data_base64:
                      full_data += base64.b64decode(data_base64)
    
    wave_file(OUTPUT_FILE_PATH, full_data)  # Saves the file to current directory
    

### CURL
    
    
    # Make sure to install gcloud cli, and sign in to your project.
    # Make sure to use your PROJECT_ID value.
    # SOURCE_AUDIO_PATH should point to your WAV audio sample (e.g., /tmp/source.wav).
    # CONSENT_AUDIO_PATH should point to the read consent WAV audio sample (e.g., /tmp/consent.wav).
    # Requires the JQ and ffmpeg library to be installed.
    PROJECT_ID=YOUR_PROJECT_ID
    SOURCE_AUDIO_PATH=YOUR_SOURCE_AUDIO_PATH.wav
    CONSENT_AUDIO_PATH=YOUR_CONSENT_AUDIO_PATH.wav
    OUTPUT_FILE_PATH=YOUR_OUTPUT_FILE_PATH.wav
    
    # Step 1: Generate a voice replication key using the Voices service.
    VOICE_REQUEST_JSON=$(cat <<EOF
    {
      "voice": {
        "model": "gemini-3.1-flash-tts-preview",
        "type": "REPLICATED",
        "replicated": {
          "source_audio": {
            "mime_type": "audio/wav",
            "data": "$(cat $SOURCE_AUDIO_PATH | base64 | tr -d '\n')"
          },
          "consent_audio": {
            "mime_type": "audio/wav",
            "data": "$(cat $CONSENT_AUDIO_PATH | base64 | tr -d '\n')"
          }
        }
      },
      "store": false
    }
    EOF
    )
    
    echo "$VOICE_REQUEST_JSON" > /tmp/voice_request.json
    
    VOICE_KEY_RESPONSE=$(curl -X POST \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "x-goog-user-project: $PROJECT_ID" \
      -H "Content-Type: application/json" \
      -d @/tmp/voice_request.json \
      "https://aiplatform.googleapis.com/v1beta1/projects/$PROJECT_ID/locations/global/voices")
    
    VOICE_KEY=$(echo "$VOICE_KEY_RESPONSE" | jq -r '.key')
    
    # Step 2: Use the voice replication key to synthesize speech with GenerateContent.
    SYNTHESIS_REQUEST_JSON=$(cat <<EOF
    {
      "contents": {
        "role": "user",
        "parts": [{ "text": "Say the following: This is a replicated voice." }]
      },
      "generation_config": {
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {
                "voice": "$VOICE_KEY"
            },
            "language_code": "en-US"
        }
      }
    }
    EOF
    )
    
    echo "$SYNTHESIS_REQUEST_JSON" > /tmp/synthesis_request.json
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "x-goog-user-project: $PROJECT_ID" \
      -H "Content-Type: application/json" \
      -d @/tmp/synthesis_request.json \
      "https://aiplatform.googleapis.com/v1beta1/projects/$PROJECT_ID/locations/global/publishers/google/models/gemini-3.1-flash-tts-preview:generateContent" \
      | jq -r '.candidates[0].content.parts[0].inlineData.data' \
      | python3 -m base64 -d | ffmpeg -y -f s16le -ar 24k -ac 1 -i - $OUTPUT_FILE_PATH
    

## Supported languages and consent scripts

The Voices API verifies the target speaker's consent by matching the transcript text of the `consent_audio` file. The following table lists the supported language codes and their corresponding required consent phrase:

Language | BCP-47 Code | Required Consent Script  
---|---|---  
Afrikaans | `af` | Ek is die eienaar van hierdie stem en het ingestem tot die skep van 'n sintetiese model van my stem deur die gebruik van Google Cloud.  
Albanian | `sq` | Unë jam pronari i këtij zëri dhe kam dhënë pëlqimin për krijimin e një modeli sintetik të zërit tim përmes përdorimit të Google Cloud.  
Amharic | `am` | የዚህ ድምጽ ባለቤት እኔ ነኝ እና የጉግል ክላውድን በመጠቀም የድምፄ ሰው ሰраሽ ሞዴል እንዲፈጠር ተስማምቻለሁ።  
Arabic | `ar` | أنا صاحب هذا الصوت وقد وافقت على إنشاء نموذج اصطناعي لصوتي باستخدام خدمة جوجل كلاود.  
Armenian | `hy` | Ես այս ձայնի սեփականատերն եմ և համაձայնություն եմ տվել Google Cloud-ի միջոցով իմ ձայնի սինթետিক մოდელი ստեղծմանը։  
Azerbaijani | `az` | Mən bu səsin sahibiyəm və Google Cloud vasitəsilə səsimin sintetik modelinin yaradılmasına razılıq vermişəm.  
Bangla | `bn` | আমি এই কণ্ঠস্বরের মালিক এবং গুগল ক্লাউড ব্যবহারের মাধ্যমে আমার কণ্ঠস্বরের একটি কৃত্রিম মডেল তৈরিতে সম্মতি দিয়েছি।  
Basque | `eu` | Ahots honen jabea naiz eta nire ahotsaren eredu sintetiko bat sortzeko baimena eman dut Google Cloud erabiliz.  
Belarusian | `be` | Я з'яўляюся ўладальнікам гэтага голасу і даў згоду на стварэнне сінтэтычнай мадэлі майго голасу з дапамогай Google Cloud.  
Bulgarian | `bg` | Аз съм собственикът на този глас и съм дал съгласието си за създаването на синтетичен модел на моя глас чрез използването на Google Cloud.  
Burmese | `my` | ကျွန်ုပ်သည် ဤအသံ၏ပိုင်ရှင်ဖြစ်ပြီး Google Cloud ကိုအသုံးပြုခြင်းဖြင့် ကျွန်ုပ်၏အသံ၏ ပေါင်းစပ်ပုံစံတစ်ခု ဖန်တီးရန် သဘောတူပါသည်။  
Catalan | `ca` | Sóc el propietari d'aquesta veu i he donat el meu consentiment per a la creació d'un model sintètic de la meva veu mitjançant l'ús de Google Cloud.  
Cebuano | `ceb` | Ako ang tag-iya niining tingog ug miuyon sa paghimo og sintetikong modelo sa akong tingog pinaagi sa paggamit sa Google Cloud.  
Chinese, Mandarin | `cmn` | 我是这段声音的所有者，并已同意通过 Google Cloud 创建我的声音合成模型。  
Croatian | `hr` | Vlasnik sam ovog glasa i pristao sam na izradu sintetičkog modela mog glasa putem Google Clouda.  
Czech | `cs` | Jsem vlastníkem tohoto hlasu a souhlasil(a) jsem s vytvořením syntetického modelu mého hlasu pomocí služby Google Cloud.  
Danish | `da` | Jeg ejer denne stemme og har givet samtykke til oprettelsen af en syntetisk model af min stemme ved hjælp af Google Cloud.  
Dutch | `nl` | Ik ben de eigenaar van deze stem en heb toestemming gegeven voor het creëren van een synthetisch model van mijn stem via Google Cloud.  
English | `en` | I am the owner of this voice and have consented to the creation of a synthetic model of my voice through the use of Google Cloud.  
Estonian | `et` | Olen selle hääle omanik ja olen andnud nõusoleku oma hääle sünteetilise mudeli loomiseks Google Cloudi abil.  
Filipino | `fil` | Ako ang may-ari ng boses na ito at pumayag na gumawa ng sintetikong modelo ng aking boses sa pamamagitan ng paggamit ng Google Cloud.  
Finnish | `fi` | Olen tämän äänen omistaja ja olen antanut suostumukseni synteettisen ääneni mallintamiseen Google Cloudin avulla.  
French | `fr` | Je suis propriétaire de cette voix et j'ai consenti à la création d'un modèle synthétique de ma voix grâce à l'utilisation de Google Cloud.  
Galician | `gl` | Son o propietario desta voz e dei o meu consentimento para a creación dun modelo sintético da miña voz mediante o uso de Google Cloud.  
Georgian | `ka` | მე ვარ ამ ხმის მფლობელი და დავთანხმდი ჩემი ხმის სინთეზური მოდელის შექმნას Google Cloud-ის გამოყენებით.  
German | `de` | Ich bin der Inhaber dieser Stimme und habe der Erstellung eines synthetischen Modells meiner Stimme mithilfe von Google Cloud zugestimmt.  
Greek | `el` | Είμαι ο κάτοχος αυτής της φωνής και έχω συναινέσει στη δημιουργία ενός συνθετικού μοντέλου της φωνής μου μέσω της χρήσης του Google Cloud.  
Gujarati | `gu` | હું આ અવાજનો માલિક છું અને ગૂગલ ક્લાઉડના ઉપયોગ દ્વારા મારા અવાજનું સિન્થેટિક મોડેલ બનાવવા માટે સંમતિ આપી છે.  
Haitian Creole | `ht` | Mwen se pwopriyetè vwa sa a epi mwen bay konsantman pou kreyasyon yon modèl sentetik vwa mwen atravè itilizasyon Google Cloud.  
Hebrew | `he` | אני הבעלים של קול זה והסכמתי ליצירת מודל סינתטי של קולי באמצעות Google Cloud.  
Hindi | `hi` | मैं इस आवाज का स्वामी हूं और मैंने Google क्लाउड के उपयोग के माध्यम से अपनी आवाज का कृत्रिम मॉडल बनाने की सहमति दी है।  
Hungarian | `hu` | Én vagyok a hang tulajdonosa, és hozzájárultam ahhoz, hogy a Google Cloud segítségével szintetikus modellt készítsenek a hangomról.  
Icelandic | `is` | Ég er eigandi þessarar raddar og hef samþykkt að búið sé til tilbúið líkan af rödd minni með því að nota Google Cloud.  
Indonesian | `id` | Saya adalah pemilik suara ini dan telah menyetujui pembuatan model sintetis suara saya melalui penggunaan Google Cloud.  
Italian | `it` | Sono il proprietario di questa voce e ho acconsentito alla creazione di un modello sintetico della mia voce tramite l'utilizzo di Google Cloud.  
Japanese | `ja` | 私はこの音声の所有者であり、Google Cloud を利用して私の音声の合成モデルを作成することに同意しました。  
Javanese | `jv` | Aku sing nduwèni swara iki lan wis sarujuk kanggo nggawé model sintetis swaraku liwat panggunaan Google Cloud.  
Kannada | `kn` | ನಾನು ಈ ಧ್ವನಿಯ ಮಾಲೀಕ ಮತ್ತು Google Cloud ಬಳಕೆಯ ಮೂಲಕ ನನ್ನ ಧ್ವನಿಯ ಸಂಶ್ಲೇಷಿತ ಮಾದರಿಯನ್ನು ರಚಿಸಲು ಸಮ್ಮತಿಸಿದ್ದೇನೆ.  
Korean | `ko` | 저는 이 음성의 소유자이며, Google Cloud를 사용하여 제 음성의 합성 모델을 생성하는 데 동의했습니다.  
Lao | `lo` | ຂ້ອຍເປັນເຈົ້າຂອງສຽງນີ້ ແລະ ໄດ້ຍິນຍອມໃຫ້ສ້າງຮູບແບບສັງເຄາະສຽງຂອງຂ້ອຍຜ່ານການນຳໃຊ້ Google Cloud  
Latin | `la` | Huius vocis dominus sum et consensi sum ad creandum exemplar syntheticum vocis meae per usum Google Cloud.  
Latvian | `lv` | Esmu šīs balss īpašnieks un esmu piekritis sintētiska manas balss modeļa izveidei, izmantojot Google Cloud.  
Lithuanian | `lt` | Esu šio balso savininkas ir sutikau, kad naudojant „Google Cloud“ būtų sukurtas sintetinis mano balso modelis.  
Luxembourgish | `lb` | Ech sinn de Besëtzer vun dëser Stëmm an hunn der Erstellung vun engem synthetesche Modell vu menger Stëmm mat Hëllef vu Google Cloud zougestëmmt.  
Macedonian | `mk` | Јас сум сопственик на овој глас и се согласив за создавање синтетички модел на мојот глас преку користење на Google Cloud.  
Malagasy | `mg` | Izaho no tompon'ity feo ity ary nanaiky ny hamorona modely sentetika amin'ny feoko amin'ny alàlan'ny fampiasana ny Google Cloud.  
Malay | `ms` | Saya pemilik suara ini dan telah bersetuju untuk penciptaan model sintetik suara saya melalui penggunaan Google Cloud.  
Malayalam | `ml` | ഈ ശബ്ദത്തിന്റെ ഉടമ ഞാനാണ്, Google ക്ലൗഡ് ഉപയോഗിച്ച് എന്റെ ശബ്ദത്തിന്റെ ഒരു സിന്തറ്റിക് മോഡൽ സൃഷ്ടിക്കാൻ ഞാൻ സമ്മതം നൽകിയിട്ടുണ്ട്.  
Marathi | `mr` | मी या आवाजाचा मालक आहे आणि गूगल क्लाउडचा वापर करून माझ्या आवाजाचे कृत्रिम मॉडेल तयार करण्यास मी संमती दिली आहे.  
Mongolian | `mn` | Би энэ дуу хоолойны эзэмшигч бөгөөд Google Cloud ашиглан өөрийн дуу хоолойны синтетик загварыг бүтээхийг зөвшөөрсөн.  
Nepali | `ne` | म यो आवाजको मालिक हुँ र गुगल क्लाउडको प्रयोग मार्फत मेरो आवाजको सिंथेटिक मोडेल सिर्जना गर्न सहमति दिएको छु।  
Norwegian, Bokmål | `nb` | Jeg eier denne stemmen og har samtykket til at det opprettes en syntetisk modell av stemmen min ved bruk av Google Cloud.  
Odia | `or` | ମୁଁ ଏହି ଭଏସ୍‌ର ମାଲିକ ଏବଂ Google Cloud ବ୍ୟବହାର କରି ମୋ ଭଏସ୍‌ର ଏକ ସିନ୍ଥେଟିକ୍ ମଡେล୍ ତିଆରି କରିବାକୁ ସମ୍ମତି ଦେଇଛି।  
Pashto | `ps` | زه د دې غږ مالک یم او د ګوګل کلاوډ په کارولو سره مې د خپل غږ د مصنوعي ماډل جوړولو ته رضایت ورکړی دی.  
Persian | `fa` | من مالک این صدا هستم و با ایجاد یک مدل مصنوعی از صدایم از طریق استفاده از Google Cloud موافقت کرده‌ام.  
Polish | `pl` | Jestem właścicielem tego głosu i wyraziłem zgodę na utworzenie syntetycznego modelu mojego głosu za pomocą Google Cloud.  
Portuguese | `pt` | Eu sou o proprietário desta voz e consinto com a criação de um modelo sintético da minha voz através do uso do Google Cloud.  
Punjabi | `pa` | ਮੈਂ ਇਸ ਆවාਜ਼ ਦਾ ਮਾਲਕ ਹਾਂ ਅਤੇ ਗੂਗਲ ਕਲਾਉਡ ਦੀ ਵਰਤੋਂ ਰਾਹੀਂ ਆਪਣੀ ਆਵਾਜ਼ ਦੇ ਇੱਕ ਸਿੰਥੈਟਿਕ ਮਾਡਲ ਨੂੰ ਬਣਾਉਣ ਲਈ ਸਹਿਮਤੀ ਦਿੱਤੀ ਹੈ।  
Romanian | `ro` | Sunt proprietarul acestei voci și am consimțit la crearea unui model sintetic al vocii mele prin utilizarea Google Cloud.  
Russian | `ru` | Я являюсь владельцем этого голоса и дал согласие на создание синтетической модели моего голоса с использованием Google Cloud.  
Serbian | `sr` | Ја сам власник овог гласа и пристао/ла сам на креирање синтетичког модела мог гласа коришћењем Google Cloud-а.  
Sindhi | `sd` | مان هن آواز جو مالڪ آهيان ۽ گوگل ڪلائوڊ جي استعمال ذريعي پنهنجي آواز جي هڪ مصنوعي ماڊل جي تخليق تي رضामندي ڏني آهي.  
Sinhala | `si` | මම මෙම හඬෙහි හිමಿಕරු වන අතර Google Cloud භාවිතය හරහා මගේ හඬෙහි කෘතිම ආකෘතියක් නිර්මාණය කිරීමට කැමැත්ත පළ කර ඇත්තෙමි.  
Slovak | `sk` | Som vlastníkom tohto hlasu a súhlasil/a som s vytvorením syntetického modelu môjho hlasu pomocou služby Google Cloud.  
Slovenian | `sl` | Sem lastnik tega glasu in sem privolil v ustvarjanje sintetičnega modela mojega glasu z uporabo storitve Google Cloud.  
Spanish | `es` | Soy el propietario de esta voz y he dado mi consentimiento para la creación de un modelo sintético de mi voz mediante el uso de Google Cloud.  
Swahili | `sw` | Mimi ndiye mmiliki wa sauti hii na nimekubali kuundwa kwa modeli ya sauti yangu iliyotengenezва kwa njia ya Google Cloud.  
Swedish | `sv` | Jag äger den här rösten och har samtyckt till att en syntetisk modell av min röst skapas med hjälp av Google Cloud.  
Tamil | `ta` | இந்தக் குரலின் உரிமையாளர் நானே, மேலும் கூகிள் கிளவுடைப் பயன்படுத்தி எனது குரலின் செயற்கை மாதிரியை உருவாக்குவதற்கும் நான் ஒப்புதல் அளித்துள்ளேன்.  
Telugu | `te` | ఈ స్వరానికి నేను యజమానిని మరియు గూగుల్ క్లౌడ్‌ను ఉపయోగించి నా స్వరం యొక్క కృత్రిమ నమూనాను రూపొందించడానికి నేను సమ్మతించాను.  
Thai | `th` | ฉันเป็นเจ้าของเสียงนี้และได้ยินยอมให้สร้างแบบจำลองเสียงสังเคราะห์ของเสียงฉันโดยใช้ Google Cloud  
Turkish | `tr` | Bu sesin sahibi benim ve Google Cloud kullanılarak sesimin sentetik bir modelinin oluşturulmasına izin verdim.  
Ukrainian | `uk` | Я є власником цього голосу та дав згоду на створення синтетичної моделі мого голосу за допомогою Google Cloud.  
Urdu | `ur` | میں اس آواز کا مالک ہوں اور میں نے گوگل کلاؤڈ کے استعمال کے ذریعے اپنی آواز کا مصنوعی ماڈل بنانے کے لیے رضامندی دی ہے۔  
Vietnamese | `vi` | Tôi là chủ sở hữu giọng nói này và đã đồng ý cho phép tạo ra một mô hình tổng hợp giọng nói của mình thông qua việc sử dụng Google Cloud.  
  
## Best practices

  * **Audio quality:** The quality of the generated speech heavily depends on the quality of the `source_audio`. Use recordings with little to no background noise.
  * **Sample length:** The `source_audio` sample should be between 10 and 30 seconds long, with longer samples typically yielding better output quality.
  * **Audio format:** Sample WAV audio (both `source_audio` and `consent_audio`) must be little-endian, LINEAR16, single-channel, and 24kHz sample rate.
  * **Consent verification:** The `consent_audio` statement must be read by the target speaker following the required consent script word-for-word. Any divergence from the script will result in a failure during voice key generation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
