---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-diarization-gcs/
title: Transcription of a file in Cloud Storage with diarization \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:02.345230+00:00
---

# Transcription of a file in Cloud Storage with diarization  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-diarization-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Transcription of a file in Cloud Storage with diarization Stay organized with collections  Save and categorize content based on your preferences. 

Recognize multiple speakers in an audio file stored in Cloud Storage.

## Code sample

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.api.gax.longrunning.[OperationFuture](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFuture.html);
    import com.google.cloud.speech.v1.[LongRunningRecognizeMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.LongRunningRecognizeMetadata.html);
    import com.google.cloud.speech.v1.[LongRunningRecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.LongRunningRecognizeResponse.html);
    import com.google.cloud.speech.v1.[RecognitionAudio](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionAudio.html);
    import com.google.cloud.speech.v1.[RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html);
    import com.google.cloud.speech.v1.[SpeakerDiarizationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeakerDiarizationConfig.html);
    import com.google.cloud.speech.v1.[SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechClient.html);
    import com.google.cloud.speech.v1.[SpeechRecognitionAlternative](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionAlternative.html);
    import com.google.cloud.speech.v1.[WordInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.WordInfo.html);
    import java.io.IOException;
    import java.util.concurrent.ExecutionException;
    
    public class TranscribeDiarizationGcs {
    
      static void transcribeDiarizationGcs()
          throws IOException, ExecutionException, InterruptedException {
        // TODO(developer): Replace these variables before running the sample.
        String gcsUri = "gs://cloud-samples-data/speech/commercial_mono.wav";
        transcribeDiarizationGcs(gcsUri);
      }
    
      // Transcribe the give gcs file using speaker diarization
      public static void transcribeDiarizationGcs(String gcsUri)
          throws IOException, ExecutionException, InterruptedException {
        // Initialize client that will be used to send requests. This client only needs to be created
        // once, and can be reused for multiple requests. After completing all of your requests, call
        // the "close" method on the client to safely clean up any remaining background resources.
        try ([SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechClient.html) speechClient = [SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechClient.html).create()) {
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
          // Set the remote path for the audio file
          [RecognitionAudio](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionAudio.html) audio = [RecognitionAudio](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionAudio.html).newBuilder().setUri(gcsUri).build();
    
          // Use non-blocking call for getting file transcription
          OperationFuture<LongRunningRecognizeResponse, LongRunningRecognizeMetadata> future =
              speechClient.[longRunningRecognizeAsync](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechClient.html#com_google_cloud_speech_v1_SpeechClient_longRunningRecognizeAsync_com_google_cloud_speech_v1_LongRunningRecognizeRequest_)(config, audio);
          System.out.println("Waiting for response...");
    
          // Speaker Tags are only included in the last result object, which has only one alternative.
          [LongRunningRecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.LongRunningRecognizeResponse.html) response = future.[get](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.longrunning.OperationFutureImpl.html#com_google_api_gax_longrunning_OperationFutureImpl_get__)();
          [SpeechRecognitionAlternative](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionAlternative.html) alternative =
              response.[getResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.LongRunningRecognizeResponse.html#com_google_cloud_speech_v1_LongRunningRecognizeResponse_getResults_int_)(response.[getResults](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.LongRunningRecognizeResponse.html#com_google_cloud_speech_v1_LongRunningRecognizeResponse_getResults_int_)Count() - 1).getAlternatives(0);
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

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
