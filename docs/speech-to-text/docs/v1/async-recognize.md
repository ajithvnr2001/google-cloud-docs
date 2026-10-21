---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/async-recognize/
title: Transcribe long audio files into text \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:49.462686+00:00
---

# Transcribe long audio files into text  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/async-recognize/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Transcribe long audio files into text Stay organized with collections  Save and categorize content based on your preferences. 

This page demonstrates how to transcribe long audio files (longer than 1 minute) to text using the Cloud Speech-to-Text API and asynchronous speech recognition.

## About asynchronous speech recognition

_Asynchronous speech recognition_ starts a long running audio processing operation. Use asynchronous speech recognition to transcribe audio that is longer than 60 seconds. For shorter audio, [synchronous speech recognition](https://docs.cloud.google.com/speech-to-text/docs/v1/sync-recognize) is faster and simpler. The upper limit for asynchronous speech recognition is 480 minutes.

### Cloud Speech-to-Text and asynchronous processing

Audio content can be sent directly to Cloud Speech-to-Text from a local file for asynchronous processing. However, the audio time limit for local files is 60 seconds. Attempting to transcribe local audio files that are longer than 60 seconds will result in an error. To use asynchronous speech recognition to transcribe audio longer than 60 seconds, you must have your data saved in a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets) .

You can retrieve the results of the operation using the [google.longrunning.Operations](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/operations#resource-operation) method. Results remain available for retrieval for 5 days (120 hours). You also have the option of [uploading your results directly](https://docs.cloud.google.com/speech-to-text/docs/v1/async-recognize#upload_your_transcription_results_to_a_bucket) to a Cloud Storage bucket.

## Transcribe long audio files using a Cloud Storage bucket

These samples use a Cloud Storage bucket to store the raw audio input for the long-running transcription process. For an example of a typical `longrunningrecognize` operation response, see the [reference documentation](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation).

### Protocol

Refer to the [`speech:longrunningrecognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/longrunningrecognize) API endpoint for complete details.

To perform synchronous speech recognition, make a `POST` request and provide the appropriate request body. The following shows an example of a `POST` request using `curl`. The example uses the [Google Cloud CLI](https://docs.cloud.google.com/sdk) to generate an access token. For instructions on installing the gcloud CLI, see the [quickstart](https://docs.cloud.google.com/speech-to-text/docs/transcribe-api). 
    
    
    curl -X POST \
         -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
         -H "Content-Type: application/json; charset=utf-8" \
         --data "{
      'config': {
        'language_code': 'en-US'
      },
      'audio':{
        'uri':'gs://cloud-samples-tests/speech/brooklyn.flac'
      }
    }" "https://speech.googleapis.com/v1/speech:longrunningrecognize"

See the [RecognitionConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionConfig) and [RecognitionAudio](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionAudio) reference documentation for more information on configuring the request body.

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format:
    
    
    {
      "name": "7612202767953098924"
    }

Where `name` is the name of the long running operation created for the request.

Wait for processing to complete. Processing time differs depending on your source audio. In most cases, you will get results in half the length of the source audio. You can get the status of your long-running operation by making a `GET` request to the `https://speech.googleapis.com/v1/operations/` endpoint. Replace `your-operation-name` with the `name` returned from your `longrunningrecognize` request.
    
    
    curl -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
         -H "Content-Type: application/json; charset=utf-8" \
         "https://speech.googleapis.com/v1/operations/your-operation-name"

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format: 
    
    
    {
      "name": "7612202767953098924",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.speech.v1.LongRunningRecognizeMetadata",
        "progressPercent": 100,
        "startTime": "2017-07-20T16:36:55.033650Z",
        "lastUpdateTime": "2017-07-20T16:37:17.158630Z"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.speech.v1.LongRunningRecognizeResponse",
        "results": [
          {
            "alternatives": [
              {
                "transcript": "how old is the Brooklyn Bridge",
                "confidence": 0.96096134,
              }
            ]
          },
          {
            "alternatives": [
              {
                ...
              }
            ]
          }
        ]
      }
    }

If the operation has not completed, you can poll the endpoint by repeatedly making the `GET` request until the `done` property of the response is `true`.

### gcloud

Refer to the [ `recognize-long-running`](https://docs.cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running) command for complete details.

To perform asynchronous speech recognition, use the Google Cloud CLI, providing the path of a local file or a Cloud Storage URL.
    
    
    gcloud ml speech recognize-long-running \
        'gs://cloud-samples-tests/speech/brooklyn.flac' \
         --language-code='en-US' --async

If the request is successful, the server returns the ID of the long-running operation in JSON format.
    
    
    {
      "name": OPERATION_ID
    }

You can then get information about the operation by running the following command.
    
    
    gcloud ml speech operations describe OPERATION_ID

You can also poll the operation until it completes by running the following command.
    
    
    gcloud ml speech operations wait OPERATION_ID

After the operation completes, the operation returns a transcript of the audio in JSON format.
    
    
    {
      "@type": "type.googleapis.com/google.cloud.speech.v1.LongRunningRecognizeResponse",
      "results": [
        {
          "alternatives": [
            {
              "confidence": 0.9840146,
              "transcript": "how old is the Brooklyn Bridge"
            }
          ]
        }
      ]
    }

### Go

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func sendGCS(w io.Writer, client *speech.Client, gcsURI string) error {
    	ctx := context.Background()
    
    	// Send the contents of the audio file with the encoding and
    	// and sample rate information to be transcripted.
    	req := &speechpb.LongRunningRecognizeRequest{
    		Config: &speechpb.RecognitionConfig{
    			Encoding:        speechpb.RecognitionConfig_LINEAR16,
    			SampleRateHertz: 16000,
    			LanguageCode:    "en-US",
    		},
    		Audio: &speechpb.RecognitionAudio{
    			AudioSource: &speechpb.RecognitionAudio_Uri{Uri: gcsURI},
    		},
    	}
    
    	op, err := client.LongRunningRecognize(ctx, req)
    	if err != nil {
    		return err
    	}
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	// Print the results.
    	for _, result := range resp.Results {
    		for _, alt := range result.Alternatives {
    			fmt.Fprintf(w, "\"%v\" (confidence=%3f)\n", alt.Transcript, alt.Confidence)
    		}
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Performs non-blocking speech recognition on remote FLAC file and prints the transcription.
     *
     * @param gcsUri the path to the remote LINEAR16 audio file to transcribe.
     */
    public static void asyncRecognizeGcs(String gcsUri) throws Exception {
      // Configure polling algorithm
      SpeechSettings.Builder speechSettings = SpeechSettings.newBuilder();
      TimedRetryAlgorithm timedRetryAlgorithm =
          OperationTimedPollAlgorithm.create(
              RetrySettings.newBuilder()
                  .setInitialRetryDelay(Duration.ofMillis(500L))
                  .setRetryDelayMultiplier(1.5)
                  .setMaxRetryDelay(Duration.ofMillis(5000L))
                  .setInitialRpcTimeout(Duration.ZERO) // ignored
                  .setRpcTimeoutMultiplier(1.0) // ignored
                  .setMaxRpcTimeout(Duration.ZERO) // ignored
                  .setTotalTimeout(Duration.ofHours(24L)) // set polling timeout to 24 hours
                  .build());
      speechSettings.longRunningRecognizeOperationSettings().setPollingAlgorithm(timedRetryAlgorithm);
    
      // Instantiates a client with GOOGLE_APPLICATION_CREDENTIALS
      try (SpeechClient speech = SpeechClient.create(speechSettings.build())) {
    
        // Configure remote file request for FLAC
        RecognitionConfig config =
            RecognitionConfig.newBuilder()
                .setEncoding(AudioEncoding.FLAC)
                .setLanguageCode("en-US")
                .setSampleRateHertz(16000)
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
    
        for (SpeechRecognitionResult result : results) {
          // There can be several alternative transcripts for a given chunk of speech. Just use the
          // first (most likely) one here.
          SpeechRecognitionAlternative alternative = result.getAlternativesList().get(0);
          System.out.printf("Transcription: %s\n", alternative.getTranscript());
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
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const gcsUri = 'gs://my-bucket/audio.raw';
    // const encoding = 'Encoding of the audio file, e.g. LINEAR16';
    // const sampleRateHertz = 16000;
    // const languageCode = 'BCP-47 language code, e.g. en-US';
    
    const config = {
      encoding: encoding,
      sampleRateHertz: sampleRateHertz,
      languageCode: languageCode,
    };
    
    const audio = {
      uri: gcsUri,
    };
    
    const request = {
      config: config,
      audio: audio,
    };
    
    // Detects speech in the audio file. This creates a recognition job that you
    // can wait for now, or get its result later.
    const [operation] = await client.longRunningRecognize(request);
    // Get a Promise representation of the final result of the job
    const [response] = await operation.promise();
    const transcription = response.results
      .map(result => result.alternatives[0].transcript)
      .join('\n');
    console.log(`Transcription: ${transcription}`);

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import speech
    
    
    def transcribe_gcs(gcs_uri: str) -> str:
        """Asynchronously transcribes the audio file from Cloud Storage
        Args:
            gcs_uri: The Google Cloud Storage path to an audio file.
                E.g., "gs://storage-bucket/file.flac".
        Returns:
            The generated transcript from the audio file provided.
        """
        client = speech.SpeechClient()
    
        audio = speech.[RecognitionAudio](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionAudio.html)(uri=gcs_uri)
        config = speech.[RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionConfig.html)(
            encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
            sample_rate_hertz=44100,
            language_code="en-US",
        )
    
        operation = client.[long_running_recognize](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.services.speech.SpeechClient.html#google_cloud_speech_v1_services_speech_SpeechClient_long_running_recognize)(config=config, audio=audio)
    
        print("Waiting for operation to complete...")
        response = operation.result(timeout=90)
    
        transcript_builder = []
        # Each result is for a consecutive portion of the audio. Iterate through
        # them to get the transcripts for the entire audio file.
        for result in response.results:
            # The first alternative is the most likely one for this portion.
            transcript_builder.append(f"\nTranscript: {result.alternatives[0].transcript}")
            transcript_builder.append(f"\nConfidence: {result.alternatives[0].confidence}")
    
        transcript = "".join(transcript_builder)
        print(transcript)
    
        return transcript
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Speech.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-speech/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-speech/latest/Google/Cloud/Speech.html)

## Upload your transcription results to a Cloud Storage bucket

Cloud Speech-to-Text supports uploading your longrunning recognition results directly to a Cloud Storage bucket. If you implement this feature with [Cloud Storage Triggers](https://cloud.google.com/functions/docs/calling/storage), Cloud Storage uploads can trigger notifications that call [Cloud Functions](https://cloud.google.com/functions/docs) and remove the need to poll Cloud Speech-to-Text for recognition results.

To have your results uploaded to a Cloud Storage bucket, provide the optional [`TranscriptOutputConfig`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/longrunningrecognize#TranscriptOutputConfig) output configuration in your longrunning recognition request.
    
    
          message TranscriptOutputConfig {
    
            oneof output_type {
              // Specifies a Cloud Storage URI for the recognition results. Must be
              // specified in the format: `gs://bucket_name/object_name`
              string gcs_uri = 1;
            }
          }
    

### Protocol

Refer to the [`longrunningrecognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/longrunningrecognize) API endpoint for complete details.

The following example shows how to send a `POST` request using `curl`, where the body of the request specifies the path to a Cloud Storage bucket. The results are uploaded to this location as a `JSON` file that stores [`SpeechRecognitionResult`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/recognize#SpeechRecognitionResult).
    
    
    curl -X POST \
         -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         --data "{
      'config': {...},
      'output_config': {
    **'gcs_uri':'gs://bucket/result-output-path.json'**
    **},**
      'audio': {
        'uri': 'gs://bucket/audio-path'
      }
    }" "https://speech.googleapis.com/v2/speech:longrunningrecognize"

The [`LongRunningRecognizeResponse`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/Shared.Types/ListOperationsResponse#operation) includes the path to the Cloud Storage bucket where the upload was attempted. If the upload was unsuccessful, an output error will be returned. If a file with the same name already exists, the upload writes the results to a new file with a timestamp as the suffix.
    
    
    {
      ...
      "metadata": {
        ...
        "outputConfig": {...}
      },
      ...
      "response": {
        ...
        "results": [...],
        "outputConfig": {
          "gcs_uri":"gs://bucket/result-output-path"
        },
        "outputError": {...}
      }
    }
    
    

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud STT performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud STT free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
