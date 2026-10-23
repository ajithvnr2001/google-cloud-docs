---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-model-selection-gcs/
title: Transcribe a file in Cloud Storage using a transcription model \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:57.358103+00:00
---

# Transcribe a file in Cloud Storage using a transcription model  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-model-selection-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Transcribe a file in Cloud Storage using a transcription model Stay organized with collections  Save and categorize content based on your preferences. 

Transcribe an audio file in Cloud Storage using a trained transcription model.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Select a transcription model](https://docs.cloud.google.com/speech-to-text/docs/v1/transcription-model)
  * [Transcribe audio from a video file using Speech-to-Text](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-audio-from-video-speech-to-text)



## Code sample

### Go

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"strings"
    
    	speech "cloud.google.com/go/speech/apiv1"
    	"cloud.google.com/go/speech/apiv1/speechpb"
    )
    
    // transcribe_model_selection_gcs Transcribes the given audio file asynchronously with
    // the selected model.
    func transcribe_model_selection_gcs(w io.Writer) error {
    	ctx := context.Background()
    
    	client, err := speech.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1.html#cloud_google_com_go_speech_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.Close()
    
    	audio := &speechpb.RecognitionAudio{
    		AudioSource: &speechpb.RecognitionAudio_Uri{Uri: "gs://cloud-samples-tests/speech/Google_Gnome.wav"},
    	}
    
    	// The speech recognition model to use
    	// See, https://cloud.google.com/speech-to-text/docs/speech-to-text-requests#select-model
    	recognitionConfig := &speechpb.RecognitionConfig{
    		Encoding:        speechpb.[RecognitionConfig_LINEAR16](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1/speechpb.html#cloud_google_com_go_speech_apiv1_speechpb_RecognitionConfig_ENCODING_UNSPECIFIED_RecognitionConfig_LINEAR16_RecognitionConfig_FLAC_RecognitionConfig_MULAW_RecognitionConfig_AMR_RecognitionConfig_AMR_WB_RecognitionConfig_OGG_OPUS_RecognitionConfig_SPEEX_WITH_HEADER_BYTE_RecognitionConfig_MP3_RecognitionConfig_WEBM_OPUS),
    		SampleRateHertz: 16000,
    		LanguageCode:    "en-US",
    		Model:           "video",
    	}
    
    	longRunningRecognizeRequest := &speechpb.LongRunningRecognizeRequest{
    		Config: recognitionConfig,
    		Audio:  audio,
    	}
    
    	operation, err := client.LongRunningRecognize(ctx, longRunningRecognizeRequest)
    	if err != nil {
    		return fmt.Errorf("error running recognize %w", err)
    	}
    
    	response, err := operation.[Wait](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1.html#cloud_google_com_go_speech_apiv1_LongRunningRecognizeOperation_Wait)(ctx)
    	if err != nil {
    		return err
    	}
    	for i, result := range response.Results {
    		alternative := result.Alternatives[0]
    		fmt.Fprintf(w, "%s\n", strings.Repeat("-", 20))
    		fmt.Fprintf(w, "First alternative of result %d", i)
    		fmt.Fprintf(w, "Transcript: %s", alternative.Transcript)
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Performs transcription of the remote audio file asynchronously with the selected model.
     *
     * @param gcsUri the path to the remote audio file to transcribe.
     */
    public static void transcribeModelSelectionGcs(String gcsUri) throws Exception {
      try (SpeechClient speech = SpeechClient.create()) {
    
        // Configure request with video media type
        RecognitionConfig config =
            RecognitionConfig.newBuilder()
                // encoding may either be omitted or must match the value in the file header
                .setEncoding(AudioEncoding.LINEAR16)
                .setLanguageCode("en-US")
                // sample rate hertz may be either be omitted or must match the value in the file
                // header
                .setSampleRateHertz(16000)
                .setModel("video")
                .build();
    
        RecognitionAudio audio = RecognitionAudio.newBuilder().setUri(gcsUri).build();
    
        // Use non-blocking call for getting file transcription
        OperationFuture<LongRunningRecognizeResponse, LongRunningRecognizeMetadata> response =
            speech.longRunningRecognizeAsync(config, audio);
    
        while (!response.isDone()) {
          System.out.println("Waiting for response...");
          Thread.sleep(10000);
        }
    
        List<SpeechRecognitionResult> results = response.get().getResultsList();
    
        // Just print the first result here.
        SpeechRecognitionResult result = results.get(0);
        // There can be several alternative transcripts for a given chunk of speech. Just use the
        // first (most likely) one here.
        SpeechRecognitionAlternative alternative = result.getAlternativesList().get(0);
        System.out.printf("Transcript : %s\n", alternative.getTranscript());
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
    
    // Creates a client
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const gcsUri = 'gs://my-bucket/audio.raw';
    // const model = 'Model to use, e.g. phone_call, video, default';
    // const encoding = 'Encoding of the audio file, e.g. LINEAR16';
    // const sampleRateHertz = 16000;
    // const languageCode = 'BCP-47 language code, e.g. en-US';
    
    const config = {
      encoding: encoding,
      sampleRateHertz: sampleRateHertz,
      languageCode: languageCode,
      model: model,
    };
    const audio = {
      uri: gcsUri,
    };
    
    const request = {
      config: config,
      audio: audio,
    };
    
    // Detects speech in the audio file.
    const [response] = await client.recognize(request);
    const transcription = response.results
      .map(result => result.alternatives[0].transcript)
      .join('\n');
    console.log('Transcription: ', transcription);

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech
    
    client = speech.SpeechClient()
    
    audio = speech.[RecognitionAudio](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionAudio.html)(
        uri="gs://cloud-samples-tests/speech/Google_Gnome.wav"
    )
    
    config = speech.[RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionConfig.html)(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
        model="video",  # Chosen model
    )
    
    operation = client.[long_running_recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_long_running_recognize)(config=config, audio=audio)
    
    print("Waiting for operation to complete...")
    response = operation.result(timeout=90)
    
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print(f"First alternative of result {i}")
        print(f"Transcript: {alternative.transcript}")
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
