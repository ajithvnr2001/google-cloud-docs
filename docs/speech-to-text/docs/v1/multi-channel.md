---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/multi-channel/
title: Transcribe audio with multiple channels \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:06.103260+00:00
---

# Transcribe audio with multiple channels  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/multi-channel/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Transcribe audio with multiple channels Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Cloud Speech-to-Text to transcribe audio files that include more than one channel. Multi-channel recognition is available for most, but not all, audio encodings supported by Cloud STT. For information about how many channels are recognized in audio files of each encoding type, see [`audioChannelCount`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig).

Audio data usually includes a channel for each speaker present on the recording. For example, audio of two people talking over the phone might contain two channels, where each line is recorded separately.

To transcribe audio data that includes multiple channels, you must provide the number of channels in your request to the Cloud Speech-to-Text API. In your request, set the `audioChannelCount` field in your request to the number of channels present in your audio.

When you send a request with multiple channels, Cloud STT returns a result to you that identifies the different channels present in the audio, labeling the alternatives for each result with the `channelTag` field.

**Note:** Processing multiple channels affects billing. See the [pricing](https://docs.cloud.google.com/speech-to-text/pricing) and [quotas & limits](https://docs.cloud.google.com/speech-to-text/docs/v1/quotas) pages for more information.

The following code sample demonstrates how to transcribe audio that contains multiple channels.

### Protocol

Refer to the [`speech:recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/recognize) API endpoint for complete details.

To perform synchronous speech recognition, make a `POST` request and provide the appropriate request body. The following shows an example of a `POST` request using `curl`. The example uses the [Google Cloud CLI](https://docs.cloud.google.com/sdk) to generate an access token. For instructions on installing the gcloud CLI, see the [quickstart](https://docs.cloud.google.com/speech-to-text/docs/transcribe-api). 

The following example show how to send a `POST` request using `curl`, where the body of the request specifies the number of channels present on the audio sample.
    
    
    curl -X POST -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data '{
        "config": {
            "encoding": "LINEAR16",
            "languageCode": "en-US",
    **"audioChannelCount": 2,**
    **"enableSeparateRecognitionPerChannel": true**
        },
        "audio": {
            "uri": "gs://cloud-samples-tests/speech/commercial_stereo.wav"
        }
    }' "https://speech.googleapis.com/v1/speech:recognize" > multi-channel.txt

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format, saved to a file named `multi-channel.json`.
    
    
    {
      "results": [
        {
          "alternatives": [
            {
              "transcript": "hi I'd like to buy a Chromecast I'm always wondering whether you could help me with that",
              "confidence": 0.8991147
            }
          ],
          "channelTag": 1,
          "languageCode": "en-us"
        },
        {
          "alternatives": [
            {
              "transcript": "certainly which color would you like we have blue black and red",
              "confidence": 0.9408236
            }
          ],
          "channelTag": 2,
          "languageCode": "en-us"
        },
        {
          "alternatives": [
            {
              "transcript": " let's go with the black one",
              "confidence": 0.98783094
            }
          ],
          "channelTag": 1,
          "languageCode": "en-us"
        },
        {
          "alternatives": [
            {
              "transcript": " would you like the new Chromecast Ultra model or the regular Chromecast",
              "confidence": 0.9573053
            }
          ],
          "channelTag": 2,
          "languageCode": "en-us"
        },
        {
          "alternatives": [
            {
              "transcript": " regular Chromecast is fine thank you",
              "confidence": 0.9671048
            }
          ],
          "channelTag": 1,
          "languageCode": "en-us"
        },
        {
          "alternatives": [
            {
              "transcript": " okay sure would you like to ship it regular or Express",
              "confidence": 0.9544821
            }
          ],
          "channelTag": 2,
          "languageCode": "en-us"
        },
        {
          "alternatives": [
            {
              "transcript": " express please",
              "confidence": 0.9487205
            }
          ],
          "channelTag": 1,
          "languageCode": "en-us"
        },
        {
          "alternatives": [
            {
              "transcript": " terrific it's on the way thank you",
              "confidence": 0.97655964
            }
          ],
          "channelTag": 2,
          "languageCode": "en-us"
        },
        {
          "alternatives": [
            {
              "transcript": " thank you very much bye",
              "confidence": 0.9735077
            }
          ],
          "channelTag": 1,
          "languageCode": "en-us"
        }
      ]
    }
    
    

### Go

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // transcribeMultichannel generates a transcript from a multichannel speech file and tags the speech from each channel.
    func transcribeMultichannel(w io.Writer) error {
    	ctx := context.Background()
    
    	client, err := speech.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.Close()
    
    	data, err := os.ReadFile("../testdata/commercial_stereo.wav")
    	if err != nil {
    		return fmt.Errorf("ReadFile: %w", err)
    	}
    
    	resp, err := client.Recognize(ctx, &speechpb.RecognizeRequest{
    		Config: &speechpb.RecognitionConfig{
    			Encoding:                            speechpb.RecognitionConfig_LINEAR16,
    			SampleRateHertz:                     44100,
    			LanguageCode:                        "en-US",
    			AudioChannelCount:                   2,
    			EnableSeparateRecognitionPerChannel: true,
    		},
    		Audio: &speechpb.RecognitionAudio{
    			AudioSource: &speechpb.RecognitionAudio_Content{Content: data},
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("Recognize: %w", err)
    	}
    
    	// Print the results.
    	for _, result := range resp.Results {
    		for _, alt := range result.Alternatives {
    			fmt.Fprintf(w, "Channel %v: %v\n", result.ChannelTag, alt.Transcript)
    		}
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Transcribe a remote audio file with multi-channel recognition
     *
     * @param gcsUri the path to the audio file
     */
    public static void transcribeMultiChannelGcs(String gcsUri) throws Exception {
    
      try (SpeechClient speechClient = SpeechClient.create()) {
    
        // Configure request to enable multiple channels
        RecognitionConfig config =
            RecognitionConfig.newBuilder()
                .setEncoding(AudioEncoding.LINEAR16)
                .setLanguageCode("en-US")
                .setSampleRateHertz(44100)
                .setAudioChannelCount(2)
                .setEnableSeparateRecognitionPerChannel(true)
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
        for (SpeechRecognitionResult result : response.get().getResultsList()) {
    
          // There can be several alternative transcripts for a given chunk of speech. Just use the
          // first (most likely) one here.
          SpeechRecognitionAlternative alternative = result.getAlternativesList().get(0);
    
          // Print out the result
          System.out.printf("Transcript : %s\n", alternative.getTranscript());
          System.out.printf("Channel Tag : %s\n", result.getChannelTag());
        }
      }
    }

### Node.js

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const speech = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)').v1;
    
    // Creates a client
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    const config = {
      encoding: 'LINEAR16',
      languageCode: 'en-US',
      audioChannelCount: 2,
      enableSeparateRecognitionPerChannel: true,
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
      .map(
        result =>
          ` Channel Tag: ${result.channelTag} ${result.alternatives[0].transcript}`
      )
      .join('\n');
    console.log(`Transcription: \n${transcription}`);

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech
    
    
    def transcribe_file_with_multichannel(audio_file: str) -> speech.RecognizeResponse:
        """Transcribe the given audio file synchronously with multi channel.
        Args:
            audio_file (str): Path to the local audio file to be transcribed.
                Example: "resources/multi.wav"
        Returns:
             cloud_speech.RecognizeResponse: The full response object which includes the transcription results.
        """
        client = speech.SpeechClient()
    
        with open(audio_file, "rb") as f:
            audio_content = f.read()
    
        audio = speech.RecognitionAudio(content=audio_content)
    
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44100,
            language_code="en-US",
            audio_channel_count=2,
            enable_separate_recognition_per_channel=True,
        )
    
        response = client.recognize(config=config, audio=audio)
    
        for i, result in enumerate(response.results):
            alternative = result.alternatives[0]
            print("-" * 20)
            print(f"First alternative of result {i}")
            print(f"Transcript: {alternative.transcript}")
            print(f"Channel Tag: {result.channel_tag}")
    
        return result

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Speech.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-speech/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-speech/latest/Google/Cloud/Speech.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
