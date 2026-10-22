---
url: https://docs.cloud.google.com/text-to-speech/docs/gemini-tts-voice-replication/
title: Gemini-TTS voice replication \u00a0|\u00a0 Cloud Text-to-Speech \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:12:32.873064+00:00
---

# Gemini-TTS voice replication  |  Cloud Text-to-Speech  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/docs/gemini-tts-voice-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)



Send feedback 

#  Gemini-TTS voice replication Stay organized with collections  Save and categorize content based on your preferences. 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This feature is available to a small set of customers who have attested to using only voices where the voice actor has granted permission and consented to use of their voice for this purpose. To request access, fill out this form: [Gemini-TTS Voice Replication Allowlist](https://docs.google.com/forms/d/1jzHeYXKM8rvoTHyvY_PFl76d6RNYJOGcZH3ctVP5XXk).

The Vertex AI API lets you generate speech using a specific voice from a reference audio file. This voice replication feature enables the model to mimic the voice, tone, cadence, and timbre of a custom voice sample, offering greater flexibility and choices than the standard [prebuilt voices](https://ai.google.dev/gemini-api/docs/speech-generation) to create unique voices.

It works by taking in a WAV reference audio sample, `voice_sample_audio`, as raw bytes and using it as a reference to synthesize the text response in a matching voice, then producing output audio as raw PCM audio bytes. The provided reference audio is only for the current session and not otherwise stored or reused.

### How to use Gemini-TTS voice replication

See [Use Vertex AI API](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts#use-vertex-ai-api) to learn how to synthesize speech using the Vertex AI API. If using Python, refer to the [Google Gen AI SDK](https://googleapis.github.io/python-genai/) documentation and be sure to install at minimum [version 1.54.0 of `google-genai`](https://pypi.org/project/google-genai/1.54.0/).

To use voice replication, you must:

  * Specify the `gemini-2.5-flash-tts-eap-11-2025` model in the `GenerateContent` request.
  * Configure the `SpeechConfig` object in the generation config to include a `ReplicatedVoiceConfig`.
  * Configure `ReplicatedVoiceConfig` to include a `voice_sample_audio` field, representing the raw bytes of the reference WAV audio file. The audio must be little-endian, LINEAR16, 24khz and mono-channel. The optimal audio length is between 10 to 30 seconds long.
  * Set `response_modalities` to `["AUDIO"]`.
  * Supply the text to synthesize in the `contents` field, following the same guidelines from [Use Vertex AI](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts#use-vertex-ai-api).



### Example of performing voice replication

The following example demonstrates how to load a local WAV file as a reference voice, configure the generation request, and save the resulting audio. Because the API returns raw PCM audio, this example also converts the raw data into a standard WAV file.

**Note:** Voice replication is only supported for synchronous synthesis, and not streaming synthesis.

### Python
    
    
    import base64
    import wave
    
    from google import genai  # minimum version 1.54.0 is required
    from google.genai import types
    
    PROJECT_ID = "YOUR_PROJECT_ID"
    VOICE_SAMPLE_PATH = "VOICE_SAMPLE_PATH.wav"
    OUTPUT_FILE_PATH = "OUTPUT_FILE_PATH.wav"
    
    # Set up the wave file to save the output:
    def wave_file(filename, pcm, channels=1, rate=24000, sample_width=2):
      with wave.open(filename, "wb") as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(sample_width)
        wf.setframerate(rate)
        wf.writeframes(pcm)
    
    # Read voice sample audio
    with open(VOICE_SAMPLE_PATH, "rb") as f:
      voice_sample_audio = f.read()
    
    # Base64 encode the audio bytes
    encoded_audio = base64.b64encode(voice_sample_audio).decode("utf-8")
    client = genai.Client(vertexai=True, project=PROJECT_ID)
    response = client.models.generate_content(
        model="gemini-2.5-flash-tts-eap-11-2025",
        contents="Say the following: This is a replicated voice.",
        config=types.GenerateContentConfig(
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    replicated_voice_config=types.ReplicatedVoiceConfig(
                        voice_sample_audio=encoded_audio
                    )
                ),
            ),
            response_modalities=["AUDIO"],
        ),
    )
    
    data = response.candidates[0].content.parts[0].inline_data.data
    
    wave_file(OUTPUT_FILE_PATH, data)  # Saves the file to current directory
    

### CURL
    
    
    # Make sure to install gcloud cli, and sign in to your project.
    # Make sure to use your PROJECT_ID value.
    # The VOICE_SAMPLE_PATH should point to your WAV audio file (e.g., /tmp/voice_sample.wav).
    # Requires the JQ and ffmpeg library to be installed.
    PROJECT_ID=YOUR_PROJECT_ID
    VOICE_SAMPLE_PATH=YOUR_VOICE_SAMPLE_PATH.wav
    OUTPUT_FILE_PATH=YOUR_OUTPUT_FILE_PATH.wav
    REQUEST_JSON=$(cat <<EOF
    {
      "contents": {
        "role": "user",
        "parts": [{ "text": "Say the following: This is a replicated voice." }]
      },
      "generation_config": {
        "response_modalities": ["AUDIO"],
        "speech_config": {
            "voice_config": {
                "replicated_voice_config": {
                  "voice_sample_audio": "$(cat $VOICE_SAMPLE_PATH | base64 | tr -d '\n')"
                }
            }
        }
      }
    }
    EOF
    )
    echo "$REQUEST_JSON" > /tmp/request.json
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "x-goog-user-project: $PROJECT_ID" \
      -H "Content-Type: application/json" \
      -d @/tmp/request.json \
      "https://aiplatform.googleapis.com/v1/projects/$PROJECT_ID/locations/global/publishers/google/models/gemini-2.5-flash-tts-eap-11-2025:generateContent" \
      | jq -r '.candidates[0].content.parts[0].inlineData.data' \
      | python3 -m base64 -d | ffmpeg -y -f s16le -ar 24k -ac 1 -i - $OUTPUT_FILE_PATH
    

### Best practices

  * **Audio quality:** The quality of the generated speech heavily depends on the quality of the voice_sample_audio. Use a recording with little to no background noise.
  * **Sample length:** The audio sample should be between 10 and 30 seconds long, with longer samples typically yielding better output quality.
  * **Audio format:** Sample WAV audio must be little-endian, LINEAR16, single-channel, and 24kHz sample rate.



### Quota

A quota of 150 requests per minute is enforced.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
