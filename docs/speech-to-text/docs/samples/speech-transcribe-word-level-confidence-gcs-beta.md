---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-word-level-confidence-gcs-beta/
title: Transcribe a file in Cloud Storage with word-level confidence (beta) \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:06.637336+00:00
---

# Transcribe a file in Cloud Storage with word-level confidence (beta)  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-word-level-confidence-gcs-beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Transcribe a file in Cloud Storage with word-level confidence (beta) Stay organized with collections  Save and categorize content based on your preferences. 

Transcribe an audio file stored in Cloud Storage, returning the confidence level for each word.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Enable word-level confidence](https://docs.cloud.google.com/speech-to-text/docs/v1/word-confidence)



## Code sample

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
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
