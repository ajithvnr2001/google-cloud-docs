---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-audio-from-video-speech-to-text/
title: Transcribe audio from a video file using Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:56.656618+00:00
---

# Transcribe audio from a video file using Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-audio-from-video-speech-to-text/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Transcribe audio from a video file using Speech-to-Text Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows how to transcribe the audio track from a video file using Cloud Speech-to-Text.

Audio files can come from many different sources. Audio data can come from a phone (like voicemail) or the soundtrack included in a video file.

Cloud STT can use one of several machine learning [_models_](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-requests#select-model) to transcribe your audio file, to best match the original source of the audio. You can get better results from your speech transcription by specifying the source of the original audio. This allows Cloud STT to process your audio files using a machine learning model trained for data similar to your audio file.

## Objectives

  * Send a audio transcription request for a video file to Cloud STT.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Cloud Speech-to-Text



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

This tutorial has several prerequisites:

  * You've [set up a Cloud Speech-to-Text project](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-client-libraries) in the Google Cloud console.
  * You've set up your environment using [Application Default Credentials](https://docs.cloud.google.com/speech-to-text/docs/v1/transcribe-client-libraries) in the Google Cloud console.
  * You have set up the development environment for your chosen programming language.
  * You've installed the [Google Cloud Client Library](https://docs.cloud.google.com/speech-to-text/docs/reference/libraries) for your chosen programming language.



## Prepare the audio data

Before you can transcribe audio from a video, you must extract the data from the video file. After you've extracted the audio data, you must store it in a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets) or convert it to base64-encoding.

**Note:** If you use a client library for transcription, you don't need to store or convert the audio data. You only need to extract the audio data from the video file before sending a transcription request.

### Extract the audio data

You can use any file conversion tool that handles audio and video files, such as [FFmpeg](https://www.ffmpeg.org/).

Use the code snippet below to convert a video file to an audio file using `ffmpeg`.
    
    
    ffmpeg -i video-input-file audio-output-file

### Store or convert the audio data

You can transcribe an audio file stored on your local machine or in a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets).

Use the following command to upload your audio file to an existing Cloud Storage bucket using the [Google Cloud CLI](https://docs.cloud.google.com/cli).
    
    
    gcloud storage cp audio-output-file storage-bucket-uri

If you use a local file and plan to send a request using the `curl` tool from the command line, you must convert the audio file to [base64-encoded data](https://docs.cloud.google.com/speech-to-text/docs/v1/base64-encoding) first.

Use the following command to convert an audio file to a text file.
    
    
    base64 audio-output-file -w 0 > audio-data-text

## Send a transcription request

Use the following code to send a transcription request to Cloud STT.

### Local file request

### Protocol

Refer to the [`speech:recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/recognize) API endpoint for complete details.

To perform synchronous speech recognition, make a `POST` request and provide the appropriate request body. The following shows an example of a `POST` request using `curl`. The example uses the [Google Cloud CLI](https://docs.cloud.google.com/sdk) to generate an access token. For instructions on installing the gcloud CLI, see the [quickstart](https://docs.cloud.google.com/speech-to-text/docs/transcribe-api). 
    
    
    curl -s -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        https://speech.googleapis.com/v2/speech:recognize \
        --data '{
        "config": {
            "encoding": "LINEAR16",
            "sampleRateHertz": 16000,
            "languageCode": "en-US",
    **"model": "video"**
        },
        "audio": {
            "uri": "gs://cloud-samples-tests/speech/Google_Gnome.wav"
        }
    }'

See the [`RecognitionConfig`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig) reference documentation for more information on configuring the request body.

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format:
    
    
    {
      "results": [
        {
          "alternatives": [
            {
              "transcript": "OK Google stream stranger things from
                Netflix to my TV okay stranger things from
                Netflix playing on TV from the people that brought you
                Google home comes the next evolution of the smart home
                and it's just outside your window me Google know hi
                how can I help okay no what's the weather like outside
                the weather outside is sunny and 76 degrees he's right
                okay no turn on the hose I'm holding sure okay no I'm can
                I eat this lemon tree leaf yes what about this Daisy yes
                but I wouldn't recommend it but I could eat it okay
                Nomad milk to my shopping list I'm sorry that sounds like
                an indoor request I keep doing that sorry you do keep
                doing that okay no is this compost really we're all
                compost if you think about it pretty much everything is
                made up of organic matter and will return",
              "confidence": 0.9251011
            }
          ]
        }
      ]
    }

### Go

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func modelSelection(w io.Writer) error {
    	ctx := context.Background()
    
    	client, err := speech.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.Close()
    
    	data, err := os.ReadFile("../testdata/Google_Gnome.wav")
    	if err != nil {
    		return fmt.Errorf("ReadFile: %w", err)
    	}
    
    	req := &speechpb.RecognizeRequest{
    		Config: &speechpb.RecognitionConfig{
    			Encoding:        speechpb.RecognitionConfig_LINEAR16,
    			SampleRateHertz: 16000,
    			LanguageCode:    "en-US",
    			Model:           "video",
    		},
    		Audio: &speechpb.RecognitionAudio{
    			AudioSource: &speechpb.RecognitionAudio_Content{Content: data},
    		},
    	}
    
    	resp, err := client.Recognize(ctx, req)
    	if err != nil {
    		return fmt.Errorf("recognize: %w", err)
    	}
    
    	for i, result := range resp.Results {
    		fmt.Fprintf(w, "%s\n", strings.Repeat("-", 20))
    		fmt.Fprintf(w, "Result %d\n", i+1)
    		for j, alternative := range result.Alternatives {
    			fmt.Fprintf(w, "Alternative %d: %s\n", j+1, alternative.Transcript)
    		}
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Performs transcription of the given audio file synchronously with the selected model.
     *
     * @param fileName the path to a audio file to transcribe
     */
    public static void transcribeModelSelection(String fileName) throws Exception {
      Path path = Paths.get(fileName);
      byte[] content = Files.readAllBytes(path);
    
      try (SpeechClient speech = SpeechClient.create()) {
        // Configure request with video media type
        RecognitionConfig recConfig =
            RecognitionConfig.newBuilder()
                // encoding may either be omitted or must match the value in the file header
                .setEncoding(AudioEncoding.LINEAR16)
                .setLanguageCode("en-US")
                // sample rate hertz may be either be omitted or must match the value in the file
                // header
                .setSampleRateHertz(16000)
                .setModel("video")
                .build();
    
        RecognitionAudio recognitionAudio =
            RecognitionAudio.newBuilder().setContent(ByteString.copyFrom(content)).build();
    
        RecognizeResponse recognizeResponse = speech.recognize(recConfig, recognitionAudio);
        // Just print the first result here.
        SpeechRecognitionResult result = recognizeResponse.getResultsList().get(0);
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
    const fs = require('fs');
    
    // Creates a client
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const filename = 'Local path to audio file, e.g. /path/to/audio.raw';
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
      content: fs.readFileSync(filename).toString('base64'),
    };
    
    const request = {
      config: config,
      audio: audio,
    };
    
    // Detects speech in the audio file
    const [response] = await client.recognize(request);
    const transcription = response.results
      .map(result => result.alternatives[0].transcript)
      .join('\n');
    console.log('Transcription: ', transcription);

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech
    
    # Instantiates a client
    client = speech.SpeechClient()
    # Reads a file as bytes
    with open("resources/Google_Gnome.wav", "rb") as f:
        audio_content = f.read()
    
    audio = speech.[RecognitionAudio](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionAudio.html)(content=audio_content)
    
    config = speech.[RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionConfig.html)(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
        model="video",  # Chosen model
    )
    
    response = client.[recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_recognize)(config=config, audio=audio)
    
    for i, result in enumerate(response.results):
        alternative = result.alternatives[0]
        print("-" * 20)
        print(f"First alternative of result {i}")
        print(f"Transcript: {alternative.transcript}")
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Speech.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-speech/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-speech/latest/Google/Cloud/Speech.html)

### Remote file request

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
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Speech.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-speech/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-speech/latest/Google/Cloud/Speech.html)

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete instances

To delete a Compute Engine instance: 

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the checkbox for the instance that you want to delete. 
  3. To delete the instance, click more_vert **More actions** , click **Delete** , and then follow the instructions. 



### Delete firewall rules for the default network

To delete a firewall rule: 

  1. In the Google Cloud console, go to the **Firewall** page. 

[Go to Firewall](https://console.cloud.google.com/networking/firewalls/list)

  2. Select the checkbox for the firewall rule that you want to delete. 
  3. To delete the firewall rule, click delete **Delete**. 



## What's next

  * Learn how to [get timestamps for audio.](https://docs.cloud.google.com/speech-to-text/docs/v1/async-time-offsets)
  * Identify [different speakers in an audio file.](https://docs.cloud.google.com/speech-to-text/docs/v1/multiple-voices)



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud STT performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud STT free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
