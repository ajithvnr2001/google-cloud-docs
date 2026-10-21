---
url: https://docs.cloud.google.com/speech-to-text/docs/v1/async-time-offsets/
title: Get word timestamps \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:36.281102+00:00
---

# Get word timestamps  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/v1/async-time-offsets/

New Cloud Speech-to-Text users should use the [V2 API](https://docs.cloud.google.com/speech-to-text/docs). Read our [migration guide](https://docs.cloud.google.com/speech-to-text/docs/migration) to learn how to migrate existing projects to the latest version. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Guides ](https://docs.cloud.google.com/speech-to-text/docs/v1)



Send feedback 

#  Get word timestamps Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to get time offset values for audio transcribed by Cloud Speech-to-Text.

Cloud STT can include **[time offset (timestamp)](https://docs.cloud.google.com/speech-to-text/docs/v1/speech-to-text-requests#time-offsets)** values in the response text for your recognize request. Time offset values show the beginning and end of each spoken word that is recognized in the supplied audio. A time offset value represents the amount of time that has elapsed from the beginning of the audio, in increments of 100ms.

Time offsets are especially useful for analyzing longer audio files, where you may need to search for a particular word in the recognized text and locate it (seek) in the original audio. Cloud STT supports time offsets for all speech recognition methods: [`speech:recognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/recognize), [`speech:longrunningrecognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/longrunningrecognize), and [Streaming](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v1p1beta1#google.cloud.speech.v1p1beta1.StreamingRecognizeRequest).

Time offset values are only included for the first alternative provided in the recognition response.

To include time offsets in the results of your request, set the `enableWordTimeOffsets` parameter to `true` in your request configuration.

### Protocol

Refer to the [`speech:longrunningrecognize`](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/speech/longrunningrecognize) API endpoint for complete details.

To perform synchronous speech recognition, make a `POST` request and provide the appropriate request body. The following shows an example of a `POST` request using `curl`. The example uses the [Google Cloud CLI](https://docs.cloud.google.com/sdk) to generate an access token. For instructions on installing the gcloud CLI, see the [quickstart](https://docs.cloud.google.com/speech-to-text/docs/transcribe-api). 
    
    
    curl -X POST \
         -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
         -H "Content-Type: application/json; charset=utf-8" \
         --data "{
      'config': {
        'language_code': 'en-US',
        'enableWordTimeOffsets': true
      },
      'audio':{
        'uri':'gs://gcs-test-data/vr.flac'
      }
    }" "https://speech.googleapis.com/v1/speech:longrunningrecognize"

See the [RecognitionConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/RecognitionConfig) and [RecognitionAudio](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1/RecognitionAudio) reference documentation for more information on configuring the request body.

If the request is successful, the server returns a `200 OK` HTTP status code and the response in JSON format. If the operation is incomplete (still processing), the response will look similar to the following:
    
    
    {
      "name": "2885768779530032514",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.speech.v1.LongRunningRecognizeMetadata",
        "progressPercent": 97,
        "startTime": "2020-12-14T03:11:54.492593Z",
        "lastUpdateTime": "2020-12-14T03:15:57.484509Z",
        "uri": "gs://{BUCKET_NAME}/{FILE_NAME}"
      }
    }

When the process is complete, the output will be similar to the following:
    
    
    {
      "name": "7612202767953098924"
    }

Where `name` is the name of the long running operation created for the request.

Processing the `vr.flac` file takes about 30 seconds to complete. To retrieve the result of the operation, make a `GET` request to the `https://speech.googleapis.com/v1/operations/` endpoint. Replace `your-operation-name` with the `name` received from your `longrunningrecognize` request.
    
    
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
                "transcript": "okay so what am I doing here...(etc)...",
                "confidence": 0.96596134,
                "words": [
                  {
                    "startTime": "1.400s",
                    "endTime": "1.800s",
                    "word": "okay"
                  },
                  {
                    "startTime": "1.800s",
                    "endTime": "2.300s",
                    "word": "so"
                  },
                  {
                    "startTime": "2.300s",
                    "endTime": "2.400s",
                    "word": "what"
                  },
                  {
                    "startTime": "2.400s",
                    "endTime": "2.600s",
                    "word": "am"
                  },
                  {
                    "startTime": "2.600s",
                    "endTime": "2.600s",
                    "word": "I"
                  },
                  {
                    "startTime": "2.600s",
                    "endTime": "2.700s",
                    "word": "doing"
                  },
                  {
                    "startTime": "2.700s",
                    "endTime": "3s",
                    "word": "here"
                  },
                  {
                    "startTime": "3s",
                    "endTime": "3.300s",
                    "word": "why"
                  },
                  {
                    "startTime": "3.300s",
                    "endTime": "3.400s",
                    "word": "am"
                  },
                  {
                    "startTime": "3.400s",
                    "endTime": "3.500s",
                    "word": "I"
                  },
                  {
                    "startTime": "3.500s",
                    "endTime": "3.500s",
                    "word": "here"
                  },
                  ...
                ]
              }
            ]
          },
          {
            "alternatives": [
              {
                "transcript": "so so what am I doing here...(etc)...",
                "confidence": 0.9642093,
              }
            ]
          }
        ]
      }
    }

If the operation has not completed, you can poll the endpoint by repeatedly making the `GET` request until the `done` property of the response is `true`.

### gcloud

Refer to the [ `recognize-long-running`](https://docs.cloud.google.com/sdk/gcloud/reference/ml/speech/recognize-long-running) command for complete details.

To perform asynchronous speech recognition, use the Google Cloud CLI, providing the path of a local file or a Google Cloud Storage URL. Include the `--include-word-time-offsets` flag.
    
    
    gcloud ml speech recognize-long-running \
        'gs://cloud-samples-tests/speech/brooklyn.flac' \
        --language-code='en-US' --include-word-time-offsets --async

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
              "transcript": "how old is the Brooklyn Bridge",
              "words": [
                {
                  "endTime": "0.300s",
                  "startTime": "0s",
                  "word": "how"
                },
                {
                  "endTime": "0.600s",
                  "startTime": "0.300s",
                  "word": "old"
                },
                {
                  "endTime": "0.800s",
                  "startTime": "0.600s",
                  "word": "is"
                },
                {
                  "endTime": "0.900s",
                  "startTime": "0.800s",
                  "word": "the"
                },
                {
                  "endTime": "1.100s",
                  "startTime": "0.900s",
                  "word": "Brooklyn"
                },
                {
                  "endTime": "1.500s",
                  "startTime": "1.100s",
                  "word": "Bridge"
                }
              ]
            }
          ]
        }
      ]
    }

### Go

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Go API reference documentation](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/speech/latest/apiv1). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func asyncWords(client *speech.Client, out io.Writer, gcsURI string) error {
    	ctx := context.Background()
    
    	// Send the contents of the audio file with the encoding and
    	// and sample rate information to be transcripted.
    	req := &speechpb.LongRunningRecognizeRequest{
    		Config: &speechpb.RecognitionConfig{
    			Encoding:              speechpb.RecognitionConfig_LINEAR16,
    			SampleRateHertz:       16000,
    			LanguageCode:          "en-US",
    			EnableWordTimeOffsets: true,
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
    			fmt.Fprintf(out, "\"%v\" (confidence=%3f)\n", alt.Transcript, alt.Confidence)
    			for _, w := range alt.Words {
    				fmt.Fprintf(out,
    					"Word: \"%v\" (startTime=%3f, endTime=%3f)\n",
    					w.Word,
    					float64(w.StartTime.Seconds)+float64(w.StartTime.Nanos)*1e-9,
    					float64(w.EndTime.Seconds)+float64(w.EndTime.Nanos)*1e-9,
    				)
    			}
    		}
    	}
    	return nil
    }
    

### Java

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Java API reference documentation](https://docs.cloud.google.com/java/docs/reference/google-cloud-speech/latest/overview). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    /**
     * Performs non-blocking speech recognition on remote FLAC file and prints the transcription as
     * well as word time offsets.
     *
     * @param gcsUri the path to the remote LINEAR16 audio file to transcribe.
     */
    public static void asyncRecognizeWords(String gcsUri) throws Exception {
      // Instantiates a client with GOOGLE_APPLICATION_CREDENTIALS
      try (SpeechClient speech = SpeechClient.create()) {
    
        // Configure remote file request for FLAC
        RecognitionConfig config =
            RecognitionConfig.newBuilder()
                .setEncoding(AudioEncoding.FLAC)
                .setLanguageCode("en-US")
                .setSampleRateHertz(16000)
                .setEnableWordTimeOffsets(true)
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
          for (WordInfo wordInfo : alternative.getWordsList()) {
            System.out.println(wordInfo.getWord());
            System.out.printf(
                "\t%s.%s sec - %s.%s sec\n",
                wordInfo.getStartTime().getSeconds(),
                wordInfo.getStartTime().getNanos() / 100000000,
                wordInfo.getEndTime().getSeconds(),
                wordInfo.getEndTime().getNanos() / 100000000);
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
    
    /**
     * TODO(developer): Uncomment the following lines before running the sample.
     */
    // const gcsUri = 'gs://my-bucket/audio.raw';
    // const encoding = 'Encoding of the audio file, e.g. LINEAR16';
    // const sampleRateHertz = 16000;
    // const languageCode = 'BCP-47 language code, e.g. en-US';
    
    const config = {
      enableWordTimeOffsets: true,
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
    response.results.forEach(result => {
      console.log(`Transcription: ${result.alternatives[0].transcript}`);
      result.alternatives[0].words.forEach(wordInfo => {
        // NOTE: If you have a time offset exceeding 2^32 seconds, use the
        // wordInfo.{x}Time.seconds.high to calculate seconds.
        const startSecs =
          `${wordInfo.startTime.seconds}` +
          '.' +
          wordInfo.startTime.nanos / 100000000;
        const endSecs =
          `${wordInfo.endTime.seconds}` +
          '.' +
          wordInfo.endTime.nanos / 100000000;
        console.log(`Word: ${wordInfo.word}`);
        console.log(`\t ${startSecs} secs - ${endSecs} secs`);
      });
    });

### Python

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). For more information, see the [Cloud STT Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/speech/latest). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    def transcribe_gcs_with_word_time_offsets(
        audio_uri: str,
    ) -> speech.RecognizeResponse:
        """Transcribe the given audio file asynchronously and output the word time
        offsets.
        Args:
            audio_uri (str): The Google Cloud Storage URI of the input audio file.
                E.g., gs://[BUCKET]/[FILE]
        Returns:
            speech.RecognizeResponse: The response containing the transcription results with word time offsets.
        """
        from google.cloud import speech
    
        client = speech.SpeechClient()
    
        audio = speech.RecognitionAudio(uri=audio_uri)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.FLAC,
            sample_rate_hertz=16000,
            language_code="en-US",
            enable_word_time_offsets=True,
        )
    
        operation = client.long_running_recognize(config=config, audio=audio)
    
        print("Waiting for operation to complete...")
        result = operation.result(timeout=90)
    
        for result in result.results:
            alternative = result.alternatives[0]
            print(f"Transcript: {alternative.transcript}")
            print(f"Confidence: {alternative.confidence}")
    
            for word_info in alternative.words:
                word = word_info.word
                start_time = word_info.start_time
                end_time = word_info.end_time
    
                print(
                    f"Word: {word}, start_time: {start_time.total_seconds()}, end_time: {end_time.total_seconds()}"
                )
    
        return result
    
    

### Additional languages

**C#** : Please follow the [C# setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for .NET.](https://googleapis.github.io/google-cloud-dotnet/docs/Google.Cloud.Speech.V1/index.html)

**PHP** : Please follow the [PHP setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for PHP.](https://docs.cloud.google.com/php/docs/reference/cloud-speech/latest)

**Ruby** : Please follow the [Ruby setup instructions](https://docs.cloud.google.com/speech-to-text/docs/client-libraries) on the client libraries page and then visit the [Cloud STT reference documentation for Ruby.](https://googleapis.dev/ruby/google-cloud-speech/latest/Google/Cloud/Speech.html)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
