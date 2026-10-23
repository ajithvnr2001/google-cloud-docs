---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-recognition-metadata-beta/
title: Transcribe a local file with recognition metadata (beta) \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:27.503811+00:00
---

# Transcribe a local file with recognition metadata (beta)  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-recognition-metadata-beta/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Transcribe a local file with recognition metadata (beta) Stay organized with collections  Save and categorize content based on your preferences. 

Transcribe a local audio file, including recognition metadata in the response.

## Code sample

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Transcribe the given audio file and include recognition metadata in the request.
     *
     * @param fileName the path to an audio file.
     */
    public static void transcribeFileWithMetadata(String fileName) throws Exception {
      Path path = Paths.get(fileName);
      byte[] content = Files.readAllBytes(path);
    
      try (SpeechClient speechClient = SpeechClient.create()) {
        // Get the contents of the local audio file
        RecognitionAudio recognitionAudio =
            RecognitionAudio.newBuilder().setContent(ByteString.copyFrom(content)).build();
    
        // Construct a recognition metadata object.
        // Most metadata fields are specified as enums that can be found
        // in speech.enums.RecognitionMetadata
        RecognitionMetadata metadata =
            RecognitionMetadata.newBuilder()
                .setInteractionType(InteractionType.DISCUSSION)
                .setMicrophoneDistance(MicrophoneDistance.NEARFIELD)
                .setRecordingDeviceType(RecordingDeviceType.SMARTPHONE)
                .setRecordingDeviceName("Pixel 2 XL") // Some metadata fields are free form strings
                // And some are integers, for instance the 6 digit NAICS code
                // https://www.naics.com/search/
                .setIndustryNaicsCodeOfAudio(519190)
                .build();
    
        // Configure request to enable enhanced models
        RecognitionConfig config =
            RecognitionConfig.newBuilder()
                .setEncoding(AudioEncoding.LINEAR16)
                .setLanguageCode("en-US")
                .setSampleRateHertz(8000)
                .setMetadata(metadata) // Add the metadata to the config
                .build();
    
        // Perform the transcription request
        RecognizeResponse recognizeResponse = speechClient.recognize(config, recognitionAudio);
    
        // Print out the results
        for (SpeechRecognitionResult result : recognizeResponse.getResultsList()) {
          // There can be several alternative transcripts for a given chunk of speech. Just use the
          // first (most likely) one here.
          SpeechRecognitionAlternative alternative = result.getAlternatives(0);
          System.out.format("Transcript: %s\n\n", alternative.getTranscript());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library for Beta API
    /**
     * TODO(developer): Update client library import to use new
     * version of API when desired features become available
     */
    const speech = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)').v1p1beta1;
    const fs = require('fs');
    
    // Creates a client
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    async function syncRecognizeWithMetaData() {
      /**
       * TODO(developer): Uncomment the following lines before running the sample.
       */
      // const filename = 'Local path to audio file, e.g. /path/to/audio.raw';
      // const encoding = 'Encoding of the audio file, e.g. LINEAR16';
      // const sampleRateHertz = 16000;
      // const languageCode = 'BCP-47 language code, e.g. en-US';
    
      const recognitionMetadata = {
        interactionType: 'DISCUSSION',
        microphoneDistance: 'NEARFIELD',
        recordingDeviceType: 'SMARTPHONE',
        recordingDeviceName: 'Pixel 2 XL',
        industryNaicsCodeOfAudio: 519190,
      };
    
      const config = {
        encoding: encoding,
        sampleRateHertz: sampleRateHertz,
        languageCode: languageCode,
        metadata: recognitionMetadata,
      };
    
      const audio = {
        content: fs.readFileSync(filename).toString('base64'),
      };
    
      const request = {
        config: config,
        audio: audio,
      };
    
      // Detects speech in the audio file
      const [response] = await client.recognize(request);
      response.results.forEach(result => {
        const alternative = result.alternatives[0];
        console.log(alternative.transcript);
      });

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech_v1p1beta1 as speech
    
    client = speech.SpeechClient()
    
    speech_file = "resources/commercial_mono.wav"
    
    with open(speech_file, "rb") as audio_file:
        content = audio_file.read()
    
    # Here we construct a recognition metadata object.
    # Most metadata fields are specified as enums that can be found
    # in speech.enums.RecognitionMetadata
    metadata = speech.RecognitionMetadata()
    metadata.interaction_type = speech.RecognitionMetadata.InteractionType.DISCUSSION
    metadata.microphone_distance = (
        speech.RecognitionMetadata.MicrophoneDistance.NEARFIELD
    )
    metadata.recording_device_type = (
        speech.RecognitionMetadata.RecordingDeviceType.SMARTPHONE
    )
    
    # Some metadata fields are free form strings
    metadata.recording_device_name = "Pixel 2 XL"
    # And some are integers, for instance the 6 digit NAICS code
    # https://www.naics.com/search/
    metadata.industry_naics_code_of_audio = 519190
    
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=8000,
        language_code="en-US",
        # Add this in the request to send metadata.
        metadata=metadata,
    )
    
    response = client.recognize(config=config, audio=audio)
    
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print(f"First alternative of result {i}")
        print(f"Transcript: {alternative.transcript}")
    
    return response.results

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
