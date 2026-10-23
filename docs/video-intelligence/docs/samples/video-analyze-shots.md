---
url: https://docs.cloud.google.com/video-intelligence/docs/samples/video-analyze-shots/
title: Detect shot changes in a local file \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:47.496999+00:00
---

# Detect shot changes in a local file  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/samples/video-analyze-shots/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Samples ](https://docs.cloud.google.com/video-intelligence/docs/samples)



#  Detect shot changes in a local file Stay organized with collections  Save and categorize content based on your preferences. 

Detect shot changes on a video file stored locally.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Detect shot changes](https://docs.cloud.google.com/video-intelligence/docs/analyze-shots)



## Code sample

### Go

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func shotChangeURI(w io.Writer, file string) error {
    	ctx := context.Background()
    	client, err := video.NewClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	op, err := client.AnnotateVideo(ctx, &videopb.AnnotateVideoRequest{
    		Features: []videopb.Feature{
    			videopb.Feature_SHOT_CHANGE_DETECTION,
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
    	result := resp.AnnotationResults[0].ShotAnnotations
    
    	for _, shot := range result {
    		start, _ := ptypes.Duration(shot.StartTimeOffset)
    		end, _ := ptypes.Duration(shot.EndTimeOffset)
    
    		fmt.Fprintf(w, "Shot: %s to %s\n", start, end)
    	}
    
    	return nil
    }
    

### Java

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Instantiate a com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient
    try (VideoIntelligenceServiceClient client = VideoIntelligenceServiceClient.create()) {
      // Provide path to file hosted on GCS as "gs://bucket-name/..."
      AnnotateVideoRequest request =
          AnnotateVideoRequest.newBuilder()
              .setInputUri(gcsUri)
              .addFeatures(Feature.SHOT_CHANGE_DETECTION)
              .build();
    
      // Create an operation that will contain the response when the operation completes.
      OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> response =
          client.annotateVideoAsync(request);
    
      System.out.println("Waiting for operation to complete...");
      // Print detected shot changes and their location ranges in the analyzed video.
      for (VideoAnnotationResults result : response.get().getAnnotationResultsList()) {
        if (result.getShotAnnotationsCount() > 0) {
          System.out.println("Shots: ");
          for (VideoSegment segment : result.getShotAnnotationsList()) {
            double startTime =
                segment.getStartTimeOffset().getSeconds()
                    + segment.getStartTimeOffset().getNanos() / 1e9;
            double endTime =
                segment.getEndTimeOffset().getSeconds()
                    + segment.getEndTimeOffset().getNanos() / 1e9;
            System.out.printf("Location: %.3f:%.3f\n", startTime, endTime);
          }
        } else {
          System.out.println("No shot changes detected in " + gcsUri);
        }
      }
    }

### Node.js

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Imports the Google Cloud Video Intelligence library
    const video = require('[@google-cloud/video-intelligence](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)').v1;
    
    // Creates a client
    const client = new video.[VideoIntelligenceServiceClient](https://docs.cloud.google.com/nodejs/docs/reference/video-intelligence/latest/overview.html)();
    
    /**
     * TODO(developer): Uncomment the following line before running the sample.
     */
    // const gcsUri = 'GCS URI of file to analyze, e.g. gs://my-bucket/my-video.mp4';
    
    const request = {
      inputUri: gcsUri,
      features: ['SHOT_CHANGE_DETECTION'],
    };
    
    // Detects camera shot changes
    const [operation] = await client.annotateVideo(request);
    console.log('Waiting for operation to complete...');
    const [operationResult] = await operation.promise();
    // Gets shot changes
    const shotChanges = operationResult.annotationResults[0].shotAnnotations;
    console.log('Shot changes:');
    
    if (shotChanges.length === 1) {
      console.log('The entire video is one shot.');
    } else {
      shotChanges.forEach((shot, shotIdx) => {
        console.log(`Scene ${shotIdx} occurs from:`);
        if (shot.startTimeOffset === undefined) {
          shot.startTimeOffset = {};
        }
        if (shot.endTimeOffset === undefined) {
          shot.endTimeOffset = {};
        }
        if (shot.startTimeOffset.seconds === undefined) {
          shot.startTimeOffset.seconds = 0;
        }
        if (shot.startTimeOffset.nanos === undefined) {
          shot.startTimeOffset.nanos = 0;
        }
        if (shot.endTimeOffset.seconds === undefined) {
          shot.endTimeOffset.seconds = 0;
        }
        if (shot.endTimeOffset.nanos === undefined) {
          shot.endTimeOffset.nanos = 0;
        }
        console.log(
          `\tStart: ${shot.startTimeOffset.seconds}` +
            `.${(shot.startTimeOffset.nanos / 1e6).toFixed(0)}s`
        );
        console.log(
          `\tEnd: ${shot.endTimeOffset.seconds}.` +
            `${(shot.endTimeOffset.nanos / 1e6).toFixed(0)}s`
        );
      });
    }
    

### PHP

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\VideoIntelligence\V1\AnnotateVideoRequest;
    use Google\Cloud\VideoIntelligence\V1\Client\VideoIntelligenceServiceClient;
    use Google\Cloud\VideoIntelligence\V1\Feature;
    
    /**
     * @param string $uri The cloud storage object to analyze (gs://your-bucket-name/your-object-name)
     * @param int $pollingIntervalSeconds
     */
    function analyze_shots(string $uri, int $pollingIntervalSeconds = 0)
    {
        # Instantiate a client.
        $video = new VideoIntelligenceServiceClient();
    
        # Execute a request.
        $features = [Feature::SHOT_CHANGE_DETECTION];
        $request = (new AnnotateVideoRequest())
            ->setInputUri($uri)
            ->setFeatures($features);
        $operation = $video->annotateVideo($request);
    
        # Wait for the request to complete.
        $operation->pollUntilComplete([
            'pollingIntervalSeconds' => $pollingIntervalSeconds
        ]);
    
        # Print the result.
        if ($operation->operationSucceeded()) {
            $results = $operation->getResult()->getAnnotationResults()[0];
            foreach ($results->getShotAnnotations() as $shot) {
                $start = $shot->getStartTimeOffset();
                $end = $shot->getEndTimeOffset();
                printf('Shot: %ss to %ss' . PHP_EOL,
                    $start->getSeconds() + $start->getNanos() / 1000000000.0,
                    $end->getSeconds() + $end->getNanos() / 1000000000.0);
            }
        } else {
            print_r($operation->getError());
        }
    }

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    """Detects camera shot changes."""
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.Feature.SHOT_CHANGE_DETECTION]
    operation = video_client.annotate_video(
        request={"features": features, "input_uri": path}
    )
    print("\nProcessing video for shot change annotations:")
    
    result = operation.result(timeout=90)
    print("\nFinished processing.")
    
    # first result is retrieved because a single video was processed
    for i, shot in enumerate(result.annotation_results[0].shot_annotations):
        start_time = (
            shot.start_time_offset.seconds + shot.start_time_offset.microseconds / 1e6
        )
        end_time = (
            shot.end_time_offset.seconds + shot.end_time_offset.microseconds / 1e6
        )
        print("\tShot {}: {} to {}".format(i, start_time, end_time))

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videointelligenceapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
