---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-async-gcs/
title: Asynchronously transcribe an audio file in Cloud Storage \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:49.586428+00:00
---

# Asynchronously transcribe an audio file in Cloud Storage  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-async-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Asynchronously transcribe an audio file in Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

Perform asynchronous transcription on an audio file stored in Cloud Storage.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Transcribe long audio files into text](https://docs.cloud.google.com/speech-to-text/docs/v1/async-recognize)



## Code sample

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

### PHP

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Speech\V2\Client\SpeechClient;
    use Google\Cloud\Speech\V2\BatchRecognizeRequest;
    use Google\Cloud\Speech\V2\RecognitionConfig;
    use Google\Cloud\Speech\V2\BatchRecognizeFileMetadata;
    use Google\Cloud\Speech\V2\ExplicitDecodingConfig;
    use Google\Cloud\Speech\V2\ExplicitDecodingConfig\AudioEncoding;
    use Google\Cloud\Speech\V2\RecognitionOutputConfig;
    use Google\Cloud\Speech\V2\InlineOutputConfig;
    
    /**
     * @param string $projectId The Google Cloud project ID.
     * @param string $location The location of the recognizer.
     * @param string $recognizerId The ID of the recognizer to use.
     * @param string $uri The Cloud Storage object to transcribe (other than global)
     *                    e.x. gs://cloud-samples-data/speech/brooklyn_bridge.raw
     */
    function transcribe_async_gcs(string $projectId, string $location, string $recognizerId, string $uri)
    {
        $apiEndpoint = $location === 'global' ? null : sprintf('%s-speech.googleapis.com', $location);
        $speech = new SpeechClient(['apiEndpoint' => $apiEndpoint]);
        $recognizerName = SpeechClient::recognizerName($projectId, $location, $recognizerId);
    
        $config = (new RecognitionConfig())
            // Can also use {@see Google\Cloud\Speech\V2\ExplicitDecodingConfig}
            // ->setExplicitDecodingConfig(new ExplicitDecodingConfig([...]);
    
            ->setExplicitDecodingConfig(new ExplicitDecodingConfig([
                // change these variables if necessary
                'encoding' => AudioEncoding::LINEAR16,
                'sample_rate_hertz' => 16000,
                'audio_channel_count' => 1,
            ]));
    
        $outputConfig = (new RecognitionOutputConfig())
            ->setInlineResponseConfig(new InlineOutputConfig());
    
        $file = new BatchRecognizeFileMetadata();
        $file->setUri($uri);
    
        $request = (new BatchRecognizeRequest())
            ->setRecognizer($recognizerName)
            ->setConfig($config)
            ->setFiles([$file])
            ->setRecognitionOutputConfig($outputConfig);
    
        try {
            $operation = $speech->batchRecognize($request);
            $operation->pollUntilComplete();
    
            if ($operation->operationSucceeded()) {
                $response = $operation->getResult();
                foreach ($response->getResults() as $result) {
                    if ($result->getError()) {
                        print('Error: ' . $result->getError()->getMessage());
                    }
                    // get the most likely transcription
                    $transcript = $result->getInlineResult()->getTranscript();
                    foreach ($transcript->getResults() as $transacriptResult) {
                        $alternatives = $transacriptResult->getAlternatives();
                        $mostLikely = $alternatives[0];
                        $transcript = $mostLikely->getTranscript();
                        $confidence = $mostLikely->getConfidence();
                        printf('Transcript: %s' . PHP_EOL, $transcript);
                        printf('Confidence: %s' . PHP_EOL, $confidence);
                    }
                }
            } else {
                print_r($operation->getError());
            }
        } finally {
            $speech->close();
        }
    }

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
    
    

### Ruby

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # storage_path = "Path to file in Cloud Storage, eg. gs://bucket/audio.raw"
    
    require "google/cloud/speech"
    
    speech = Google::Cloud::[Speech](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech/latest/Google-Cloud-Speech.html).[speech](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech/latest/Google-Cloud-Speech.html) version: :v1
    
    config = { encoding:          :LINEAR16,
               sample_rate_hertz: 16_000,
               language_code:     "en-US" }
    audio = { uri: storage_path }
    
    operation = speech.long_running_recognize config: config, audio: audio
    
    puts "Operation started"
    
    operation.wait_until_done!
    
    raise operation.results.message if operation.error?
    
    results = operation.response.results
    
    alternatives = results.first.alternatives
    alternatives.each do |alternative|
      puts "Transcription: #{alternative.transcript}"
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
