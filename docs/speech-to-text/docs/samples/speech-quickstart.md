---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-quickstart/
title: Make an audio transcription request \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:01.513020+00:00
---

# Make an audio transcription request  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Make an audio transcription request Stay organized with collections  Save and categorize content based on your preferences. 

Transcribe a local audio file synchronously.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Quickstart: Transcribe speech to text by using client libraries](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-client-libraries)



## Code sample

### Go

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Sample speech-quickstart uses the Google Cloud Speech API to transcribe
    // audio.
    package main
    
    import (
    	"context"
    	"fmt"
    	"log"
    
    	speech "cloud.google.com/go/speech/apiv1"
    	"cloud.google.com/go/speech/apiv1/speechpb"
    )
    
    func main() {
    	ctx := context.Background()
    
    	// Creates a client.
    	client, err := speech.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1.html#cloud_google_com_go_speech_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		log.Fatalf("Failed to create client: %v", err)
    	}
    	defer client.Close()
    
    	// The path to the remote audio file to transcribe.
    	fileURI := "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
    
    	// Detects speech in the audio file.
    	resp, err := client.Recognize(ctx, &speechpb.RecognizeRequest{
    		Config: &speechpb.RecognitionConfig{
    			Encoding:        speechpb.[RecognitionConfig_LINEAR16](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1/speechpb.html#cloud_google_com_go_speech_apiv1_speechpb_RecognitionConfig_ENCODING_UNSPECIFIED_RecognitionConfig_LINEAR16_RecognitionConfig_FLAC_RecognitionConfig_MULAW_RecognitionConfig_AMR_RecognitionConfig_AMR_WB_RecognitionConfig_OGG_OPUS_RecognitionConfig_SPEEX_WITH_HEADER_BYTE_RecognitionConfig_MP3_RecognitionConfig_WEBM_OPUS),
    			SampleRateHertz: 16000,
    			LanguageCode:    "en-US",
    		},
    		Audio: &speechpb.RecognitionAudio{
    			AudioSource: &speechpb.RecognitionAudio_Uri{Uri: fileURI},
    		},
    	})
    	if err != nil {
    		log.Fatalf("failed to recognize: %v", err)
    	}
    
    	// Prints the results.
    	for _, result := range resp.Results {
    		for _, alt := range result.Alternatives {
    			fmt.Printf("\"%v\" (confidence=%3f)\n", alt.Transcript, alt.Confidence)
    		}
    	}
    }
    

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    import com.google.cloud.speech.v1.[RecognitionAudio](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionAudio.html);
    import com.google.cloud.speech.v1.[RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html);
    import com.google.cloud.speech.v1.[RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html).[AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.AudioEncoding.html);
    import com.google.cloud.speech.v1.[RecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognizeResponse.html);
    import com.google.cloud.speech.v1.[SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechClient.html);
    import com.google.cloud.speech.v1.[SpeechRecognitionAlternative](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionAlternative.html);
    import com.google.cloud.speech.v1.[SpeechRecognitionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionResult.html);
    import java.util.List;
    
    public class QuickstartSample {
    
      /** Demonstrates using the Speech API to transcribe an audio file. */
      public static void main(String... args) throws Exception {
        // Instantiates a client
        try ([SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechClient.html) speechClient = [SpeechClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechClient.html).create()) {
    
          // The path to the audio file to transcribe
          String gcsUri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw";
    
          // Builds the sync recognize request
          [RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html) config =
              [RecognitionConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.html).newBuilder()
                  .[setEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.Builder.html#com_google_cloud_speech_v1_RecognitionConfig_Builder_setEncoding_com_google_cloud_speech_v1_RecognitionConfig_AudioEncoding_)([AudioEncoding](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.AudioEncoding.html).LINEAR16)
                  .[setSampleRateHertz](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionConfig.Builder.html#com_google_cloud_speech_v1_RecognitionConfig_Builder_setSampleRateHertz_int_)(16000)
                  .setLanguageCode("en-US")
                  .build();
          [RecognitionAudio](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionAudio.html) audio = [RecognitionAudio](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognitionAudio.html).newBuilder().setUri(gcsUri).build();
    
          // Performs speech recognition on the audio file
          [RecognizeResponse](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognizeResponse.html) response = speechClient.recognize(config, audio);
          List<SpeechRecognitionResult> results = response.[getResultsList](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.RecognizeResponse.html#com_google_cloud_speech_v1_RecognizeResponse_getResultsList__)();
    
          for ([SpeechRecognitionResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionResult.html) result : results) {
            // There can be several alternative transcripts for a given chunk of speech. Just use the
            // first (most likely) one here.
            [SpeechRecognitionAlternative](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionAlternative.html) alternative = result.getAlternativesList().get(0);
            System.out.printf("Transcription: %s%n", alternative.[getTranscript](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/com.google.cloud.speech.v1.SpeechRecognitionAlternative.html#com_google_cloud_speech_v1_SpeechRecognitionAlternative_getTranscript__)());
          }
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library
    const speech = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)');
    
    // Creates a client
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    async function quickstart() {
      // The path to the remote LINEAR16 file
      const gcsUri = 'gs://cloud-samples-data/speech/brooklyn_bridge.raw';
    
      // The audio file's encoding, sample rate in hertz, and BCP-47 language code
      const audio = {
        uri: gcsUri,
      };
      const config = {
        encoding: 'LINEAR16',
        sampleRateHertz: 16000,
        languageCode: 'en-US',
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
    quickstart();

### PHP

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Includes the autoloader for libraries installed with composer
    require __DIR__ . '/vendor/autoload.php';
    
    # Imports the Google Cloud client library
    
    use Google\Cloud\Speech\V2\Client\SpeechClient;
    use Google\Cloud\Speech\V2\CreateRecognizerRequest;
    use Google\Cloud\Speech\V2\ExplicitDecodingConfig;
    use Google\Cloud\Speech\V2\ExplicitDecodingConfig\AudioEncoding;
    use Google\Cloud\Speech\V2\RecognitionConfig;
    use Google\Cloud\Speech\V2\Recognizer;
    use Google\Cloud\Speech\V2\RecognizeRequest;
    
    # The name of the audio file to transcribe
    $gcsURI = 'gs://cloud-samples-data/speech/brooklyn_bridge.raw';
    
    # Your Google Cloud Project ID and location
    $projectId = 'YOUR_PROJECT_ID';
    $location = 'global';
    
    # Instantiates a client
    $speech = new SpeechClient();
    
    // Create a Recognizer
    $createRecognizerRequest = new CreateRecognizerRequest([
        'parent' => SpeechClient::locationName($projectId, $location),
        'recognizer_id' => $recognizerId = 'quickstart-recognizer-' . uniqid(),
        'recognizer' => new Recognizer([
            'language_codes' => ['en-US'],
            'model' => 'latest_short'
        ])
    ]);
    
    $operation = $speech->createRecognizer($createRecognizerRequest);
    
    // Wait for the operation to complete
    $operation->pollUntilComplete();
    if ($operation->operationSucceeded()) {
        $result = $operation->getResult();
        printf('Created Recognizer: %s' . PHP_EOL, $result->getName());
    } else {
        print_r($operation->getError());
    }
    
    $config = (new RecognitionConfig())
        // Can also use {@see Google\Cloud\Speech\V2\AutoDetectDecodingConfig}
        // ->setAutoDecodingConfig(new AutoDetectDecodingConfig());
    
        ->setExplicitDecodingConfig(new ExplicitDecodingConfig([
            'encoding' => AudioEncoding::LINEAR16,
            'sample_rate_hertz' => 16000,
            'audio_channel_count' => 1,
        ]));
    
    $recognizerName = SpeechClient::recognizerName($projectId, $location, $recognizerId);
    $request = (new RecognizeRequest())
        ->setRecognizer($recognizerName)
        ->setConfig($config)
        ->setUri($gcsURI);
    
    # Detects speech in the audio file
    $response = $speech->recognize($request);
    
    # Print most likely transcription
    foreach ($response->getResults() as $result) {
        $alternatives = $result->getAlternatives();
        $mostLikely = $alternatives[0];
        $transcript = $mostLikely->getTranscript();
        printf('Transcript: %s' . PHP_EOL, $transcript);
    }
    
    $speech->close();
    

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # Imports the Google Cloud client library
    
    
    from google.cloud import speech
    
    
    
    def run_quickstart() -> speech.RecognizeResponse:
        # Instantiates a client
        client = speech.SpeechClient()
    
        # The name of the audio file to transcribe
        gcs_uri = "gs://cloud-samples-data/speech/brooklyn_bridge.raw"
    
        audio = speech.[RecognitionAudio](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionAudio.html)(uri=gcs_uri)
    
        config = speech.[RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionConfig.html)(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code="en-US",
        )
    
        # Detects speech in the audio file
        response = client.[recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_recognize)(config=config, audio=audio)
    
        for result in response.results:
            print(f"Transcript: {result.alternatives[0].transcript}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
