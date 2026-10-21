---
url: https://docs.cloud.google.com/video-intelligence/docs/samples/video-speech-transcription-gcs/
title: Transcribe speech in a Cloud Storage file \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:08.294301+00:00
---

# Transcribe speech in a Cloud Storage file  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/samples/video-speech-transcription-gcs/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Samples ](https://docs.cloud.google.com/video-intelligence/docs/samples)



#  Transcribe speech in a Cloud Storage file Stay organized with collections  Save and categorize content based on your preferences. 

Transcribe speech to text from a video file stored in Cloud Storage.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Get audio track transcription](https://docs.cloud.google.com/video-intelligence/docs/transcription)



## Code sample

### Go

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func speechTranscriptionURI(w io.Writer, file string) error {
    	ctx := context.Background()
    	client, err := video.NewClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	op, err := client.AnnotateVideo(ctx, &videopb.AnnotateVideoRequest{
    		Features: []videopb.Feature{
    			videopb.Feature_SPEECH_TRANSCRIPTION,
    		},
    		VideoContext: &videopb.VideoContext{
    			SpeechTranscriptionConfig: &videopb.SpeechTranscriptionConfig{
    				LanguageCode:               "en-US",
    				EnableAutomaticPunctuation: true,
    			},
    		},
    		InputUri: file,
    	})
    	if err != nil {
    		return err
    	}
    	resp, err := op.Wait(ctx)
    	if err != nil {
    		return err
    	}
    
    	// A single video was processed. Get the first result.
    	result := resp.AnnotationResults[0]
    
    	for _, transcription := range result.SpeechTranscriptions {
    		// The number of alternatives for each transcription is limited by
    		// SpeechTranscriptionConfig.MaxAlternatives.
    		// Each alternative is a different possible transcription
    		// and has its own confidence score.
    		for _, alternative := range transcription.GetAlternatives() {
    			fmt.Fprintf(w, "Alternative level information:\n")
    			fmt.Fprintf(w, "\tTranscript: %v\n", alternative.GetTranscript())
    			fmt.Fprintf(w, "\tConfidence: %v\n", alternative.GetConfidence())
    
    			fmt.Fprintf(w, "Word level information:\n")
    			for _, wordInfo := range alternative.GetWords() {
    				startTime := wordInfo.GetStartTime()
    				endTime := wordInfo.GetEndTime()
    				fmt.Fprintf(w, "\t%4.1f - %4.1f: %v (speaker %v)\n",
    					float64(startTime.GetSeconds())+float64(startTime.GetNanos())*1e-9, // start as seconds
    					float64(endTime.GetSeconds())+float64(endTime.GetNanos())*1e-9,     // end as seconds
    					wordInfo.GetWord(),
    					wordInfo.GetSpeakerTag())
    			}
    		}
    	}
    
    	return nil
    }
    

### Java

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Instantiate a com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient
    try (VideoIntelligenceServiceClient client = VideoIntelligenceServiceClient.create()) {
      // Set the language code
      SpeechTranscriptionConfig config =
          SpeechTranscriptionConfig.newBuilder()
              .setLanguageCode("en-US")
              .setEnableAutomaticPunctuation(true)
              .build();
    
      // Set the video context with the above configuration
      VideoContext context = VideoContext.newBuilder().setSpeechTranscriptionConfig(config).build();
    
      // Create the request
      AnnotateVideoRequest request =
          AnnotateVideoRequest.newBuilder()
              .setInputUri(gcsUri)
              .addFeatures(Feature.SPEECH_TRANSCRIPTION)
              .setVideoContext(context)
              .build();
    
      // asynchronously perform speech transcription on videos
      OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> response =
          client.annotateVideoAsync(request);
    
      System.out.println("Waiting for operation to complete...");
      // Display the results
      for (VideoAnnotationResults results :
          response.get(600, TimeUnit.SECONDS).getAnnotationResultsList()) {
        for (SpeechTranscription speechTranscription : results.getSpeechTranscriptionsList()) {
          try {
            // Print the transcription
            if (speechTranscription.getAlternativesCount() > 0) {
              SpeechRecognitionAlternative alternative = speechTranscription.getAlternatives(0);
    
              System.out.printf("Transcript: %s\n", alternative.getTranscript());
              System.out.printf("Confidence: %.2f\n", alternative.getConfidence());
    
              System.out.println("Word level information:");
              for (WordInfo wordInfo : alternative.getWordsList()) {
                double startTime =
                    wordInfo.getStartTime().getSeconds() + wordInfo.getStartTime().getNanos() / 1e9;
                double endTime =
                    wordInfo.getEndTime().getSeconds() + wordInfo.getEndTime().getNanos() / 1e9;
                System.out.printf(
                    "\t%4.2fs - %4.2fs: %s\n", startTime, endTime, wordInfo.getWord());
              }
            } else {
              System.out.println("No transcription found");
            }
          } catch (IndexOutOfBoundsException ioe) {
            System.out.println("Could not retrieve frame: " + ioe.getMessage());
          }
        }
      }
    }

### Node.js

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Video Intelligence library
    const videoIntelligence = require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)');
    
    // Creates a client
    const client = new videoIntelligence.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const gcsUri = 'GCS URI of video to analyze, e.g. gs://my-bucket/my-video.mp4';
    
    async function analyzeVideoTranscript() {
      const videoContext = {
        speechTranscriptionConfig: {
          languageCode: 'en-US',
          enableAutomaticPunctuation: true,
        },
      };
    
      const request = {
        inputUri: gcsUri,
        features: ['SPEECH_TRANSCRIPTION'],
        videoContext: videoContext,
      };
    
      const [operation] = await client.annotateVideo(request);
      console.log('Waiting for operation to complete...');
      const [operationResult] = await operation.promise();
      // There is only one annotation_result since only
      // one video is processed.
      const annotationResults = operationResult.annotationResults[0];
    
      for (const speechTranscription of annotationResults.speechTranscriptions) {
        // The number of alternatives for each transcription is limited by
        // SpeechTranscriptionConfig.max_alternatives.
        // Each alternative is a different possible transcription
        // and has its own confidence score.
        for (const alternative of speechTranscription.alternatives) {
          console.log('Alternative level information:');
          console.log(`Transcript: ${alternative.transcript}`);
          console.log(`Confidence: ${alternative.confidence}`);
    
          console.log('Word level information:');
          for (const wordInfo of alternative.words) {
            const word = wordInfo.word;
            const start_time =
              wordInfo.startTime.seconds + wordInfo.startTime.nanos * 1e-9;
            const end_time =
              wordInfo.endTime.seconds + wordInfo.endTime.nanos * 1e-9;
            console.log('\t' + start_time + 's - ' + end_time + 's: ' + word);
          }
        }
      }
    }
    
    analyzeVideoTranscript();

### PHP

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\VideoIntelligence\V1\AnnotateVideoRequest;
    use Google\Cloud\VideoIntelligence\V1\Client\VideoIntelligenceServiceClient;
    use Google\Cloud\VideoIntelligence\V1\Feature;
    use Google\Cloud\VideoIntelligence\V1\SpeechTranscriptionConfig;
    use Google\Cloud\VideoIntelligence\V1\VideoContext;
    
    /**
     * @param string $uri The cloud storage object to analyze (gs://your-bucket-name/your-object-name)
     * @param int $pollingIntervalSeconds
     */
    function analyze_transcription(string $uri, int $pollingIntervalSeconds = 0)
    {
        # set configs
        $speechTranscriptionConfig = (new SpeechTranscriptionConfig())
            ->setLanguageCode('en-US')
            ->setEnableAutomaticPunctuation(true);
        $videoContext = (new VideoContext())
            ->setSpeechTranscriptionConfig($speechTranscriptionConfig);
    
        # instantiate a client
        $client = new VideoIntelligenceServiceClient();
    
        # execute a request.
        $features = [Feature::SPEECH_TRANSCRIPTION];
        $request = (new AnnotateVideoRequest())
            ->setInputUri($uri)
            ->setVideoContext($videoContext)
            ->setFeatures($features);
        $operation = $client->annotateVideo($request);
    
        print('Processing video for speech transcription...' . PHP_EOL);
        # Wait for the request to complete.
        $operation->pollUntilComplete([
            'pollingIntervalSeconds' => $pollingIntervalSeconds
        ]);
    
        # Print the result.
        if ($operation->operationSucceeded()) {
            $result = $operation->getResult();
            # there is only one annotation_result since only
            # one video is processed.
            $annotationResults = $result->getAnnotationResults()[0];
            $speechTranscriptions = $annotationResults ->getSpeechTranscriptions();
    
            foreach ($speechTranscriptions as $transcription) {
                # the number of alternatives for each transcription is limited by
                # $max_alternatives in SpeechTranscriptionConfig
                # each alternative is a different possible transcription
                # and has its own confidence score.
                foreach ($transcription->getAlternatives() as $alternative) {
                    print('Alternative level information' . PHP_EOL);
    
                    printf('Transcript: %s' . PHP_EOL, $alternative->getTranscript());
                    printf('Confidence: %s' . PHP_EOL, $alternative->getConfidence());
    
                    print('Word level information:');
                    foreach ($alternative->getWords() as $wordInfo) {
                        printf(
                            '%s s - %s s: %s' . PHP_EOL,
                            $wordInfo->getStartTime()->getSeconds(),
                            $wordInfo->getEndTime()->getSeconds(),
                            $wordInfo->getWord()
                        );
                    }
                }
            }
        }
        $client->close();
    }

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    """Transcribe speech from a video stored on GCS."""
    from google.cloud import videointelligence
    
    video_client = videointelligence.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html)()
    features = [videointelligence.[Feature](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.Feature.html).SPEECH_TRANSCRIPTION]
    
    config = videointelligence.[SpeechTranscriptionConfig](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.SpeechTranscriptionConfig.html)(
        language_code="en-US", enable_automatic_punctuation=True
    )
    video_context = videointelligence.[VideoContext](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.types.VideoContext.html)(speech_transcription_config=config)
    
    operation = video_client.[annotate_video](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1.services.video_intelligence_service.VideoIntelligenceServiceClient.html#google_cloud_videointelligence_v1_services_video_intelligence_service_VideoIntelligenceServiceClient_annotate_video)(
        request={
            "features": features,
            "input_uri": path,
            "video_context": video_context,
        }
    )
    
    print("\nProcessing video for speech transcription.")
    
    result = operation.result(timeout=600)
    
    # There is only one annotation_result since only
    # one video is processed.
    annotation_results = result.annotation_results[0]
    for speech_transcription in annotation_results.speech_transcriptions:
        # The number of alternatives for each transcription is limited by
        # SpeechTranscriptionConfig.max_alternatives.
        # Each alternative is a different possible transcription
        # and has its own confidence score.
        for alternative in speech_transcription.alternatives:
            print("Alternative level information:")
    
            print("Transcript: {}".format(alternative.transcript))
            print("Confidence: {}\n".format(alternative.confidence))
    
            print("Word level information:")
            for word_info in alternative.words:
                word = word_info.word
                start_time = word_info.start_time
                end_time = word_info.end_time
                print(
                    "\t{}s - {}s: {}".format(
                        start_time.seconds + start_time.microseconds * 1e-6,
                        end_time.seconds + end_time.microseconds * 1e-6,
                        word,
                    )
                )

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videointelligenceapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
