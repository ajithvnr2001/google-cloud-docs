---
url: https://docs.cloud.google.com/video-intelligence/docs/samples/video-analyze-explicit-content/
title: Detect explicit content in a local video file \u00a0|\u00a0 Video Intelligence API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:06:24.067414+00:00
---

# Detect explicit content in a local video file  |  Video Intelligence API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/video-intelligence/docs/samples/video-analyze-explicit-content/

Starting on September 14, 2026, Video Intelligence API is officially deprecated and will no longer be supported. You can continue using Video Intelligence API until September 14, 2027, when it will be shut down. We recommend migrating to [Gemini family of models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/google-models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Video Intelligence API ](https://docs.cloud.google.com/video-intelligence/docs)
  * [ Samples ](https://docs.cloud.google.com/video-intelligence/docs/samples)



#  Detect explicit content in a local video file Stay organized with collections  Save and categorize content based on your preferences. 

Detect explicit content in a video file stored locally.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Detect explicit content in videos](https://docs.cloud.google.com/video-intelligence/docs/analyze-safesearch)



## Code sample

### Go

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    func explicitContentURI(w io.Writer, file string) error {
    	ctx := context.Background()
    	client, err := video.NewClient(ctx)
    	if err != nil {
    		return err
    	}
    	defer client.Close()
    
    	op, err := client.AnnotateVideo(ctx, &videopb.AnnotateVideoRequest{
    		Features: []videopb.Feature{
    			videopb.Feature_EXPLICIT_CONTENT_DETECTION,
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
    	result := resp.AnnotationResults[0].ExplicitAnnotation
    
    	for _, frame := range result.Frames {
    		offset, _ := ptypes.Duration(frame.TimeOffset)
    		fmt.Fprintf(w, "%s - %s\n", offset, frame.PornographyLikelihood.String())
    	}
    
    	return nil
    }
    

### Java

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // Instantiate a com.google.cloud.videointelligence.v1.VideoIntelligenceServiceClient
    try (VideoIntelligenceServiceClient client = VideoIntelligenceServiceClient.create()) {
      // Create an operation that will contain the response when the operation completes.
      AnnotateVideoRequest request =
          AnnotateVideoRequest.newBuilder()
              .setInputUri(gcsUri)
              .addFeatures(Feature.EXPLICIT_CONTENT_DETECTION)
              .build();
    
      OperationFuture<AnnotateVideoResponse, AnnotateVideoProgress> response =
          client.annotateVideoAsync(request);
    
      System.out.println("Waiting for operation to complete...");
      // Print detected annotations and their positions in the analyzed video.
      for (VideoAnnotationResults result : response.get().getAnnotationResultsList()) {
        for (ExplicitContentFrame frame : result.getExplicitAnnotation().getFramesList()) {
          double frameTime =
              frame.getTimeOffset().getSeconds() + frame.getTimeOffset().getNanos() / 1e9;
          System.out.printf("Location: %.3fs\n", frameTime);
          System.out.println("Adult: " + frame.getPornographyLikelihood());
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
    // const gcsUri = 'GCS URI of video to analyze, e.g. gs://my-bucket/my-video.mp4';
    
    const request = {
      inputUri: gcsUri,
      features: ['EXPLICIT_CONTENT_DETECTION'],
    };
    
    // Human-readable likelihoods
    const likelihoods = [
      'UNKNOWN',
      'VERY_UNLIKELY',
      'UNLIKELY',
      'POSSIBLE',
      'LIKELY',
      'VERY_LIKELY',
    ];
    
    // Detects unsafe content
    const [operation] = await client.annotateVideo(request);
    console.log('Waiting for operation to complete...');
    const [operationResult] = await operation.promise();
    // Gets unsafe content
    const explicitContentResults =
      operationResult.annotationResults[0].explicitAnnotation;
    console.log('Explicit annotation results:');
    explicitContentResults.frames.forEach(result => {
      if (result.timeOffset === undefined) {
        result.timeOffset = {};
      }
      if (result.timeOffset.seconds === undefined) {
        result.timeOffset.seconds = 0;
      }
      if (result.timeOffset.nanos === undefined) {
        result.timeOffset.nanos = 0;
      }
      console.log(
        `\tTime: ${result.timeOffset.seconds}` +
          `.${(result.timeOffset.nanos / 1e6).toFixed(0)}s`
      );
      console.log(
        `\t\tPornography likelihood: ${likelihoods[result.pornographyLikelihood]}`
      );
    });

### PHP

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    use Google\Cloud\VideoIntelligence\V1\AnnotateVideoRequest;
    use Google\Cloud\VideoIntelligence\V1\Client\VideoIntelligenceServiceClient;
    use Google\Cloud\VideoIntelligence\V1\Feature;
    use Google\Cloud\VideoIntelligence\V1\Likelihood;
    
    /**
     * @param string $uri The cloud storage object to analyze (gs://your-bucket-name/your-object-name)
     * @param int $pollingIntervalSeconds
     */
    function analyze_explicit_content(string $uri, int $pollingIntervalSeconds = 0)
    {
        $video = new VideoIntelligenceServiceClient();
    
        # Execute a request.
        $features = [Feature::EXPLICIT_CONTENT_DETECTION];
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
            $explicitAnnotation = $results->getExplicitAnnotation();
            foreach ($explicitAnnotation->getFrames() as $frame) {
                $time = $frame->getTimeOffset();
                printf('At %ss:' . PHP_EOL, $time->getSeconds() + $time->getNanos() / 1000000000.0);
                printf('  pornography: ' . Likelihood::name($frame->getPornographyLikelihood()) . PHP_EOL);
            }
        } else {
            print_r($operation->getError());
        }
    }

### Python

To authenticate to Video Intelligence, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    """Detects explicit content from the GCS path to a video."""
    video_client = videointelligence.VideoIntelligenceServiceClient()
    features = [videointelligence.Feature.EXPLICIT_CONTENT_DETECTION]
    
    operation = video_client.annotate_video(
        request={"features": features, "input_uri": path}
    )
    print("\nProcessing video for explicit content annotations:")
    
    result = operation.result(timeout=90)
    print("\nFinished processing.")
    
    # Retrieve first result because a single video was processed
    for frame in result.annotation_results[0].explicit_annotation.frames:
        likelihood = videointelligence.Likelihood(frame.pornography_likelihood)
        frame_time = frame.time_offset.seconds + frame.time_offset.microseconds / 1e6
        print("Time: {}s".format(frame_time))
        print("\tpornography: {}".format(likelihood.name))

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=videointelligenceapi). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
