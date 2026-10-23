---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/word-confidence/
title: Enable word-level confidence \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:31.674353+00:00
---

# Enable word-level confidence  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/word-confidence/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Enable word-level confidence Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can specify that Cloud Speech-to-Text indicate a value of accuracy, or [confidence level](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-requests#confidence-values), for individual words in a transcription.

## Word-level confidence

When the Cloud Speech-to-Text transcribes an audio clip, it also measures the degree of accuracy for the response. The response sent from Cloud STT states the confidence level for the entire transcription request as a number between 0.0 and 1.0. The following code sample shows an example of the confidence level value returned by Cloud STT.
    
    
    {
      "results": [
        {
          "alternatives": [
            {
              "transcript": "how old is the Brooklyn Bridge",
              **"confidence": 0.96748614**
            }
          ]
        }
      ]
    }
    

In addition to the confidence level of the entire transcription, Cloud STT can also provide the confidence level of individual words within the transcription. The response then includes [`WordInfo`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/recognize#WordInfo) details in the transcription, indicating the confidence level for individual words as shown in the following example.
    
    
    {
      "results": [
        {
          "alternatives": [
            {
              "transcript": "how old is the Brooklyn Bridge",
              "confidence": 0.98360395,
              "words": [
                {
                  "startTime": "0s",
                  "endTime": "0.300s",
                  "word": "how",
                  **"confidence": SOME NUMBER**
                },
                ...
              ]
            }
          ]
        }
      ]
    }
    

## Enable word-level confidence in a request

The following code snippet demonstrates how to enable word-level confidence in a transcription request to Cloud Speech-to-Text using local and remote files

### Use a local file

### Protocol

Refer to the [`speech:recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/recognize) API endpoint for complete details.

To perform synchronous speech recognition, make a `POST` request and provide the appropriate request body. The following shows an example of a `POST` request using `curl`. The example uses the [Google Cloud CLI](https://docs.cloud.google.com/sdk) to generate an access token. For instructions on installing the gcloud CLI, see the [quickstart](https://docs.cloud.google.com/speech-to-text/docs/transcribe-api). 

The following example show how to send a `POST` request using `curl`, where the body of the request enables word-level confidence.
    
    
    curl -s -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        https://speech.googleapis.com/v1p1beta1/speech:recognize \
        --data '{
        "config": {
            "encoding": "FLAC",
            "sampleRateHertz": 16000,
            "languageCode": "en-US",
            "enableWordTimeOffsets": true,
    **"enableWordConfidence": true**
        },
        "audio": {
            "uri": "gs://cloud-samples-tests/speech/brooklyn.flac"
        }
    }' > word-level-confidence.txt

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format, saved to a file named `word-level-confidence.txt`.
    
    
    {
      "results": [
        {
          "alternatives": [
            {
              "transcript": "how old is the Brooklyn Bridge",
              "confidence": 0.98360395,
              "words": [
                {
                  "startTime": "0s",
                  "endTime": "0.300s",
                  "word": "how",
                  "confidence": 0.98762906
                },
                {
                  "startTime": "0.300s",
                  "endTime": "0.600s",
                  "word": "old",
                  "confidence": 0.96929157
                },
                {
                  "startTime": "0.600s",
                  "endTime": "0.800s",
                  "word": "is",
                  "confidence": 0.98271006
                },
                {
                  "startTime": "0.800s",
                  "endTime": "0.900s",
                  "word": "the",
                  "confidence": 0.98271006
                },
                {
                  "startTime": "0.900s",
                  "endTime": "1.100s",
                  "word": "Brooklyn",
                  "confidence": 0.98762906
                },
                {
                  "startTime": "1.100s",
                  "endTime": "1.500s",
                  "word": "Bridge",
                  "confidence": 0.98762906
                }
              ]
            }
          ],
          "languageCode": "en-us"
        }
      ]
    }
    

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Transcribe a local audio file with word level confidence
     *
     * @param fileName the path to the local audio file
     */
    public static void transcribeWordLevelConfidence(String fileName) throws Exception {
      Path path = Paths.get(fileName);
      byte[] content = Files.readAllBytes(path);
    
      try (SpeechClient speechClient = SpeechClient.create()) {
        RecognitionAudio recognitionAudio =
            RecognitionAudio.newBuilder().setContent(ByteString.copyFrom(content)).build();
        // Configure request to enable word level confidence
        RecognitionConfig config =
            RecognitionConfig.newBuilder()
                .setEncoding(AudioEncoding.LINEAR16)
                .setSampleRateHertz(16000)
                .setLanguageCode("en-US")
                .setEnableWordConfidence(true)
                .build();
        // Perform the transcription request
        RecognizeResponse recognizeResponse = speechClient.recognize(config, recognitionAudio);
    
        // Print out the results
        for (SpeechRecognitionResult result : recognizeResponse.getResultsList()) {
          // There can be several alternative transcripts for a given chunk of speech. Just use the
          // first (most likely) one here.
          SpeechRecognitionAlternative alternative = result.getAlternatives(0);
          System.out.format("Transcript : %s\n", alternative.getTranscript());
          System.out.format(
              "First Word and Confidence : %s %s \n",
              alternative.getWords(0).getWord(), alternative.getWords(0).getConfidence());
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
      encoding: 'FLAC',
      sampleRateHertz: 16000,
      languageCode: 'en-US',
      enableWordConfidence: true,
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
    const confidence = response.results
      .map(result => result.alternatives[0].confidence)
      .join('\n');
    console.log(`Transcription: ${transcription} \n Confidence: ${confidence}`);
    
    console.log('Word-Level-Confidence:');
    const words = response.results.map(result => result.alternatives[0]);
    words[0].words.forEach(a => {
      console.log(` word: ${a.word}, confidence: ${a.confidence}`);
    });

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech_v1p1beta1 as speech
    
    client = speech.SpeechClient()
    
    speech_file = "resources/Google_Gnome.wav"
    
    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()
    
    audio = speech.RecognitionAudio(content=content)
    
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
        enable_word_confidence=True,
    )
    
    response = client.recognize(config=config, audio=audio)
    
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print(f"First alternative of result {i}")
        print(f"Transcript: {alternative.transcript}")
        print(
            "First Word and Confidence: ({}, {})".format(
                alternative.words[0].word, alternative.words[0].confidence
            )
        )
    
    return response.results

### Use a remote file

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Transcribe a remote audio file with word level confidence
     *
     * @param gcsUri path to the remote audio file
     */
    public static void transcribeWordLevelConfidenceGcs(String gcsUri) throws Exception {
      try (SpeechClient speechClient = SpeechClient.create()) {
    
        // Configure request to enable word level confidence
        RecognitionConfig config =
            RecognitionConfig.newBuilder()
                .setEncoding(AudioEncoding.FLAC)
                .setSampleRateHertz(44100)
                .setLanguageCode("en-US")
                .setEnableWordConfidence(true)
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
        // Just print the first result here.
        SpeechRecognitionResult result = response.get().getResultsList().get(0);
    
        // There can be several alternative transcripts for a given chunk of speech. Just use the
        // first (most likely) one here.
        SpeechRecognitionAlternative alternative = result.getAlternativesList().get(0);
        // Print out the result
        System.out.printf("Transcript : %s\n", alternative.getTranscript());
        System.out.format(
            "First Word and Confidence : %s %s \n",
            alternative.getWords(0).getWord(), alternative.getWords(0).getConfidence());
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
      encoding: 'FLAC',
      sampleRateHertz: 16000,
      languageCode: 'en-US',
      enableWordConfidence: true,
    };
    
    const audio = {
      uri: gcsUri,
    };
    
    const request = {
      config: config,
      audio: audio,
    };
    
    const [response] = await client.recognize(request);
    const transcription = response.results
      .map(result => result.alternatives[0].transcript)
      .join('\n');
    const confidence = response.results
      .map(result => result.alternatives[0].confidence)
      .join('\n');
    console.log(`Transcription: ${transcription} \n Confidence: ${confidence}`);
    
    console.log('Word-Level-Confidence:');
    const words = response.results.map(result => result.alternatives[0]);
    words[0].words.forEach(a => {
      console.log(` word: ${a.word}, confidence: ${a.confidence}`);
    });

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech_v1p1beta1 as speech
    
    
    def transcribe_file_with_word_level_confidence(audio_uri: str) -> str:
        """Transcribe a remote audio file with word level confidence.
        Args:
            audio_uri (str): The Cloud Storage URI of the input audio.
                E.g., gs://[BUCKET]/[FILE]
        Returns:
            The generated transcript from the audio file provided with word level confidence.
        """
    
        client = speech.SpeechClient()
    
        # Configure request to enable word level confidence
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
            sample_rate_hertz=44100,
            language_code="en-US",
            enable_word_confidence=True,  # Enable word level confidence
        )
    
        # Set the remote path for the audio file
        audio = speech.RecognitionAudio(uri=audio_uri)
    
        # Use non-blocking call for getting file transcription
        response = client.long_running_recognize(config=config, audio=audio).result(
            timeout=300
        )
    
        transcript_builder = []
        for i, result in enumerate(response.results):
            alternative = result.alternatives[0]
            transcript_builder.append("-" * 20)
            transcript_builder.append(f"\nFirst alternative of result {i}")
            transcript_builder.append(f"\nTranscript: {alternative.transcript}")
            transcript_builder.append(
                "\nFirst Word and Confidence: ({}, {})".format(
                    alternative.words[0].word, alternative.words[0].confidence
                )
            )
    
        transcript = "".join(transcript_builder)
        print(transcript)
    
        return transcript
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
