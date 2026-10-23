---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/enhanced-models/
title: Recognize speech by using enhanced models \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:39.731299+00:00
---

# Recognize speech by using enhanced models  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/enhanced-models/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Recognize speech by using enhanced models Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to request an enhanced speech recognition model when you send a transcription request to Cloud Speech-to-Text.

There are two enhanced models: **phone call** and **video**. These models have been optimized to more accurately transcribe audio data from these specific sources. See the [supported languages page](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-supported-languages) to see if the enhanced models are available for your language.

Google creates and improves enhanced models based on data collected through data logging. While opting in to [data logging](https://docs.cloud.google.com/speech-to-text/docs/v1/data-logging) is not required in order to use enhanced models, if you do opt in you can help Google improve these models and also enjoy a discount on your usage.

To use the enhanced recognition models set the following fields in [RecognitionConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig):

  1. Set `useEnhanced` to `true`.
  2. Pass either the `phone_call` or `video` string in the `model` field.



Cloud STT supports enhanced models for all speech recognition methods: [`speech:recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/recognize) [`speech:longrunningrecognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/longrunningrecognize), and [Streaming](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.StreamingRecognizeRequest).

The following code samples demonstrate how to request to use an enhanced model for a transcription request.

### Protocol

Refer to the [`speech:recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/recognize) API endpoint for complete details.

To perform synchronous speech recognition, make a `POST` request and provide the appropriate request body. The following shows an example of a `POST` request using `curl`. The example uses the [Google Cloud CLI](https://docs.cloud.google.com/sdk) to generate an access token. For instructions on installing the gcloud CLI, see the [quickstart](https://docs.cloud.google.com/speech-to-text/docs/transcribe-api). 
    
    
    curl -s -H "Content-Type: application/json" \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        https://speech.googleapis.com/v1/speech:recognize \
        --data '{
        "config": {
            "encoding": "LINEAR16",
            "languageCode": "en-US",
            "enableWordTimeOffsets": false,
            "enableAutomaticPunctuation": true,
    **"model": "phone_call",**
    **"useEnhanced": true**
        },
        "audio": {
            "uri": "gs://cloud-samples-tests/speech/commercial_mono.wav"
        }
    }'

See the [`RecognitionConfig`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig) reference documentation for more information on configuring the request body.

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format:
    
    
    {
      "results": [
        {
          "alternatives": [
            {
              "transcript": "Hi, I'd like to buy a Chromecast. I was wondering whether you could help me with that.",
              "confidence": 0.8930228
            }
          ],
          "resultEndTime": "5.640s"
        },
        {
          "alternatives": [
            {
              "transcript": " Certainly, which color would you like? We are blue black and red.",
              "confidence": 0.9101991
            }
          ],
          "resultEndTime": "10.220s"
        },
        {
          "alternatives": [
            {
              "transcript": " Let's go with the black one.",
              "confidence": 0.8818244
            }
          ],
          "resultEndTime": "13.870s"
        },
        {
          "alternatives": [
            {
              "transcript": " Would you like the new Chromecast Ultra model or the regular Chromecast?",
              "confidence": 0.94733626
            }
          ],
          "resultEndTime": "18.460s"
        },
        {
          "alternatives": [
            {
              "transcript": " Regular Chromecast is fine. Thank you. Okay. Sure. Would you like to ship it regular or Express?",
              "confidence": 0.9519095
            }
          ],
          "resultEndTime": "25.930s"
        },
        {
          "alternatives": [
            {
              "transcript": " Express, please.",
              "confidence": 0.9101229
            }
          ],
          "resultEndTime": "28.260s"
        },
        {
          "alternatives": [
            {
              "transcript": " Terrific. It's on the way. Thank you. Thank you very much. Bye.",
              "confidence": 0.9321616
            }
          ],
          "resultEndTime": "34.150s"
        }
     ]
    }
    

### Go

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func enhancedModel(w io.Writer) error {
    	ctx := context.Background()
    
    	client, err := speech.NewClient(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.Close()
    
    	data, err := os.ReadFile("../testdata/commercial_mono.wav")
    	if err != nil {
    		return fmt.Errorf("ReadFile: %w", err)
    	}
    
    	resp, err := client.Recognize(ctx, &speechpb.RecognizeRequest{
    		Config: &speechpb.RecognitionConfig{
    			Encoding:        speechpb.RecognitionConfig_LINEAR16,
    			SampleRateHertz: 8000,
    			LanguageCode:    "en-US",
    			UseEnhanced:     true,
    			// A model must be specified to use enhanced model.
    			Model: "phone_call",
    		},
    		Audio: &speechpb.RecognitionAudio{
    			AudioSource: &speechpb.RecognitionAudio_Content{Content: data},
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("client.Recognize: %w", err)
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
    

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech
    
    
    def transcribe_file_with_enhanced_model(audio_file: str) -> speech.RecognizeResponse:
        """Transcribe the given audio file using an enhanced model.
        Args:
            audio_file (str): Path to the local audio file to be transcribed.
                Example: "resources/commercial_mono.wav"
        Returns:
            speech.RecognizeResponse: The response containing the transcription results.
        """
    
        client = speech.SpeechClient()
    
        # audio_file = 'resources/commercial_mono.wav'
        with open(audio_file, "rb") as f:
            audio_content = f.read()
    
        audio = speech.RecognitionAudio(content=audio_content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=8000,
            language_code="en-US",
            use_enhanced=True,
            # A model must be specified to use enhanced model.
            model="phone_call",
        )
    
        response = client.recognize(config=config, audio=audio)
    
        for i, result in enumerate(response.results):
            alternative = result.alternatives[0]
            print("-" * 20)
            print(f"First alternative of result {i}")
            print(f"Transcript: {alternative.transcript}")
    
        return response

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Transcribe the given audio file using an enhanced model.
     *
     * @param fileName the path to an audio file.
     */
    public static void transcribeFileWithEnhancedModel(String fileName) throws Exception {
      Path path = Paths.get(fileName);
      byte[] content = Files.readAllBytes(path);
    
      try (SpeechClient speechClient = SpeechClient.create()) {
        // Get the contents of the local audio file
        RecognitionAudio recognitionAudio =
            RecognitionAudio.newBuilder().setContent(ByteString.copyFrom(content)).build();
    
        // Configure request to enable enhanced models
        RecognitionConfig config =
            RecognitionConfig.newBuilder()
                .setEncoding(AudioEncoding.LINEAR16)
                .setLanguageCode("en-US")
                .setSampleRateHertz(8000)
                .setUseEnhanced(true)
                // A model must be specified to use enhanced model.
                .setModel("phone_call")
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
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const filename = 'Local path to audio file, e.g. /path/to/audio.raw';
    // const encoding = 'Encoding of the audio file, e.g. LINEAR16';
    // const sampleRateHertz = 16000;
    // const languageCode = 'BCP-47 language code, e.g. en-US';
    
    const config = {
      encoding: encoding,
      languageCode: languageCode,
      useEnhanced: true,
      model: 'phone_call',
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

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Speech.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-speech/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-speech/latest/Google/Cloud/Speech.html)

## What's next

Review [how to make synchronous transcription requests](https://docs.cloud.google.com/speech-to-text/docs/v1/sync-recognize).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
