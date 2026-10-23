---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/automatic-punctuation/
title: Get automatic punctuation \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:20.647485+00:00
---

# Get automatic punctuation  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/automatic-punctuation/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Get automatic punctuation Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to get automatic punctuation in transcription results from Cloud Speech-to-Text. When you enable this feature, Cloud STT automatically infers the presence of periods, commas, and question marks in your audio data and adds them to the transcript.

By default, Cloud STT does not include punctuation marks in the results from speech recognition. However, you can request that Cloud STT automatically detect and insert punctuation in transcription results. When you enable automatic punctuation Cloud STT will also automatically capitalize the first letter after each period and question mark.

**Note:** Review the list of [supported features by language](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-supported-languages) to see the list of languages supported for this feature.

To enable automatic punctuation, set the `enableAutomaticPunctuation` field to `true` in the [`RecognitionConfig`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig) parameters for the request. The Cloud Speech-to-Text API supports automatic punctuation for all speech recognition methods: [`speech:recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/recognize), [`speech:longrunningrecognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/longrunningrecognize), and [Streaming](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1#google.cloud.speech.v1.StreamingRecognizeRequest).

The following code samples demonstrate how to get automatic punctuation details in a transcription request.

### Protocol

Refer to the [`speech:recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/recognize) API endpoint for complete details. 

To perform synchronous speech recognition, make a `POST` request and provide the appropriate request body. The following shows an example of a `POST` request using `curl`. The example uses the [Google Cloud CLI](https://docs.cloud.google.com/sdk) to generate an access token. For instructions on installing the gcloud CLI, see the [quickstart](https://docs.cloud.google.com/speech-to-text/docs/transcribe-api). 
    
    
    curl -s -H "Content-Type: application/json" \
        -H "Authorization: Bearer "$(gcloud auth print-access-token) \
        https://speech.googleapis.com/v1/speech:recognize \
        --data '{
      "config": {
        "encoding":"FLAC",
        "sampleRateHertz": 16000,
        "languageCode": "en-US",
        **"enableAutomaticPunctuation": true**
      },
      "audio": {
        "uri":"gs://cloud-samples-tests/speech/brooklyn.flac"
      }
    }'
    

See the [`RecognitionConfig`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig) reference documentation for more information on configuring the request body.

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format:
    
    
    {
      "results": [
        {
          "alternatives": [
            {
              "transcript": "How old is the Brooklyn Bridge?",
              "confidence": 0.98360395
            }
          ]
        }
      ]
    }
    

### Go

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import (
    	"context"
    	"fmt"
    	"io"
    	"os"
    	"strings"
    
    	speech "cloud.google.com/go/speech/apiv1"
    	"cloud.google.com/go/speech/apiv1/speechpb"
    )
    
    func autoPunctuation(w io.Writer, path string) error {
    	ctx := context.Background()
    
    	client, err := speech.[NewClient](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1.html#cloud_google_com_go_speech_apiv1_Client_NewClient)(ctx)
    	if err != nil {
    		return fmt.Errorf("NewClient: %w", err)
    	}
    	defer client.Close()
    
    	// path = "../testdata/commercial_mono.wav"
    	data, err := os.ReadFile(path)
    	if err != nil {
    		return fmt.Errorf("ReadFile: %w", err)
    	}
    
    	resp, err := client.Recognize(ctx, &speechpb.RecognizeRequest{
    		Config: &speechpb.RecognitionConfig{
    			Encoding:        speechpb.[RecognitionConfig_LINEAR16](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1/speechpb.html#cloud_google_com_go_speech_apiv1_speechpb_RecognitionConfig_ENCODING_UNSPECIFIED_RecognitionConfig_LINEAR16_RecognitionConfig_FLAC_RecognitionConfig_MULAW_RecognitionConfig_AMR_RecognitionConfig_AMR_WB_RecognitionConfig_OGG_OPUS_RecognitionConfig_SPEEX_WITH_HEADER_BYTE_RecognitionConfig_MP3_RecognitionConfig_WEBM_OPUS),
    			SampleRateHertz: 8000,
    			LanguageCode:    "en-US",
    			// Enable automatic punctuation.
    			EnableAutomaticPunctuation: true,
    		},
    		Audio: &speechpb.RecognitionAudio{
    			AudioSource: &speechpb.RecognitionAudio_Content{Content: data},
    		},
    	})
    	if err != nil {
    		return fmt.Errorf("Recognize: %w", err)
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
     * Performs transcription on remote FLAC file and prints the transcription.
     *
     * @param gcsUri the path to the remote FLAC audio file to transcribe.
     */
    public static void transcribeGcsWithAutomaticPunctuation(String gcsUri) throws Exception {
      try (SpeechClient speechClient = SpeechClient.create()) {
        // Configure request with raw PCM audio
        RecognitionConfig config =
            RecognitionConfig.newBuilder()
                .setEncoding(AudioEncoding.FLAC)
                .setLanguageCode("en-US")
                .setSampleRateHertz(16000)
                .setEnableAutomaticPunctuation(true)
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
      }
    }

### Node.js

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Node.js API reference documentation](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud client library for API
    /**
     * TODO(developer): Update client library import to use new
     * version of API when desired features become available
     */
    
    const speech = require('[@google-cloud/speech](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)');
    const fs = require('fs');
    
    // Creates a client
    const client = new speech.[SpeechClient](https://docs.cloud.google.com/nodejs/docs/reference/speech/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     * Include the sampleRateHertz field in the config object.
     */
    // const filename = 'Local path to audio file, e.g. /path/to/audio.raw';
    // const encoding = 'Encoding of the audio file, e.g. LINEAR16';
    // const sampleRateHertz = 16000;
    // const languageCode = 'BCP-47 language code, e.g. en-US';
    
    const config = {
      encoding: encoding,
      languageCode: languageCode,
      enableAutomaticPunctuation: true,
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
    
    
    def transcribe_file_with_auto_punctuation(audio_file: str) -> speech.RecognizeResponse:
        """Transcribe the given audio file with auto punctuation enabled.
        Args:
            audio_file (str): Path to the local audio file to be transcribed.
        Returns:
            speech.RecognizeResponse: The response containing the transcription results.
        """
        client = speech.SpeechClient()
    
        with open(audio_file, "rb") as f:
            audio_content = f.read()
    
        audio = speech.RecognitionAudio(content=audio_content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=8000,
            language_code="en-US",
            # Enable automatic punctuation
            enable_automatic_punctuation=True,
        )
    
        response = client.recognize(config=config, audio=audio)
    
        for i, result in enumerate(response.results):
            alternative = result.alternatives[0]
            print("-" * 20)
            print(f"First alternative of result {i}")
            print(f"Transcript: {alternative.transcript}")
    
        return response

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
