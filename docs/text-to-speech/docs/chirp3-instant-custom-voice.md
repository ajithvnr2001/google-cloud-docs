---
url: https://docs.cloud.google.com/text-to-speech/docs/chirp3-instant-custom-voice/
title: Chirp 3: Instant Custom Voice \u00a0|\u00a0 Cloud Text-to-Speech \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:54.621773+00:00
---

# Chirp 3: Instant Custom Voice  |  Cloud Text-to-Speech  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/docs/chirp3-instant-custom-voice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)
  * [ Guides ](https://docs.cloud.google.com/text-to-speech/docs/create-audio-text-client-libraries)



Send feedback 

#  Chirp 3: Instant Custom Voice Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** Access to Instant Custom Voice is restricted to allow-listed users. To request access, [contact a member of the sales team](https://cloud.google.com/contact).[ Try Instant Custom Voice in Vertex AI Studio](https://console.cloud.google.com/agent-platform/studio/media/speech) [Try in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/audio/speech/getting-started/get_started_with_chirp3_instant_custom_voice.ipynb) [View notebook on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/audio/speech/getting-started/get_started_with_chirp3_instant_custom_voice.ipynb)

Chirp 3's Instant Custom Voice feature lets you create personalized voice models by training a model with their high-quality audio recordings. Instant Custom Voice can rapidly generate personal voices, which can then be used to synthesize audio using the Cloud Cloud TTS API, which supports streaming and long-form text.

## Technical details

Available languages | See Available languages  
---|---  
Region availability | `global`, `us`, `eu`, `asia-southeast1`, `asia-northeast1`, `europe-west2`  
Supported output formats | 

  * `streaming`: `LINEAR16` (default), `ALAW`, `MULAW`, `OGG_OPUS`, `PCM`
  * `batch`: `LINEAR16` (default), `ALAW`, `MULAW`, `OGG_OPUS`, `PCM`

  
Supported encoding formats | `LINEAR16`, `PCM`, `MP3`, `M4A`  
Supported features | 

  * **Text-based prompting** : Use punctuation, pauses, and disfluency to add natural flow and pacing.
  * **Pause tags** : (Experimental) Introduce on-demand pauses to synthesized audio.
  * **Pace control** : Adjust the speed of synthesized audio from 0.25x speed to 2x speed.
  * **Pronunciation control** : (Experimental) Custom pronunciations of words or phrases using IPA or X-SAMPA phonetic encoding.
  * **Language transfers** : Voice cloning keys with locale `en-US` can synthesize output in the following locales: `de-DE`, `es-US`, `es-ES`, `fr-CA`, `fr-FR`, `pt-BR`

  
  
## Available languages

Instant Custom Voice is supported in the following languages:

Language | BCP-47 code | Consent statement  
---|---|---  
Arabic (XA) | ar-XA | .أنا مالك هذا الصوت وأوافق على أن تستخدم Google هذا الصوت لإنشاء نموذج صوتي اصطناعي  
Bengali (India) | bn-IN | আমি এই ভয়েসের মালিক এবং আমি একটি সিন্থেটিক ভয়েস মডেল তৈরি করতে এই ভয়েস ব্যবহার করে Google-এর সাথে সম্মতি দিচ্ছি।  
Chinese (China) | cmn-CN | 我是此声音的拥有者并授权谷歌使用此声音创建语音合成模型  
English (Australia) | en-AU | I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model.  
English (India) | en-IN | I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model.  
English (UK) | en-GB | I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model.  
English (US) | en-US | I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model.  
French (Canada) | fr-CA | Je suis le propriétaire de cette voix et j'autorise Google à utiliser cette voix pour créer un modèle de voix synthétique.  
French (France) | fr-FR | Je suis le propriétaire de cette voix et j'autorise Google à utiliser cette voix pour créer un modèle de voix synthétique.  
German (Germany) | de-DE | Ich bin der Eigentümer dieser Stimme und bin damit einverstanden, dass Google diese Stimme zur Erstellung eines synthetischen Stimmmodells verwendet.  
Gujarati (India) | gu-IN | હું આ વોઈસનો માલિક છું અને સિન્થેટિક વોઈસ મોડલ બનાવવા માટે આ વોઈસનો ઉપયોગ કરીને google ને હું સંમતિ આપું છું  
Hindi (India) | hi-IN | मैं इस आवाज का मालिक हूं और मैं सिंथेटिक आवाज मॉडल बनाने के लिए Google को इस आवाज का उपयोग करने की सहमति देता हूं  
Indonesian (Indonesia) | id-ID | Saya pemilik suara ini dan saya menyetujui Google menggunakan suara ini untuk membuat model suara sintetis.  
Italian (Italy) | it-IT | Sono il proprietario di questa voce e acconsento che Google la utilizzi per creare un modello di voce sintetica.  
Japanese (Japan) | ja-JP | 私はこの音声の所有者であり、Googleがこの音声を使用して音声合成 モデルを作成することを承認します。  
Kannada (India) | kn-IN | ನಾನು ಈ ಧ್ವನಿಯ ಮಾಲಿಕ ಮತ್ತು ಸಂಶ್ಲೇಷಿತ ಧ್ವನಿ ಮಾದರಿಯನ್ನು ರಚಿಸಲು ಈ ಧ್ವನಿಯನ್ನು ಬಳಸಿಕೊಂಡುಗೂಗಲ್ ಗೆ ನಾನು ಸಮ್ಮತಿಸುತ್ತೇನೆ.  
Korean (Korea) | ko-KR | 나는 이 음성의 소유자이며 구글이 이 음성을 사용하여 음성 합성 모델을 생성할 것을 허용합니다.  
Malayalam (India) | ml-IN | ഈ ശബ്ദത്തിന്റെ ഉടമ ഞാനാണ്, ഒരു സിന്തറ്റിക് വോയ്‌ಸ್ മോഡൽ സൃഷ്ടിക്കാൻ ഈ ശബ്‌ദം ഉപയോഗിക്കുന്നതിന് ഞാൻ Google-ന് സമ്മതം നൽകുന്നു."  
Marathi (India) | mr-IN | मी या आवाजाचा मालक आहे आणि सिंथेटिक व्हॉइस मॉडेल तयार करण्यासाठी हा आवाज वापरण्यासाठी मी Google ला संमती देतो  
Dutch (Netherlands) | nl-NL | Ik ben de eigenaar van deze stem en ik geef Google toestemming om deze stem te gebruiken om een synthetisch stemmodel te maken.  
Polish (Poland) | pl-PL | Jestem właścicielem tego głosu i wyrażam zgodę na wykorzystanie go przez Google w celu utworzenia syntetycznego modelu głosu.  
Portuguese (Brazil) | pt-BR | Eu sou o proprietário desta voz e autorizo o Google a usá-la para criar um modelo de voz sintética.  
Russian (Russia) | ru-RU | Я являюсь владельцем этого голоса и даю согласие Google на использование этого голоса для создания модели синтетического голоса.  
Tamil (India) | ta-IN | நான் இந்த குரலின் உரிமையாளர் மற்றும் செயற்கை குரல் மாதிரியை உருவாக்க இந்த குரலை பயன்படுத்த குகல்க்கு நான் ஒப்புக்கொள்கிறேன்.  
Telugu (India) | te-IN | నేను ఈ వాయిస్ యజమానిని మరియు సింతటిక్ వాయిస్ మోడల్ ని రూపొందించడానికి ఈ వాయిస్ ని ఉపయోగించడానికి googleకి నేను సమ్మతిస్తున్నాను.  
Thai (Thailand) | th-TH | ฉันเป็นเจ้าของเสียงนี้ และฉันยินยอมให้ Google ใช้เสียงนี้เพื่อสร้างแบบจำลองเสียงสังเคราะห์  
Turkish (Turkey) | tr-TR | Bu sesin sahibi benim ve Google'ın bu sesi kullanarak sentetik bir ses modeli oluşturmasına izin veriyorum.  
Vietnamese (Vietnam) | vi-VN | Tôi là chủ sở hữu giọng nói này và tôi đồng ý cho Google sử dụng giọng nói này để tạo mô hình giọng nói tổng hợp.  
Spanish (Spain) | es-ES | Soy el propietario de esta voz y doy mi consentimiento para que Google la utilice para crear un modelo de voz sintética.  
Spanish (US) | es-US | Soy el propietario de esta voz y doy mi consentimiento para que Google la utilice para crear un modelo de voz sintética.  
  
## Use Instant Custom Voice

The following sections explore how to use Chirp 3: Instant Custom Voice capabilities in Text-to-Speech API.

### Record consent and reference audio

  1. **Record the consent statement** : To comply with legal and ethical guidelines for Instant Custom Voice, record the required consent statement as a single-channel audio file in the appropriate language and in a supported audio encoding, up to 10 seconds long. (_"I am the owner of this voice, and I consent to Google using this voice to create a synthetic voice model."_)

  2. **Record reference audio** : Use your computer microphone to record up to 10 seconds of audio as a single-channel audio file in a supported audio encoding. There should be no background noise during the recording. Record the consent and reference audio in the same environment.

  3. **Store audio files** : Save the recorded audio files in a designated Cloud Storage location.




### Guidelines for producing high-quality reference and consent audios

Follow these guidelines for producing high-quality reference and consent audios:

  * The audio should be as close to 10 seconds as possible.
  * The audio should include natural pauses and pacing.
  * The audio should have minimal background noise.
  * For more information, see Supported audio encodings. Any sample rate can be used.
  * The model replicates the quality of the microphone, so if the recording sounds fuzzy then the output will sound fuzzy as well.
  * The voice should be dynamic and a bit more expressive than what the final output should sound like. The voice should also have the cadence you want the cloned voice to have. For example, if the reference audio has no natural pauses or breaks in it, then the cloned voice won't be good at pausing.
  * A good prompt is more excited and energetic than monotone and bored, so that the model will take cues to replicate this energy.



### Create an instant custom voice using the REST API

An instant custom voice takes the form of a _voice cloning key_ , which is a text-string representation of your voice data.

#### Key things to note

Here are some key things to know about creating a custom voice:

  * There is no limit to the number of voice cloning keys that you can create, because voice cloning keys are stored on the client side and provided per request.
  * The same voice cloning key can be used by multiple clients or devices at the same time.
  * You can create 10 voice cloning keys per minute per project. For more information, see [Requests limit](https://docs.cloud.google.com/text-to-speech/quotas#requests_limit).
  * You can't use a custom consent script instead of the default. You **must** use the provided consent statement script for your chosen language.


    
    
    import requests, os, json
    
    def create_instant_custom_voice_key(
        access_token, project_id, reference_audio_bytes, consent_audio_bytes
    ):
        url = "https://texttospeech.googleapis.com/v1beta1/voices:generateVoiceCloningKey"
    
        request_body = {
            "reference_audio": {
                # Supported audio_encoding values are LINEAR16, PCM, MP3, and M4A.
                "audio_config": {"audio_encoding": "LINEAR16"},
                "content": reference_audio_bytes,
            },
            "voice_talent_consent": {
                # Supported audio_encoding values are LINEAR16, PCM, MP3, and M4A.
                "audio_config": {"audio_encoding": "LINEAR16"},
                "content": consent_audio_bytes,
            },
            "consent_script": "I am the owner of this voice and I consent to Google using this voice to create a synthetic voice model.",
            "language_code": "en-US",
        }
    
        try:
            headers = {
                "Authorization": f"Bearer {access_token}",
                "x-goog-user-project": project_id,
                "Content-Type": "application/json; charset=utf-8",
            }
    
            response = requests.post(url, headers=headers, json=request_body)
            response.raise_for_status()
    
            response_json = response.json()
            return response_json.get("voiceCloningKey")
    
        except requests.exceptions.RequestException as e:
            print(f"Error making API request: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    

### Synthesize with an instant custom voice using the REST API

Use the voice cloning key to synthesize audio using the REST API.
    
    
    import requests, os, json, base64
    from IPython.display import Audio, display
    
    def synthesize_text_with_cloned_voice(access_token, project_id, voice_key, text):
        url = "https://texttospeech.googleapis.com/v1beta1/text:synthesize"
    
        request_body = {
            "input": {
                "text": text
            },
            "voice": {
                "language_code": "en-US",
                "voice_clone": {
                    "voice_cloning_key": voice_key,
                }
            },
            "audioConfig": {
                # Supported audio_encoding values are LINEAR16, PCM, MP3, and M4A.
                "audioEncoding": "LINEAR16",
            }
        }
    
        try:
            headers = {
                "Authorization": f"Bearer {access_token}",
                "x-goog-user-project": project_id,
                "Content-Type": "application/json; charset=utf-8"
            }
    
            response = requests.post(url, headers=headers, json=request_body)
            response.raise_for_status()
    
            response_json = response.json()
            audio_content = response_json.get("audioContent")
    
            if audio_content:
                display(Audio(base64.b64decode(audio_content), rate=24000))
            else:
                print("Error: Audio content not found in the response.")
                print(response_json)
    
        except requests.exceptions.RequestException as e:
            print(f"Error making API request: {e}")
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    

### Synthesize with an instant custom voice using the Python client library

This example uses the Python client library to perform instant custom voice synthesis, using a voice cloning key that has been saved to the file, `voice_cloning_key.txt`. To generate a voice cloning key, see Create an instant custom voice using the REST API.
    
    
    from google.cloud import texttospeech
    from google.cloud.texttospeech_v1beta1.services.text_to_speech import client
    
    
    def perform_voice_cloning(
        voice_cloning_key: str,
        transcript: str,
        language_code: str,
        synthesis_output_path: str,
        tts_client: client.[TextToSpeechClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.html),
    ) -> None:
      """Perform voice cloning and write output to a file.
    
      Args:
        voice_cloning_key: The voice cloning key.
        transcript: The transcript to synthesize.
        language_code: The language code.
        synthesis_output_path: The synthesis audio output path.
        tts_client: The TTS client to use.
      """
      voice_clone_params = texttospeech.[VoiceCloneParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.VoiceCloneParams.html)(
          voice_cloning_key=voice_cloning_key
      )
      voice = texttospeech.[VoiceSelectionParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.VoiceSelectionParams.html)(
          language_code=language_code, voice_clone=voice_clone_params
      )
      request = texttospeech.[SynthesizeSpeechRequest](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.SynthesizeSpeechRequest.html)(
          input=texttospeech.[SynthesisInput](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.SynthesisInput.html)(text=transcript),
          voice=voice,
          audio_config=texttospeech.[AudioConfig](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AudioConfig.html)(
              audio_encoding=texttospeech.[AudioEncoding](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AudioEncoding.html).LINEAR16,
              sample_rate_hertz=24000,
          ),
      )
      response = tts_client.[synthesize_speech](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.html#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_synthesize_speech)(request)
      with open(synthesis_output_path, 'wb') as out:
        out.write(response.audio_content)
        print(f'Audio content written to file {synthesis_output_path}.')
    
    
    if __name__ == '__main__':
      client = texttospeech.[TextToSpeechClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.html)()
      with open('voice_cloning_key.txt', 'r') as f:
        key = f.read()
      perform_voice_cloning(
          voice_cloning_key=key,
          transcript='Hello world!',
          language_code='en-US',
          synthesis_output_path='/tmp/output.wav',
          tts_client=client,
      )
    

### Streaming synthesize with an instant custom voice using the Python client library

This example uses the Python client library to perform instant custom voice streaming synthesis, using a voice cloning key saved to `voice_cloning_key.txt`. To generate a voice cloning key, see Create an instant custom voice using the REST API.
    
    
    import io
    import wave
    from google.cloud import texttospeech
    from google.cloud.texttospeech_v1beta1.services.text_to_speech import client
    
    
    def perform_voice_cloning_with_simulated_streaming(
        voice_cloning_key: str,
        simulated_streamed_text: list[str],
        language_code: str,
        synthesis_output_path: str,
        tts_client: client.[TextToSpeechClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.html),
    ) -> None:
      """Perform voice cloning for a given reference audio, voice talent consent, and consent script.
    
      Args:
        voice_cloning_key: The voice cloning key.
        simulated_streamed_text: The list of transcripts to synthesize, where each
          item represents a chunk of streamed text. This is used to simulate
          streamed text input and is not meant to be representative of real-world
          streaming usage.
        language_code: The language code.
        synthesis_output_path: The path to write the synthesis audio output to.
        tts_client: The TTS client to use.
      """
      voice_clone_params = texttospeech.[VoiceCloneParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.VoiceCloneParams.html)(
          voice_cloning_key=voice_cloning_key
      )
      streaming_config = texttospeech.[StreamingSynthesizeConfig](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingSynthesizeConfig.html)(
          voice=texttospeech.[VoiceSelectionParams](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.VoiceSelectionParams.html)(
              language_code=language_code, voice_clone=voice_clone_params
          ),
          streaming_audio_config=texttospeech.[StreamingAudioConfig](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingAudioConfig.html)(
              audio_encoding=texttospeech.[AudioEncoding](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.AudioEncoding.html).PCM,
              sample_rate_hertz=24000,
          ),
      )
      config_request = texttospeech.[StreamingSynthesizeRequest](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingSynthesizeRequest.html)(
          streaming_config=streaming_config
      )
    
      # Request generator. Consider using Gemini or another LLM with output
      # streaming as a generator.
      def request_generator():
        yield config_request
        for text in simulated_streamed_text:
          yield texttospeech.[StreamingSynthesizeRequest](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingSynthesizeRequest.html)(
              input=texttospeech.[StreamingSynthesisInput](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.types.StreamingSynthesisInput.html)(text=text)
          )
    
      streaming_responses = tts_client.[streaming_synthesize](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.html#google_cloud_texttospeech_v1_services_text_to_speech_TextToSpeechClient_streaming_synthesize)(request_generator())
      audio_buffer = io.BytesIO()
      for response in streaming_responses:
        print(f'Audio content size in bytes is: {len(response.audio_content)}')
        audio_buffer.write(response.audio_content)
    
      # Write collected audio outputs to a WAV file.
      with wave.open(synthesis_output_path, 'wb') as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(24000)
        wav_file.writeframes(audio_buffer.getvalue())
        print(f'Audio content written to file {synthesis_output_path}.')
    
    
    if __name__ == '__main__':
      client = texttospeech.[TextToSpeechClient](https://docs.cloud.google.com/python/docs/reference/texttospeech/latest/google.cloud.texttospeech_v1.services.text_to_speech.TextToSpeechClient.html)()
      with open('voice_cloning_key.txt', 'r') as f:
        key = f.read()
      perform_voice_cloning_with_simulated_streaming(
          voice_cloning_key=key,
          simulated_streamed_text=[
              'Hello world!',
              'This is the second text chunk.',
              'This simulates streaming text for synthesis.',
          ],
          language_code='en-US',
          synthesis_output_path='streaming_output.wav',
          tts_client=client,
      )
    

## Use Chirp 3: HD voice controls

Instant Custom Voice supports the same pace control, pause control, and custom pronunciation features that Chirp 3: HD voices supports. For more information on Chirp 3: HD voice controls, see [Chirp 3: HD voice controls](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd#chirp3-hd-voice-controls).

All three features can be enabled for instant custom voice by adjusting the `SynthesizeSpeechRequest` or `StreamingSynthesizeConfig` in the same way that it's done for Instant Custom Voice.

### Language availability for voice controls

  * Pace control is available across all locales.

  * Pause control is available across all locales.

  * Custom pronunciations is available across all locales except: `bn-IN`, `gu-IN`, `th-TH`, and `vi-VN`.




## Enable multilingual transfer

Instant Custom Voice supports multilingual transfer for specified pairs of locales. This means that given a voice cloning key generated with a given language code like `en-US`, the key can be used to synthesize language in a different language like `es-ES`. Voice cloning keys with locale `en-US` can synthesize output in the following locales: `de-DE`, `es-US`, `es-ES`, `fr-CA`, `fr-FR`, `pt-BR`.

This code sample demonstrates the configuration of `SynthesizeRequest` to synthesize `es-ES` using an `en-US` voice cloning key:
    
    
    voice_clone_params = texttospeech.VoiceCloneParams(
        voice_cloning_key=en_us_voice_cloning_key
    )
    request = texttospeech.SynthesizeSpeechRequest(
      input=texttospeech.SynthesisInput(text=transcript),
      voice=texttospeech.VoiceSelectionParams(
          language_code='es-ES', voice_clone=voice_clone_params
      ),
      audio_config=texttospeech.AudioConfig(
          audio_encoding=texttospeech.AudioEncoding.LINEAR16,
          sample_rate_hertz=24000,
      ),
    )
    

Example of configuring `StreamingSynthesizeConfig` to synthesize `es-ES` using an `en-US` voice cloning key:
    
    
    voice_clone_params = texttospeech.VoiceCloneParams(
        voice_cloning_key=en_us_voice_cloning_key
    )
    streaming_config = texttospeech.StreamingSynthesizeConfig(
        voice=texttospeech.VoiceSelectionParams(
            language_code='es-ES', voice_clone=voice_clone_params
        ),
        streaming_audio_config=texttospeech.StreamingAudioConfig(
            audio_encoding=texttospeech.AudioEncoding.PCM,
            sample_rate_hertz=24000,
        ),
    )
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
