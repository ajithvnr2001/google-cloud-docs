---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/profanity-filter/
title: Enable the profanity filter \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:22.752927+00:00
---

# Enable the profanity filter  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/profanity-filter/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Enable the profanity filter Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Cloud Speech-to-Text to automatically detect profane words in your audio data and censor them in the transcript.

You can enable the profanity filter by setting `profanityFilter=true` in the [`RecognitionConfig`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig). If enabled, Cloud Speech-to-Text will attempt to detect profane words and return only the first letter followed by asterisks in the transcript (for example, f***). If this field is set to `false` or not set, Cloud Speech-to-Text will not attempt to filter profanities.

The following sample demonstrates how to enable the profanity filter to recognize audio stored in a Cloud Storage bucket.

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.speech.v1.[RecognitionAudio](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionAudio.html);
    import com.google.cloud.speech.v1.[RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html);
    import com.google.cloud.speech.v1.[RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html).[AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.AudioEncoding.html);
    import com.google.cloud.speech.v1.[RecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognizeResponse.html);
    import com.google.cloud.speech.v1.[SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechClient.html);
    import com.google.cloud.speech.v1.[SpeechRecognitionAlternative](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionAlternative.html);
    import com.google.cloud.speech.v1.[SpeechRecognitionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionResult.html);
    import java.util.List;
    
    public class SpeechProfanityFilter {
    
      public void speechProfanityFilter() throws Exception {
        String uriPath = "gs://cloud-samples-tests/speech/brooklyn.flac";
        speechProfanityFilter(uriPath);
      }
    
      /**
       * Transcribe a remote audio file with multi-channel recognition
       *
       * @param gcsUri the path to the audio file
       */
      public static void speechProfanityFilter(String gcsUri) throws Exception {
        // Instantiates a client with GOOGLE_APPLICATION_CREDENTIALS
        try ([SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechClient.html) speech = [SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechClient.html).create()) {
    
          // Configure remote file request
          [RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html) config =
              [RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html).newBuilder()
                  .[setEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.Builder.html#com_google_cloud_speech_v1_RecognitionConfig_Builder_setEncoding_com_google_cloud_speech_v1_RecognitionConfig_AudioEncoding_)([AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.AudioEncoding.html).FLAC)
                  .setLanguageCode("en-US")
                  .[setSampleRateHertz](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.Builder.html#com_google_cloud_speech_v1_RecognitionConfig_Builder_setSampleRateHertz_int_)(16000)
                  .[setProfanityFilter](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.Builder.html#com_google_cloud_speech_v1_RecognitionConfig_Builder_setProfanityFilter_boolean_)(true)
                  .build();
    
          // Set the remote path for the audio file
          [RecognitionAudio](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionAudio.html) audio = [RecognitionAudio](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionAudio.html).newBuilder().setUri(gcsUri).build();
    
          // Use blocking call to get audio transcript
          [RecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognizeResponse.html) response = speech.recognize(config, audio);
          List<SpeechRecognitionResult> results = response.[getResultsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognizeResponse.html#com_google_cloud_speech_v1_RecognizeResponse_getResultsList__)();
    
          for ([SpeechRecognitionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionResult.html) result : results) {
            // There can be several alternative transcripts for a given chunk of speech. Just use the
            // first (most likely) one here.
            [SpeechRecognitionAlternative](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionAlternative.html) alternative = result.getAlternativesList().get(0);
            System.out.printf("Transcription: %s\n", alternative.[getTranscript](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionAlternative.html#com_google_cloud_speech_v1_SpeechRecognitionAlternative_getTranscript__)());
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Filters profanity
    
    /**
     * TODO(developer): Uncomment these variables before running the sample.
     */
    // const gcsUri = 'gs://my-bucket/audio.raw';
    
    async function syncRecognizeWithProfanityFilter() {
      // Imports the Google Cloud client library
      const speech = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)');
    
      // Creates a client
      const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
      const audio = {
        uri: gcsUri,
      };
    
      const config = {
        encoding: 'FLAC',
        sampleRateHertz: 16000,
        languageCode: 'en-US',
        profanityFilter: true, // set this to true
      };
      const request = {
        audio: audio,
        config: config,
      };
    
      // Detects speech in the audio file
      const [response] = await client.recognize(request);
      const transcription = response.results
        .map(result => result.alternatives[0].transcript)
        .join('\n');
      console.log(`Transcription: ${transcription}`);
    }
    syncRecognizeWithProfanityFilter().catch(console.error);

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech
    from google.cloud.speech import RecognizeResponse
    
    
    def sync_recognize_with_profanity_filter_gcs(audio_uri: str) -> RecognizeResponse:
        """Recognizes speech from an audio file in Cloud Storage and filters out profane language.
        Args:
            audio_uri (str): The Cloud Storage URI of the input audio, e.g., gs://[BUCKET]/[FILE]
        Returns:
            cloud_speech.RecognizeResponse: The full response object which includes the transcription results.
        """
        # Define the audio source
        audio = {"uri": audio_uri}
    
        client = speech.SpeechClient()
        config = speech.[RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionConfig.html)(
            encoding=speech.RecognitionConfig.AudioEncoding.FLAC,  # Audio format
            sample_rate_hertz=16000,
            language_code="en-US",
            # Enable profanity filter
            profanity_filter=True,
        )
    
        response = client.[recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_recognize)(config=config, audio=audio)
    
        for result in response.results:
            alternative = result.alternatives[0]
            print(f"Transcript: {alternative.transcript}")
    
        return response.results
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
