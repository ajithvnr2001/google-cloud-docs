---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-diarization/
title: Transcription with diarization \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:02.845373+00:00
---

# Transcription with diarization  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-diarization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Transcription with diarization Stay organized with collections  Save and categorize content based on your preferences. 

Identify the different speakers in the audio sample.

## Code sample

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.speech.v1.[RecognitionAudio](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionAudio.html);
    import com.google.cloud.speech.v1.[RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html);
    import com.google.cloud.speech.v1.[RecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognizeResponse.html);
    import com.google.cloud.speech.v1.[SpeakerDiarizationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeakerDiarizationConfig.html);
    import com.google.cloud.speech.v1.[SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechClient.html);
    import com.google.cloud.speech.v1.[SpeechRecognitionAlternative](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionAlternative.html);
    import com.google.cloud.speech.v1.[WordInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.WordInfo.html);
    import com.google.protobuf.[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html);
    import java.io.IOException;
    import java.nio.file.Files;
    import java.nio.file.Path;
    import java.nio.file.Paths;
    
    class TranscribeDiarization {
    
      static void transcribeDiarization() throws IOException {
        // TODO(developer): Replace these variables before running the sample.
        String fileName = "resources/commercial_mono.wav";
        transcribeDiarization(fileName);
      }
    
      // Transcribe the given audio file using speaker diarization.
      static void transcribeDiarization(String fileName) throws IOException {
        Path path = Paths.get(fileName);
        byte[] content = Files.readAllBytes(path);
    
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechClient.html) client = [SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechClient.html).create()) {
          // Get the contents of the local audio file
          [RecognitionAudio](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionAudio.html) recognitionAudio =
              [RecognitionAudio](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionAudio.html).newBuilder().setContent([ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html).[copyFrom](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html#com_google_protobuf_ByteString_copyFrom_byte___)(content)).build();
          [SpeakerDiarizationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeakerDiarizationConfig.html) speakerDiarizationConfig =
              [SpeakerDiarizationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeakerDiarizationConfig.html).newBuilder()
                  .[setEnableSpeakerDiarization](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeakerDiarizationConfig.Builder.html#com_google_cloud_speech_v1_SpeakerDiarizationConfig_Builder_setEnableSpeakerDiarization_boolean_)(true)
                  .[setMinSpeakerCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeakerDiarizationConfig.Builder.html#com_google_cloud_speech_v1_SpeakerDiarizationConfig_Builder_setMinSpeakerCount_int_)(2)
                  .[setMaxSpeakerCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeakerDiarizationConfig.Builder.html#com_google_cloud_speech_v1_SpeakerDiarizationConfig_Builder_setMaxSpeakerCount_int_)(2)
                  .build();
          // Configure request to enable Speaker diarization
          [RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html) config =
              [RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html).newBuilder()
                  .[setEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.Builder.html#com_google_cloud_speech_v1_RecognitionConfig_Builder_setEncoding_com_google_cloud_speech_v1_RecognitionConfig_AudioEncoding_)([RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html).AudioEncoding.LINEAR16)
                  .setLanguageCode("en-US")
                  .[setSampleRateHertz](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.Builder.html#com_google_cloud_speech_v1_RecognitionConfig_Builder_setSampleRateHertz_int_)(8000)
                  .[setDiarizationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.Builder.html#com_google_cloud_speech_v1_RecognitionConfig_Builder_setDiarizationConfig_com_google_cloud_speech_v1_SpeakerDiarizationConfig_)(speakerDiarizationConfig)
                  .build();
    
          // Perform the transcription request
          [RecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognizeResponse.html) recognizeResponse = client.recognize(config, recognitionAudio);
    
          // Speaker Tags are only included in the last result object, which has only one alternative.
          [SpeechRecognitionAlternative](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionAlternative.html) alternative =
              recognizeResponse.[getResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognizeResponse.html#com_google_cloud_speech_v1_RecognizeResponse_getResults_int_)(recognizeResponse.[getResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognizeResponse.html#com_google_cloud_speech_v1_RecognizeResponse_getResults_int_)Count() - 1).getAlternatives(0);
          // The alternative is made up of WordInfo objects that contain the speaker_tag.
          [WordInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.WordInfo.html) wordInfo = alternative.[getWords](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionAlternative.html#com_google_cloud_speech_v1_SpeechRecognitionAlternative_getWords_int_)(0);
          int currentSpeakerTag = wordInfo.[getSpeakerTag](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.WordInfo.html#com_google_cloud_speech_v1_WordInfo_getSpeakerTag__)();
          // For each word, get all the words associated with one speaker, once the speaker changes,
          // add a new line with the new speaker and their spoken words.
          StringBuilder speakerWords =
              new StringBuilder(
                  String.format("Speaker %d: %s", wordInfo.[getSpeakerTag](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.WordInfo.html#com_google_cloud_speech_v1_WordInfo_getSpeakerTag__)(), wordInfo.[getWord](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.WordInfo.html#com_google_cloud_speech_v1_WordInfo_getWord__)()));
          for (int i = 1; i < alternative.[getWordsCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionAlternative.html#com_google_cloud_speech_v1_SpeechRecognitionAlternative_getWordsCount__)(); i++) {
            wordInfo = alternative.[getWords](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionAlternative.html#com_google_cloud_speech_v1_SpeechRecognitionAlternative_getWords_int_)(i);
            if (currentSpeakerTag == wordInfo.[getSpeakerTag](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.WordInfo.html#com_google_cloud_speech_v1_WordInfo_getSpeakerTag__)()) {
              speakerWords.append(" ");
              speakerWords.append(wordInfo.[getWord](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.WordInfo.html#com_google_cloud_speech_v1_WordInfo_getWord__)());
            } else {
              speakerWords.append(
                  String.format("\nSpeaker %d: %s", wordInfo.[getSpeakerTag](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.WordInfo.html#com_google_cloud_speech_v1_WordInfo_getSpeakerTag__)(), wordInfo.[getWord](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.WordInfo.html#com_google_cloud_speech_v1_WordInfo_getWord__)()));
              currentSpeakerTag = wordInfo.[getSpeakerTag](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.WordInfo.html#com_google_cloud_speech_v1_WordInfo_getSpeakerTag__)();
            }
          }
          System.out.println(speakerWords.toString());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const fs = require('fs');
    
    // Imports the Google Cloud client library
    const speech = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)');
    
    // Creates a client
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    // Set config for Diarization
    const diarizationConfig = {
      enableSpeakerDiarization: true,
      maxSpeakerCount: 2,
    };
    
    const config = {
      encoding: 'LINEAR16',
      sampleRateHertz: 8000,
      languageCode: 'en-US',
      diarizationConfig: diarizationConfig,
      model: 'phone_call',
    };
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const fileName = 'Local path to audio file, e.g. /path/to/audio.raw';
    
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
    console.log('Speaker Diarization:');
    const result = response.results[response.results.length - 1];
    const wordsInfo = result.alternatives[0].words;
    // Note: The transcript within each result is separate and sequential per result.
    // However, the words list within an alternative includes all the words
    // from all the results thus far. Thus, to get all the words with speaker
    // tags, you only have to take the words list from the last result:
    wordsInfo.forEach(a =>
      console.log(` word: ${a.word}, speakerTag: ${a.speakerTag}`)
    );

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
