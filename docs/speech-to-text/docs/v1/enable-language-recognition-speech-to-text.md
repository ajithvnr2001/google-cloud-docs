---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/enable-language-recognition-speech-to-text/
title: Enable language recognition in Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:22.348227+00:00
---

# Enable language recognition in Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/enable-language-recognition-speech-to-text/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Enable language recognition in Cloud Speech-to-Text Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to enable language recognition for audio transcription requests sent to Cloud Speech-to-Text.

In some situations, you don't know for certain what language your audio recordings contain. For example, if you publish your service, app, or product in a country with multiple official languages, you can potentially receive audio input from users in a variety of languages. This can make specifying a single language code for transcription requests significantly more difficult.

## Multiple language recognition

Cloud Speech-to-Text offers a way for you to specify a set of alternative languages that your audio data might contain. When you send an audio transcription request to Cloud Speech-to-Text, you can provide a list of additional languages that the audio data might include. If you include a list of languages in your request, Cloud Speech-to-Text attempts to transcribe the audio based upon the language that best fits the sample from the alternates you provide. Cloud Speech-to-Text then labels the transcription results with the predicted language code.

This feature is ideal for apps that need to transcribe short statements like voice commands or search. You can list up to three alternative languages from [among those that Cloud Speech-to-Text supports](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-supported-languages) in addition to your primary language (for four languages total).

Even though you can specify alternative languages for your speech transcription request, you must still provide a primary language code in the `languageCode` field. Also, you should constrain the number of languages you request to a bare minimum. The fewer alternative language codes that you request helps Cloud Speech-to-Text more successfully select the correct one. Specifying just a single language produces the best results.

## Enable language recognition in audio transcription requests

To specify alternative languages in your audio transcription, you must set the `alternativeLanguageCodes` field to a list of language codes in the [`RecognitionConfig`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig) parameters for the request. Cloud STT supports alternative language codes for all speech recognition methods: [`speech:recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/recognize), [`speech:longrunningrecognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/longrunningrecognize), and [Streaming](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.StreamingRecognizeRequest).

**Note:** The alternative languages feature only works if [the model is available](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-supported-languages) in all the requested languages. For more information about how to specify different models, see the [`RecognitionConfig`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig) reference documentation.

### Use a local file

### Protocol

Refer to the [`speech:recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/recognize) API endpoint for complete details.

To perform synchronous speech recognition, make a `POST` request and provide the appropriate request body. The following shows an example of a `POST` request using `curl`. The example uses the [Google Cloud CLI](https://docs.cloud.google.com/sdk) to generate an access token. For instructions on installing the gcloud CLI, see the [quickstart](https://docs.cloud.google.com/speech-to-text/docs/transcribe-api). 

The following example shows how to request transcription of an audio file that may include speech in English, French, or German.
    
    
    curl -s -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        https://speech.googleapis.com/v1p1beta1/speech:recognize \
        --data '{
        "config": {
            "encoding": "LINEAR16",
            "languageCode": "en-US",
    **"alternativeLanguageCodes": ["fr-FR", "de-DE"],**
            "model": "command_and_search"
        },
        "audio": {
            "uri": "gs://cloud-samples-tests/speech/commercial_mono.wav"
        }
    }' > multi-language.txt

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format, saved to a file named `multi-language.txt`.
    
    
    {
      "results": [
        {
          "alternatives": [
            {
              "transcript": "hi I'd like to buy a Chromecast I'm ..."
              "confidence": 0.9466864
            }
          ],
          "languageCode": "en-us"
        },
        {
          "alternatives": [
            {
              "transcript": " let's go with the black one",
              "confidence": 0.9829583
            }
          ],
          "languageCode": "en-us"
        },
      ]
    }
    

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Transcribe a local audio file with multi-language recognition
     *
     * @param fileName the path to the audio file
     */
    public static void transcribeMultiLanguage(String fileName) throws Exception {
      Path path = Paths.get(fileName);
      // Get the contents of the local audio file
      byte[] content = Files.readAllBytes(path);
    
      try (SpeechClient speechClient = SpeechClient.create()) {
    
        RecognitionAudio recognitionAudio =
            RecognitionAudio.newBuilder().setContent(ByteString.copyFrom(content)).build();
        ArrayList<String> languageList = new ArrayList<>();
        languageList.add("es-ES");
        languageList.add("en-US");
    
        // Configure request to enable multiple languages
        RecognitionConfig config =
            RecognitionConfig.newBuilder()
                .setEncoding(AudioEncoding.LINEAR16)
                .setSampleRateHertz(16000)
                .setLanguageCode("ja-JP")
                .addAllAlternativeLanguageCodes(languageList)
                .build();
        // Perform the transcription request
        RecognizeResponse recognizeResponse = speechClient.recognize(config, recognitionAudio);
    
        // Print out the results
        for (SpeechRecognitionResult result : recognizeResponse.getResultsList()) {
          // There can be several alternative transcripts for a given chunk of speech. Just use the
          // first (most likely) one here.
          SpeechRecognitionAlternative alternative = result.getAlternatives(0);
          System.out.format("Transcript : %s\n\n", alternative.getTranscript());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const fs = require('fs');
    
    // Imports the Google Cloud client library
    const speech = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)').v1p1beta1;
    
    // Creates a client
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const fileName = 'Local path to audio file, e.g. /path/to/audio.raw';
    
    const config = {
      encoding: 'LINEAR16',
      sampleRateHertz: 44100,
      languageCode: 'en-US',
      alternativeLanguageCodes: ['es-ES', 'en-US'],
    };
    
    const audio = {
      content: fs.readFileSync(fileName).toString('base64'),
    };
    
    const request = {
      config: config,
      audio: audio,
    };
    
    const [response] = await client.recognize(request);
    const transcription = response.results
      .map(result => result.alternatives[0].transcript)
      .join('\n');
    console.log(`Transcription: ${transcription}`);

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech_v1p1beta1 as speech
    
    client = speech.SpeechClient()
    
    speech_file = "resources/multi.wav"
    first_lang = "en-US"
    second_lang = "es"
    
    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()
    
    audio = speech.RecognitionAudio(content=content)
    
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        audio_channel_count=2,
        language_code=first_lang,
        alternative_language_codes=[second_lang],
    )
    
    print("Waiting for operation to complete...")
    response = client.recognize(config=config, audio=audio)
    
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print(f"First alternative of result {i}: {alternative}")
        print(f"Transcript: {alternative.transcript}")
    
    return response.results

### Use a remote file

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Transcribe a remote audio file with multi-language recognition
     *
     * @param gcsUri the path to the remote audio file
     */
    public static void transcribeMultiLanguageGcs(String gcsUri) throws Exception {
      try (SpeechClient speechClient = SpeechClient.create()) {
    
        ArrayList<String> languageList = new ArrayList<>();
        languageList.add("es-ES");
        languageList.add("en-US");
    
        // Configure request to enable multiple languages
        RecognitionConfig config =
            RecognitionConfig.newBuilder()
                .setEncoding(AudioEncoding.LINEAR16)
                .setSampleRateHertz(16000)
                .setLanguageCode("ja-JP")
                .addAllAlternativeLanguageCodes(languageList)
                .build();
    
        // Set the remote path for the audio file
        RecognitionAudio audio = RecognitionAudio.newBuilder().setUri(gcsUri).build();
    
        // Use non-blocking call for getting file transcription
        OperationFuture<LongRunningRecognizeResponse, LongRunningRecognizeMetadata> response =
            speechClient.longRunningRecognizeAsync(config, audio);
    
        while (!response.isDone()) {
          System.out.println("Waiting for response...");
          Thread.sleep(10000);
        }
    
        for (SpeechRecognitionResult result : response.get().getResultsList()) {
    
          // There can be several alternative transcripts for a given chunk of speech. Just use the
          // first (most likely) one here.
          SpeechRecognitionAlternative alternative = result.getAlternativesList().get(0);
    
          // Print out the result
          System.out.printf("Transcript : %s\n\n", alternative.getTranscript());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const speech = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)').v1p1beta1;
    
    // Creates a client
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const uri = path to GCS audio file e.g. `gs:/bucket/audio.wav`;
    
    const config = {
      encoding: 'LINEAR16',
      sampleRateHertz: 44100,
      languageCode: 'en-US',
      alternativeLanguageCodes: ['es-ES', 'en-US'],
    };
    
    const audio = {
      uri: gcsUri,
    };
    
    const request = {
      config: config,
      audio: audio,
    };
    
    const [operation] = await client.longRunningRecognize(request);
    const [response] = await operation.promise();
    const transcription = response.results
      .map(result => result.alternatives[0].transcript)
      .join('\n');
    console.log(`Transcription: ${transcription}`);

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech_v1p1beta1 as speech
    
    
    def transcribe_file_with_multilanguage_gcs(audio_uri: str) -> str:
        """Transcribe a remote audio file with multi-language recognition
        Args:
            audio_uri (str): The Google Cloud Storage path to an audio file.
                E.g., gs://[BUCKET]/[FILE]
        Returns:
            str: The generated transcript from the audio file provided.
        """
    
        client = speech.SpeechClient()
    
        first_language = "es-ES"
        alternate_languages = ["en-US", "fr-FR"]
    
        # Configure request to enable multiple languages
        recognition_config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
            sample_rate_hertz=44100,
            language_code=first_language,
            alternative_language_codes=alternate_languages,
        )
    
        # Set the remote path for the audio file
        audio = speech.RecognitionAudio(uri=audio_uri)
    
        # Use non-blocking call for getting file transcription
        response = client.long_running_recognize(
            config=recognition_config, audio=audio
        ).result(timeout=300)
    
        transcript_builder = []
        for i, result in enumerate(response.results):
            alternative = result.alternatives[0]
            transcript_builder.append("-" * 20 + "\n")
            transcript_builder.append(f"First alternative of result {i}: {alternative}")
            transcript_builder.append(f"Transcript: {alternative.transcript} \n")
    
        transcript = "".join(transcript_builder)
        print(transcript)
    
        return transcript
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
