---
url: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-async-word-time-offsets-gcs/
title: Asynchronously transcribe an audio file with time offsets \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:10.481423+00:00
---

# Asynchronously transcribe an audio file with time offsets  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/samples/speech-transcribe-async-word-time-offsets-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



#  Asynchronously transcribe an audio file with time offsets Stay organized with collections  Save and categorize content based on your preferences. 

Perform asynchronous transcription including time offsets on an audio file stored in Cloud Storage.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Get word timestamps](https://docs.cloud.google.com/speech-to-text/docs/v1/async-time-offsets)



## Code sample

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

### PHP

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\Speech\V2\BatchRecognizeFileMetadata;
    use Google\Cloud\Speech\V2\Client\SpeechClient;
    use Google\Cloud\Speech\V2\BatchRecognizeRequest;
    use Google\Cloud\Speech\V2\ExplicitDecodingConfig;
    use Google\Cloud\Speech\V2\ExplicitDecodingConfig\AudioEncoding;
    use Google\Cloud\Speech\V2\InlineOutputConfig;
    use Google\Cloud\Speech\V2\RecognitionConfig;
    use Google\Cloud\Speech\V2\RecognitionFeatures;
    use Google\Cloud\Speech\V2\RecognitionOutputConfig;
    use Google\Cloud\Speech\V2\SpeakerDiarizationConfig;
    
    /**
     * @param string $projectId The Google Cloud project ID.
     * @param string $location The location of the recognizer.
     * @param string $recognizerId The ID of the recognizer to use. The recognizer's model must support
     *                             diarization (e.g. "chirp_3").
     * @param string $uri The Cloud Storage object to transcribe (other than global)
     *                    e.x. gs://cloud-samples-data/speech/brooklyn_bridge.raw
     */
    function transcribe_async_words(string $projectId, string $location, string $recognizerId, string $uri)
    {
        $apiEndpoint = $location === 'global' ? null : sprintf('%s-speech.googleapis.com', $location);
        $speech = new SpeechClient(['apiEndpoint' => $apiEndpoint]);
        $recognizerName = SpeechClient::recognizerName($projectId, $location, $recognizerId);
    
        // When this is enabled, we send all the words from the beginning of the audio.
        $features = new RecognitionFeatures([
            'diarization_config' => new SpeakerDiarizationConfig(),
        ]);
    
        $config = (new RecognitionConfig())
            ->setFeatures($features)
            // When running outside the "global" location, you can set the model to "chirp_3" in
            // RecognitionConfig instead of on the recognizer.
            // ->setModel('chirp_3')
    
            // Can also use {@see Google\Cloud\Speech\V2\AutoDetectDecodingConfig}
            // ->setAutoDecodingConfig(new AutoDetectDecodingConfig());
    
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
                        foreach ($mostLikely->getWords() as $wordInfo) {
                            $startTime = $wordInfo->getStartOffset();
                            $endTime = $wordInfo->getEndOffset();
                            printf('  Word: %s (start: %s, end: %s)' . PHP_EOL,
                                $wordInfo->getWord(),
                                $startTime?->serializeToJsonString(),
                                $endTime?->serializeToJsonString()
                            );
                        }
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
    
    

### Ruby

To learn how to install and use the client library for Cloud STT, see [Cloud STT client libraries](https://docs.cloud.google.com/speech-to-text/docs/client-libraries). 

To authenticate to Cloud STT, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # storage_path = "Path to file in Cloud Storage, eg. gs://bucket/audio.raw"
    
    require "google/cloud/speech"
    
    speech = Google::Cloud::[Speech](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech/latest/Google-Cloud-Speech.html).[speech](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech/latest/Google-Cloud-Speech.html) version: :v1
    
    config = { encoding:                 :LINEAR16,
               sample_rate_hertz:        16_000,
               language_code:            "en-US",
               enable_word_time_offsets: true }
    audio  = { uri: storage_path }
    
    operation = speech.long_running_recognize config: config, audio: audio
    
    puts "Operation started"
    
    operation.wait_until_done!
    
    raise operation.results.message if operation.error?
    
    results = operation.response.results
    
    results.first.alternatives.each do |alternative|
      puts "Transcription: #{alternative.transcript}"
    
      alternative.words.each do |word|
        start_time = word.start_time.seconds + (word.start_time.nanos / 1_000_000_000.0)
        end_time   = word.end_time.seconds + (word.end_time.nanos / 1_000_000_000.0)
    
        puts "Word: #{word.word} #{start_time} #{end_time}"
      end
    end

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=speechtotext). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
